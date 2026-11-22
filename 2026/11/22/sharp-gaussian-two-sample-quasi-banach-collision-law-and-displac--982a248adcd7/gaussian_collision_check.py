"""Independent numerical checks for two-site Gaussian cardinal interpolation.

Requires only the Python standard library. Finite checks do not prove the
uniform optimizer localization or the infinite limiting claims.
"""
import math


def cardinal(t, h):
    den = math.sinh(4*h*h)
    pref = math.exp(h*h-t*t)/den
    return pref*math.sinh(2*h*(h-t)), pref*math.sinh(2*h*(h+t))


def factor(t, h, p):
    a, b = cardinal(t, h)
    return (abs(a)**p+abs(b)**p)**(1/p)


def golden_max(f, lo, hi, iterations=100):
    z = (math.sqrt(5)-1)/2
    x, y = hi-z*(hi-lo), lo+z*(hi-lo)
    fx, fy = f(x), f(y)
    for _ in range(iterations):
        if fx < fy:
            lo, x, fx = x, y, fy
            y = lo+z*(hi-lo)
            fy = f(y)
        else:
            hi, y, fy = y, x, fx
            x = hi-z*(hi-lo)
            fx = f(x)
    t = (lo+hi)/2
    return t, f(t)


def check():
    count = 0
    for p in (0.25, 0.5, 0.75, 0.9):
        for h in (0.2, 0.1, 0.05, 0.025):
            q = math.exp(-4*h*h)
            for t in (-1.2, -0.7, -h, 0.0, h, 0.7, 1.2):
                x, y = cardinal(t, h)
                left = x+q*y
                right = q*x+y
                assert abs(left-math.exp(-(t+h)**2)) < 1e-10
                assert abs(right-math.exp(-(t-h)**2)) < 1e-10
                count += 2
            t, observed = golden_max(lambda x: factor(x, h, p), 0.5, 0.95)
            amp = 2**(1/p-1)/math.sqrt(2*math.e)
            predicted = amp/h*(1+(p+1/3)*h*h)
            center = 1/math.sqrt(2)+math.sqrt(2)*(2/3-p/2)*h*h
            assert abs(observed/predicted-1) < 0.002
            assert abs(t-center) < 0.002
            count += 2
            # Supplementary finite global grid, NOT a uniqueness proof.
            for j in range(1001):
                point = -3+j*0.006
                assert factor(point, h, p) <= observed*(1+1e-8)
                count += 1
    print('GAUSSIAN_TWO_SITE_COLLISION_CHECK_OK', count)


if __name__ == '__main__':
    check()
