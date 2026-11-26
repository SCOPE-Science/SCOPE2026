"""Exact-rational checks for a two-cell weighted mass-preconditioner theorem.

Uses only Python's standard library. These finite checks independently assemble
local mass matrices and local inverse matrices; the general theorem is proved
algebraically in RESULT.md.
"""
from fractions import Fraction as F
import random


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def principal_two(A):
    return sum(A[i][i]*A[j][j]-A[i][j]*A[j][i]
               for i in range(3) for j in range(i+1,3))


def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
            -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
            +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))


def assemble(r, w):
    assert r > 0 and w > 0
    M = [[F(0) for _ in range(3)] for _ in range(3)]
    K = [[F(0) for _ in range(3)] for _ in range(3)]
    d = [w, w+1, F(1)]
    for cell, (length, weight) in enumerate(((r,w),(F(1),F(1)))):
        local_mass = [[length*F(2,6),length*F(1,6)],
                      [length*F(1,6),length*F(2,6)]]
        local_inv = [[F(4)/length,-F(2)/length],
                     [-F(2)/length,F(4)/length]]
        for i in range(2):
            for j in range(2):
                M[cell+i][cell+j] += local_mass[i][j]
                K[cell+i][cell+j] += weight**2 * local_inv[i][j]
    B = [[K[i][j]/(d[i]*d[j]) for j in range(3)] for i in range(3)]
    Jac = [[M[i][j]/M[i][i] for j in range(3)] for i in range(3)]
    return M, B, Jac


def test_one(r,w):
    M,B,J = assemble(r,w)
    A = mul(B,M)
    ell = F(4,3)*(1+(w-r)**2/(r*(1+w)**2))
    assert sum(A[i][i] for i in range(3)) == 2+ell
    assert principal_two(A) == 1+2*ell
    assert det3(A) == ell
    assert sum(J[i][i] for i in range(3)) == 3
    assert principal_two(J) == F(11,4)
    assert det3(J) == F(3,4)
    assert ell>=F(4,3)
    assert (ell==F(4,3))==(w==r)
    return 9


def main():
    count = 0
    random.seed(73639)
    vals=[F(1,100),F(1,7),F(1,2),F(1),F(2),F(7),F(100)]
    for r in vals:
        for w in vals+[r]:
            count+=test_one(r,w)
    for _ in range(900):
        r=F(random.randint(1,500),random.randint(1,500))
        w=F(random.randint(1,500),random.randint(1,500))
        count+=test_one(r,w)
    for r in vals:
        assert F(4,3)*(1+(r-r)**2/(r*(1+r)**2))==F(4,3)
        assert F(4,3)*(1+(1-r)**2/(r*4)) == (1+r)**2/(3*r)
        count+=2
    print(f"PASS: {count} exact-rational identities; independent two-cell local assembly")

if __name__=='__main__':
    main()
