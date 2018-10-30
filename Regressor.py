import numpy
from numpy import sum, power, dot
from matplotlib import pyplot as plt
import random

p_crossover = 0.7
p_mutation = 1
population_size = 100
generations = 10000


class Regressor:
    def __init__(self, args):
        self.points_n = args[0]
        self.degree = args[1]
        self.x = numpy.array([args[2]])
        self.y = numpy.array(args[3])
        self.population = []

        self.add_degrees()
        self.best_theta = self.generate_starting_thetas()
        self.second_best_theta = self.generate_starting_thetas()

        self.best_forever = self.generate_starting_thetas()
        self.genetic_stuff()
        self.plot()

    def add_degrees(self):
        """add polynomial degrees to the x if needed and adding the ones column for zero degree"""
        for i in range(2, self.degree + 1):
            self.x = numpy.concatenate((self.x, numpy.array([[pow(j, i) for j in self.x[0]]])), axis=0)
        self.x = numpy.concatenate(([numpy.ones(64, )], self.x), axis=0)

    def generate_starting_thetas(self):
        """return array of thetas of length degree + 1, Also it acts as the chromosome"""
        return numpy.random.uniform(low=-10, high=10, size=self.degree + 1)

    def mse(self, theta):
        """return mean squared error, Also works as fitness function"""
        return sum(power((dot(self.x.transpose(), theta) - self.y), 2)) / self.points_n

    def plot(self):
        """plot original points with green and my hypothesis with red"""
        plt.plot(self.x[1], self.y, 'go')
        plt.plot(self.x[1], dot(self.x.transpose(), self.best_forever), 'ro')
        plt.show()
        print(self.best_forever)

    def genetic_stuff(self):
        for i in range(generations):
            self.initialize_population(population_size)
            self.select_population()
            self.crossover()

    def get_all_mse(self):
        return sum([self.mse(i) for i in self.population])

    def get_best_theta(self):
        self.population.sort(key=self.mse)
        # print(self.population)
        # print([self.mse(i) for i in self.population])

    def initialize_population(self, population_size):
        while len(self.population) < population_size:
            self.population.append(self.generate_starting_thetas())

    def select_population(self):
        self.get_best_theta()
        self.best_theta = self.population[0]
        self.second_best_theta = self.population[1]

        if self.mse(self.best_theta) < self.mse(self.best_forever):
            self.best_forever = self.best_theta.copy()
        if self.mse(self.second_best_theta) < self.mse(self.best_forever):
            self.best_forever = self.second_best_theta.copy()

    def crossover(self):
        check = random.uniform(0, 1)
        point_crossover = random.randint(0, self.degree)
        if check < p_crossover:
            temp = self.best_theta.copy()
            first_offspring = numpy.concatenate((self.best_theta[:point_crossover],
                                                 self.second_best_theta[point_crossover:]))
            second_offspring = numpy.concatenate(
                (self.second_best_theta[:point_crossover], temp[point_crossover:]))
            if self.mse(first_offspring) < self.mse(self.best_theta):
                self.best_theta = first_offspring
            if self.mse(second_offspring) < self.mse(self.second_best_theta):
                self.second_best_theta = second_offspring
