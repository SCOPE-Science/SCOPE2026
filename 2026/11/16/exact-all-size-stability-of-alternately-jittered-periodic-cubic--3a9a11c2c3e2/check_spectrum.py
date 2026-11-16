"""Independent finite tests of a periodic cubic B-spline collocation spectrum.

Usage: python check_spectrum.py
Requires: numpy.  Finite tests do not replace the all-size analytic proof.
"""
import math
import numpy as np


def beta(t):
    t = abs(t)
    if t <= 1:
        return (4 - 6*t*t + 3*t*t*t)/6
    if t <= 2:
        return (2-t)**3/6
    return 0.0


def periodized_beta(t, n):
    return sum(beta(t + h*n) for h in range(-2, 3))


def full_matrix(n, delta):
    assert n % 2 == 0 and n >= 4
    xs = np.array([j + (delta if j % 2 == 0 else -delta) for j in range(n)])
    return np.array([[periodized_beta(x-j, n) for j in range(n)] for x in xs])


def parameters(delta):
    a = (4 - 6*delta**2 + 3*delta**3)/6
    b = (4 - 6*(1-delta)**2 + 3*(1-delta)**3)/6
    c = (1-delta)**3/6
    e = delta**3/6
    return a,b,c,e


def predicted_singular_values(n, delta):
    m = n // 2
    a,b,c,e = parameters(delta)
    vals = []
    for r in range(m):
        ct = math.cos(2*math.pi*r/m)
        U = math.sqrt(max(0.,a*a+e*e+2*a*e*ct))
        V = math.sqrt(max(0.,b*b+c*c+2*b*c*ct))
        vals.extend((U+V,abs(U-V)))
    return np.sort(np.array(vals))


def gamma(delta):
    return (1-2*delta)*(1+2*delta-2*delta**2)/3


def run():
    tests=0
    for n in range(4, 66, 2):
        for delta in (0.0,0.03125,0.1,0.2,0.24,0.3,0.4,0.49,0.5):
            A = full_matrix(n, delta)
            actual = np.sort(np.linalg.svd(A, compute_uv=False))
            expect = predicted_singular_values(n, delta)
            assert np.max(abs(actual-expect)) < 1e-10,(n,delta,actual,expect)
            tests+=1
            assert abs(actual[-1] - 1) < 1e-10,(n,delta,actual[-1]);tests+=1
            if delta < 0.5:
                assert abs(actual[0]-gamma(delta))<1e-10,(n,delta,actual[0]);tests+=1
                assert np.linalg.matrix_rank(A,tol=1e-10)==n;tests+=1
            else:
                assert np.linalg.matrix_rank(A,tol=1e-10)==n//2;tests+=1
    print(f"PASS: {tests} direct full-matrix spectral/rank/bound assertions")


if __name__ == '__main__':
    run()
