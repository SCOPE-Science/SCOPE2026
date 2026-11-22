"""Reproduce exact-arithmetic and spectral checks for one-step coordinate-sketched Ritz values.
Run: python verify.py
"""
from fractions import Fraction as F
from math import sqrt, atan, pi, sin, cos
from itertools import combinations
import numpy as np
from scipy.linalg import qr

checks=0

def check(c, label='assertion'):
    global checks
    if not c:
        raise AssertionError(label)
    checks+=1

# Exact rational dimension-37 counterexample. A = I + t*t.T/72,
# t = (-6, 1, ..., 1), b = constant. For a row subset, the
# one-dimensional sampled Ritz value is the average row sum.
n=37
t=(-6,)+(1,)*36
check(sum(x*x for x in t)==72)
A=[[F(i==j)+F(t[i]*t[j],72) for j in range(n)] for i in range(n)]
row_sums=[sum(row) for row in A]
check(row_sums[0]==F(-3,2))
for j in range(1,n):
    check(row_sums[j]==F(17,12))
for s in range(2,n+1):
    selected=(0,)+tuple(range(1,s))
    theta=sum((row_sums[j] for j in selected),F(0))/s
    check(theta==F(-18+17*(s-1),12*s))
    if s==2: check(theta==F(-1,24))
    if s==3: check(theta==F(4,9))
# Full ordinary Rayleigh quotient is between the two SPD eigenvalues.
check(sum(row_sums)/n==F(99,74))

# Q-DEIM on the exact two-vector Krylov space: row 0 is the unique
# maximum-leverage first pivot; the second must be an ordinary row.
for n in [3,4,6,10,17,35,37,50,100]:
    v=np.ones(n)/sqrt(n)
    w=np.ones(n)/sqrt(n*(n-1))
    w[0]=-sqrt((n-1)/n)
    check(abs(v@w)<1e-12)
    V=np.column_stack([v,w])
    _,_,p=qr(V.T,pivoting=True, mode='economic')
    check(p[0]==0)
    check(p[1]!=0)
    # Only the exceptional coordinate can distinguish the two row types.
    for j,k in combinations(range(1,min(n,7)),2):
        check(abs(np.linalg.det(V[[j,k],:])) < 1e-12)
    for j in range(1,min(n,7)):
        check(abs(np.linalg.det(V[[0,j],:])) > 1e-12)

# Direct finite-dimensional matrix and QR verification of sharp extrema
# for a range of dimensions, sketch sizes and condition numbers.
for n in [3,4,10,17,35,36,37,50,100]:
    v=np.ones(n)/sqrt(n)
    w=np.ones(n)/sqrt(n*(n-1))
    w[0]=-sqrt((n-1)/n)
    for K in [1.2,2.0,5.0,20.0]:
        for s in sorted(set([2,3,min(n,5),max(2,n//2),n])):
            if s>n: continue
            d=(n-s)/(s*sqrt(n-1))
            lo=(K+1)/2 - (K-1)*sqrt(1+d*d)/2
            hi=(K+1)/2 + (K-1)*sqrt(1+d*d)/2
            for phi in [0.17,0.41,0.9,1.2,(pi-atan(d))/2, -atan(d)/2]:
                u=cos(phi)*v+sin(phi)*w
                Av=v+(K-1)*u*(u@v)
                chosen=np.arange(s)
                h=(v[chosen]@Av[chosen])/(v[chosen]@v[chosen])
                predicted=1+(K-1)*(cos(phi)**2-d*sin(phi)*cos(phi))
                check(abs(h-predicted)<2e-11)
                check(lo-1e-11 <=h <= hi+1e-11)
                if phi==(pi-atan(d))/2:
                    check(abs(h-lo)<2e-11)
                if phi==-atan(d)/2:
                    check(abs(h-hi)<2e-11)
            safe=(s > n/(1+2*sqrt(K*(n-1))/(K-1)))
            check(safe==(lo>0))

check((35-2)**2>=32*(35-1))
check((34-2)**2<32*(34-1))
print('VERIFY_OK',checks)
