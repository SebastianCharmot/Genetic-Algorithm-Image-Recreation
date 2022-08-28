import numpy as np
from PIL import Image, ImageOps, ImageDraw, ImagePath
from Individual import Individual
import random
import math
from pandas import DataFrame

import matplotlib.pyplot as plt

class GP:
    def __init__(self, filename):
        original_image = Image.open(filename)

        # davidson image 
        # self.target_image = original_image.resize((160,120))

        # debugging 
        # self.target_image = original_image.resize((200,200))
        
        # mona lisa image
        self.target_image = original_image.resize((176,203))

        self.l, self.w = self.target_image.size
        
        self.target_image_array = self.to_array(self.target_image)

    def run_gp(self, pop_size, epochs):
        data = {'epoch':[], 'fitness_estimate':[], 'crossover_used':[], 'pop_gen_used':[], 'im_size':[]}
        
        population = []

        # initialize starting population
        for i in range(pop_size):
            new_indiv = Individual(self.l, self.w)

            new_indiv.get_fitness(self.target_image)

            population.append(new_indiv)

        for i in range(epochs):
            new_pop = []

            # estimate for fitness of fittest individual from current epoch's population 
            fittest_estimate = float('inf')

            # populate our new population
            while len(new_pop) < len(population):
                # select parents for crossover
                parent_one = self.tournament_select(population)
                parent_two = self.tournament_select(population)

                fittest_estimate = min(parent_one.fitness, parent_two.fitness, fittest_estimate)

                # used to probabilistically determine how child of both parents is created 
                rand = random.uniform(0, 1)

                # if rand <= 0.23:
                #     child = self.crossover(parent_one, parent_two)

                #     while child == None:
                #         parent_one = self.tournament_select(population)
                #         parent_two = self.tournament_select(population)

                #         child = self.crossover(parent_one, parent_two)
                        
                if rand < 0.3:
                    child = self.crossover(parent_one, parent_two)

                    while child == None:
                        parent_one = self.tournament_select(population)
                        parent_two = self.tournament_select(population)

                        child = self.crossover(parent_one, parent_two)

                elif rand <= 0.9:
                    child = self.crossover_2(parent_one, parent_two, 0.5)

                    while child == None:
                        parent_one = self.tournament_select(population)
                        parent_two = self.tournament_select(population)

                        child = self.crossover_2(parent_one, parent_two, 0.5)
                    
                # perform mutate some percentage of the time
                # elif rand <= 0.93:
                #     self.mutate_2(parent_one)
                #     child = parent_one
                
                else:
                    child = self.mutate(parent_one)

                    while child == None:
                        parent_one = self.tournament_select(population)
                        child = self.mutate(parent_one)
                    # child = parent_one

                # make a new individual
                # else:
                #     child = Individual(self.l, self.w)
                #     child.get_fitness(self.target_image)

                # add mutated or crossed indiv to new_pop
                new_pop.append(child)

            # set population = new_pop
            population = new_pop
            
            if i % 100 == 0 or i == epochs - 1:
                data['epoch'].append(i)
                data['fitness_estimate'].append(fittest_estimate)
                data['crossover_used'].append("crossover_1")
                data['pop_gen_used'].append("random_image_array_1")
                data['im_size'].append("(" + str(self.w) + "," + str(self.l) + ")")
            
            if i % 100 == 0 or i == epochs - 1:
                print("Most fit individual in epoch " + str(i) +
                      " has fitness: " + str(fittest_estimate))
                
                data_df = DataFrame(data)
    
                data_df.to_csv("data_cross.csv")

            # fittest.to_image()
#             Image.fromarray(fittest.array).show()

            # fittest = Image.fromarray(fittest.array)
            
#             fittest.save("fittest.png", "PNG")

        data_df = DataFrame(data)
    
        data_df.to_csv("data_cross.csv")

        population.sort(key=lambda ind: ind.fitness)
        fittest = population[0]

        return fittest

#             display(fittest)

    def tournament_select(self, population):
        tournament_size = 6

        indices = np.random.choice(len(population), tournament_size)

        random_subset = [population[i] for i in indices]

        winner = None

        for i in random_subset:
            if (winner == None):
                winner = i

            elif i.fitness < winner.fitness:
                # if current tree is more fit than current winner
                winner = i

        return winner

    def crossover(self, ind1, ind2):
        child = Individual(self.l, self.w)

        # random float between 0 and 1 
        blend_alpha = random.random()

        # child_image = Image.blend(ind1.image, ind2.image, 0.5)

        # if alpha is 0.0, a copy of the first image is returned. 
        # If alpha is 1.0, a copy of the second image is returned.
        # use a random blend_alpha \in (0,1) 
        child_image = Image.blend(ind1.image, ind2.image, blend_alpha)
        child.image = child_image
        child.array = np.array(child_image)
        child.get_fitness(self.target_image)

        if child.fitness == min(ind1.fitness, ind2.fitness, child.fitness):
            return child

        return None
    
    def crossover_2(self, ind1, ind2, horizontal_prob):

        rand = random.random()

        # perform horizontal crossover point 
        if rand <= horizontal_prob:

            split_point = random.randint(1, self.w)
            
            first = np.ones((split_point, self.l))
            first = np.vstack((first, np.zeros((self.w-split_point, self.l))))

        # perform vertical crossover point 
        else:
            split_point = random.randint(1, self.l)
        
            first = np.ones((self.w, split_point))

            first = np.hstack((first, np.zeros((self.w, self.l-split_point))))
            
        second = 1 - first

        # Creates the 4 dimensional versions to perform the mutliplying across all color channels 
        first = np.dstack([first,first,first,first])
        second = np.dstack([second,second,second,second])

        # Multiply parent1 with first and multiply parent2 with second. Then simplay add them element wise and it should produce the crossover child.

        half_chromo_1 = np.multiply(first, ind1.array)
        half_chromo_2 = np.multiply(second, ind2.array)
        
        child_array = np.add(half_chromo_1, half_chromo_2)
        
        child = Individual(self.l, self.w)
        
        child.image = Image.fromarray(child_array.astype(np.uint8))
        child.array = child_array.astype(np.uint8)
        
        child.get_fitness(self.target_image)

        # elitism 
        if child.fitness == min(ind1.fitness, ind2.fitness, child.fitness):
            return child

        return None

    def crossover_3(self, ind1, ind2):
        first = np.random.randint(2, size=(self.w, self.l, 4))
        
        second = 1 - first
        
        half_chromo_1 = np.multiply(first, ind1.array)
        
        half_chromo_2 = np.multiply(second, ind2.array)
        
        child_array = np.add(half_chromo_1, half_chromo_2)
        
        child = Individual(self.l, self.w)
        
        child.image = Image.fromarray(child_array.astype(np.uint8))
        child.array = child_array.astype(np.uint8)
        
        child.get_fitness(self.target_image)
        
        return child

    def mutate(self, ind):

        iterations = random.randint(1, 3)
        region = random.randint(1,(self.l + self.w)//4)

        img = ind.image

        for i in range(iterations):
            num_points = random.randint(3, 6)
            region_x = random.randint(0, self.l)
            region_y = random.randint(0, self.w)

            xy = []
            for j in range(num_points):
                xy.append((random.randint(region_x - region, region_x + region),
                           random.randint(region_y - region, region_y + region)))

            img1 = ImageDraw.Draw(img)
            img1.polygon(xy, fill=ind.rand_color())

        child = Individual(ind.l, ind.w)
        child.image = img
        child.array = child.to_array(child.image)
        child.get_fitness(self.target_image)

        return child 

        if child.fitness == min(ind.fitness, child.fitness):
            return child

        return None

        
    def mutate_2(self, ind):
        constant = 40
        
        num_pix = 40
        
        for i in range(num_pix):
            x = random.randint(0, self.l-1)
            y = random.randint(0, self.w-1)
            z = random.randint(0, 3)
            
            ind.array[x][y][z] = ind.array[x][y][z] + constant
                
        ind.image = self.to_image(ind.array)
        ind.get_fitness(self.target_image)

    def to_image(self, array):
        return Image.fromarray(array)

    def to_array(self, image):
        return np.array(image)

def main():
    gp = GP(r"mona_lisa.png")

    fittest = gp.run_gp(100, 500)
    plt.imshow(fittest.image)
    plt.show()

    # gp = GP(r"davidson2.png")

    # ind1 = Individual(100, 100)
    # plt.imshow(ind1.image)
    # plt.show()
    # ind2 = Individual(100, 100)
    # plt.imshow(ind2.image)
    # plt.show()

    # ind3 = gp.crossover_3(ind1, ind2)
    # plt.imshow(ind3.image)
    # plt.show()





if __name__ == "__main__":
    main()
