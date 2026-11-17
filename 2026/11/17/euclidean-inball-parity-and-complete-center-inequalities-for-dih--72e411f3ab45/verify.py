#!/usr/bin/env python3
"""Exact combinatorial and independent Euclidean polytope checks for dihedral orbit polytope inballs."""
from itertools import combinations, product
from math import comb, sqrt
import numpy as np
from scipy.spatial import ConvexHull


def section_vertices(n):
    if n % 2 == 0:
        for pos in combinations(range(n), n // 2):
            y = [-1] * n
            for j in pos: y[j] = 1
            yield tuple(y)
    else:
        for z in range(n):
            rest = [j for j in range(n) if j != z]
            for pos in combinations(rest, (n - 1) // 2):
                y = [-1] * n
                y[z] = 0
                for j in pos: y[j] = 1
                yield tuple(y)


def energy(y):
    return sum((y[(j + 1) % len(y)] - y[j]) ** 2 for j in range(len(y)))


def expected_pattern(y):
    n = len(y)
    if n % 2 == 0:
        return all(y[j] == -y[(j + 1) % n] for j in range(n))
    z, = [j for j,v in enumerate(y) if v == 0]
    return all(y[(z + a) % n] == (-1)**(a - 1) * y[(z + 1) % n]
               for a in range(1, n))


def exact_cube_checks():
    count = 0
    for n in range(3, 13):
        yy = list(section_vertices(n))
        en = [energy(y) for y in yy]
        maximum = 4 * n if n % 2 == 0 else 4 * n - 6
        assert max(en) == maximum
        maximizers = [y for y,e in zip(yy, en) if e == maximum]
        assert len(maximizers) == (2 if n % 2 == 0 else 2 * n)
        assert all(expected_pattern(y) for y in maximizers)
        count += len(yy)
    return count


def polygon_checks():
    checks = 0
    for n in range(3, 9):
        s = np.arange(1, n + 1, dtype=float) - (n + 1)/2
        Vs = np.array([np.roll(s, j) for j in range(n)]).T
        assert np.allclose(Vs.sum(axis=1), 0)
        assert np.linalg.matrix_rank(Vs, tol=1.e-8) == n-1
        assert np.allclose(np.ones(n)@Vs,0)
        for j in range(n):
            d = Vs[:, (j+1)%n]-Vs[:,j]
            e = np.zeros(n); e[j]=1
            assert np.allclose(d, n*e-np.ones(n))
            checks += 1
        # Obtain orthonormal Euclidean coordinates for H, independent of facet combinatorics.
        U = np.linalg.svd(Vs)[0][:,:n-1]
        xy = np.vstack([Vs.T@U,-Vs.T@U]); hull=ConvexHull(xy)
        A=hull.equations[:,:-1]; b=hull.equations[:,-1]
        lengths=np.linalg.norm(A,axis=1)
        distances=-b/lengths
        r=sqrt(n)/2 if n%2 == 0 else n/sqrt(4*n-6)
        assert abs(distances.min()-r)<1.e-8
        normals=np.column_stack([A/lengths[:,None],distances])
        # Eliminate triangulation duplicates in nonsimplicial facets.
        unique={tuple(np.round(row,8)) for row in normals}
        active=[row for row in unique if abs(row[-1]-r)<1.e-8]
        assert len(unique)==(comb(n,n//2) if n%2==0 else n*comb(n-1,(n-1)//2))
        assert len(active)==(2 if n%2==0 else 2*n)
        active_rank=np.linalg.matrix_rank(np.asarray(active)[:,:-1],tol=1.e-7)
        assert active_rank==(1 if n%2==0 else n-1)
        # For even n, a small perturbation in a direction perpendicular to the
        # active normals preserves all facet inequalities at the optimal radius.
        if n%2==0:
            a=np.asarray(active)[:,:-1]
            _,_,vt=np.linalg.svd(a,full_matrices=True)
            direction=vt[-1]
            assert np.linalg.norm(a@direction)<1.e-7
            slack=min(row[-1]-r for row in unique if row not in active)
            assert slack>0
            eps=0.1*slack
            for row in unique:
                assert row[-1]-eps*abs(np.dot(row[:-1],direction))>=r-1.e-7
        checks+=len(unique)
    return checks

if __name__=='__main__':
    a=exact_cube_checks()
    b=polygon_checks()
    print(f'PASS: {a} exact cube-section vertices and {b} independent Euclidean/facet checks')
    print('Verified n=3..12 for exact centered-cube optimization, n=3..8 for Euclidean hull facets and active-normal ranks.')
