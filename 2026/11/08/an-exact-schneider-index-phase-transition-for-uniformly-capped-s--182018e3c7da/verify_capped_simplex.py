#!/usr/bin/env python3
"""Exact rational checks of a capped-simplex Schneider-index formula.

This finite verifier supplements, but cannot replace, an all-dimensional proof.
"""
from fractions import Fraction as F
from itertools import permutations
from math import factorial


def verts(d, t):
    n=d+1
    return tuple(sorted(set(tuple(p) for p in permutations((t,1-t)+(F(0),)*(n-2)))))


def L(d,t):
    return max(F(d-1),F(d+1)*t-1)


def in_P(y,t):
    return sum(y)==1 and all(F(0)<=yi<=t for yi in y)


def in_union_scaled(z,vs,lam,t):
    return any(in_P(tuple((zi-vi)/lam for zi,vi in zip(z,v)),t) for v in vs)


def test():
    checks=0
    for d in range(3,8):
        for t in sorted(set((F(1,2),F(3,5),F(2,3),F(3,4),F(4,5),F(9,10),F(d,d+1),F(1)-F(1,3*d)))):
            if not F(1,2)<=t<1: continue
            vs=verts(d,t)
            n=d+1
            lam=L(d,t)
            center=tuple(F(1+lam,n) for _ in range(n))
            for v in vs:
                assert in_P(tuple((zi-vi)/lam for zi,vi in zip(center,v)),t)
                checks+=1
            # Points on every facet, sampled as exact convex averages of face vertices.
            for i in range(n):
                for boundary in (F(0),t):
                    face=[v for v in vs if v[i]==boundary]
                    assert len(face)>=d
                    for den in range(1,6):
                        for ix in range(min(4,len(face))):
                            weights=[F(1,len(face)) for _ in face]
                            weights[ix] += F(1,den)
                            weights=[w/sum(weights) for w in weights]
                            y=tuple(sum(w*v[j] for w,v in zip(weights,face)) for j in range(n))
                            assert in_P(y,t)
                            z=tuple((1+lam)*yy for yy in y)
                            assert in_union_scaled(z,vs,lam,t), (d,t,i,boundary,den)
                            checks+=1
            # Arbitrary convex averages of vertices, including the center.
            for a in range(min(9,len(vs))):
                for b in range(min(9,len(vs))):
                    for alpha in (F(1,4),F(1,2),F(3,4)):
                        y=tuple(alpha*vs[a][j]+(1-alpha)*vs[b][j] for j in range(n))
                        z=tuple((1+lam)*yy for yy in y)
                        assert in_union_scaled(z,vs,lam,t)
                        checks+=1
            # A lower-bound witness at any lambda strictly below the threshold.
            below=lam-F(1,100)
            if (n*t-1)>=d-1:
                z=tuple(F(1+below,n) for _ in range(n))
                assert not in_union_scaled(z,vs,below,t)
                checks+=1
            else:
                # A facet barycenter on the upper cap, away from all constituent
                # simplex-vertex translates at lambda<d-1.
                i=0
                point=tuple(t if j==i else (1-t)/d for j in range(n))
                z=tuple((1+below)*u for u in point)
                assert not in_union_scaled(z,vs,below,t)
                checks+=1
    print('CAPPED_SIMPLEX_EXACT_OK', checks)

if __name__=='__main__':
    test()
