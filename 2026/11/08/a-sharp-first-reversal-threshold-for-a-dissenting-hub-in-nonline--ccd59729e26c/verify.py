"""Exact first-reversal tests for the nonlinear voter star model. Pure Python."""
from fractions import Fraction
from math import exp, log, prod


def law(m, q):
    # Probability of no hub reversal from j dissenting leaves, solved as an absorbing hitting recursion.
    # Uses rates directly, independently of the product expression.
    a = [Fraction(1)] + [Fraction(0)] * m
    for j in range(1, m + 1):
        r = Fraction(j, m) ** q
        a[j] = Fraction(j, 1) * a[j - 1] / (j + r)
    return a


def product(m, q, k):
    out = Fraction(1)
    for j in range(m, k, -1):
        r = Fraction(j, m) ** q
        out *= Fraction(j, 1) / (j + r)
    return out


def solve(A, b):
    n = len(b)
    for col in range(n):
        row = next(r for r in range(col, n) if A[r][col] != 0)
        A[col], A[row] = A[row], A[col]
        b[col], b[row] = b[row], b[col]
        pivot = A[col][col]
        for j in range(col, n): A[col][j] /= pivot
        b[col] /= pivot
        for i in range(n):
            if i == col: continue
            coeff = A[i][col]
            if coeff:
                for j in range(col, n): A[i][j] -= coeff * A[col][j]
                b[i] -= coeff * b[col]
    return b


def consensus(m, q):
    # Full opposite-opinion absorbing chain, not restricted to first hub reversal.
    # State (h,k) has hub h=0 or 1; k leaves opposite to hub.
    states = [(h,k) for h in (0,1) for k in range(1,m+1)]
    pos = {z:i for i,z in enumerate(states)}
    n = len(states)
    mat = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    b = [Fraction(0) for _ in range(n)]
    for (h,k), i in pos.items():
        r = Fraction(k, m) ** q
        mat[i][i] = k + r
        if k == 1: b[i] += k if h == 1 else 0
        else: mat[i][pos[(h,k-1)]] -= k
        if m-k == 0: b[i] += r if h == 0 else 0
        else: mat[i][pos[(1-h,m-k)]] -= r
    return solve(mat,b)[pos[(1,m)]]


def main():
    tests = 0
    for m in range(2,17):
        for q in range(1,5):
            a = law(m,q)
            for k in range(m+1):
                # CDF via independent conditioning from state m down to level k:
                assert a[m] / a[k] == product(m,q,k)
                tests += 1
            assert product(m,q,0) == a[m]
            assert product(m,q,m) == 1
            assert product(m,q,0) < product(m,q,m)
    for m in range(2,9):
        for q in (1,2,3):
            c = consensus(m,q)
            p = product(m,q,0)
            assert c >= p, (m,q,c,p)
            tests += 1
    assert product(2,2,0) == Fraction(8,15)
    for m in range(2,17):
        assert product(m,1,0) == Fraction(m,m+1)**m
        assert product(m,2,0) > Fraction(1,2)
        tests += 2
    for q in (0.5,1.,1.5,2.,3.):
        for m in (100,200,500):
            calc = prod(1.0/(1+(j/m)**q/j) for j in range(1,m+1))
            assert abs(calc-exp(-1./q)) < .032, (q,m,calc)
            tests += 1
    print('VERIFY_OK',tests,'exact rational and bounded floating tests')


if __name__ == '__main__':
    main()
