class Mutation:
    @staticmethod
    def mutate():
        return ""
def nonuniform_mutation(self, theta, current_generation, max_generation, dependency_factor):
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