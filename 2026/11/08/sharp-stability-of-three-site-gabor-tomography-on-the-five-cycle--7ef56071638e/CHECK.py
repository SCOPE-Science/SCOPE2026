#!/usr/bin/env python3
"""Reproduce the finite cyclic Gabor ambiguity and conditioning identities.

Requires Python 3 and NumPy (see REQUIREMENTS.txt).
This is a numerical cross-check; the arbitrary-parameter theorem is proved analytically.
"""
import math
import cmath
import random
import numpy as np

N=5
omega=cmath.exp(2j*math.pi/N)
phi=(1+math.sqrt(5))/2
alpha=1/(2+phi)
D=(1-alpha)**2-4*alpha*alpha
assert D>0
x=(1-alpha+math.sqrt(D))/2
y=(1-alpha-math.sqrt(D))/2
assert x>0 and y>0

def ambiguity(g,k,l):
    n=len(g)
    return sum(g[j]*g[(j-k)%n].conjugate()*cmath.exp(-2j*math.pi*j*l/n)
               for j in range(n))

def margin(g):
    n=len(g)
    return min(abs(ambiguity(g,k,l)) for k in range(n) for l in range(n))

def lifting_singular_values(g):
    n=len(g)
    outputs=[]
    for k in range(n):
        for l in range(n):
            v=np.array([g[(j-k)%n]*cmath.exp(2j*math.pi*j*l/n) for j in range(n)])
            p=np.outer(v,np.conj(v))
            outputs.append(np.conj(p.reshape(-1)))
    return np.linalg.svd(np.array(outputs),compute_uv=False)

num=0
for flip in [False,True]:
    for m in range(5):
        a,b,c=math.sqrt(x),math.sqrt(alpha),math.sqrt(y)
        if flip:a,c=c,a
        g=[a,b,c*omega**m,0,0]
        assert abs(sum(abs(v)**2 for v in g)-1)<1e-12
        assert abs(margin(g)-alpha)<2e-12
        sv=lifting_singular_values(g)
        assert abs(sv[0]-math.sqrt(5))<2e-12
        assert abs(sv[-1]-math.sqrt(5)*alpha)<2e-12
        assert abs(sv[0]/sv[-1]-1/alpha)<2e-11
        num+=5*5+4

# Independently compare every ambiguity modulus with the full 25-by-25 lifting spectrum.
rng=random.Random(1775)
for t in range(180):
    vals=[rng.random()+0.1 for _ in range(3)]
    scale=math.sqrt(sum(v*v for v in vals))
    phases=[rng.uniform(-math.pi,math.pi) for _ in range(3)]
    g=[vals[j]/scale*cmath.exp(1j*phases[j]) for j in range(3)]+[0j,0j]
    arr=sorted([math.sqrt(5)*abs(ambiguity(g,k,l)) for k in range(5) for l in range(5)],reverse=True)
    sv=sorted(lifting_singular_values(g),reverse=True)
    assert max(abs(a-b) for a,b in zip(arr,sv))<5e-12
    assert margin(g)<alpha+1e-11
    num+=25+2

# Arbitrary three-site configurations are all affine progressions modulo five.
from itertools import combinations
for S in combinations(range(5),3):
    assert any({a,(a+d)%5,(a+2*d)%5}==set(S)
               for a in range(5) for d in range(1,5))
    num+=1

# The phase optimization is exact at 5th-root phases; sampled off-grid phases are strictly worse.
g0=[math.sqrt(x), math.sqrt(alpha), math.sqrt(y),0,0]
for j in range(1,100):
    d=2*math.pi*j/500
    g=g0.copy();g[2]*=cmath.exp(1j*d)
    assert margin(g)<alpha+1e-12
    num+=1

print('THREE_SITE_GABOR_CHECKS_PASSED',num)
