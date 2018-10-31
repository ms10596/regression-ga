class Crossover:
    @staticmethod
    def cross():
        return ""

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
