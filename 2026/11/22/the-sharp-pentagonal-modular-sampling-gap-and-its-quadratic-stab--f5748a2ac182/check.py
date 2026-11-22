#!/usr/bin/env python3
"""Standalone exact-integer and floating-point diagnostics for pentagonal Fourier modular sampling.
The analytic theorem does not rely on the finite numerical tests.
"""
import cmath, itertools, math

ZETA=cmath.exp(2j*math.pi/5)
PHI=(1+math.sqrt(5))/2

def conv(a,b):
    return [sum(a[i]*b[(j-i)%5] for i in range(5)) for j in range(5)]

def mk(k):
    n=[1,-1,0,0,0]
    u=[1,1,0,0,1]
    for _ in range(k): n=conv(n,u)
    return n

def det4(a):
    d=0
    for perm in itertools.permutations(range(4)):
        inv=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        t=1 if inv%2==0 else -1
        for i in range(4): t*=a[i][perm[i]]
        d+=t
    return d

def multiply_poly(a,b):
    c=[0]*7
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    for i in range(6,3,-1):
        t=c[i]
        for j in range(4): c[i-4+j]-=t
        c[i]=0
    return c[:4]

def norm_beta(n):
    assert sum(n)==0
    q=[sum(n[:j+1]) for j in range(4)]
    cols=[multiply_poly(q,[int(j==i) for j in range(4)]) for i in range(4)]
    return det4([[cols[j][i] for j in range(4)] for i in range(4)])

def four(n,k): return sum(x*ZETA**(k*j) for j,x in enumerate(n))

def projections(n):
    a=math.sqrt(2/5)*abs(four(n,1))
    b=math.sqrt((sum(n)**2)/5+(2/5)*abs(four(n,2))**2)
    return a,b

# exact integer algebraic norm checks
num=0
for v in itertools.product(range(-2,3),repeat=4):
    n=list(v)+[-sum(v)]
    if not any(n):continue
    d=norm_beta(n)
    assert d!=0 and abs(d)>=1,(n,d)
    a,b=projections(n)
    ref=(2/math.sqrt(5))*math.sqrt(abs(d))
    assert abs(a*b-ref)<2e-8*max(1,ref),(n,a,b,ref)
    num+=1
print('exact-norm-and-projection-tests',num)
for k in range(20):
    n=mk(k)
    assert sum(n)==0
    d=norm_beta(n)
    assert abs(d)==1,(k,d)
    a,b=projections(n)
    assert abs(a-math.sqrt(2/5)*abs(1-ZETA)*PHI**k)<1e-7*max(1,a)
    assert abs(b-math.sqrt(2/5)*abs(1-ZETA**2)*PHI**(-k))<1e-7*max(1,b)
    assert abs(a*b-2/math.sqrt(5))<1e-7,(k,a,b)
    if k in [0,3,6,10]:print('unit-k',k,'norm-f',round(a,7),'distance-upper',round(b,9),'product',round(a*b,9))
print('PASS')
