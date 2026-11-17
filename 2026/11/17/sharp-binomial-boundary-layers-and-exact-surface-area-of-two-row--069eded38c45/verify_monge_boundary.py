"""Direct Euclidean facet reconstructions and exact surface identities.

Requires numpy and scipy (see requirements.txt). Run:
    python verify_monge_boundary.py
"""
from fractions import Fraction
from math import comb, factorial, sqrt, isclose
import numpy as np
from scipy.spatial import ConvexHull


def vertices(q):
    p = 2
    v = []
    for a in range(1, p):
        for b in range(1, q):
            m = np.zeros((p, q))
            m[:a, q-b:] = 1/(a*b)
            v.append(m.ravel())
            m = np.zeros((p, q))
            m[p-a:, :b] = 1/(a*b)
            v.append(m.ravel())
    for i in range(p):
        m = np.zeros((p, q))
        m[i, :] = 1/q
        v.append(m.ravel())
    for j in range(q):
        m = np.zeros((p, q))
        m[:, j] = 0.5
        v.append(m.ravel())
    return np.unique(np.asarray(v), axis=0)


def facet_measure(v, mask, ambient_dim):
    w = v[mask]
    assert len(w) >= ambient_dim-1
    _, singular, vh = np.linalg.svd(w-w[0], full_matrices=False)
    dim = int(np.sum(singular > 1e-10))
    assert dim == ambient_dim-2, (dim, ambient_dim)
    coords = (w-w[0]) @ vh[:dim].T
    return float(ConvexHull(coords).volume)


def exact_coordinate_multiplier(q, row, i):
    assert 1 <= i <= q and row in (0, 1)
    numer = (sum(comb(q, k) for k in range(i,q+1)) if row == 0
             else sum(comb(q, k) for k in range(0,i)))
    return Fraction(2*numer, 2**q)


def exact_wall_aggregate(q):
    # E f(D)=1/4, E |D| f(D)=1/8, E |D|=1,
    # where D has Laplace density f(t)=exp(-abs(t))/2.
    n = q-1
    return 2*q*(q*n*Fraction(1,4)
                + n*Fraction(1,8) + n*(n-1)*Fraction(1,4)
                + n*Fraction(1,8))


def verify():
    tested = 0
    for q in range(2,6):
        m = 2*q
        v = vertices(q)
        assert len(v) == 3*q
        volume = sqrt(m)/(factorial(m-1)*factorial(q))
        unit = (m-1)*sqrt((m-1)/m)
        coordinate_sum = 0.0
        for row in range(2):
            for i in range(1,q+1):
                mask = np.abs(v[:,row*q+i-1]) < 1e-12
                actual = facet_measure(v,mask,m)
                expected = volume*unit*float(exact_coordinate_multiplier(q,row,i))
                assert isclose(actual,expected,rel_tol=1e-9,abs_tol=1e-11), (q,row,i,actual,expected)
                coordinate_sum += actual
                tested += 1
        assert isclose(coordinate_sum/volume,2*q*unit,rel_tol=1e-9)
        wall_sum=0.
        for i in range(q-1):
            g=v[:,i+1]-v[:,q+i+1]-v[:,i]+v[:,q+i]
            area=facet_measure(v,np.abs(g)<1e-12,m)
            wall_sum+=area
            tested += 1
        assert isclose(wall_sum/volume,float(exact_wall_aggregate(q)),rel_tol=1e-9)
        print(f'GEOMETRIC_DIRECT_PASS q={q} vertices={len(v)} coordinate_facets={2*q} monge_facets={q-1}')
    for q in range(2,101):
        for i in range(1,q+1):
            a=exact_coordinate_multiplier(q,0,i)
            b=exact_coordinate_multiplier(q,1,i)
            assert a+b == 2
        assert exact_coordinate_multiplier(q,0,1)/exact_coordinate_multiplier(q,0,q) == 2**q-1
        assert exact_wall_aggregate(q) == Fraction(q*(q-1)*(2*q-1),2)
    print(f'MONGE_BOUNDARY_PASS direct_facets={tested} exact_dimensions=2..100')


if __name__ == '__main__':
    verify()
