from functools import reduce


def calcula_raizes(coeficientes):
    factors_a = factors(abs(coeficientes[0]))
    factors_b = factors(abs(coeficientes[-1]))
    print(factors_a)
    print(factors_b)

    raizes = []

    for r in factors_b:
        for r2 in factors_a:
            raizes.append(r/r2)

    return raizes


# calcula os fatores dos numeros


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def calc_polinomio(raiz):
    return (pow(raiz, 3)+4*pow(raiz, 2) - 7*raiz - 10)


raizes = calcula_raizes([3, 12, -21, -30])
print(raizes)
raizes_negativas = list(map(lambda x: x*(-1), raizes))
print(raizes_negativas)


for r in raizes:
    print(f"{r} é raiz? {calc_polinomio(r)}")


for r in raizes_negativas:
    print(f"{r} é raiz? {calc_polinomio(r)}")
