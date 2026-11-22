"""Exact consistency checks for fractional Volterra self-commutator theorem.

Standard-library only; finite checks are not substitutes for the analytic proof.
"""
from fractions import Fraction as Q
from math import comb, factorial


def determinant(matrix):
    a = [list(map(Q, row)) for row in matrix]
    n = len(a)
    sign = 1
    value = Q(1)
    for k in range(n):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return Q(0)
        if pivot != k:
            a[pivot], a[k] = a[k], a[pivot]
            sign = -sign
        p = a[k][k]
        value *= p
        for i in range(k + 1, n):
            c = a[i][k] / p
            if c:
                for j in range(k + 1, n):
                    a[i][j] -= c * a[k][j]
                a[i][k] = Q(0)
    return sign * value


def coefficient_matrix(m):
    """Expand endpoint-primitive expression for exact kernel K_m."""
    n = 2 * m
    A = [[Q(0) for j in range(n)] for i in range(n)]
    den = factorial(m-1) ** 2
    for p in range(m):
        for q in range(m):
            c = Q((-1)**(p+q)*comb(m-1,p)*comb(m-1,q),
                  den*(p+q+1))
            # G(x), G(y), -G(1) at t=1; G(0)=0
            A[m+q][m-1-q] += c
            A[m-1-p][m+p] += c
            A[m-1-p][m-1-q] -= c
    return A


def check_integer(m):
    A = coefficient_matrix(m)
    n = 2*m
    assert all(A[i][j] == A[j][i] for i in range(n) for j in range(n))
    for i in range(n):
        for j in range(n):
            if i+j > n-1:
                assert A[i][j] == 0
        j=n-1-i
        expected=Q((-1)**(m-1-min(i,j)), factorial(i)*factorial(j))
        assert A[i][j] == expected
    det_A=((-1)**m)*Q(1, ( __import__('math').prod(factorial(j) for j in range(n)))**2)
    assert determinant(A)==det_A
    H=[[Q(1,i+j+1) for j in range(n)] for i in range(n)]
    det_H=__import__('math').prod(Q(factorial(j)**4,
                            factorial(2*j)*factorial(2*j+1)) for j in range(n))
    assert determinant(H)==det_H
    AH=[[sum((A[i][k]*H[k][j] for k in range(n)),Q(0))
         for j in range(n)] for i in range(n)]
    expected_product=((-1)**m)*Q(
       __import__('math').prod(factorial(j)**2 for j in range(n)),
       __import__('math').prod(factorial(j) for j in range(2*n)))
    assert determinant(AH)==expected_product


def check_vandermonde(alpha, n):
    assert alpha>0 and alpha.denominator!=1
    nodes=[Q(j+2,j+11) for j in range(n)]
    assert len(set(nodes))==n
    # Fractional series coefficients, with common nonzero Gamma factor omitted.
    for k in range(n):
        binom=Q(1)
        for j in range(k):
            binom *= (alpha-1-j)/Q(j+1)
        assert binom!=0
    V=[[node**(-k) for node in nodes] for k in range(n)]
    assert determinant(V)!=0


def main():
    for m in range(1,7):
        check_integer(m)
    for alpha in (Q(1,2),Q(3,2),Q(7,3),Q(11,4)):
        for n in range(1,8):
            check_vandermonde(alpha,n)
    print('PASS: m=1,...,6 exact polynomial-kernel and spectral-product identities;')
    print('PASS: 28 noninteger finite Vandermonde consistency certificates.')

if __name__=='__main__':
    main()
