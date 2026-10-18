from math import comb

def chi_closed(n, d):
    num = (1-d) ** (n+2) - 1
    assert num % d == 0
    return num // d + n + 2

def chi_chern(n, d):
    return d * sum(comb(n+2, j) * (-d) ** (n-j) for j in range(n+1))

def dual_degree(n, d):
    return d * (d-1) ** n

checks = equalities = reverse = forward = 0
for n in range(1, 101):
    for d in range(2, 101):
        c1 = chi_closed(n, d)
        c2 = chi_chern(n, d)
        assert c1 == c2, (n, d, c1, c2)

        D = dual_degree(n, d)
        A = abs(c1)
        sign = (D > A) - (D < A)

        if (n, d) == (1, 2):
            assert sign == 0 and D == A == 2
            equalities += 1
        elif d == 2:
            assert n >= 2 and sign == -1
            reverse += 1
        else:
            assert d >= 3 and sign == 1
            forward += 1
        checks += 1

assert equalities == 1
print("VERIFY_OK", checks, equalities, reverse, forward)
