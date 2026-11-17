#!/usr/bin/env python3
"""Exact-rational 2x2 checks for a rank-drop bilinear-resolvent family.

All arithmetic uses fractions.Fraction. This finite consistency test is
supplementary to the analytic proof; it does not certify limiting variation.
"""
from fractions import Fraction as Q

def matrix(v):
    return tuple(tuple(Q(x) for x in row) for row in v)

def plus(u, v):
    return matrix([[u[i][j] + v[i][j] for j in range(2)] for i in range(2)])

def scale(c, u):
    return matrix([[c * u[i][j] for j in range(2)] for i in range(2)])

def mult(u, v):
    return matrix([[sum(u[i][k] * v[k][j] for k in range(2)) for j in range(2)] for i in range(2)])

def det(u):
    return u[0][0] * u[1][1] - u[0][1] * u[1][0]

def inverse(u):
    t = det(u)
    assert t != 0
    return scale(1/t, matrix([[u[1][1],-u[0][1]],[-u[1][0],u[0][0]]]))

def check_case(a,b,d,e,px,py):
    a,b,d,e,px,py = map(Q,(a,b,d,e,px,py))
    assert px*px + py*py == 1
    P=matrix([[px*px,px*py],[px*py,py*py]])
    I=matrix([[1,0],[0,1]])
    A=matrix([[d,0],[0,a]])
    B=plus(scale(b,I),scale(e-b,P))
    C=plus(plus(scale(b,A),scale(a,B)),scale(-a*b,I))
    c=d*e-(a-d)*(b-e)*px*px
    assert 0<=c<d*e
    assert det(C)==a*b*c
    assert C[0][0]>=0 and C[1][1]>=0
    K0=scale(Q(1)/(a*b),plus(scale(b*d+a*e,I),scale(-1,C)))
    K1=scale(1/a,plus(A,scale(-d,I)))
    K2=scale(1/b,plus(B,scale(-e,I)))
    assert plus(plus(K0,K1),K2)==I
    for m in range(9):
        for n in range(9):
            D=1+d*m+e*n+c*m*n
            L=inverse(plus(plus(plus(I,scale(m,A)),scale(n,B)),scale(m*n,C)))
            R=scale(1/D,plus(plus(K0,scale(1/(1+a*m),K1)),scale(1/(1+b*n),K2)))
            assert L==R, (m,n,c,L,R)
    return str(c), str(det(C)), str(K0[0][0]+K0[1][1])

if __name__ == '__main__':
    cases=[(8,8,3,3,Q(3,5),Q(4,5)),(8,8,3,3,Q(5,13),Q(12,13)),
           (8,8,3,3,Q(7,25),Q(24,25)),(8,8,3,3,Q(8,17),Q(15,17))]
    for case in cases:
        print('c, detC, trK0 =', check_case(*case))
    print('PASS: 4 rational cases x 81 exact matrix identities; c=0 boundary included')
