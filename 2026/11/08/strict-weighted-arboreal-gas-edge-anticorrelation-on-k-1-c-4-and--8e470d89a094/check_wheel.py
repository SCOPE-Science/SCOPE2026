#!/usr/bin/env python3
"""Exact, dependency-free polynomial certificate for weighted forests of W_5.

The wheel has center 0 and rim 1,2,3,4 in cyclic order.
Edges are indexed 0:(0,1), 1:(0,2), 2:(0,3), 3:(0,4),
4:(1,2), 5:(1,4), 6:(2,3), 7:(3,4).
"""
from itertools import product
from fractions import Fraction
import random

E = ((0,1),(0,2),(0,3),(0,4),(1,2),(1,4),(2,3),(3,4))
N=8
ZERO=(0,)*N

def add(*ps):
    q={}
    for p in ps:
        for e,c in p.items():
            q[e]=q.get(e,0)+c
            if not q[e]: del q[e]
    return q

def scale(p,c): return {e:c*v for e,v in p.items() if c*v}

def mul(*ps):
    r={ZERO:1}
    for q in ps:
        nxt={}
        for e,c in r.items():
            for f,d in q.items():
                g=tuple(x+y for x,y in zip(e,f))
                nxt[g]=nxt.get(g,0)+c*d
        r={e:c for e,c in nxt.items() if c}
    return r

def var(j):
    e=list(ZERO); e[j]=1
    return {tuple(e):1}

def power(p,j):
    r={ZERO:1}
    for _ in range(j):r=mul(r,p)
    return r

def deriv(p,j):
    r={}
    for e,c in p.items():
        if e[j]:
            f=list(e);f[j]-=1
            f=tuple(f);r[f]=r.get(f,0)+c*e[j]
    return r

def forest(mask):
    parent=list(range(5))
    def root(v):
        while parent[v]!=v:v=parent[v]
        return v
    for i,(u,v) in enumerate(E):
        if (mask>>i)&1:
            x,y=root(u),root(v)
            if x==y:return False
            parent[x]=y
    return True

FOREST_MASKS=[mask for mask in range(1<<N) if forest(mask)]
Z={}
for mask in FOREST_MASKS:
    m=tuple((mask>>i)&1 for i in range(N))
    Z[m]=Z.get(m,0)+1
assert len(FOREST_MASKS)==134

# Each orbit under the dihedral symmetry has one representative.
ORBIT_PAIRS=((0,1),(0,2),(0,4),(2,4),(4,5),(4,7))
RAYS={}
for i,j in ORBIT_PAIRS:
    R=add(mul(deriv(Z,i),deriv(Z,j)),
          scale(mul(Z,deriv(deriv(Z,i),j)),-1))
    assert all(e[i]==e[j]==0 for e in R)
    RAYS[(i,j)]=R

# Verify (rather than merely assume) the six representatives exhaust all
# 28 unordered edge pairs under the eight rim dihedral automorphisms.
edge_lookup={frozenset(e):i for i,e in enumerate(E)}
all_pairs={(i,j) for i in range(N) for j in range(i+1,N)}
seen=set()
for i,j in ORBIT_PAIRS:
    orbit=set()
    for offset in range(4):
        for sense in (-1,1):
            def vertex_map(v):
                return 0 if v==0 else 1+((offset+sense*(v-1))%4)
            mapping=[edge_lookup[frozenset((vertex_map(u),vertex_map(v)))]
                     for u,v in E]
            orbit.add(tuple(sorted((mapping[i],mapping[j]))))
    assert orbit and not (orbit & seen), (i,j)
    seen|=orbit
assert seen==all_pairs, sorted(all_pairs-seen)

# Five orbit representatives have coefficientwise positive Rayleigh differences.
EXPECTED={(0,1):172,(0,2):90,(0,4):240,(4,5):149,(4,7):93}
for pair,nterms in EXPECTED.items():
    R=RAYS[pair]
    assert len(R)==nterms, (pair,len(R),nterms)
    assert min(R.values())>0, pair

# The remaining orbit: nonincident spoke and rim edge.
# x=a1, t=a6, u=a5, v=a7, alpha=a0, delta=a3.
alpha, x, delta, t, u, v = (var(i) for i in (0,1,3,6,5,7))
one={ZERO:1}
uv=mul(u,v)
h=mul(add(one,u),add(one,v))
S=add(mul(alpha,delta),mul(alpha,u),mul(alpha,v),alpha,
      mul(delta,u),delta)
U=add(S,h)
V=add(mul(alpha,delta,u),mul(alpha,delta,v),mul(alpha,delta),
      mul(alpha,power(u,2)),scale(mul(alpha,u,v),2),
      scale(mul(alpha,u),2),mul(alpha,power(v,2)),
      scale(mul(alpha,v),2),alpha,mul(delta,power(u,2)),mul(delta,u))
Q=mul(U,V)
assert min(U.values())>0 and min(V.values())>0
R=RAYS[(2,4)]
# P is the coefficient of t in R at x=0. This is independent of t and x.
P={}
for e,c in R.items():
    if e[1]==0 and e[6]==1:
        f=list(e);f[6]-=1
        P[tuple(f)]=c
assert min(P.values())>0
assert add(mul(h,P),scale(mul(uv,power(S,2)),-1))==Q
A=mul(uv,h)
CERT=add(mul(A,power(x,2)),mul(add(A,scale(mul(uv,t,S),-2)),x),
         mul(t,add(t,one),P))
assert R==CERT
assert len(R)==68
# An explicit positivity certificate is
# R = A (x - t*S/h)^2 + A*x + t*P + t^2*Q/h,
# because h*P - uv*S^2 = Q = U*V.
# All denominators and factors are strictly positive for positive weights.

# Separate direct probability test, with deterministic nonuniform edge weights.
def brute_cov(weights,i,j):
    z=sa=sb=sab=Fraction(0)
    for mask in range(1<<8):
        if not forest(mask):continue
        w=Fraction(1)
        for k in range(8):
            if (mask>>k)&1:w*=weights[k]
        z+=w
        if mask>>i&1:sa+=w
        if mask>>j&1:sb+=w
        if mask>>i&1 and mask>>j&1:sab+=w
    return sab/z-sa*sb/z**2
rng=random.Random(1729)
for zcase in range(48):
    weights=[Fraction(rng.randint(1,9),rng.randint(1,9)) for _ in range(8)]
    for i in range(8):
        for j in range(i+1,8):
            assert brute_cov(weights,i,j)<0, (zcase,i,j)
print('PASS: 134 forests; six orbit differences; five positive-coefficient certificates')
print('PASS: exceptional square certificate and 48x28 direct rational correlations')
print('orbit term counts:',{str(k):len(v) for k,v in RAYS.items()})
