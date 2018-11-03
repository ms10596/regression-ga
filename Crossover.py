import random
import numpy
from Selection import select_pair, fitness
random.seed(1)
p_crossover = 0.7


def cross(n, population, x, y):
    for i in range(n):
        first, second = select_pair(population, x, y)
        crossover(population, first, second, x, y)


def crossover(population, first, second, x, y):
    check = random.uniform(0, 1)
    point_crossover = random.randint(0, len(population[0] - 1))
    if check <= p_crossover:
        first_offspring = numpy.concatenate((population[first][:point_crossover],
                                             population[second][point_crossover:]))
        second_offspring = numpy.concatenate(
            (population[second][:point_crossover], population[first][point_crossover:]))

        if fitness(x, y, first_offspring) + fitness(x, y, second_offspring) < fitness(x, y, population[first]) + fitness(x, y, population[second]):
            population[first] = first_offspring
            population[second] = second_offspring


# if __name__ == '__main__':
#     thetas = numpy.array([0, 0, 0])
#     population = [thetas, numpy.array([0, 0, 1]), numpy.array([1, 0, 0]), numpy.array([0, 1, 0])]
#     x = numpy.array([[1, 1, 1, 1, 1], [1, 2, 3, 4, 5], [1, 4, 9, 16, 25]])
#     y = numpy.array([1, 4, 9, 16, 25])
#
#     print(population)
#     cross(100000, population, x, y)
#     print(population)
