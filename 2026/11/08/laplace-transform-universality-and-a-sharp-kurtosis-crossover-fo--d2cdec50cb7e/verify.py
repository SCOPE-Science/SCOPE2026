#!/usr/bin/env python3
"""Exact checks for the renewal run/rest harmonic-confinement theorem.
Only Python standard library is needed; finite tests do not replace the proof.
"""
from fractions import Fraction as F
from itertools import product

def solve(matrix, vector):
    n = len(vector)
    a = [list(map(F, matrix[i])) + [F(vector[i])] for i in range(n)]
    for j in range(n):
        i = next(i for i in range(j, n) if a[i][j])
        a[j], a[i] = a[i], a[j]
        pivot = a[j][j]
        for k in range(j, n+1):
            a[j][k] /= pivot
        for i in range(n):
            if i == j: continue
            scale = a[i][j]
            for k in range(j, n+1):
                a[i][k] -= scale*a[j][k]
    return [a[i][-1] for i in range(n)]

def finite_state_moments(a,b,k):
    assert a>0 and b>0 and k>=1
    size=k+2
    Q=[[F(0) for _ in range(size)] for _ in range(size)]
    for i in range(2):
        Q[i][i]=-a
        Q[i][2]=a
    for j in range(k-1):
        Q[2+j][2+j]=-b
        Q[2+j][2+j+1]=b
    Q[-1][-1]=-b
    Q[-1][0]=Q[-1][1]=b/2
    P=[b/(2*(b+k*a)),b/(2*(b+k*a))]+[a/(b+k*a)]*k
    assert sum(P)==1
    v=[F(1),F(-1)]+[F(0)]*k
    moments={0:F(1)}
    for n in range(1,5):
        A=[[n*(i==j)-Q[j][i] for j in range(size)] for i in range(size)]
        P=solve(A,[n*v[i]*P[i] for i in range(size)])
        moments[n]=sum(P)
    return moments

def renewal_moments(a,mean,t2,t4):
    rr=lambda j:a/(a+j)
    u2=1-2*rr(1)+rr(2)
    u22=rr(2)-2*rr(3)+rr(4)
    u4=1-4*rr(1)+6*rr(2)-4*rr(3)+rr(4)
    # Moment recursion for the embedded run-beginning affine perpetuity.
    y2=t2*u2/(1-t2*rr(2))
    y4=t4*(6*u22*y2+u4)/(1-t4*rr(4))
    z2=rr(2)*y2+u2
    z4=rr(4)*y4+6*u22*y2+u4
    duration=1/a+mean
    m2=(y2/(a+2)+u2/a+(1-t2)*z2/2)/duration
    m4=(y4/(a+4)+6*u22*y2/a+u4/a+(1-t4)*z4/4)/duration
    return m2,m4

def erlang2_closed(a,b):
    m2=b/((a+1)*(2*a+b))
    m4=3*b*(b+2)**2/((a+1)*(a+3)*(2*a+b)*(2*a*b+2*a+b*b+4*b+4))
    return m2,m4

def exponential_closed(a,c):
    return (c/((a+1)*(a+c)),
            3*c*(c+2)/((a+1)*(a+3)*(a+c)*(a+c+2)))

def critical_poly(a,b):
    return 3*a*a*b+4*a*a-2*a*b*b+a*b+4*a-b**3-4*b*b-4*b

def exp_poly(a,c):
    return a*a-a*c+a-c*c-2*c

checks=0
rates_a=[F(1,3),F(1,2),F(1),F(3,2),F(2),F(5)]
rates_b=[F(1,4),F(1,2),F(1),F(4),F(7)]
for k,a,b in product([1,2,3],rates_a,rates_b):
    t2=(b/(b+2))**k
    t4=(b/(b+4))**k
    ms=finite_state_moments(a,b,k)
    m2,m4=renewal_moments(a,F(k,1)/b,t2,t4)
    assert ms[1]==ms[3]==0
    assert (ms[2],ms[4])==(m2,m4)
    if k==2:
        assert (m2,m4)==erlang2_closed(a,b)
        K=m4-3*m2*m2
        numer=critical_poly(a,b)
        denom=(a+1)**2*(a+3)*(2*a+b)**2*(2*a*b+2*a+b*b+4*b+4)
        assert K==6*b*numer/denom
    if k==1:
        assert (m2,m4)==exponential_closed(a,b)
    checks+=1

for a,c in product(rates_a,rates_b):
    # Exact polynomial division; holds identically as shown in the proof.
    assert critical_poly(a,2*c)==(6*c+4)*exp_poly(a,c)-2*c*c*(a+c)
    checks+=1

# Exact rational root isolations for three illustrative parameters.
for a,lo,hi in [(F(1),F(1064177,1000000),F(1064178,1000000)),
                (F(2),F(2112402,1000000),F(2112403,1000000)),
                (F(5),F(5173535,1000000),F(5173536,1000000))]:
    assert critical_poly(a,lo)>0 and critical_poly(a,hi)<0
    checks+=1
print('VERIFIED',checks,'independent exact-rational cases; arbitrary-Erlang renewal reward vs full CTMC generators for k=1,2,3.')
