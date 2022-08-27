import numpy as np
from PIL import Image, ImageOps, ImageDraw, ImagePath
from Individual import Individual
import random
import math
from pandas import DataFrame

import matplotlib.pyplot as plt

# plt.imshow(ind.image)
# plt.show()

# from IPython.display import Image


class GP:
    def __init__(self, filename):
        original_image = Image.open(filename)
        
        self.target_image = original_image.resize((100,100))

        # convert image to grayscale
        # self.target_image = ImageOps.grayscale(target_image)

        self.l, self.w = self.target_image.size
        
#         self.target_image = self.target_image.resize((int(self.w / 2), int(self.l / 2))
        
#         self.l = int(self.l / 2)
#         self.w = int(self.w / 2)
        
        self.target_image_array = self.to_array(self.target_image)
        

    def run_gp(self, pop_size, epochs):
        data = {'epoch':[], 'fitness':[], 'crossover_used':[], 'pop_gen_used':[], 'im_size':[]}
        
        population = []

        # initialize starting population
        for i in range(pop_size):
            new_indiv = Individual(self.l, self.w)

            new_indiv.get_fitness(self.target_image_array)

            population.append(new_indiv)

        for i in range(epochs):
            new_pop = []

            # populate our new population
            while len(new_pop) < len(population):
                # select parents for crossover
                parent_one = self.tournament_select(population)
                parent_two = self.tournament_select(population)
                # rand_ind = random.randint(0, len(population) - 1)
                # parent_two = population[rand_ind]

                # perform crossover some percentage of the time
                # if crossover, select another indiv
                rand = random.uniform(0, 1)

                if rand <= 0.4:
                    child = self.crossover(parent_one, parent_two)

                    while child == None:
                        parent_one = self.tournament_select(population)
                        parent_two = self.tournament_select(population)
                        # rand_ind = random.randint(0, len(population) - 1)
                        # parent_two = population[rand_ind]
                        child = self.crossover(parent_one, parent_two)
                        
                elif rand <= 0.8:
                    child = self.crossover_2(parent_one, parent_two)

                    while child == None:
                        parent_one = self.tournament_select(population)
                        parent_two = self.tournament_select(population)
                        # rand_ind = random.randint(0, len(population) - 1)
                        # parent_two = population[rand_ind]
                        child = self.crossover_2(parent_one, parent_two)
                    
                # perform mutate some percentage of the time
                elif rand <= 0.95:
                    self.mutate_2(parent_one)
                    child = parent_one

                # make a new individual
                else:
                    child = Individual(self.l, self.w)
                    child.get_fitness(self.target_image_array)

                # add mutated or crossed indiv to new_pop
                new_pop.append(child)

            # set population = new_pop
            population = new_pop
            population.sort(key=lambda ind: ind.fitness)
            fittest = population[0]
            
            if i % 100 == 0 or i == epochs - 1:
                data['epoch'].append(i)
                data['fitness'].append(fittest.fitness)
                data['crossover_used'].append("crossover_1")
                data['pop_gen_used'].append("random_image_array_1")
                data['im_size'].append("(" + str(self.w) + "," + str(self.l) + ")")
            
            if i % 1000 == 0 or i == epochs - 1:
                print("Most fit individual in epoch " + str(i) +
                      " has fitness: " + str(fittest.fitness))
                
                data_df = DataFrame(data)
    
                data_df.to_csv("data_cross.csv")

            # fittest.to_image()
#             Image.fromarray(fittest.array).show()

            # fittest = Image.fromarray(fittest.array)
            
#             fittest.save("fittest.png", "PNG")

        data_df = DataFrame(data)
    
        data_df.to_csv("data_cross.csv")

        return fittest

#             display(fittest)

    def tournament_select(self, population):
        tournament_size = 7

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

        child_image = Image.blend(ind1.image, ind2.image, 0.5)

        child.image = child_image
        child.array = np.array(child_image)
        # np.mean([ind1.array, ind2.array], axis=0)

        child.get_fitness(self.target_image_array)

        if child.fitness == min(ind1.fitness, ind2.fitness, child.fitness):
            return child

        return None
    
    def crossover_2(self, ind1, ind2):
        split_point = random.randint(1, self.w)
        
        first = np.ones((split_point, self.l))
        first = np.vstack((first, np.zeros((self.w-split_point, self.l))))
        
        second = 1 - first

#         # Creates the 4 dimensional versions to perform the mutliplying across all color channels 
        first = np.dstack([first,first,first,first])
        second = np.dstack([second,second,second,second])

#         # What is left to do is multiply parent1 with first and multiply parent2 with second. Then simplay add them element wise and it should produce the crossover child.

        half_chromo_1 = np.multiply(first, ind1.array)
        
        half_chromo_2 = np.multiply(second, ind2.array)

#         half_image_1 = Image.fromarray(half_chromo_1.astype(np.uint8))
        
#         half_image_2 = Image.fromarray(half_chromo_2.astype(np.uint8))
        
        child_array = np.add(half_chromo_1, half_chromo_2)
        
        child = Individual(self.l, self.w)
        
        child.image = Image.fromarray(child_array.astype(np.uint8))
        child.array = child_array.astype(np.uint8)
        
        child.get_fitness(self.target_image_array)
        
#         return child
        
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
        
        child.get_fitness(self.target_image_array)
        
        if child.fitness == min(ind1.fitness, ind2.fitness, child.fitness):
            return child
        
        return None
    

    def mutate(self, ind):
        ind.add_shape()
        
    def mutate_2(self, ind):
        constant = 10
        
        num_pix = 10
        
        for i in range(num_pix):
            x = random.randint(0, self.l-1)
            y = random.randint(0, self.w-1)
            z = random.randint(0, 3)
            
            ind.array[x][y][z] = ind.array[x][y][z] + constant
                
        ind.image = self.to_image(ind.array)
        ind.get_fitness(self.target_image_array)

    def to_image(self, array):
        return Image.fromarray(array)

    def to_array(self, image):
        return np.array(image)


def main():
    gp = GP(r"sky.png")

    fittest = gp.run_gp(100, 100000)
    plt.imshow(fittest.image)
    plt.show()


if __name__ == "__main__":
    main()
