#!/usr/bin/env python3
"""Integer cross-checks for two-edge matching Walsh kernels."""
from math import factorial, comb, sqrt, pi
from itertools import product
from fractions import Fraction
import random

SIGNS=list(product((-1,1),repeat=3))

def coefficient_from_sums(columns):
    rows=[sum(v[i] for v in columns) for i in range(3)]
    corr=[[sum(v[i]*v[j] for v in columns) for j in range(3)] for i in range(3)]
    return sum(rows[i]*rows[j]-corr[i][j] for i in range(3) for j in range(i+1,3))

def direct_character(columns):
    n=len(columns)
    return sum(columns[a][i]*columns[b][j]
               for i in range(3) for j in range(i+1,3)
               for a in range(n) for b in range(n) if a!=b)

def multinomial_spectrum(n):
    fac=[factorial(j) for j in range(n+1)]
    t=[0]*8
    spectrum={}
    def visit(pos,rem):
        if pos==7:
            t[7]=rem
            S=[sum(t[h]*SIGNS[h][i] for h in range(8)) for i in range(3)]
            C=sum(sum(t[h]*SIGNS[h][i]*SIGNS[h][j] for h in range(8)) for i in range(3) for j in range(i+1,3))
            W=sum(S[i]*S[j] for i in range(3) for j in range(i+1,3))-C
            multinom=fac[n]//__import__('math').prod(fac[x] for x in t)
            spectrum[W]=spectrum.get(W,0)+multinom
            return
        for x in range(rem+1):
            t[pos]=x;visit(pos+1,rem-x)
    visit(0,n)
    assert sum(spectrum.values())==8**n
    return spectrum

def fwht(a):
    a=a[:];N=len(a); step=1
    while step<N:
        for st in range(0,N,2*step):
            for i in range(st,st+step):
                x,y=a[i],a[i+step];a[i]=x+y;a[i+step]=x-y
        step*=2
    return a

def direct_walsh_spectrum(n):
    d=3*n; a=[0]*(1<<d)
    for i in range(3):
        for j in range(i+1,3):
            for x in range(n):
                for y in range(n):
                    if x!=y:
                        a[(1<<(i*n+x))|(1<<(j*n+y))]=1
    assert sum(a)==3*n*(n-1)
    spec={}
    for w in fwht(a):spec[w]=spec.get(w,0)+1
    return spec

for n in range(2,13):
    spec=multinomial_spectrum(n)
    if n<=5:
        full=direct_walsh_spectrum(n)
        assert spec==full,(n,spec,full)
        for j in range(300):
            columns=[random.choice(SIGNS) for _ in range(n)]
            assert direct_character(columns)==coefficient_from_sums(columns)
    assert all(w%4 == (3*n*(n-1))%4 for w in spec)
    zero=(0 in spec)
    assert zero==(n%4 in (0,1))
    e2=sum(k*k*v for k,v in spec.items())
    assert e2==(8**n)*(3*n*(n-1))
    norm=Fraction(sum(abs(k)*v for k,v in spec.items()),8**n)
    print('n',n,'freqs',8**n,'coeff_types',len(spec),'zeros',spec.get(0,0),'norm',norm,'norm/n',round(float(norm/n),10))
# Constructions, all classes
for n in range(4,65):
    if n%4 in (0,1):
        base=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]*(n//4)
        if n%4==1:base.append((1,1,1))
        assert len(base)==n and coefficient_from_sums(base)==0
# Gaussian constant via independent numerical Monte Carlo
rng=random.Random(1701)
A=0.0;N=100000
for _ in range(N):
    z=[rng.gauss(0,1) for _ in range(3)]
    A+=abs(z[0]*z[1]+z[0]*z[2]+z[1]*z[2])
A/=N
assert abs(A-2/sqrt(3))<0.03
print('GAUSSIAN_CHAOS_MONTE_CARLO',A,'exact_constant',2/sqrt(3))
print('K3N_TWO_MATCHING_WALSH_ALL_CHECKS_PASS')
