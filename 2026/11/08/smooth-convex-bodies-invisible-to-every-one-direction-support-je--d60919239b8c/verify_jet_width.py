#!/usr/bin/env python3
"""Numerical consistency checks for a smooth support-function family.

The exact conclusions follow from the analytic argument; these quadratures
check selected identities and separations, not infinitely many directions.
"""
import math

PI = math.pi
DELTA = PI / 100.0
EPS = DELTA * DELTA / 1000.0
N = 120000  # divisible by 6 so the test shifts fit the grid


def bump_and_derivatives(x):
    """The periodic bump and its first two angle derivatives."""
    t = (x + PI / 2.0) % PI - PI / 2.0
    s = t / DELTA
    if abs(s) >= 1.0:
        return 0.0, 0.0, 0.0
    q = 1.0 - s*s
    f = math.exp(-1.0/q)
    f1 = f*(-2.0*s / (q*q)) / DELTA
    f2 = f*(4*s*s/q**4 - 2/q**2 - 8*s*s/q**3) / (DELTA*DELTA)
    return f, f1, f2


def profiles(alpha):
    hs, rs, d1 = [], [], []
    for i in range(N):
        th = PI*i/N
        v1, p1, z1 = bump_and_derivatives(th)
        v2, p2, z2 = bump_and_derivatives(th-alpha)
        hs.append(1.0 + EPS*(v1+v2))
        d1.append(EPS*(p1+p2))
        rs.append(1.0 + EPS*(v1+v2+z1+z2))
    return hs, d1, rs


def quad_bump(func, n=50000):
    step = 2*DELTA/n
    return step*sum(func(-DELTA + (j + .5)*step) for j in range(n))


def check():
    alphas = [PI/3, PI/2]
    out = [profiles(a) for a in alphas]
    b_integral = quad_bump(lambda t: bump_and_derivatives(t)[0])
    energy = quad_bump(lambda t: (lambda b, bp, bpp:b*b-bp*bp)(*bump_and_derivatives(t)))
    b_sq = quad_bump(lambda t: bump_and_derivatives(t)[0]**2)
    theory_P = 2*PI + 4*EPS*b_integral
    theory_A = PI + 4*EPS*b_integral + 2*EPS*EPS*energy
    for hs, hprime, rs in out:
        assert min(rs) > 0.968, min(rs)
        p = (2*PI/N)*sum(hs)
        area = (PI/N)*sum(h*r for h, r in zip(hs, rs))
        assert abs(p - theory_P) < 2e-11, (p, theory_P)
        assert abs(area - theory_A) < 2e-11, (area, theory_A)
        assert all(h >= 1.0 for h in hs)
    for j in (0,1,2):
        arr0 = sorted(out[0][j])
        arr1 = sorted(out[1][j])
        err = max(abs(a-b) for a, b in zip(arr0,arr1))
        assert err < 5e-10, (j,err)
    def autocorr(hs):
        return sum((hs[i]-1)*(hs[(i+N//3)%N]-1) for i in range(N))/N
    a = autocorr(out[0][0])
    b = autocorr(out[1][0])
    predicted = EPS*EPS*b_sq/PI
    assert predicted > 0
    assert abs(a - predicted) < predicted * 1e-6, (a,predicted)
    assert abs(b) < 1e-25, b
    print('VERIFY_OK shapes=2 normal_samples_per_shape=120000 jet_orders=0,1,2',
          'perimeter_area_identities=4 distinct_two_angle_correlations=1',
          'minimum_radius_greater_than=0.968')
    print('area=',format(theory_A,'.15g'),'perimeter=',format(theory_P,'.15g'),
          'alpha_correlation=',format(a,'.12g'),'beta_correlation=',format(b,'.12g'))

if __name__=='__main__':
    check()
