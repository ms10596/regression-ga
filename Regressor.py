import numpy
from numpy import sum, power, dot


class Regressor:
    def __init__(self, args):
        self.points_n = args[0]
        self.degree = args[1]
        self.x = numpy.array([args[2]])
        self.y = numpy.array(args[3])

        self.add_degrees()
        self.thetas = self.generate_starting_thetas()

    def add_degrees(self):
        """add polynomial degrees to the x if needed and adding the ones column for zero degree"""
        for i in range(2, self.degree + 1):
            self.x = numpy.concatenate((self.x, numpy.array([[pow(j, i) for j in self.x[0]]])), axis=0)
        self.x = numpy.concatenate(([numpy.ones(64, )], self.x), axis=0)

    def generate_starting_thetas(self):
        """return array of thetas of length degree + 1"""
        return numpy.zeros(shape=(self.degree + 1, 1))

    def mse(self):
        """return mean squared error, Also works as fitness function"""
        return sum(power((dot(self.x.transpose(), self.thetas) - self.y), 2))
