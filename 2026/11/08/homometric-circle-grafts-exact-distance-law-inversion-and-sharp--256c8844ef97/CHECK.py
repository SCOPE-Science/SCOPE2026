"""Reproduce the circular-attachment distance-law calculation.
Usage: python CHECK.py
Requires only Python standard library.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import exp
import random

C=8
A=(0,1,3,4)
B=(0,1,2,5)
ELL=0.7

def distances(S,c=C):
    return tuple(sorted(min((y-x)%c,(x-y)%c) for x,y in combinations(S,2)))

def gap_multiset(S,c=C):
    S=sorted(S)
    return sorted((S[(i+1)%len(S)]-S[i])%c for i in range(len(S)))

assert distances(A)==distances(B)==(1,1,2,3,3,4)
assert gap_multiset(A)!=gap_multiset(B)

def dihedral_orbit(S,n):
    return {tuple(sorted((sgn*x+t)%n for x in S)) for sgn in (1,-1) for t in range(n)}
assert B not in dihedral_orbit(A,8)
# Finite-grid corroboration, not a proof of continuum minimality.
for n in range(4,17):
    for k in (1,2,3):
        seen={}
        for xs in combinations(range(n),k):
            signature=distances(xs,n)
            representative=min(dihedral_orbit(xs,n))
            assert signature not in seen or seen[signature]==representative
            seen[signature]=representative

# Segment as rooted tree, length ELL. U = Laplace transform of depth;
# V = Laplace transform of within-segment absolute-distance.
def laplace_law(S,ell,s,c=C):
    m=len(S)
    L=c+m*ell
    alpha=2*(-__import__('math').expm1(-s*c/2))/(s*c)
    U=-__import__('math').expm1(-s*ell)/(s*ell)
    V=2*(s*ell+__import__('math').expm1(-s*ell))/(s*s*ell*ell)
    return (c*c*alpha+2*c*m*ell*alpha*U+m*ell*ell*V+2*ell*ell*U*U*sum(exp(-s*d) for d in distances(S,c)))/(L*L)

for s in (0.17,0.7,1.43,2.7,4.1):
    assert abs(laplace_law(A,ELL,s)-laplace_law(B,ELL,s))<1e-14

def monte_carlo(S, n=130000, seed=9231):
    rng=random.Random(seed)
    m=len(S)
    L=C+m*ELL
    z=0.0
    z2=0.0
    for _ in range(n):
        # cycle location indexed -1; pendant location indexed 0..m-1
        def sample():
            v=rng.random()*L
            if v<C:
                return -1,v
            j=min(m-1,int((v-C)/ELL))
            return j,v-C-j*ELL
        (i,x),(j,y)=sample(),sample()
        if i==-1 and j==-1:
            delta=abs(x-y)
            d=min(delta,C-delta)
        elif i==-1:
            delta=abs(x-S[j])
            d=y+min(delta,C-delta)
        elif j==-1:
            delta=abs(y-S[i])
            d=x+min(delta,C-delta)
        elif i==j:
            d=abs(x-y)
        else:
            delta=abs(S[i]-S[j])
            d=x+y+min(delta,C-delta)
        w=exp(-.7*d)
        z+=w
        z2+=w*w
    avg=z/n
    sd=(max(z2/n-avg*avg,0)/n)**.5
    theory=laplace_law(S,ELL,.7)
    assert abs(avg-theory)<7*sd+0.0004,(avg,theory,sd)
    return avg,theory

v1=monte_carlo(A)
v2=monte_carlo(B,seed=12931)
assert abs(v1[1]-v2[1])<1e-14
print('CIRCULAR_ROOTED_TREE_HOMOMETRY_CLASSIFICATION_OK',distances(A),v1,v2)
