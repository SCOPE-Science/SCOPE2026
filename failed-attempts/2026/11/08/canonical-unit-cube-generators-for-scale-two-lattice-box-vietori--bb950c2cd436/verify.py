#!/usr/bin/env python3
"""Exhaustive finite local Euler and oriented cube-cycle checks.

All global conclusions in the accompanying proof reduce to these fixed finite
local cases and stated mathematical theorems. No network/dependencies.
"""
import itertools
from collections import Counter, defaultdict
from math import prod


def cliques(points):
    """Enumerate every nonempty clique by recursion on increasing vertex indices."""
    d=len(points[0]); n=len(points)
    adj=[{j for j in range(i+1,n)
          if sum(abs(points[i][k]-points[j][k]) for k in range(d))<=2}
         for i in range(n)]
    def go(face,candidates):
        for j in sorted(candidates):
            f=face+(j,)
            yield f
            yield from go(f,candidates.intersection(adj[j]))
    yield from go((),set(range(n)))


def local_weight(c):
    pts=list(itertools.product(*(range(z+1) for z in c)))
    return sum((-1)**(len(s)-1) for s in cliques(pts)
               if all(min(pts[j][k] for j in s)==0 for k in range(3)))


def facecount(bounds):
    pts=list(itertools.product(*(range(z+1) for z in bounds)))
    h=Counter(len(s) for s in cliques(pts))
    return h


def orientation(simplex):
    inv=sum(simplex[i]>simplex[j] for i in range(len(simplex))
            for j in range(i+1,len(simplex)))
    return -1 if inv%2 else 1

EVEN=[(0,0,0),(0,1,1),(1,0,1),(1,1,0)]
PAIRS=[(v, tuple(1-x for x in v)) for v in EVEN]

def oriented_cycle():
    c=defaultdict(int)
    for bits in itertools.product((0,1),repeat=4):
        verts=tuple(PAIRS[i][bits[i]] for i in range(4))
        assert all(sum(abs(a-b) for a,b in zip(verts[i],verts[j]))<=2
                   for i in range(4) for j in range(i+1,4))
        key=tuple(sorted(verts))
        perm=tuple(key.index(x) for x in verts)
        c[key]+=(-1)**sum(bits)*orientation(perm)
    return dict((k,v) for k,v in c.items() if v)

def boundary(chain):
    out=defaultdict(int)
    for s,coeff in chain.items():
        for i in range(len(s)):
            out[s[:i]+s[i+1:]]+=coeff*(-1)**i
    return {k:v for k,v in out.items() if v}

def act_chain(c, f):
    out=defaultdict(int)
    for face,coeff in c.items():
        transformed=tuple(f(v) for v in face)
        key=tuple(sorted(transformed))
        perm=tuple(key.index(v) for v in transformed)
        out[key]+=coeff*orientation(perm)
    return dict((k,v) for k,v in out.items() if v)


def main():
    table={}
    for c in itertools.product((0,1,2),repeat=3):
        w=local_weight(c)
        expected=1 if c==(0,0,0) else (-1 if min(c)>=1 else 0)
        assert w==expected,(c,w,expected)
        table[c]=w
    print('LOCAL_EULER_TABLE_27_OK',len(table))
    for bounds in [(1,1,1),(1,1,3),(1,2,3),(2,2,2),(2,3,4),(3,3,3)]:
        f=facecount(bounds)
        chi=sum((-1)**(k-1)*v for k,v in f.items())
        assert chi==1-prod(bounds),(bounds,f,chi)
        print('BOX',bounds,'EULER',chi,'F_VECTOR',','.join(map(str,(f[k] for k in sorted(f)))))
    z=oriented_cycle()
    assert len(z)==16 and set(z.values())=={-1,1}
    assert not boundary(z)
    assert z[tuple(sorted(EVEN))] in [-1,1]
    for p in itertools.permutations(range(3)):
        expected=orientation(p)
        for flips in itertools.product((0,1),repeat=3):
            f=lambda v,p=p,flips=flips:tuple(v[p[i]]^flips[i] for i in range(3))
            acted=act_chain(z,f)
            assert acted=={key:expected*coeff for key,coeff in z.items()},(p,flips)
    print('CROSSPOLYTOPE_S3_CHAIN_AND_ALL_48_SYMMETRIES_OK')
    for n in range(3,7):
        a=[v+(0,)*(n-3) for v in EVEN]
        within=[x for x in itertools.product(range(-2,4),repeat=n)
                if all(sum(abs(x[j]-v[j]) for j in range(n))<=2 for v in a)]
        assert set(within)==set(a),(n,within)
    print('PARITY_TETRAHEDRA_MAXIMAL_IN_DIMENSIONS_3_TO_6_OK')
    print('EXHAUSTIVE_LOCAL_CERTIFICATE_OK')

if __name__=='__main__':
    main()
