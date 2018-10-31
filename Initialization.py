import numpy


def initialize(population_size, low, hi, chromosome_length):
    """return array of random chromosomes"""
    population = []
    for i in range(population_size):
        population.append(generate_chromosome(low, hi, chromosome_length))
    return population


def generate_chromosome(low, hi, chromosome_length):
    """return array of thetas of length degree + 1, Also it acts as the chromosome"""
    return numpy.random.uniform(low=low, high=hi, size=chromosome_length)


if __name__ == '__main__':
    print(initialize(5, -10, 10, 5))
