from Individual import Individual
from GP2 import GP
import matplotlib.pyplot as plt

"""4 Initial Individuals Example"""

def four_initial_example():

    ind1 = Individual(200,200)
    ind2 = Individual(200,200)
    ind3 = Individual(200,200)
    ind4 = Individual(200,200)

    f, axarr = plt.subplots(2,2)
    axarr[0,0].imshow(ind1.image)
    axarr[0,0].set_title("Initial Individual 1")
    axarr[0,1].imshow(ind2.image)
    axarr[0,1].set_title("Initial Individual 2")
    axarr[1,0].imshow(ind3.image)
    axarr[1,0].set_title("Initial Individual 3")
    axarr[1,1].imshow(ind4.image)
    axarr[1,1].set_title("Initial Individual 4")
    plt.show()

def crossover_illustration():
    ind1 = Individual(200,200)
    ind2 = Individual(200,200)

    gp = GP(r"davidson3.png")

    child1 = gp.crossover(ind1,ind2)
    
    f, axarr = plt.subplots(1,3)
    axarr[0].imshow(ind1.image)
    axarr[0].set_title("Parent 1")
    axarr[1].imshow(ind2.image)
    axarr[1].set_title("Parent 2")
    axarr[2].imshow(child1.image)
    axarr[2].set_title("Child")
    plt.show()

    child2 = gp.crossover_2(ind1,ind2)
    
    f, axarr = plt.subplots(1,3)
    axarr[0].imshow(ind1.image)
    axarr[0].set_title("Parent 1")
    axarr[1].imshow(ind2.image)
    axarr[1].set_title("Parent 2")
    axarr[2].imshow(child2.image)
    axarr[2].set_title("Child")
    plt.show()

    child3 = gp.crossover_3(ind1,ind2)
    
    f, axarr = plt.subplots(1,3)
    axarr[0].imshow(ind1.image)
    axarr[0].set_title("Parent 1")
    axarr[1].imshow(ind2.image)
    axarr[1].set_title("Parent 2")
    axarr[2].imshow(child3.image)
    axarr[2].set_title("Child")
    plt.show()

def mutation_illustration():
    ind1 = Individual(200,200)
    ind2 = Individual(200,200)

    gp = GP(r"davidson3.png")
    
    f, axarr = plt.subplots(1,2)
    axarr[0].imshow(ind1.image)
    axarr[0].set_title("Pre-Mutation")
    # mutate 
    gp.mutate(ind1)
    axarr[1].imshow(ind1.image)
    axarr[1].set_title("Post-Mutation")
    plt.show()
    
    f, axarr = plt.subplots(1,2)
    axarr[0].imshow(ind2.image)
    axarr[0].set_title("Pre-Mutation")
    # mutate 
    gp.mutate_2(ind2)
    axarr[1].imshow(ind2.image)
    axarr[1].set_title("Post-Mutation")
    plt.show()

