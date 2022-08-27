import numpy as np
from PIL import Image, ImageOps, ImageDraw, ImagePath
import random
import math


class Individual:
    def __init__(self, l, w):
        self.l = l
        self.w = w
        self.fitness = float('inf')
        self.array = None
        self.image = None
        self.create_random_image_array_2()

    def rand_color(self):
        return "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])

    def create_random_image_array(self):

        # Add polygons to image
        iterations = random.randint(1, 1)

        region = 40

        img = Image.new("RGBA", (self.l, self.w), self.rand_color())

        for i in range(iterations):
            num_points = random.randint(3, 7)

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

        region = 50

        img = self.image

        for i in range(iterations):
            num_points = random.randint(3, 7)

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

    def to_image(self):
        im = Image.fromarray(self.array)
        im.show()

    def to_array(self, image):
        return np.array(image)

    def get_fitness(self, target):
        diff_array = np.subtract(target, self.array)
        diff = np.sum(np.absolute(diff_array))
        self.fitness = diff
