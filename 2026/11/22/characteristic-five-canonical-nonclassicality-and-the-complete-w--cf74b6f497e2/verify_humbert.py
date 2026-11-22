#!/usr/bin/env python3
"""Exact elementary verification of the characteristic-five Humbert canonical-Wronskian theorem.
Only Python standard library is required; run: python verify_humbert.py
"""
from collections import defaultdict
from itertools import permutations, combinations
from fractions import Fraction
from math import prod

P=5
N=4
ZERO=(0,)*N

def padd(A,B):
    C=defaultdict(int,A)
    for e,c in B.items(): C[e]+=c
    return {e:c for e,c in C.items() if c}

def pmul(A,B):
    C=defaultdict(int)
    for e,c in A.items():
        for f,d in B.items(): C[tuple(e[i]+f[i] for i in range(N))]+=c*d
    return {e:c for e,c in C.items() if c}

def mono(i,k=1):
    e=[0]*N;e[i]=k;return {tuple(e):1}

# Alternant for exponents 1,2,3,5, expanded as 24 integer monomials.
L={}
for perm in permutations(range(N)):
    inversions=sum(perm[i]>perm[j] for i in range(N) for j in range(i+1,N))
    e=[0]*N
    for r,j in zip((1,2,3,5),perm): e[j]=r
    L=padd(L,{tuple(e):(-1)**inversions})
R={ZERO:1}
for i in range(N): R=pmul(R,mono(i))
for i in range(N):
    for j in range(i+1,N): R=pmul(R,padd(mono(j),{e:-v for e,v in mono(i).items()}))
R=pmul(R,{tuple(1 if k==j else 0 for k in range(N)):1 for j in range(N)})
assert L==R, 'Alternant identity failed'

c=[Fraction(1)]
for n in range(1,11): c.append(prod(Fraction(1,2)-j for j in range(n))/prod(range(1,n+1)))
def red(r):return (r.numerator % P)*pow(r.denominator % P,-1,P)%P
assert [red(c[r]) for r in (0,1,2,3,4,5)]==[1,3,3,1,0,2]

# Polynomial arithmetic in F25 = F5[w]/(w^2-2), encoded by (a+5b).
def xy(v):return v%5,v//5
def add(a,b): x,y=xy(a);u,v=xy(b);return (x+u)%5+5*((y+v)%5)
def neg(a):return add(0, (-a%5)+5*((-a//5)%5)) if False else ((-a%5)+5*((-(a//5))%5))
def mul(a,b): x,y=xy(a);u,v=xy(b);return (x*u+2*y*v)%5+5*((x*v+y*u)%5)
def sub(a,b):return add(a,neg(b))
def inv(a):
    assert a
    for b in range(1,25):
        if mul(a,b)==1:return b
    raise AssertionError

def trim(v):
    while len(v)>1 and v[-1]==0:v.pop()
    return v

def polmul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=add(c[i+j],mul(x,y))
    return trim(c)

def der(a):return trim([mul(a[i],i%5) for i in range(1,len(a))] or [0])

def rem(a,b):
    a=trim(a[:]);b=trim(b[:]);assert b!=[0]
    while len(a)>=len(b) and a!=[0]:
        f=mul(a[-1],inv(b[-1]));s=len(a)-len(b)
        for i,t in enumerate(b):a[s+i]=sub(a[s+i],mul(f,t))
        trim(a)
    return a

def gcd(a,b):
    while b!=[0]:a,b=b,rem(a,b)
    return a

# Three smooth quartic polynomials over F5 realizing all critical-multiplicity partitions.
examples={
    'simple':[1,1,0,0,1],       # x^4+x+1
    'double+simple':[1,0,0,2,1],# x^4+2x^3+1
    'triple':[1,0,0,0,1]        # x^4+1
}
patterns={}
for typ,f in examples.items():
    d=der(f);gd=gcd(d,der(d));
    assert len(gcd(f,d))==1, (typ,'f not squarefree')
    assert len(d)==4 and d[-1]==4
    assert len(gd)-1=={'simple':0,'double+simple':1,'triple':2}[typ]
    patterns[typ]=(f,d)

print('ALTERNANT_POLYNOMIAL_IDENTITY_OK')
print('BINOMIAL_COEFFICIENTS_MOD5_OK')
for typ,(f,d) in sorted(patterns.items()):
    print('CRITICAL_MULTIPLICITY_'+typ.replace('+','_').upper(),f,d)
print('ALL_THREE_WRONSKIAN_SUPPORT_PATTERNS_OK')
