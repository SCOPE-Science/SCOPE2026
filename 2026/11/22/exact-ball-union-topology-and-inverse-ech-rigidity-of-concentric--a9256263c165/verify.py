#!/usr/bin/env python3
"""Numerical and finite-chain checks for a geometric four-ball nerve theorem.

Python 3 standard library only. This tests representative shapes, not the
universal analytic claims in the accompanying proof.
"""
import itertools
import math
import random

SIGNS = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
TOL = 3e-10

def dot(v, w):
    return sum(a*b for a, b in zip(v, w))

def sqdist(v, w):
    return sum((a-b)**2 for a, b in zip(v, w))

def rank2(matrix):
    """Exact binary rank by bit-packed elimination."""
    rows = [sum((int(x) & 1) << j for j, x in enumerate(row)) for row in matrix]
    rank = 0
    for bit in range(len(matrix[0]) if matrix else 0):
        pivot = next((i for i in range(rank, len(rows)) if rows[i] & (1 << bit)), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for i in range(len(rows)):
            if i != rank and (rows[i] & (1 << bit)):
                rows[i] ^= rows[rank]
        rank += 1
    return rank

def betti(crit, radius):
    faces = {k: [face for face in itertools.combinations(range(4), k+1)
                 if crit[face] <= radius] for k in range(4)}
    ranks = []
    for k in range(1, 4):
        higher = faces[k]
        lower = faces[k-1]
        mat = [[int(set(a).issubset(b)) for b in higher] for a in lower]
        ranks.append(rank2(mat))
    n = [len(faces[k]) for k in range(4)]
    return (n[0]-ranks[0], n[1]-ranks[0]-ranks[1],
            n[2]-ranks[1]-ranks[2], n[3]-ranks[2])

def verify(a, b, c):
    scale = math.sqrt(a*a+b*b+c*c)
    a, b, c = (x/scale for x in (a,b,c))
    h2 = 1/(1/a**2+1/b**2+1/c**2)
    h = math.sqrt(h2)
    rho = h/math.sqrt(1-h2)
    radi = math.sqrt(1/(1-h2))
    u = [tuple(q*x for q, x in zip(sign,(a,b,c))) for sign in SIGNS]
    cent = [tuple(-h*q/(x*math.sqrt(1-h2))
                  for q,x in zip(sign,(a,b,c))) for sign in SIGNS]
    assert all(abs(dot(x,x)-1)<TOL for x in u)
    assert all(abs(dot(x,x)-radi*radi)<TOL for x in cent)
    assert all(abs(sum(v[j] for v in cent))<TOL for j in range(3))
    edge = {f:math.sqrt(sqdist(cent[f[0]],cent[f[1]]))/2
            for f in itertools.combinations(range(4), 2)}
    r = sorted({round(x,12) for x in edge.values()})
    assert len(edge)==6
    assert all(0 < x < 1 for x in edge.values())
    edge_sorted = sorted(edge.values())
    radi_reconstruct = math.sqrt(sum(edge_sorted[0::2][i]**2 for i in range(3))/2)
    # Sorted pairs have multiplicity 2; use pair representatives.
    assert abs(radi_reconstruct-radi)<TOL
    p = [tuple(rho*x for x in v) for v in u]
    for i in range(4):
        for j in range(4):
            if j != i:
                assert abs(sqdist(p[i],cent[j])-1)<TOL
                assert abs(dot(p[i],cent[j])-rho*rho)<TOL
    # Every facet triangle is acute, hence its circumcenter lies inside it.
    for subset in itertools.combinations(range(4),3):
        squared = sorted(sqdist(cent[i],cent[j]) for i,j in itertools.combinations(subset,2))
        assert squared[2] < squared[0]+squared[1]
        missing = next(i for i in range(4) if i not in subset)
        assert abs(dot(p[missing],p[missing])-rho*rho)<TOL
        # Independently recover positive barycentric coordinates of the face circumcenter.
        q0, q1, q2 = (cent[j] for j in subset)
        e1 = tuple(x-y for x,y in zip(q1,q0))
        e2 = tuple(x-y for x,y in zip(q2,q0))
        w = tuple(x-y for x,y in zip(p[missing],q0))
        aa, ab, bb = dot(e1,e1),dot(e1,e2),dot(e2,e2)
        det=aa*bb-ab*ab
        assert det>0
        x=(dot(w,e1)*bb-dot(w,e2)*ab)/det
        y=(dot(w,e2)*aa-dot(w,e1)*ab)/det
        assert min(x,y,1-x-y)>-TOL
        assert abs(sqdist(p[missing],q0)-1)<TOL
        # Hence at fixed unit outer-ball radii, a smaller central core
        # of radius q<rho misses this unique triple contact.
        assert rho>0
    crit = {f:0. for f in itertools.combinations(range(4),1)}
    for f,val in edge.items(): crit[f]=val
    for f in itertools.combinations(range(4),3): crit[f]=1.
    crit[(0,1,2,3)]=radi
    r1, r2, r3 = (edge_sorted[i] for i in (0,2,4))
    assert abs(r1*r1+r2*r2+r3*r3-2*radi*radi)<TOL
    assert abs(1-2/(r1*r1+r2*r2+r3*r3)-h2)<TOL
    # Absolute Betti values at the interiors of the distinct strata.
    thresholds = sorted(set([0.,r1,r2,r3,1.,radi]))
    for left,right in zip(thresholds[:-1],thresholds[1:]):
        radius=(left+right)/2
        actual=betti(crit,radius)
        if radius<r1: expected=(4,0,0,0)
        elif radius<r2: expected=(2,0,0,0)
        elif radius<r3: expected=(1,1,0,0)
        elif radius<1: expected=(1,3,0,0)
        elif radius<radi: expected=(1,0,1,0)
        else: expected=(1,0,0,0)
        assert actual==expected,(a,b,c,radius,actual,expected)
    assert betti(crit,radi+0.2)==(1,0,0,0)
    return (r1,r2,r3,radi,rho)

def main():
    shapes=[(1,1,1),(2,2,1),(2,1,1),(3,2,1),(100,2,1),(1,.02,.01),
            (1,1,.01),(1,.9,.8)]
    rnd=random.Random(20261121)
    for i in range(200):
        shapes.append(tuple(math.exp(rnd.uniform(-2.5,2.5)) for _ in range(3)))
    for axes in shapes:
        vals=verify(*axes)
        if axes in shapes[:8]:
            print('half-axes:',axes,'edge thresholds / full / core:',tuple(round(x,9) for x in vals))
    print('PASS:',len(shapes),'geometric configurations, finite exact binary chain ranks and independent metric identities')

if __name__=='__main__':main()
