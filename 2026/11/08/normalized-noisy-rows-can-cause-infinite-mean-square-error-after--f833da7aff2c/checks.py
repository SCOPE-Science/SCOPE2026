#!/usr/bin/env python3
"""Finite auxiliary checks for the normalized-row signal-averaging construction.

The infinite-expectation proof is analytic; simulations cannot establish it.
"""
import math
import random


def f_a(t, a):
    return (1 - a*a) / (2*math.pi*(1 - 2*a*math.cos(t) + a*a))


def tikhonov(vx, vy, lam):
    den = vx*vx + vy*vy + lam
    return vx/den, vy/den


def sample_angle(a, rng):
    # Wrapped Cauchy/Poisson-kernel representation via complex Moebius map.
    t = 2 * math.pi * rng.random()
    zx, zy = math.cos(t), math.sin(t)
    # (a+z)/(1+a z) (unit circle mapped to itself)
    dr, di = 1+a*zx, a*zy
    nr, ni = a+zx, zy
    dd = dr*dr + di*di
    ux = (nr*dr + ni*di)/dd
    uy = (ni*dr - nr*di)/dd
    return ux, uy


def run():
    checks = 0
    for a in (0.05, 0.2, 0.6, 0.95, 0.999):
        # Exact batch-one (unregularized) expected risk.
        assert abs((1 + a**-2 - 2*a**-1*a) - (a**-2 - 1)) < 1e-10
        nquad = 16384
        mean0 = mean1 = mass = 0.0
        for k in range(nquad):
            t = 2*math.pi*(k+0.5)/nquad
            p = (2*math.pi/nquad) * f_a(t, a)
            mass += p
            mean0 += p*math.cos(t)
            mean1 += p*math.sin(t)
        assert abs(mass-1) < 2e-7
        assert abs(mean0-a) < 2e-7
        assert abs(mean1) < 2e-7
        checks += 3
    for n in range(3, 256):
        angles = [2*math.pi*j/n for j in range(n)]
        x = sum(map(math.cos, angles))/n
        y = sum(map(math.sin, angles))/n
        assert math.hypot(x, y) < 1e-12
        t0, t1 = angles[:2]
        jac_det = ((-math.sin(t0))*math.cos(t1) - (-math.sin(t1))*math.cos(t0))/(n*n)
        assert abs(abs(jac_det) - abs(math.sin(2*math.pi/n))/(n*n)) < 2e-14
        assert abs(jac_det) > 1e-15
        checks += 3
    rng = random.Random(20261101)
    for a in (0.3, 0.85):
        for n in (2, 3, 4, 16, 64):
            sum_x=sum_y=sum_sq=0.0
            trials = 2000
            for _ in range(trials):
                vv = [sample_angle(a, rng) for _ in range(n)]
                vx=sum(t[0] for t in vv)/n
                vy=sum(t[1] for t in vv)/n
                r2 = vx*vx + vy*vy
                assert 0 < r2 < 1.000000000001
                # x0=0, b=(1,0) -> row 1 only has residual.
                for theta in (0.0, 0.4, 1.0):
                    norm_res1=1/r2
                    thresh=theta*norm_res1+(1-theta)/(r2+1)
                    assert 0 < thresh <= norm_res1+1e-10
                    checks += 1
                xx, yy=tikhonov(vx,vy,1/n)
                sum_sq += (xx-1/a)**2 + yy*yy
                sum_x += vx
                sum_y += vy
            mser=sum_sq/trials
            bound = (32*(1-a*a)/(n*a**4) + 8*(n/2+2/a**2)*math.exp(-n*a*a/16) + 2/(n*n*a**6))
            assert mser < bound + 1e-12
            assert abs(sum_x/trials-a) < 0.3
            assert abs(sum_y/trials) < 0.3
            checks += 3
    print(f'FINITE_CHECKS_OK {checks} (no empirical claim of an infinite moment)')


if __name__ == '__main__':
    run()
