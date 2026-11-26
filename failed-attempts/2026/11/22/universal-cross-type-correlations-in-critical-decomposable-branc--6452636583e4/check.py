"""Exact tests for covariance and Beta-Hankel identities in triangular branching models.

All computations are rational. This checks specified Poisson examples, not the
universal infinite-population argument in RESULT.md.
"""
from fractions import Fraction as Q
from math import factorial, comb

ASSERTIONS = 0

def eq(actual, expected):
    global ASSERTIONS
    ASSERTIONS += 1
    assert actual == expected, (actual, expected)

def det(M):
    d = Q(1)
    M = [[Q(x) for x in row] for row in M]
    for k in range(len(M)):
        pivot = M[k][k]
        assert pivot > 0
        d *= pivot
        for i in range(k + 1, len(M)):
            f = M[i][k] / pivot
            for j in range(k + 1, len(M)):
                M[i][j] -= f * M[k][j]
    return d

def coefficients(A, b):
    """Return exact covariance-polynomial highest-order coefficients.

    Every type-s individual has mutually independent Poisson offspring of
    means A[i][s], and immigration coordinates are independent Poisson(b[i]).
    """
    p = len(A)
    means = [[0] * p]
    covs = [[[0] * p for _ in range(p)]]
    for n in range(1, 2 * p + 1):
        old = means[-1]
        m = [sum(A[i][j] * old[j] for j in range(p)) + b[i] for i in range(p)]
        oldC = covs[-1]
        C = [[sum(A[i][s] * oldC[s][t] * A[j][t]
                  for s in range(p) for t in range(p)) + (m[i] if i == j else 0)
              for j in range(p)] for i in range(p)]
        means.append(m)
        covs.append(C)
    c = [1]
    for i in range(1, p):
        c.append(c[-1] * A[i][i - 1])
    for i in range(p):
        eq(means[-1][i] > 0, True)
        md = i + 1
        mean_difference = sum((-1)**(md-k)*comb(md,k)*means[k][i]
                              for k in range(md+1))
        eq(Q(mean_difference, factorial(md)), Q(b[0]*c[i], factorial(i+1)))
        for j in range(p):
            degree = i + j + 2
            finite_diff = sum((-1)**(degree-k)*comb(degree,k)*covs[k][i][j]
                              for k in range(degree + 1))
            highest = Q(finite_diff, factorial(degree))
            predicted = Q(b[0]*A[0][0]*c[i]*c[j],
                          factorial(i)*factorial(j)*(i+j+1)*(i+j+2))
            eq(highest, predicted)

def run():
    for p in range(1, 10):
        H = [[Q(1, (i+j+1)*(i+j+2)) for j in range(p)] for i in range(p)]
        value = det(H)
        expected = Q(1)
        for r in range(p):
            expected *= Q(factorial(r)**2 * factorial(r+1)**2,
                          factorial(2*r+1)*factorial(2*r+2))
        eq(value, expected)
        eq(value > 0, True)
    for p in range(1, 7):
        for case in range(3):
            A = [[0] * p for _ in range(p)]
            for i in range(p):
                for j in range(i + 1):
                    if i == j:
                        A[i][j] = 1
                    elif i == j+1:
                        A[i][j] = 1+((i+case)%3)
                    elif case in (1, 2):
                        A[i][j] = 1+((i+j+case)%2)
            b = [2 + case] + [int((i+case)%2 == 0) for i in range(1,p)]
            coefficients(A,b)
    print(f"PASS: {ASSERTIONS} exact rational checks (18 Poisson model cases, 9 Hankel sizes)")

if __name__ == '__main__':
    run()
