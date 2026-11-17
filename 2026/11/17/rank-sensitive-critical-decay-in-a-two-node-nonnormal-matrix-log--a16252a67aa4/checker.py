#!/usr/bin/env python3
"""Standalone checks for the two-by-two critical matrix-logistic map.

Exact rational identities are checked at finite steps. Long-run tests are
numerical diagnostics only; the asymptotic proof is in RESULT.md.
"""
from fractions import Fraction as F
from decimal import Decimal as D, getcontext


def step(x, z, y, c):
    a = x-x*x-z*z
    b = z-z*(x+y)
    d = y-y*y-z*z
    return (a+2*c*b+c*c*d, b+c*d, d)


def mm(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def tr(A):
    return [[A[0][0], A[1][0]], [A[0][1], A[1][1]]]


def inv(A):
    de=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    assert de != 0
    return [[A[1][1]/de, -A[0][1]/de], [-A[1][0]/de, A[0][0]/de]]


def assert_inverse_riccati(c, start, rounds=5):
    x,z,y=start
    S=[[F(1),-c],[F(0),F(1)]]
    for _ in range(rounds):
        H=[[x,z],[z,y]]
        Q=inv(H)
        R=inv([[F(1)-x,-z],[-z,F(1)-y]])
        Qexpected=mm(mm(tr(S),[[Q[i][j]+R[i][j] for j in range(2)] for i in range(2)]),S)
        x,z,y=step(x,z,y,c)
        assert inv([[x,z],[z,y]]) == Qexpected


def assert_rank_one(c, alpha, rounds=9):
    x,z,y=F(0),F(0),alpha
    for _ in range(rounds):
        assert x*y==z*z
        x,z,y=step(x,z,y,c)


def long_run(c, init, n):
    x,z,y=init
    for _ in range(n):
        x,z,y=step(x,z,y,c)
    return D(n)*x, D(n*n)*c*z, D(n*n*n)*c*c*y


def main():
    for c in (F(1,2), F(1)):
        assert_inverse_riccati(c,(F(1,5),F(0),F(1,7)))
        assert_rank_one(c,F(1,5))
        e=F(1,10)
        x1,z1,y1=step(e,F(0),e,c)
        assert x1+y1 == e*(1-e)*(2+c*c)
    getcontext().prec=50
    targets={
        'full':(D(4),D(6),D(12)),
        'rank1transverse':(D(3),D(3),D(3)),
        'rank1eigen':(D(1),D(0),D(0)),
    }
    for c in (D(1)/2,D(1)):
        cases={
            'full':(D(1)/5,D(0),D(1)/5),
            'rank1transverse':(D(0),D(0),D(1)/5),
            'rank1eigen':(D(1)/5,D(0),D(0)),
        }
        for kind,initial in cases.items():
            got=long_run(c,initial,20000)
            for a,b in zip(got,targets[kind]):
                assert abs(a-b)<max(D('0.18'),abs(b)*D('.04')),(c,kind,got)
            print('case',str(c),kind,'scaled',*(str(round(float(q),6)) for q in got))
    print('CRITICAL_JORDAN_MATRIX_LOGISTIC_CHECK_OK exact_inverse=10 rankone=18 asymptotic_cases=6')


if __name__=='__main__':
    main()
