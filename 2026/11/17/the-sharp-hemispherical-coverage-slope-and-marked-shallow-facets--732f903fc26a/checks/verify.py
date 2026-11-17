"""Reproducible finite checks for the four-cap hemispherical boundary law.

Requires numpy; numerical checks support but do not replace the analytic proof.
"""
import math
import numpy as np


def gauss_integral(acute):
    nodes, weights = np.polynomial.legendre.leggauss(90)
    out = 0.0
    for a, wa in zip(nodes, weights):
        u = (a + 1) * (math.pi / 4 if acute else math.pi / 2)
        lo = math.pi / 2 - u if acute else 0.0
        hi = math.pi / 2 if acute else math.pi - u
        vs = lo + (nodes + 1) * (hi - lo) / 2
        v_integral = np.dot(weights, np.sin(vs) * np.sin(u + vs)) * (hi - lo) / 2
        out += wa * math.sin(u) * v_integral
    return out * (math.pi / 4 if acute else math.pi / 2)


def tetra_sample(seed=20261113, count=480000):
    rng = np.random.default_rng(seed)
    inside_total = 0
    near_total = 0
    plane_total = 0
    t = 0.01
    for size in [80000] * (count // 80000):
        pts = rng.normal(size=(size,4,3))
        pts /= np.linalg.norm(pts, axis=2, keepdims=True)
        inside = np.ones(size, dtype=bool)
        heights = []
        for j in range(4):
            ii = [k for k in range(4) if k != j]
            a,b,c = (pts[:,k,:] for k in ii)
            n = np.cross(b-a,c-a)
            origin_side = np.einsum('ij,ij->i',-a,n)
            vertex_side = np.einsum('ij,ij->i',pts[:,j,:]-a,n)
            inside &= origin_side * vertex_side > 0
            heights.append(np.abs(origin_side)/np.linalg.norm(n,axis=1))
        near = np.min(np.stack(heights),axis=0) < t
        inside_total += inside.sum()
        near_total += (inside & near).sum()
        plane_total += (heights[0] < t).sum()
    containment = inside_total/count
    estimate = near_total/(count*t)
    plane = plane_total/(count*t)
    assert abs(containment-1/8) < 0.003, (containment,inside_total)
    assert abs(estimate-1.5) < 0.35, estimate
    assert abs(plane-1.5) < 0.16, plane
    return containment,estimate,plane


def main():
    j=gauss_integral(False)
    ja=gauss_integral(True)
    assert abs(j-3*math.pi/8)<1e-10,j
    assert abs(ja-3*math.pi/16)<1e-10,ja
    assert abs(ja/j-0.5)<1e-12
    c,coeff,face= tetra_sample()
    print(f'angular integrals J={j:.12f}, Jacute={ja:.12f}; ratio={ja/j:.12f}')
    print(f'simulation: P(center inside)={c:.6f}, ' +
          f'near-inradius P(R<0.01 & centered)/0.01={coeff:.5f}, ' +
          f'plane distance P(H<0.01)/0.01={face:.5f}')
    print('FOUR_CAP_HEMISPHERE_CHECKS_OK')

if __name__=='__main__':
    main()
