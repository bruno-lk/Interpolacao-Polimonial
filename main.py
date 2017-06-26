# Atividade de calculo de interpolacoes polinomias
# Metodos: Lagrange, Newton e minimos quadrados
# Linugaguem: Python 2.7
# Aluno: Bruno Nogueira de Carvalho

def main():
    points = [[1, 3], [2, 5], [3, 1]]  # [x,y]
    x = 2.66  # questao 3

    print "pontos: ", points
    print "x =", x, "\n"
    print "Interpolacao pelo metodo de Lagrange:", lagrange(points, x)
    print "Interpolacao pelo metodo de Newton:", newton(points, x)
    # print "Metodo dos minimos quadrados:", mmq(points, x)


def lagrange(points, x):
    n = len(points)
    L = []
    total = 0

    for i in range(n):
        xi, yi = points[i]

        for j in range(n):
            if i == j:
                continue
            xj, yj = points[j]
            L.append((x - xj)/float(xi - xj))

    for i in range(n):
        # print points[i][1]
        total += points[i][1] * L[i]

    return total


def newton(points, x):
    # codigo usado como base: https://gist.github.com/KelviNosse/3979bb6878c926ea98dd7923740f9833
    n = len(points)
    matriz = [0.0] * n
    for i in range(n):
        matriz[i] = [0.0] * n

    for i in range(1, n):
        for j in range(1, n):
            matriz[i][j] = ((points[j][1] - points[j-1][1]) / float(points[i][0] - points[i-1][0]))

    aprx = 0
    mul = 1.0
    for i in range(n):
        mul = matriz[i][i]
        for j in range(1, i+1):
            mul *= x - points[j-1][0]
        aprx += mul

    return aprx

def mmq():
    pass

if __name__ == "__main__":
    main()
