import numpy

class Regressor:
    def __init__(self, args):
        self.points_n = args[0]
        self.degree = args[1]
        self.x = numpy.array([args[2]])
        self.y = numpy.array(args[3])

        self.add_degrees()
        print(self.x[0])
        print(self.x[1])
        print(self.x[2])

    def add_degrees(self):
        """add polynomial degrees to the x"""
        for i in range(2, self.degree+1):
            self.x = numpy.concatenate((self.x, numpy.array([[pow(j, i) for j in self.x[0]]])), axis=0)
        self.x = numpy.concatenate(([numpy.ones(64,)], self.x), axis=0)





