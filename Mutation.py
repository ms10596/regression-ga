import random
import numpy
random.seed(1)
lower_bound = -10
upper_bound = 10
p_mutation = 1


def mutate(population, current_generation, max_generation, dependency_factor):
    for i in range(len(population)):
        population[i] = nonuniform_mutation(population[i], current_generation, max_generation, dependency_factor)


def nonuniform_mutation(theta, current_generation, max_generation, dependency_factor):
    r2 = random.uniform(0, 1)
    if r2 <= p_mutation:
        for i in range(len(theta)):
            r_dash = random.uniform(0, 1)
            if r_dash <= 0.5:
                y = theta[i] - lower_bound
            else:
                y = upper_bound - theta[i]
            r = random.uniform(0, 1)
            delta = y * (1 - r ** (1 - current_generation / max_generation) ** dependency_factor)

            r1 = random.uniform(0, delta)
            if r_dash <= 0.5:
                theta[i] = theta[i] - r1
            else:
                theta[i] = theta[i] + r1
            # return theta
    return theta


# if __name__ == '__main__':
#     thetas = numpy.array([0, 0, 0])
#     population = [thetas, numpy.array([0, 0, 1]), numpy.array([1, 0, 0]), numpy.array([0, 1, 0])]
#     x = numpy.array([[1, 1, 1, 1, 1], [1, 2, 3, 4, 5], [1, 4, 9, 16, 25]])
#     y = numpy.array([1, 4, 9, 16, 25])
#
#     print(population)
#     mutate(population, 5, 25, 2)
#     print(population)
