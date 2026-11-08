"""Reproduce exact Fourier Gram matrices and narrow two-arc asymptotics.

Requires Python >= 3.10 and mpmath >= 1.3. Pure numerical cross-check;
the analytical limit is proved separately.
"""
from math import comb
from mpmath import mp
mp.dps = 65


def gram(m, halfwidth, center):
    ks = range(-m, m + 1)
    def moment(k):
        if k == 0:
            return 2 * halfwidth / mp.pi
        return 2 * mp.sin(k * halfwidth) * mp.cos(k * center) / (mp.pi * k)
    return mp.matrix([[moment(k - j) for k in ks] for j in ks])


def smallest(m, halfwidth, center):
    values, _ = mp.eigsy(gram(m, halfwidth, center))
    return values[0]


def polynomial_norm(m, c):
    coefficients = [mp.mpf(1)]
    for _ in range(m):
        newer = [mp.mpf(0)] * (len(coefficients) + 2)
        for k, a in enumerate(coefficients):
            newer[k] += a
            newer[k + 1] -= 2 * c * a
            newer[k + 2] += a
        coefficients = newer
    return mp.fsum(a * a for a in coefficients)


def sharp_constant(m, theta):
    b = comb(2*m, m)
    return (mp.power(2, 4*m+1) * mp.sin(theta)**(2*m)
            / (mp.pi * (2*m+1) * b*b * polynomial_norm(m, mp.cos(theta))))


def run():
    count = 0
    for m in range(1, 6):
        b = comb(2*m, m)
        cstar = mp.power(2, 4*m+1)/(mp.pi*(2*m+1)*b**3)
        assert mp.almosteq(sharp_constant(m, mp.pi/2), cstar)
        count += 1
        assert mp.almosteq(polynomial_norm(m, 0), b)
        count += 1
        for theta in [mp.pi/4, mp.pi/3, 2*mp.pi/5, mp.pi/2, 3*mp.pi/5]:
            value = sharp_constant(m, theta)
            assert value > 0 and value <= cstar*(1+mp.mpf('1e-55'))
            count += 1
            a = mp.mpf('0.022')
            scaled = smallest(m, a, theta)/a**(2*m+1)
            assert abs(scaled/value-1) < mp.mpf('0.005')
            count += 1
        for c in [mp.mpf('0.01'), mp.mpf('0.1'), mp.mpf('0.3'), mp.mpf('0.8')]:
            assert polynomial_norm(m,c) > polynomial_norm(m,0)
            count += 1
        if m <= 4:
            a = mp.mpf('0.035')
            middle = smallest(m,a,mp.pi/2)
            for k in range(1, 9):
                theta = mp.pi*k/18
                if theta <= a or theta >= mp.pi-a:
                    continue
                assert smallest(m,a,theta) < middle
                count += 1
    print('NARROW_TWO_ARC_CHECKS_PASS',count)

if __name__ == '__main__':
    run()
