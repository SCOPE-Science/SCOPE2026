#!/usr/bin/env python3
"""Exact checks for Radau IIA diffusion on complete bipartite graphs.

Requires Python 3 and SymPy. This is supplementary finite-algebra
reproducibility; the accompanying proof establishes the all-parameter claim.
"""
from fractions import Fraction as Q
import sympy as sp

p, q, h, w = sp.symbols('p q h w', positive=True)
N = p + q
D = lambda t: t*t + 4*t + 6
F = lambda t: 2*(3-t)/D(t)
fl, fq, fn = F(p*h), F(q*h), F(N*h)

# Spectral-projector expressions for each of the five entry classes.
cross = (1-fn)/N
left_off = (p+q*fn-N*fq)/(p*N)
right_off = (q+p*fn-N*fl)/(q*N)
left_diag = left_off+fq
right_diag = right_off+fl
assert sp.cancel(cross-h*(N*h+6)/D(N*h)) == 0
assert sp.cancel(left_off-h*h*q*(h*h*N*q+h*(6*p+12*q)+18)/(D(q*h)*D(N*h))) == 0
assert sp.cancel(right_off-h*h*p*(h*h*N*p+h*(12*p+6*q)+18)/(D(p*h)*D(N*h))) == 0
assert sp.cancel(sp.diff(F(h),h)-2*(h*h-6*h-18)/D(h)**2) == 0
assert sp.simplify(F(3+3*sp.sqrt(3))-(sp.Rational(5,2)-3*sp.sqrt(3)/2)) == 0

C = 32*(w+1)*(56*w+89)/(51*(32*w*w+80*w+51))
assert sp.cancel(left_diag.subs({h:8/q,p:w*q})-(-sp.Rational(5,51)+C/(q*(1+w)))) == 0
assert sp.cancel(sp.Rational(20,17)-C - 4*(32*w*w+40*w+53)/(51*(32*w*w+80*w+51))) == 0


def matrix_multiply(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def inverse(A):
    n=len(A)
    T=[row[:]+[Q(i==j) for j in range(n)] for i,row in enumerate(A)]
    for col in range(n):
        pivot=next(r for r in range(col,n) if T[r][col])
        T[col],T[pivot]=T[pivot],T[col]
        fac=T[col][col]
        T[col]=[v/fac for v in T[col]]
        for r in range(n):
            if r!=col:
                fac=T[r][col]
                if fac:
                    T[r]=[T[r][i]-fac*T[col][i] for i in range(2*n)]
    return [row[n:] for row in T]

def radau_full(p0,q0,h0):
    n=p0+q0
    L=[[Q(0) for j in range(n)] for i in range(n)]
    for i in range(p0):
        for j in range(p0,n):
            L[i][i]+=1; L[j][j]+=1
            L[i][j]-=1; L[j][i]-=1
    L2=matrix_multiply(L,L)
    num=[[Q(i==j)-h0*L[i][j]/3 for j in range(n)] for i in range(n)]
    den=[[Q(i==j)+2*h0*L[i][j]/3+h0*h0*L2[i][j]/6 for j in range(n)] for i in range(n)]
    return matrix_multiply(num,inverse(den))

def ff(z):
    return 2*(3-z)/(z*z+4*z+6)

def predicted(p0,q0,h0):
    n=p0+q0
    fn=ff(h0*n); fp=ff(h0*p0); fq=ff(h0*q0)
    ld=(Q(1,n)+Q(q0,p0*n)*fn+(1-Q(1,p0))*fq)
    rd=(Q(1,n)+Q(p0,q0*n)*fn+(1-Q(1,q0))*fp)
    lo=(p0+q0*fn-n*fq)/Q(p0*n)
    ro=(q0+p0*fn-n*fp)/Q(q0*n)
    cr=(1-fn)/Q(n)
    return [[(ld if i==j else lo) if i<p0 and j<p0 else (rd if i==j else ro) if i>=p0 and j>=p0 else cr for j in range(n)] for i in range(n)]

cases=0
for p0 in range(1,7):
    for q0 in range(p0,13):
        for h0 in (Q(1,5),Q(1,1),Q(3,2),Q(8,q0)):
            M=radau_full(p0,q0,h0)
            P=predicted(p0,q0,h0)
            assert M==P, (p0,q0,h0)
            assert all(sum(row)==1 for row in M)
            if p0+q0<=11:
                assert min(min(row) for row in M)>=0
            if p0+q0>=12 and h0==Q(8,q0):
                assert M[0][0]<0
            cases+=1

print(f'PASS: 7 universal symbolic identities, exact scalar/witness identities, {cases} full rational matrix checks')
