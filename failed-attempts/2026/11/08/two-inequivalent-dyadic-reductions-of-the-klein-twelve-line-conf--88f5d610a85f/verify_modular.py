#!/usr/bin/env python3
"""Exact characteristic-uniform incidence and dyadic-fiber checks for a 12-line divisor."""
from collections import Counter
from itertools import combinations

# Arithmetic in Z[A]/(A^2+A+2), represented by pairs (u,v)=u+vA.
def R(z):
    return (z, 0) if isinstance(z,int) else z

def plus(a,b):
    a,b=R(a),R(b)
    return(a[0]+b[0],a[1]+b[1])

def minus(a,b):
    a,b=R(a),R(b)
    return(a[0]-b[0],a[1]-b[1])

def times(a,b):
    a,b=R(a),R(b)
    u,v=a; w,t=b
    return(u*w-2*v*t,u*t+v*w-v*t)

def det(A,B,C):
    return plus(minus(times(A[0],minus(times(B[1],C[2]),times(B[2],C[1]))),
                      times(A[1],minus(times(B[0],C[2]),times(B[2],C[0])))),
                times(A[2],minus(times(B[0],C[1]),times(B[1],C[0]))))

def norm(w):
    u,v=R(w)
    return u*u-u*v+2*v*v

A=(0,1)
# Gevay--Pokora subarrangement K': lines 3,4,6,7,8,9,10,11,13,14,16,17.
LINES=[(A,1,-1),(A,-1,1),(1,A,-1),(A,-1,-1),(-1,1,A),
       (A,1,1),(-1,A,1),(-1,-1,A),(-1,A,-1),(1,A,1),
       (1,-1,A),(1,1,A)]
assert len(LINES)==12
triples={t:det(*(LINES[i] for i in t)) for t in combinations(range(12),3)}
assert len(triples)==220
census=Counter(norm(v) for v in triples.values())
assert census=={0:12,8:56,16:84,32:64,64:4},census
zero=[t for t,d in triples.items() if d==(0,0)]
assert len(zero)==12
assert set(sum((list(t) for t in zero),[]))==set(range(12))
assert Counter(i for t in zero for i in t)=={i:3 for i in range(12)}
assert max(Counter(pair for t in zero for pair in combinations(t,2)).values())==1
# Every pair meets; 12 triple points account for 36 pair intersections.
assert len(set(pair for t in zero for pair in combinations(t,2)))==36
assert 66-36==30
# No two distinct characteristic-zero lines become identical away from 2.
assert all(any(triples[tuple(sorted((i,j,k)))]!=(0,0)
               for k in range(12) if k not in (i,j))
           for i,j in combinations(range(12),2))

# Two primes of Z[A] above 2, with residues A=0 and A=1.
for root,expected in [(0,{(0,1,1):4,(1,0,1):4,(1,1,0):4}),
                      (1,{(1,1,1):12})]:
    c=Counter(tuple((u+v*root)%2 for u,v in map(R,line)) for line in LINES)
    assert c==expected,(root,c)

# Independent finite-field point-incidence reconstruction for odd prime p.
# Use F_p if there is a root; otherwise use the quadratic field F_p[A].
def check_mod_p(p):
    roots=[x for x in range(p) if (x*x+x+2)%p==0]
    a=roots[0] if roots else None
    def elm(x):
        u,v=R(x)
        return ((u+v*a)%p,0) if a is not None else (u%p,v%p)
    def m(x,y):
        if a is not None:return ((x[0]*y[0])%p,0)
        return ((x[0]*y[0]-2*x[1]*y[1])%p,
                (x[0]*y[1]+x[1]*y[0]-x[1]*y[1])%p)
    def s(x,y):return ((x[0]-y[0])%p,(x[1]-y[1])%p)
    def inv(x):
        if a is not None:return (pow(x[0],-1,p),0)
        n=(x[0]*x[0]-x[0]*x[1]+2*x[1]*x[1])%p
        assert n
        u=pow(n,-1,p)
        return (((x[0]-x[1])*u)%p,(-x[1]*u)%p)
    def cross(v,w):
        return (s(m(v[1],w[2]),m(v[2],w[1])),
                s(m(v[2],w[0]),m(v[0],w[2])),
                s(m(v[0],w[1]),m(v[1],w[0])))
    LL=[tuple(elm(z) for z in line) for line in LINES]
    pts={}
    for i,j in combinations(range(12),2):
        x=cross(LL[i],LL[j])
        pivot=next((t for t in x if t!=(0,0)),None)
        assert pivot is not None,(p,i,j)
        w=tuple(m(z,inv(pivot)) for z in x)
        pts.setdefault(w,set()).update((i,j))
    counts=Counter(map(len,pts.values()))
    assert counts=={2:30,3:12},(p,counts)
    for w,support in pts.items():
        def dot(v,w):
            u=(0,0)
            for t,z in zip(v,w):
                z=m(t,z)
                u=((u[0]+z[0])%p,(u[1]+z[1])%p)
            return u
        assert support=={i for i,v in enumerate(LL) if dot(v,w)==(0,0)}
    return p, p if a is not None else p*p

# Direct-point check uses the independent cross-product formula above; the
# support count already validates all geometric coincidences.
fields=[check_mod_p(p) for p in (3,5,7,11,13,17,19)]
print('VERIFY_KLEIN12_MODULAR_OK',dict(sorted(census.items())),fields)
