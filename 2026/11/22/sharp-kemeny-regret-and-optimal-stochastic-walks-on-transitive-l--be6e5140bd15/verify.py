"""Independent exact-rational verification of a corona Kemeny trace identity.

Run with Python 3: python verify.py. Uses only standard library.
"""
from fractions import Fraction as F
from math import isclose, sqrt


def inv(a):
    n = len(a)
    rows = [[F(x) for x in row] + [F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        pivot = next(i for i in range(j,n) if rows[i][j] != 0)
        rows[j], rows[pivot] = rows[pivot], rows[j]
        z=rows[j][j]
        rows[j]=[x/z for x in rows[j]]
        for i in range(n):
            if i==j: continue
            z=rows[i][j]
            rows[i]=[x-z*y for x,y in zip(rows[i],rows[j])]
    return [row[n:] for row in rows]


def trace_pseudo(n,edges):
    L=[[F(0) for _ in range(n)] for _ in range(n)]
    for i,j,w in edges:
        w=F(w)
        L[i][i]+=w;L[j][j]+=w;L[i][j]-=w;L[j][i]-=w
    M=[[L[i][j]+F(1,n) for j in range(n)] for i in range(n)]
    T=inv(M)
    return sum(T[i][i] for i in range(n))-1


def corona(n, core, leaf):
    return list(core)+[(i,n+i,leaf[i]) for i in range(n)]

checks=0
for m in range(3,9):
    # Tests with inhomogeneous core and leaf conductances; these are not symmetric examples.
    for seed in range(3):
        core=[(i,(i+1)%m,F(1+((i+2*seed)%5),2+((3*i+seed)%4))) for i in range(m)]
        leaves=[F(1+((i+seed)%4),3+((i+2*seed)%5)) for i in range(m)]
        actual=trace_pseudo(2*m,corona(m,core,leaves))
        expected=2*trace_pseudo(m,core)+F(2*m-1,2*m)*sum(1/a for a in leaves)
        assert actual==expected,(m,seed,actual,expected)
        checks+=1
        # As a separate check, constant weights yield the exact Fourier/spectral expression.
        if seed==0:
            for a,b in [(F(1,5),F(1,4)),(F(2,7),F(1,3))]:
                if a+2*b<=1:
                    graph=[(i,(i+1)%m,b) for i in range(m)]
                    formula=F(m*m-1,6)/b+F(2*m-1,2)/a
                    assert trace_pseudo(2*m,corona(m,graph,[a]*m))==formula
                    checks+=1
# Check the analytic optimal pair, positivity, saturation and strict improvement over max-degree.
for m in range(3,101):
    B=F(m*m-1,3); C=F(2*m-1,2)
    a=sqrt(float(C))/(sqrt(float(C))+sqrt(float(B)))
    b=(1-a)/2
    optimum=(sqrt(float(B))+sqrt(float(C)))**2
    assert isclose(float(B)/(1-a)+float(C)/a,optimum,rel_tol=1e-13)
    assert 0<a<1 and b>0 and isclose(a+2*b,1,abs_tol=1e-14)
    baseline=float(B)/(2/3)+3*float(C) # B/(1-a) for a=1/3
    assert optimum<baseline
    checks+=1
# Check sharp global regret on asymmetric transition choices and equality for symmetric saturated choices.
for m in range(3,9):
    B=F(m*m-1,3)
    C=F(2*m-1,2)
    for seed in range(4):
        a=[F(1,4)+F((3*i+seed)%4,40) for i in range(m)]
        b=[F(1,10)+F((2*i+seed)%5,40) for i in range(m)]
        assert all(a[i]+b[i]+b[(i-1)%m]<=1 for i in range(m))
        core=[(i,(i+1)%m,b[i]) for i in range(m)]
        K=trace_pseudo(2*m,corona(m,core,a))
        avg=sum(a)/m
        lower=B/(1-avg)+C/avg
        assert K>=lower,(m,seed,K,lower)
        checks+=1
    a=F(1,3); b=F(1,3)
    core=[(i,(i+1)%m,b) for i in range(m)]
    K=trace_pseudo(2*m,corona(m,core,[a]*m))
    assert K==B/(1-a)+C/a
    checks+=1
print('PASS',checks,'exact-rational or analytic numerical assertions')
