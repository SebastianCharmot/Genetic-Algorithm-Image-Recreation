import numpy as np
from PIL import Image, ImageOps, ImageDraw, ImagePath
from PIL import ImageDraw
from IPython.display import display
import colour

import matplotlib.pyplot as plt

import random
import math

# from IPython.display import Image

class Individual:
    def __init__(self, l, w):
        self.l = l
        self.w = w
        self.fitness = float('inf')
        self.array = None
        self.image = None
        coinflip = random.randint(1, 4)
        # if coinflip == 3:
        #     self.create_random_image_array_2()
        # else:
        self.create_random_image_array()

    def rand_color(self):
        return "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])

    def create_one_color(self):
        self.image = Image.new(mode="RGBA", size=(self.l, self.w), color=self.rand_color())

    def create_random_image_array(self):

        # number of polygons to add to image
        # the higher this is the higher stochasticity and potential for detail we have 
        iterations = random.randint(3, 6)

        region = (self.l + self.w)//8

        img = Image.new("RGBA", (self.l, self.w), self.rand_color())

        #number of points for each polygon
        for i in range(iterations):
            num_points = random.randint(3, 6)

            region_x = random.randint(0, self.l)
            region_y = random.randint(0, self.w)

            xy = []
            for j in range(num_points):
                xy.append((random.randint(region_x - region, region_x + region),
                           random.randint(region_y - region, region_y + region)))

            # xy = [
            #     ((math.cos(th) + 1) * 90,
            #      (math.sin(th) + 1) * 60)
            #     for th in [i * (2 * math.pi) / num_points for i in range(num_points)]
            # ]

            img1 = ImageDraw.Draw(img)
            img1.polygon(xy, fill=self.rand_color())

        self.image = img
        self.array = self.to_array(img)
        
    def create_random_image_array_2(self):
        self.array = np.random.randint(low = 0, high = 255, size = (self.l, self.w, 4))
        
        self.array = self.array.astype('uint8')

        self.image = Image.fromarray(self.array.astype('uint8'))

    def add_shape(self):
        iterations = random.randint(1, 1)

        region = random.randint(1,(self.l + self.w)//4)

        img = self.image

        for i in range(iterations):
            num_points = random.randint(3, 6)

            region_x = random.randint(0, self.l)
            region_y = random.randint(0, self.w)

            xy = []
            for j in range(num_points):
                xy.append((random.randint(region_x - region, region_x + region),
                           random.randint(region_y - region, region_y + region)))

            img1 = ImageDraw.Draw(img)
            img1.polygon(xy, fill=self.rand_color())

        self.image = img
        self.array = self.to_array(img)

    def to_image(self):
        im = Image.fromarray(self.array)
        im.show()

    def to_array(self, image):
        return np.array(image)


# Try this for later 
# PIL.ImageChops.difference(image1, image2)[source]
# Returns the absolute value of the pixel-by-pixel difference between the two images.
    def get_fitness(self, target):

        self.fitness = np.mean(colour.difference.delta_e.delta_E_CIE1976(target, self.array))

    def get_fitness_euclidean(self, target):
        diff_array = np.subtract(np.array(target), self.array)
        self.fitness = np.mean(np.absolute(diff_array))

# ind = Individual(175,175)
# display(ind.image)
# plt.imshow(ind.image)
# plt.show()