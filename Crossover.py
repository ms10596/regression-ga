import random
import numpy
from Selection import select_pair

p_crossover = 1


def cross(n, population, x, y):
    for i in range(n):
        first, second = select_pair(population, x, y)
        crossover(population, first, second)


def crossover(population, first, second):
    check = random.uniform(0, 1)
    point_crossover = random.randint(0, len(population[0]))
    if check <= p_crossover:
        temp = population[first].copy()
        first_offspring = numpy.concatenate((population[first][:point_crossover],
                                             population[second][point_crossover:]))
        second_offspring = numpy.concatenate(
            (population[second][:point_crossover], temp[point_crossover:]))

        population[first] = first_offspring
        population[second] = second_offspring


if __name__ == '__main__':
    thetas = numpy.array([0, 0, 0])
    population = [thetas, numpy.array([0, 0, 1]), numpy.array([1, 0, 0]), numpy.array([0, 1, 0])]
    x = numpy.array([[1, 1, 1, 1, 1], [1, 2, 3, 4, 5], [1, 4, 9, 16, 25]])
    y = numpy.array([1, 4, 9, 16, 25])

    print(population)
    cross(100000, population, x, y)
    print(population)
