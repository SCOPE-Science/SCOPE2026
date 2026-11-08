"""Finite exact diagnostic checks for Pascal transfer maps.

Standard-library only. These checks support, but do not replace, the
asymptotic Fourier argument in the accompanying proof.
"""
from math import comb, isclose
from fractions import Fraction


def binom(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def pascal_matrix(m, n):
    # Matrix from degree m+n down to degree m, with row starting at index i.
    return [[binom(n, k-i) for k in range(m+n+1)] for i in range(m+1)]


def polynomial_coefficient(y, n, k):
    return sum(y[i] * binom(n, k-i) for i in range(len(y)))


def count_check(flag, description):
    assert flag, description
    return 1


def run():
    assertions = 0
    for m in range(7):
        for n in range(1, 29):
            P = pascal_matrix(m, n)
            assertions += count_check(len(P) == m+1, ('rows',m,n))
            assertions += count_check(all(len(row)==m+n+1 for row in P), ('columns',m,n))
            # Test the integer adjoint/convolution identity on several vectors.
            for a in (-3, -1, 0, 2):
                y = [(-1)**i * (i+1+a*a) for i in range(m+1)]
                out1 = [sum(P[i][k]*y[i] for i in range(m+1)) for k in range(m+n+1)]
                out2 = [polynomial_coefficient(y, n, k) for k in range(m+n+1)]
                assertions += count_check(out1 == out2, ('adjoint',m,n,a))
            # Vandermonde's exact Gram identity.
            for i in range(m+1):
                for j in range(m+1):
                    val = sum(P[i][k]*P[j][k] for k in range(m+n+1))
                    assertions += count_check(val == binom(2*n,n+i-j), ('Gram',m,n,i,j))
    for n in range(1, 140):
        v = [binom(n,k) for k in range(n+1)]
        assertions += count_check(sum(v)==2**n, ('mass',n))
        assertions += count_check(max(v)==binom(n,n//2), ('mode',n))
        assertions += count_check(sum(t*t for t in v)==binom(2*n,n), ('sq mass',n))
        v1 = [binom(n,k)-binom(n,k-1) for k in range(n+2)]
        assertions += count_check(sum(abs(t) for t in v1)==2*binom(n,n//2), ('diff total var',n))
    # Bounded single-step block norm of the row-sum shift via elementary p=1, infinity tests.
    for m in range(1,16):
        P = pascal_matrix(m,1)
        colsum = [sum(abs(P[i][k]) for i in range(m+1)) for k in range(m+2)]
        rowsum = [sum(abs(v) for v in row) for row in P]
        assertions += count_check(max(colsum)<=2 and max(rowsum)<=2,('block bounds',m))
    print('PASS: %d exact finite assertions' % assertions)


if __name__ == '__main__':
    run()
