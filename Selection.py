from numpy import sum, power, dot
import numpy


def select():
    return ""


def fitness(x, y, theta):
    """return mean squared error, Also works as fitness function"""
    return sum(power((dot(x.transpose(), theta) - y), 2)) / len(x)


def get_all_fitness(population):
    return sum([fitness(i) for i in population])

if __name__ == '__main__':
    thetas = numpy.array([0, 0, 1])
    x = numpy.array([[1, 1, 1, 1, 1], [1, 2, 3, 4, 5], [1, 4, 9, 16, 25]])
    y = numpy.array([1, 4, 9, 16, 25])
    print(fitness(x, y, thetas))
