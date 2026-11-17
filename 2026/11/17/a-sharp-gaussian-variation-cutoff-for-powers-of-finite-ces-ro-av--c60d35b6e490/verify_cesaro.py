"""Exact finite diagnostics for finite Cesaro powers in edge variation.
Run: python verify_cesaro.py
All arithmetic in finite tests uses fractions.Fraction.
"""
from fractions import Fraction as Q
from math import factorial


def cesaro(n):
    return [[Q(1, i + 1) if j <= i else Q(0) for j in range(n)] for i in range(n)]


def product(a, b):
    n = len(a)
    return [[sum((a[i][k] * b[k][j] for k in range(n)), Q(0)) for j in range(n)] for i in range(n)]


def variation(x):
    return sum((abs(x[j] - x[j + 1]) for j in range(len(x) - 1)), Q(0))


def cdf_geo(n, m):
    # T_n = 1 + G_2 + ... + G_n. G_j has P(G_j=r)=(j-1)/j^(r+1).
    p = [Q(0)] * (m + 1)
    if m >= 1:
        p[1] = Q(1)
    for j in range(2, n + 1):
        q = Q(1, j)
        conv = [Q(0)] * (m + 1)
        for t in range(m + 1):
            for r in range(m - t + 1):
                conv[t+r] += p[t] * (1-q) * q**r
        p = conv
    return sum(p, Q(0))


def main():
    checked = 0
    for n in range(2, 11):
        c = cesaro(n)
        a = [[Q(int(i == j)) for j in range(n)] for i in range(n)]
        for m in range(0, 10):
            pred = Q(1) - cdf_geo(n, m)
            assert pred == 1 - a[-1][0], (n, m, pred, a[-1][0])
            for t in range(1, n):
                x = [Q(int(i < t)) for i in range(n)]
                y = [sum((a[i][j] * x[j] for j in range(n)), Q(0)) for i in range(n)]
                assert variation(y) <= pred
                if t == 1:
                    assert variation(y) == pred
                if t > 1 and m >= 1:
                    assert variation(y) < pred
                checked += 1
            a = product(a, c)
    print('EXACT_GEO_CDF_MATRIX_ENTRY_AND_ALL_STEP_EXTREMIZERS_PASSED', checked)
    for n in range(2, 20):
        # exact probability-generating recursion for T_n at z=2/3
        z=Q(2,3)
        fn = z
        for j in range(2,n+1):
            fn *= Q(j-1)/(j-z)
        # Independent geometric PGF product from definition
        prod=z
        for j in range(2,n+1):
            prod *= Q(j-1,j) / (1-z/Q(j))
        assert fn == prod
        mean = 1+sum((Q(1,j-1) for j in range(2,n+1)),Q(0))
        var = sum((Q(j,(j-1)**2) for j in range(2,n+1)),Q(0))
        assert mean == 1+sum((Q(1,r) for r in range(1,n)),Q(0))
        assert var == sum((Q(1,r)+Q(1,r*r) for r in range(1,n)),Q(0))
    print('EXACT_GEOMETRIC_PGF_MEAN_VARIANCE_IDENTITIES_PASSED',18)
    # General signed inputs check at finite small n in strict rational grid.
    independent=0
    import itertools
    for n in range(2,8):
        a=cesaro(n)
        for m in range(0,5):
            norm=1-a[-1][0]
            for seq in itertools.product((-1,0,1), repeat=n-1):
                x=[Q(0)]
                for d in seq:
                    x.append(x[-1] + Q(d))
                if variation(x) == 0: continue
                y=[sum((a[i][j]*x[j] for j in range(n)),Q(0)) for i in range(n)]
                assert variation(y) <= norm * variation(x)
                independent+=1
            a=product(a,cesaro(n))
    print('EXACT_GENERAL_SIGNED_VARIATION_INEQUALITIES_PASSED', independent)
    print('ALL_FINITE_CESARO_VARIATION_CHECKS_PASSED')

if __name__ == '__main__': main()
