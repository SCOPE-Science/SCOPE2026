"""Exact arithmetic checks for Gini variation of discrete polynomial projectors."""
from fractions import Fraction as Q
from itertools import combinations


def solve(A, b):
    n = len(b)
    a = [[Q(A[i][j]) for j in range(n)] + [Q(b[i])] for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if a[i][j])
        a[j], a[pivot] = a[pivot], a[j]
        v = a[j][j]
        a[j] = [x/v for x in a[j]]
        for i in range(n):
            if i == j:
                continue
            v = a[i][j]
            a[i] = [a[i][k] - v*a[j][k] for k in range(n+1)]
    return [row[-1] for row in a]


def polynomial_projector(n, degree):
    V = [[Q(i)**j for j in range(degree+1)] for i in range(n)]
    gram = [[sum(V[i][a]*V[i][b] for i in range(n))
             for b in range(degree+1)] for a in range(degree+1)]
    cols = []
    for k in range(n):
        co = solve(gram, V[k])
        cols.append([sum(V[i][j]*co[j] for j in range(degree+1))
                     for i in range(n)])
    return [[cols[k][i] for k in range(n)] for i in range(n)]


def gini(x):
    return sum(abs(x[i]-x[j]) for i in range(len(x))
               for j in range(i+1, len(x)))


def exact_cut_norm(P):
    n = len(P)
    best = Q(0)
    witness = ()
    for k in range(1, n):
        for subset in combinations(range(n), k):
            y = [sum(P[i][j] for j in subset) for i in range(n)]
            ratio = gini(y)/Q(k*(n-k))
            if ratio > best:
                best, witness = ratio, subset
    return best, witness


def quadratic_endpoint_formula(n, j):
    return Q(3*(10*j*j+(6-12*n)*j+3*n*n-3*n+2),
             n*(n+1)*(n+2))


def check():
    assert exact_cut_norm(polynomial_projector(4, 2)) == (Q(17, 15), (0,))
    print('EXACT_FOUR_SITE_SHARP_NORM_17_OVER_15_PASSED')
    degree_cases = 0
    for n in range(4, 12):
        for d in range(2, n-1):
            P = polynomial_projector(n, d)
            q = [P[i][0] for i in range(n)]
            assert sum(q) == 1
            assert sum(i*q[i] for i in range(n)) == 0
            assert sum(i*i*q[i] for i in range(n)) == 0
            assert gini(q) > n-1
            degree_cases += 1
        P2 = polynomial_projector(n, 2)
        assert all(P2[j][0] == quadratic_endpoint_formula(n, j)
                   for j in range(n))
        assert P2[n-1][0]-P2[n-2][0] == Q(24*(n-3), n*(n+1)*(n+2))
        assert gini([P2[j][0] for j in range(n)]) >= Q(n-1)+Q(48*(n-3), n*(n+1)*(n+2))
    print('EXACT_ALL_POLYNOMIAL_DEGREE_CASES_PASSED', degree_cases)
    for n in range(2, 11):
        for d in (0, 1, n-1):
            P = polynomial_projector(n, d)
            norm, _ = exact_cut_norm(P)
            assert norm == (0 if d == 0 else 1)
    print('EXACT_ALL_BOUNDARY_DEGREES_AND_BINARY_CUTS_PASSED')
    for n in (20, 50, 100, 250):
        q = [quadratic_endpoint_formula(n, i) for i in range(n)]
        ratio = gini(q)/Q(n-1)
        assert ratio > 1
        print('QUADRATIC_ENDPOINT_RATIO',n, str(ratio), float(ratio))
    def antiderivative(t):
        return Q(15, 4)*t**4 - 26*t**3 + 66*t**2 - 72*t
    correction = antiderivative(Q(2)) - antiderivative(Q(6, 5))
    assert correction == Q(64, 125)
    assert 1+correction == Q(189, 125)
    print('EXACT_CONTINUUM_INTEGRAL_189_OVER_125_PASSED')
    print('ALL_POLYNOMIAL_GINI_CHECKS_PASSED')


if __name__ == '__main__':
    check()
