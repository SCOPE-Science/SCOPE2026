"""Exact volume identities and independent low-dimensional hull checks.

Usage: python verify.py. Uses standard-library fractions and scipy for an
independent floating-point convex-hull check in the small dimensions only.
"""
from fractions import Fraction
from math import comb, factorial
from itertools import product
import numpy as np
from scipy.spatial import ConvexHull


def polynomial_integral(p, q):
    return p * (p - 1) * sum(
        (Fraction((-1)**j * comb(q,j) * 2**(q-j), p - 1 + j) for j in range(q + 1)), Fraction(0))


def binomial_formula(p, q):
    n = p + q
    return Fraction(n * sum(comb(n - 1,j) for j in range(p-1,n)),comb(n,p))


def hull_volume(p,q):
    n = p+q
    edges = [(i,j) for i in range(p) for j in range(i+1,p)] + [(i,j) for i in range(p) for j in range(p,n)]
    pts=[]
    for vals in product(range(-2,3),repeat=n-1):
        a=(0,)+vals
        if any(abs(a[i]-a[j])>1 for i,j in edges):continue
        adj=[set() for _ in range(n)]
        for i,j in edges:
            if abs(a[i]-a[j])==1: adj[i].add(j);adj[j].add(i)
        reached={0};stack=[0]
        while stack:
            i=stack.pop()
            for j in adj[i]:
                if j not in reached:reached.add(j);stack.append(j)
        if len(reached)==n:pts.append(vals)
    if not pts:raise AssertionError('no vertices')
    hull=ConvexHull(np.array(pts,dtype=float))
    return len(pts), hull.volume


def main():
    n_exact=0
    for p in range(2,30):
        for q in range(0,30):
            lhs=polynomial_integral(p,q)
            rhs=binomial_formula(p,q)
            assert lhs==rhs,(p,q,lhs,rhs)
            n_exact+=1
    n_geo=0
    for p,q in [(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(4,1),(4,2)]:
        count, v=hull_volume(p,q)
        want=float(binomial_formula(p,q))
        assert abs(v-want)<1e-8*max(1.,want),(p,q,count,v,want)
        n_geo+=1
    print(f'SPLIT_LIPSCHITZ_POLAR_VOLUME_CHECKS_PASSED exact_profiles={n_exact} independent_hulls={n_geo}')

if __name__=='__main__': main()
