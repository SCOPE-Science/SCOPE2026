"""Exact-rational verification for a lossy dephased three-site quantum chain.

Run with Python 3.9 or newer: python verify.py
The nine real state variables are [p1,p2,p3,Re12,Im12,Re23,Im23,Re13,Im13].
"""
from fractions import Fraction as F
from itertools import product
from math import isfinite


def fraction(value):
    return value if isinstance(value,F) else F(value)


def generator(delta, gamma, kappa):
    d, g, k = map(fraction, (delta, gamma, kappa))
    # Generators in the basis of real Hermitian 3x3 matrices.
    def action(y):
        p1,p2,p3,a,b,e,f,c,h=y
        return [
            -2*b,
            2*b-2*f,
            2*f-k*p3,
            -d*b-h-g*a/2,
            p1-p2+d*a+c-g*b/2,
            h+d*f-(g+k)*e/2,
            -c-d*e-p3+p2-(g+k)*f/2,
            f-b-k*c/2,
            a-e-k*h/2
        ]
    cols=[]
    for j in range(9):
        basis=[F(0)]*9;basis[j]=F(1)
        cols.append(action(basis))
    return [[cols[j][i] for j in range(9)] for i in range(9)]


def gauss(a,b):
    n=len(b)
    t=[[fraction(a[i][j]) for j in range(n)]+[fraction(b[i])] for i in range(n)]
    for col in range(n):
        pivot=next((j for j in range(col,n) if t[j][col]!=0),None)
        if pivot is None: raise ValueError('singular generator')
        t[col],t[pivot]=t[pivot],t[col]
        v=t[col][col]
        t[col]=[x/v for x in t[col]]
        for r in range(n):
            if r==col:continue
            z=t[r][col]
            if z: t[r]=[x-z*y for x,y in zip(t[r],t[col])]
    return [row[-1] for row in t]


def exact_integrated_state(delta,gamma,kappa):
    m=generator(delta,gamma,kappa)
    # Solve M*u=-rho(0), where u=integral_0^infty rho(t)dt.
    b=[F(-1)]+[F(0)]*8
    return gauss(m,b)


def predicted_mean(delta,gamma,kappa):
    d,g,k=map(fraction,(delta,gamma,kappa))
    return F(3)/k+(3*g+2*k)/4+d*d*k*(3*g+k)/(k*g*g+(k*k+8)*g+4*k)


def predicted_diff(delta,gamma,kappa):
    d,g,k=map(fraction,(delta,gamma,kappa))
    z=d*d
    q=3*k*g*g+(3*k*k+24-z*k*k)*g+k*(12+z*(4-k*k))
    den=k*g*g+(k*k+8)*g+4*k
    return g*q/(4*den)


if __name__=='__main__':
    count=0
    for k,d,g in product((F(1,2),F(1),F(3,2),F(2),F(5,2),F(3),F(5)),
                         (F(-7),F(-4),F(-1),F(0),F(1),F(4),F(7)),
                         (F(0),F(1,10),F(1,2),F(1),F(2),F(5))):
        u=exact_integrated_state(d,g,k)
        t=sum(u[:3])
        assert t==predicted_mean(d,g,k),(d,g,k,t,predicted_mean(d,g,k))
        assert t-predicted_mean(d,0,k)==predicted_diff(d,g,k)
        assert u[2]==F(1)/k
        assert u[4]==F(1,2)==u[6]
        assert u[7]==0
        count+=1
    # At kappa=2 the exactly derived global threshold is delta^2=15.
    assert predicted_diff(4,2,2)==F(-1,10)
    assert predicted_diff(3,2,2)>0
    # At kappa=3, delta^2=4 exceeds the continuous threshold 12/5.
    assert predicted_diff(2,F(1,4),3)<0
    # At kappa=1 the first-order threshold lies strictly below 100.
    assert predicted_diff(10,10,1)<0
    print(f'PASS: {count} exact-rational, nine-variable resolvent comparisons; threshold witnesses pass')
