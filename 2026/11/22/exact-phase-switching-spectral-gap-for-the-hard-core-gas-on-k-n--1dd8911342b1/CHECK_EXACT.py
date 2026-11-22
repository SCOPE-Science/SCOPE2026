"""Rational finite checks of the deleted-state cofactor identity.

Requirements: Python 3 standard library only. Tests do not replace the proof.
"""
from fractions import Fraction as F
from math import comb


def determinant(matrix):
    a = [list(row) for row in matrix]
    n = len(a)
    if n == 0:
        return F(1)
    acc = F(1)
    for k in range(n):
        r = next((i for i in range(k, n) if a[i][k]), None)
        if r is None:
            return F(0)
        if r != k:
            a[k], a[r] = a[r], a[k]
            acc = -acc
        pivot = a[k][k]
        acc *= pivot
        for i in range(k + 1, n):
            factor = a[i][k] / pivot
            for j in range(k + 1, n):
                a[i][j] -= factor * a[k][j]
            a[i][k] = F(0)
    return acc


def killed_count_matrix(n, activity, shift):
    a = [[F(0) for _ in range(n)] for _ in range(n)]
    for k in range(1, n + 1):
        i = k - 1
        a[i][i] = (n-k)*activity + k - shift
        if k < n:
            a[i][i+1] = -(n-k)*activity
        if k > 1:
            a[i][i-1] = -k
    return a


def cofactor_expression(n, lam, a):
    b = 1 + lam
    terms = []
    for j in range(n+1):
        product = F(1)
        for k in range(n+1):
            if k != j:
                product *= k*b-a
        terms.append(comb(n,j) * lam**j * product)
    return sum(terms, F(0)) / (b**n)


def main():
    checks = 0
    for n in range(1, 10):
        for lam in (F(1,2), F(1), F(2)):
            for shift in (F(1,7),F(1,3),F(2,5),F(4,7)):
                lhs=determinant(killed_count_matrix(n,lam,shift))
                rhs=cofactor_expression(n,lam,shift)
                assert lhs==rhs, (n,lam,shift,lhs,rhs)
                checks+=1
    assert determinant(killed_count_matrix(1,F(3,5),F(1)))==0
    assert determinant(killed_count_matrix(2,F(1),F(2)))==-2
    print('EXACT_COFACTOR_IDENTITIES_PASSED',checks)

if __name__=='__main__':
    main()
