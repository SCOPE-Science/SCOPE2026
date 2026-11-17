#!/usr/bin/env python3
"""Exact rational stationary covariance checks for a three-vehicle linear stochastic ring.
Uses standard-library Fractions and an independent 25-equation Lyapunov solve.
"""
from fractions import Fraction as F


def solve_linear(A,b):
    n=len(b)
    a=[row[:]+[v] for row,v in zip(A,b)]
    for j in range(n):
        p=next((k for k in range(j,n) if a[k][j]),None)
        if p is None: raise ArithmeticError('singular Lyapunov equation')
        a[j],a[p]=a[p],a[j]
        pivot=a[j][j]
        a[j]=[v/pivot for v in a[j]]
        for k in range(n):
            if k!=j and a[k][j]:
                z=a[k][j]
                a[k]=[u-z*v for u,v in zip(a[k],a[j])]
    return [row[-1] for row in a]


def covariance(gamma,T,alpha,sigma):
    gt=gamma/T
    z=F(0)
    B=[
        [z,z,-1,1,z],
        [z,z,z,-1,1],
        [gt+2*alpha,alpha,-gamma,z,z],
        [-alpha,gt+alpha,z,-gamma,z],
        [-gt-alpha,-gt-2*alpha,z,z,-gamma],
    ]
    Q=[[z for _ in range(5)] for _ in range(5)]
    for i in (2,3,4):Q[i][i]=sigma*sigma
    A=[];rhs=[]
    for i in range(5):
        for j in range(5):
            row=[]
            for k in range(5):
                for l in range(5):
                    row.append((B[i][k] if l==j else z)+(B[j][l] if k==i else z))
            A.append(row)
            rhs.append(-Q[i][j])
    v=solve_linear(A,rhs)
    S=[[v[5*i+j] for j in range(5)] for i in range(5)]
    assert S==[[S[j][i] for j in range(5)] for i in range(5)]
    G=(S[0][0]+S[1][1]+S[0][0]+2*S[0][1]+S[1][1])/3
    K=(S[2][2]+S[3][3]+S[4][4])/6
    H=K+alpha*G/2
    return G,K,H


def formulas(gamma,T,alpha,sigma):
    d=alpha+gamma/(2*T)-1/(4*T*T)
    assert d>0
    G=sigma*sigma/(3*gamma*d)
    K=sigma*sigma/(4*gamma)+sigma*sigma/(24*gamma*T*T*d)
    H=sigma*sigma/(12*gamma)+sigma*sigma*(2*alpha+gamma/(2*T))/(6*gamma*d)
    HD=sigma*sigma*(gamma*T-1)/(12*gamma*T*T*d*d)
    return (G,K,H,HD)


def run():
    trials=0
    for gamma,T,alpha,sigma in [
        (F(2),F(1),F(0),F(1)),
        (F(2),F(1),F(1),F(1)),
        (F(2),F(1),F(2),F(1)),
        (F(1),F(1),F(0),F(1)),
        (F(1),F(1),F(2),F(3)),
        (F(3,4),F(1),F(0),F(1)),
        (F(3,4),F(1),F(2),F(2)),
        (F(1),F(2),F(1),F(1)),
        (F(3),F(2),F(1),F(2)),
        (F(2),F(3),F(1),F(1)),
    ]:
        actual=covariance(gamma,T,alpha,sigma)
        expected=formulas(gamma,T,alpha,sigma)[:3]
        assert actual==expected,(gamma,T,alpha,sigma,actual,expected)
        trials+=1
    a=formulas(F(2),F(1),F(0),F(1))
    b=formulas(F(2),F(1),F(1),F(1))
    assert a[0]==F(2,9) and b[0]==F(2,21)
    assert a[1]==F(11,72) and b[1]==F(23,168)
    assert a[2]==F(11,72) and b[2]==F(31,168)
    assert a[0]>b[0] and a[1]>b[1] and a[2]<b[2]
    for gamma in (F(3,4),F(1),F(2)):
        left=formulas(gamma,F(1),F(1),F(1))[3]
        assert (left<0)==(gamma<1) and (left==0)==(gamma==1) and (left>0)==(gamma>1)
    print('PASS: 10 exact-rational 25-equation Lyapunov covariance tests, sharp-sign checks, rational witness')

if __name__=='__main__':run()
