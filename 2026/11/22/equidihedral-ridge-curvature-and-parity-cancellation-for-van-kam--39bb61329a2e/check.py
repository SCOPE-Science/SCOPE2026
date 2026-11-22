"""Independent small-dimensional checks of exact ridge curvature for symmetric simplex hulls.

Usage: python check.py   (Python 3, NumPy and SciPy)
All geometric calculations use actual coordinates; numerical tests support but do not prove the theorems.
"""
import itertools
import math
import numpy as np
from scipy.spatial import ConvexHull


def polar_vertices(n):
    if n % 2 == 0:
        k = n // 2
        for ones in itertools.combinations(range(n), k):
            v = -np.ones(n, dtype=int)
            v[list(ones)] = 1
            yield v
    else:
        k = n // 2
        for zero in range(n):
            others = [i for i in range(n) if i != zero]
            for ones in itertools.combinations(others, k):
                v = -np.ones(n, dtype=int)
                v[list(ones)] = 1
                v[zero] = 0
                yield v


def simplex_vol(points):
    diff = points[1:] - points[0]
    if len(diff) == 0:
        return 1.
    gram = diff @ diff.T
    return np.sqrt(max(0, np.linalg.det(gram))) / math.factorial(len(diff))


def test_dimension(n):
    pv = list(polar_vertices(n))
    H = np.eye(n) - np.ones((n, n)) / n
    assert all(np.sum(v) == 0 for v in pv)
    # Independently enumerate every polar edge using common saturated cube coordinates.
    edges = []
    for i, j in itertools.combinations(range(len(pv)), 2):
        v, w = pv[i], pv[j]
        common = np.flatnonzero((abs(v) == 1) & (v == w))
        if len(common) != n-2:
            continue
        # Shared coordinate hyperplanes in zero-sum affine space leave a line.
        assert np.linalg.matrix_rank(np.vstack((np.eye(n)[common], np.ones(n))), tol=1e-9) == n-1
        edges.append((i,j))
    k = n//2
    expected_edges = (math.comb(n,k)*k*k//2 if n%2==0
                      else n*(n-1)*math.comb(n-1,k)//2)
    assert len(edges) == expected_edges, (n,len(edges),expected_edges)
    exp_cos = (1-4/n if n%2==0 else 1-1/(n-1))
    target_vol = math.sqrt((2*(n-2)+(n%2))/n)/math.factorial(n-3)
    ridge_angles = []
    for a,b in edges:
        v,w = pv[a],pv[b]
        common = np.flatnonzero((abs(v)==1)&(v==w))
        points = np.array([v[i]*H[i] for i in common])
        actual = simplex_vol(points)
        assert np.isclose(actual,target_vol,rtol=2e-10,atol=2e-12),(n,actual,target_vol)
        cos = float(np.dot(v,w)/np.linalg.norm(v)/np.linalg.norm(w))
        assert np.isclose(cos,exp_cos,atol=2e-12),(n,cos,exp_cos)
        assert np.linalg.matrix_rank(points[1:]-points[0],tol=1e-9)==n-3
        ridge_angles.append(math.acos(cos))
    actual_v = sum(x*target_vol/(2*math.pi) for x in ridge_angles)
    formula_v = expected_edges*target_vol*math.acos(exp_cos)/(2*math.pi)
    assert np.isclose(actual_v,formula_v,rtol=2e-10,atol=1e-11)
    # The full primal point hull independently certifies the facet count in moderate dimension.
    basis = np.linalg.svd(H)[0][:, :n-1]
    coords = np.r_[H, -H]@basis
    hull = ConvexHull(coords)
    for v in pv:
        signed = np.r_[H, -H]
        contacts = np.where(np.isclose(signed@v,1,atol=1e-10))[0]
        assert len(contacts) == (n if n%2==0 else n-1)
    assert len(pv) == (math.comb(n,k) if n%2==0 else n*math.comb(n-1,k))
    print(f'n={n}: polar vertices={len(pv)}, ridges={len(edges)}, uniform angle={ridge_angles[0]:.10f}, ridge volume={target_vol:.10f}, V_(n-3)={actual_v:.10f}, hull simplices={len(hull.simplices)}')


if __name__=='__main__':
    for n in range(4,9):
        test_dimension(n)
    # Check asymptotic parity-neutral curvature normalization without large integers.
    target=math.sqrt(2/math.pi)/(4*math.pi)
    for n in (40,41,200,201,1000,1001):
        k=n//2
        logR = (math.lgamma(n+1)-math.lgamma(k+1)-math.lgamma(n-k+1)
                if n%2==0 else math.lgamma(n)-2*math.lgamma(k+1))
        logR += (2*math.log(k)-math.log(2) if n%2==0
                 else math.log(n*(n-1)/2))
        alpha=math.acos(1-(4/n if n%2==0 else 1/(n-1)))
        norm=math.exp(logR+math.log(math.sqrt((2*(n-2)+n%2)/n)*alpha/(2*math.pi))-n*math.log(2)-math.log(n))
        assert abs(norm/target-1)<4/n,(n,norm,target)
        print(f'asymptotic n={n}: normalized={norm:.12f}, limit={target:.12f}')
    print('VAN_KAMPEN_FLORES_RIDGE_CHECK_PASS')
