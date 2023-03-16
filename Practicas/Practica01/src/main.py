def sumar(x, y):
    return x + y

def combinatoria(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

def factorial(n):
    acum = 1
    for i in range(1, n+1):
        acum = acum * i
    return acum

def permutacion(n, k):
    return factorial(n) / factorial(n - k)