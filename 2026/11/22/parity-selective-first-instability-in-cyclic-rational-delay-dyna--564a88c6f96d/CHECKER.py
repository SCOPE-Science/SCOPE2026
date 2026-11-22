"""Independent numerical diagnostics for a cyclic rational-map equilibrium spectrum.
The analytical proof is in RESULT.md; these finite checks are not its substitute.
"""
import cmath
import math


def f(a, cosine):
    return 1 - 9*a*a + 4*cosine*a**3 + 12*a**4


def root_bisect(k, iterations=90):
    cosine = -1.0 if k % 2 == 0 else -math.cos(math.pi/k)
    left, right = 0.0, 0.5
    for _ in range(iterations):
        mid = (left + right)/2
        if f(mid, cosine) > 0:
            left = mid
        else:
            right = mid
    return (left+right)/2


def roots_mode(a, k, j):
    w = cmath.exp(2j*math.pi*j/k)
    disc = cmath.sqrt(a*a*w*w - 8*a*w)
    return ((a*w + disc)/2, (a*w - disc)/2)


def check():
    samples = [2,3,4,5,6,7,9,10,11,17,21,32,51,100]
    for k in samples:
        a = root_bisect(k)
        t = a/(1-a)**2
        if k % 2 == 0:
            assert abs(a - 1/3) < 1e-12
            assert abs(t - 0.75) < 1e-12
        else:
            assert 1/3 < a < 0.5
            assert t > 0.75
            expected = 0.75 + 3*math.pi**2/(50*k*k)
            assert abs(t-expected) < 0.05/k**2
        eps = 1e-7
        rad_below = max(abs(l) for j in range(k) for l in roots_mode(a-eps,k,j))
        rad_at = max(abs(l) for j in range(k) for l in roots_mode(a,k,j))
        rad_above = max(abs(l) for j in range(k) for l in roots_mode(a+eps,k,j))
        assert rad_below < 1 and abs(rad_at-1) < 5e-10 and rad_above > 1
        print(f'k={k:3d} alpha_critical={a:.12f} t_critical={t:.12f}')
    assert abs(root_bisect(3)-0.348356193200759) < 1e-12
    assert abs(root_bisect(3)/(1-root_bisect(3))**2 - 0.820357195635835) < 1e-12
    print('PASS: 14 ring sizes, spectrum, parity, asymptotic, k=3 benchmark')


if __name__ == '__main__':
    check()
