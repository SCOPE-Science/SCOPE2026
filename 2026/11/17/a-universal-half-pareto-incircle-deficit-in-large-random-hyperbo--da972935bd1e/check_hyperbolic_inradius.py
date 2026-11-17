"""Reproducible diagnostics for the hyperbolic-circle random-incircle limit.

Usage: python check_hyperbolic_inradius.py (requires numpy >=1.24).
A numerical check does not prove the uniform-tail or conditional-limit theorems.
"""
import math
import numpy as np


def lorentz_dot(v, w):
    return -float(v[0]*w[0])+float(np.dot(v[1:], w[1:]))


def inradius_via_normals(R, angles):
    # Signed Lorentz-unit inward normals to the three geodesic edges.
    X = np.array([[math.cosh(R), math.sinh(R)*math.cos(a),
                   math.sinh(R)*math.sin(a)] for a in angles])
    linear_rows = []
    for i, j, k in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
        n = np.cross(X[i]*[-1.0, 1.0, 1.0], X[j]*[-1.0, 1.0, 1.0])
        n /= math.sqrt(lorentz_dot(n, n))
        if lorentz_dot(X[k], n) < 0:
            n = -n
        linear_rows.append(n*[-1.0, 1.0, 1.0])
    q = np.linalg.solve(np.asarray(linear_rows), np.ones(3))
    return math.asinh(1.0/math.sqrt(-lorentz_dot(q, q)))


def inradius_via_sides(R, angles):
    lengths = [math.acosh(1+2*math.sinh(R)**2*math.sin((angles[i]-angles[j])/2)**2)
               for i,j in ((1,2),(2,0),(0,1))]
    s = sum(lengths)/2
    q2 = math.prod(-math.expm1(-2*(s-a)) for a in lengths)/(-math.expm1(-2*s))/4
    return math.atanh(math.sqrt(q2))


def limit_statistic(angles):
    ordered = np.sort(np.asarray(angles))
    gaps = np.diff(np.r_[ordered, ordered[0]+2*math.pi])/2
    cot = 1/np.tan(gaps)
    return sum((cot[i]+cot[(i+1)%3])**2 for i in range(3))/3


def run():
    rng = np.random.default_rng(20261110)
    for R in (1.0, 2.0, 4.0, 6.0):
        for _ in range(8):
            angles = rng.uniform(0, 2*math.pi, 3)
            a = inradius_via_sides(R, angles)
            b = inradius_via_normals(R, angles)
            assert abs(a-b) < 2e-9, (R, a, b)
            assert 0 < a < math.log(3)/2
    fixed = (0.0, 1.6, 3.8)
    z = limit_statistic(fixed)
    discrepancies = [abs(math.exp(2*R)*(math.log(3)/2 - inradius_via_sides(R,fixed))/z - 1)
                     for R in (3.0,4.0,5.0,6.0)]
    assert discrepancies[-1] < .002 and all(x>y for x,y in zip(discrepancies,discrepancies[1:])), discrepancies

    # Independent normalized-exponential sampling of Dirichlet(1,1,1) gaps.
    sample_size=1_600_000
    raw = rng.exponential(size=(sample_size,3))
    gaps = math.pi*raw/raw.sum(axis=1)[:,None]
    co = 1/np.tan(gaps)
    Z = ((co[:,0]+co[:,1])**2+(co[:,1]+co[:,2])**2+(co[:,2]+co[:,0])**2)/3
    constant=6*math.sqrt(2/3)/math.pi
    threshold=6000
    observed = float(np.mean(Z>threshold)*math.sqrt(threshold))
    assert abs(observed/constant - 1) < .035, (observed, constant)
    take=Z>threshold
    scale=np.sqrt(threshold)*np.min(gaps[take],axis=1)
    next_gap=gaps[take][np.arange(np.count_nonzero(take)),
                        (np.argmin(gaps[take],axis=1)+1)%3]/math.pi
    location=np.bincount(np.argmin(gaps[take],axis=1),minlength=3)/np.count_nonzero(take)
    assert abs(np.mean(scale) - math.sqrt(2/3)/2) < .025
    assert abs(np.mean(next_gap)-.5)<.025
    assert max(abs(location-1/3))<.04
    print('HYPERBOLIC_INCIRCLE_PARETO_GEOMETRY_CHECK_OK')
    print('tail constant predicted',constant,'observed',observed)
    print('near-collision scale mean',np.mean(scale),'next-gap fraction mean',np.mean(next_gap))
    print('short-gap location frequencies',location)
    print('fixed-angle convergence relative errors',discrepancies)

if __name__ == '__main__':
    run()
