import numpy
from numpy import sum, power, dot
from matplotlib import pyplot as plt
import Initialization, Selection, Crossover, Mutation
import random

p_crossover = 0.7
p_mutation = 1
population_size = 100
generations = 100
lower_bound = -10
upper_bound = 10
depending_factor = 2


class Regressor:
    def __init__(self, args):
        self.points_n = args[0]
        self.degree = args[1]
        self.x = numpy.array([args[2]])
        self.y = numpy.array(args[3])

        self.add_degrees()
        self.ga_stuff()
        self.plot()

    def add_degrees(self):
        """add polynomial degrees to the x if needed and adding the ones column for zero degree"""
        for i in range(2, self.degree + 1):
            self.x = numpy.concatenate((self.x, numpy.array([[pow(j, i) for j in self.x[0]]])), axis=0)
        self.x = numpy.concatenate(([numpy.ones(self.points_n, )], self.x), axis=0)

    def generate_starting_thetas(self):
        """return array of thetas of length degree + 1, Also it acts as the chromosome"""
        return numpy.random.uniform(low=-10, high=10, size=self.degree + 1)

    @staticmethod
    def mse(x, y, theta):
        """return mean squared error, Also works as fitness function"""
        return sum(power((dot(x.transpose(), theta) - y), 2)) / len(x)

    def plot(self):
        """plot original points with green and my hypothesis with red"""
        plt.plot(self.x[1], self.y, 'go')
        plt.plot(self.x[1], dot(self.x.transpose(), self.best_forever), 'ro')
        plt.show()
        print(self.best_forever)

    def ga_stuff(self):
        population = Initialization.initialize(population_size, lower_bound, upper_bound, self.degree + 1)
        for current_generation in range(generations):
            self.best_forever = Selection.get_best(population, self.x, self.y)
            Crossover.cross(population_size, population, self.x, self.y)
            Mutation.mutate(population, current_generation, generations, depending_factor)
