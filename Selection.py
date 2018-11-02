from numpy import sum, power, dot
import numpy
import random


def select_n_pairs(n, population, x, y):
    return [select_pair(population, x, y) for i in range(n)]


def select_pair(population, x, y):
    return select(population, x, y), select(population, x, y)


def select(population, x, y):
    """since we prefer chromosomes with small mse, Our roulette wheel will
    behave different. We will start with all fitness of all population, then
    we start removing fitness of every chromosome. if fitness is small a bigger
    chance to be choosen and vice versa"""
    all_fitness = get_all_fitness(population, x, y)
    # print(all_fitness)
    lucky = random.uniform(0, all_fitness)
    # print("lucky:", lucky)
    for chromosome in population:
        # print("fitness of chromosome", fitness(x, y, chromosome))
        all_fitness -= fitness(x, y, chromosome)
        # print("all fitness:", all_fitness)
        if lucky <= all_fitness:
            return chromosome
    return population[len(population) - 1]


def fitness(x, y, theta):
    """return mean squared error, Also works as fitness function"""
    return sum(power((dot(x.transpose(), theta) - y), 2)) / len(x)


def get_all_fitness(population, x, y):
    return sum([fitness(x, y, i) for i in population])


if __name__ == '__main__':
    thetas = numpy.array([0, 0, 0])
    population = [thetas, numpy.array([0, 0, 1]), numpy.array([1, 0, 0]), numpy.array([0, 1, 0])]
    x = numpy.array([[1, 1, 1, 1, 1], [1, 2, 3, 4, 5], [1, 4, 9, 16, 25]])
    y = numpy.array([1, 4, 9, 16, 25])

    print(select_n_pairs(2, population, x, y))
