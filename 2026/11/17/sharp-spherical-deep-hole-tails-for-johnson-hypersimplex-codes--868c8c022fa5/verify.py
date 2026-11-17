"""Independent finite-dimensional checks for spherical Johnson-code deep holes.
The proof, not these finite tests, supports all parameter values.
Requires Python 3, NumPy, SciPy.
"""
from itertools import combinations
from math import factorial, gamma, pi, sqrt
import numpy as np
from scipy.spatial import ConvexHull, HalfspaceIntersection


def basis(n):
    a = np.zeros((n, n - 1))
    for j in range(n - 1):
        a[:j + 1, j] = 1.0
        a[j + 1, j] = -(j + 1)
        a[:, j] /= sqrt((j + 1) * (j + 2))
    return a


def code(n, k):
    sets = list(combinations(range(n), k))
    a = np.zeros((len(sets), n))
    for j, ss in enumerate(sets):
        a[j, list(ss)] = 1
    a -= k / n
    r = sqrt(k * (n - k) / n)
    return a / r


def polar_volume(m, s):
    return sqrt(m) * m ** (m - 1) / (
        factorial(s) * factorial(m - 1 - s)
        * (m - s) ** s * s ** (m - 1 - s)
    )


def coefficient(n, k):
    s = min(k, n - k)
    rad = sqrt(k * (n - k) / n)
    dim = n - 2
    sphere_area = 2 * pi ** ((dim + 1) / 2) / gamma((dim + 1) / 2)
    hole_count = 2 * n if 2 * k == n else n
    return hole_count * rad ** dim * polar_volume(n - 1, s) / sphere_area


def check():
    count = 0
    for m in range(3, 7):
        b = basis(m)
        for s in range(1, m):
            A = np.zeros((len(list(combinations(range(m), s))), m))
            for j, ss in enumerate(combinations(range(m), s)):
                A[j, list(ss)] = 1
            # Exact polytope Q = {sum y=0, sum_S y_i<=1}.
            H = np.hstack([A @ b, -np.ones((len(A), 1))])
            vertices = HalfspaceIntersection(H, np.zeros(m - 1)).intersections
            measured = ConvexHull(vertices).volume
            pred = polar_volume(m, s)
            assert abs(measured - pred) < 4e-8 * pred, (m, s, measured, pred)
            count += 1
    for n in range(3, 8):
        b = basis(n)
        for k in range(1, n):
            C = code(n, k)
            rad = sqrt(k * (n-k)/n)
            c = min(k,n-k) / sqrt((n-1)*k*(n-k))
            # Independently construct convex hull facets and test minimal plane distances.
            V = C @ b
            hull = ConvexHull(V)
            dist = -hull.equations[:, -1]  # normals unit
            assert abs(np.min(dist)-c) < 8e-8, (n,k,np.min(dist),c)
            u = (np.eye(n)-np.ones((n,n))/n)
            u /= np.linalg.norm(u, axis=1)[:,None]
            hole_signs = [-1] if k < n/2 else ([1] if k > n/2 else [-1,1])
            for sig in hole_signs:
                for v in sig*u:
                    assert abs(np.max(C @ v)-c)<2e-12
                    count+=1
            rng=np.random.default_rng(n*193+k)
            normals=rng.normal(size=(2500,n))
            normals-=normals.mean(axis=1,keepdims=True)
            normals/=np.linalg.norm(normals,axis=1)[:,None]
            minimum = np.max(normals@C.T,axis=1).min()
            assert minimum>=c-1e-12
            count+=1
    print('SUCCESS:',count,'exact-structure tests; all finite Q volumes and code supports agree')
    for n,k in [(3,1),(4,1),(4,2),(5,2),(6,3),(7,2),(8,3)]:
        print(f'  (n,k)=({n},{k}), coscover={min(k,n-k)/sqrt((n-1)*k*(n-k)):.12g}, C={coefficient(n,k):.12g}')
if __name__=='__main__':
    check()
