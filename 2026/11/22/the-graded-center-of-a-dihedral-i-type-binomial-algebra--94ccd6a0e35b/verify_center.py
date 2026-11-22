"""Recompute the graded center census for a four-generator I-type monoid.

Run with Python 3: python verify_center.py. Requires no third-party packages.
"""
from itertools import product
from collections import defaultdict

def cycle(xs):
    p=list(range(4))
    for a,b in zip(xs,xs[1:]+xs[:1]):p[a]=b
    return tuple(p)

def mul(a,b):
    return tuple(a[b[i]] for i in range(4))

I=tuple(range(4))
L=[cycle([0,3]),cycle([0,1,3,2]),cycle([1,2]),cycle([0,2,3,1])]
F={I}
while True:
    new={mul(a,b) for a in F for b in L}|F
    if len(new)==len(F):break
    F=new
assert len(F)==8

def good(v):
    return (v[0]-v[3])%2==0 and (v[0]+v[1]-v[2]-v[3])%4==0

# The positive I-type coordinates and permutation component, separately
# from the congruence test.
labels={(0,0,0,0):I}
shell=[(0,0,0,0)]
counts=[]
for d in range(17):
    ker={v for v in shell if labels[v]==I}
    assert all((labels[v]==I)==good(v) for v in shell)
    orbits=set()
    for v in ker:
        orb=frozenset(tuple(v[p[j]] for j in range(4)) for p in F)
        assert all(good(w) for w in orb)
        orbits.add(orb)
    counts.append(len(orbits))
    if d==16: break
    new=[]
    for v in shell:
        p=labels[v]
        for a in range(4):
            w=list(v);w[p[a]]+=1;w=tuple(w)
            pp=mul(p,L[a])
            if w not in labels:
                labels[w]=pp;new.append(w)
            else:
                assert labels[w]==pp
    shell=new
    assert len(shell)==(d+4)*(d+3)*(d+2)//6

# Compute the coefficients of (1-t^2+t^4)/[(1-t^2)^2(1-t^4)^2]
# using exact integer polynomial multiplication and long division.
D={0:1}
for stride in (2,2,4,4):
    E=defaultdict(int)
    for j,a in D.items():
        E[j]+=a;E[j+stride]-=a
    D=dict(E)
P={0:1,2:-1,4:1}
h=[]
for n in range(17):
    rhs=P.get(n,0)
    for j,a in D.items():
        if 0<j<=n:rhs-=a*h[n-j]
    h.append(rhs)
assert counts==h,(counts,h)
assert counts[::2]==[1,1,4,5,11,14,24,30,45]
print('I_TYPE_DIHEDRAL_CENTER_OK',len(F),len(labels),counts)
