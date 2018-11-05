import numpy
import Initialization, Selection, Crossover, Mutation
from numpy import sum, power, dot
from matplotlib import pyplot as plt

population_size = 1000
generations = 500
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
        self.plot(self.ga_stuff())

    def add_degrees(self):
        """add polynomial degrees to the x if needed and adding the ones column for zero degree"""
        for i in range(2, self.degree + 1):
            self.x = numpy.concatenate((self.x, numpy.array([[pow(j, i) for j in self.x[0]]])), axis=0)
        self.x = numpy.concatenate(([numpy.ones(self.points_n, )], self.x), axis=0)

    def generate_starting_thetas(self):
        """return array of thetas of length degree + 1, Also it acts as the chromosome"""
        return numpy.random.uniform(low=lower_bound, high=upper_bound, size=self.degree + 1)

    def mse(self, theta):
        """return mean squared error, Also works as fitness function"""
        return sum(power((dot(self.x.transpose(), theta) - self.y), 2)) / len(self.y)

    def plot(self, theta):
        """plot original points with green and my hypothesis with red"""
        plt.plot(self.x[1], self.y, 'go')
        plt.plot(self.x[1], dot(self.x.transpose(), theta), 'r')
        plt.title("MSE: %f" % self.mse(theta))
        plt.show()
        print(theta)

    def ga_stuff(self):
        population = Initialization.initialize(population_size, lower_bound, upper_bound, self.degree + 1)
        best_forever = population[0].copy()
        for current_generation in range(generations):
            self.sort_population(population)
            best_of_generation = population[0].copy()
            best_forever = best_of_generation.copy() if self.mse(best_of_generation) < self.mse(
                best_forever) else best_forever
            Crossover.cross(population_size // 2, population, self.x, self.y)
            Mutation.mutate(population, current_generation, generations, depending_factor)
        return best_forever

    def sort_population(self, population):
        population.sort(key=self.mse)
