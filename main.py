def createMatrix(matrix, size, val):
    if val == 0:
        matrix = [[0 for i in range(size)] for j in range(size)]
    elif val == 1:
        matrix = [[int(i == j) for i in range(size)] for j in range(size)]
    return matrix


def calcDet(matrix):
    size = len(matrix)
    det = 0
    if size == 2:
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return det
    minor = createMatrix(matrix, size - 1, 0)
    for k in range(len(matrix)):
        i, j = 0, 0
        while i < size:
            if i != k:
                minor[j] = matrix[i][1:]
                j += 1
            i += 1
        det += matrix[k][0] * ((-1) ** k) * calcDet(minor)
    return det


def invertMatrix(matrix):
    determinant = calcDet(matrix)
    if len(matrix) == 2:
        return [[matrix[1][1] / determinant, -1 * matrix[0][1] / determinant],
                [-1 * matrix[1][0] / determinant], matrix[0][0] / determinant]

    inverse = []
    for i in range(len(matrix)):
        inverseRow = []
        for j in range(len(matrix)):
            minor = [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]
            inverseRow.append(((-1) ** (i + j)) * calcDet(minor))
        inverse.append(inverseRow)
    inverse = list(map(list, zip(*inverse)))
    for i in range(len(inverse)):
        for j in range(len(inverse)):
            inverse[i][j] = inverse[i][j] / determinant
    return inverse


def Mul_matrix(a, b):
    temp = [0 for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a)):
            temp[i] += a[i][j] * b[j]
    return temp


def Linear_Method(list, xf):
    for i in range(len(list)):
        if list[i][0] < xf < list[i + 1][0]:
            return (list[i][1] - list[i + 1][1]) / (list[i][0] - list[i + 1][0]) * xf + (
                    (list[i + 1][1] * list[i][0]) - (list[i][1] * list[i + 1][0])) / (list[i][0] - list[i + 1][0])


def Polynomial_Method(list, xf):
    result, b = 0, [list[i][1] for i in range(len(list))]
    poly = Mul_matrix(invertMatrix(Polynomial_creation(list)), b)
    for i in range(len(poly)):
        result += poly[i] * (xf ** i)
    return result


def Lagrange_Method(list, xf):
    sum, temp = 0, 1
    for i in range(len(list)):
        for j in range(len(list)):
            if i != j:
                temp *= (xf - list[j][0]) / ((list[i][0]) - list[j][0])
        sum += temp * list[i][1]
        temp = 1
    return sum


def Polynomial_creation(list):
    for i in range(len(list)):
        list[i].insert(0, 1)
    return [[list[i][1] ** j for j in range(len(list))] for i in range(len(list))]
