

class Regressor:
    def __init__(self, args):
        self.points_n = args[0]
        self.degree = args[1]
        self.x = [args[2]]
        self.y = args[3]
        # print(self.x)
        # print(self.x.shape[0])
        # print(self.x.shape[1])
        self.add_degrees()
        print(len(self.x))

    def add_degrees(self):
        for i in range(2, self.degree+1):
            self.x.append([pow(j, i) for j in self.x[0]])



