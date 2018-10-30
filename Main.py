from Regressor import Regressor


def scan_test_cases_n(f):
    """read number of test cases from file"""
    return int(f.readline())


def scan_input(f):
    """read n, x, y, degree and return them """
    line = list(map(int, f.readline().split()))
    points_n = line[0]
    degree = line[1]
    x, y = [], []
    for j in range(points_n):
        line = list(map(float, f.readline().split()))
        x.append(line[0])
        y.append(line[1])
    return points_n, degree, x, y


if __name__ == '__main__':
    f = open('input.txt')
    test_cases_n = scan_test_cases_n(f)
    for i in range(test_cases_n):
        # print(scan_input(f))
        regressor = Regressor(scan_input(f))
