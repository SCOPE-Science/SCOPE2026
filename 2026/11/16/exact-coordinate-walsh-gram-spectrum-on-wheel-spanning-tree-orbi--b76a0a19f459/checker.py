#!/usr/bin/env python3
"""Direct finite check of the wheel spanning-tree coordinate-Walsh Gram spectrum.
Run: python checker.py. Requires numpy. Uses exhaustive combinatorial trees, not a transfer-current formula.
"""
import itertools
import math
import numpy as np


def connected_tree(edge_ids, edges, nv):
    parent = list(range(nv))
    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for k in edge_ids:
        a, b = edges[k]
        a, b = root(a), root(b)
        if a == b:
            return False
        parent[a] = b
    return True


def explicit_spectrum(n):
    r = (3.0-math.sqrt(5.0))/2.0
    h = (1+r**n)/(1-r**n)
    mu = 1-2*h/math.sqrt(5)
    zero_high = 16*h/(5*math.sqrt(5))-16*n*r**n/(5*(1-r**n)**2)+2*n*mu*mu
    eigen = [0.0, zero_high]
    for k in range(1, n):
        t = abs(math.cos(math.pi*k/n))
        eigen.append((8*h/math.sqrt(5))*(1-t)/(3-2*t))
        eigen.append((8*h/math.sqrt(5))*(1+t)/(3+2*t))
    return np.sort(np.array(eigen, dtype=float))


def direct_gram(n):
    # hub vertex 0, rim vertices 1..n
    edges = [(0, i+1) for i in range(n)] + [(i+1,(i+1)%n+1) for i in range(n)]
    M = 2*n
    gram_integer = np.zeros((M,M),dtype=np.int64)
    count = 0
    for subset in itertools.combinations(range(M), n):
        if not connected_tree(subset, edges, n+1):
            continue
        z = np.ones(M,dtype=np.int64)
        z[list(subset)] = -1
        gram_integer += np.outer(z,z)
        count += 1
    return count, gram_integer/count, gram_integer


def test():
    for n in range(3, 11):
        count, gram, g_int = direct_gram(n)
        a,b = 2,1    # Lucas L_0=2,L_1=1
        for _ in range(2*n):
            a,b = b,a+b
        assert count == a-2, (n,count,a-2)
        assert np.all(np.diag(g_int)==count)
        assert np.all(g_int==g_int.T)
        assert np.max(np.abs(np.sum(g_int,axis=1)))==0  # sum of all edge characters = 0
        got = np.linalg.eigvalsh(gram)
        exact = explicit_spectrum(n)
        err = float(np.max(np.abs(got-exact)))
        assert err < 2e-11,(n,err,got,exact)
        # Parseval/frame trace and unique nullity
        assert abs(float(np.sum(got)) - 2*n)<2e-10
        assert abs(got[0])<2e-10 and got[1]>1e-3
        print(f'n={n} trees={count} max_spectral_error={err:.2g} min_positive={got[1]:.12g} max={got[-1]:.12g}')
    print('WHEEL_COORDINATE_WALSH_SPECTRUM_ALL_PASS')


if __name__=='__main__':test()
