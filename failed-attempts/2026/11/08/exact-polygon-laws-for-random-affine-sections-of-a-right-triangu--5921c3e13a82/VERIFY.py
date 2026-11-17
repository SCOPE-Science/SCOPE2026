"""Reproducibility checks for affine-plane section counts of triangular bipyramids.

Python 3 standard library only. Numerical tests are not substitutes for the proof.
"""
import math
import random

PI = math.pi
C = 3 * math.sqrt(3) / 4


def fg(h):
    s = math.sqrt(1 + h * h)
    f = (3 / PI) * ((math.sqrt(3) / 2) * math.atan(2 * h)
                    - s * math.atan(math.sqrt(3) * h / s)
                    + PI * h / 3)
    g = (3 / PI) * (-(math.sqrt(3) / 2) * math.atan(1 / (2 * h))
                    + s * math.atan(s / (math.sqrt(3) * h))
                    - PI * h / 6)
    return f, g


def probs(h):
    f, g = fg(h)
    width = h + C - f
    return [(h - f) / width, (C - f - g) / width,
            f / width, g / width]


def midpoint_integral(fn, left, right, n=120000):
    step = (right - left) / n
    return step * sum(fn(left + (i + .5) * step) for i in range(n))


def fprime(h):
    return (3 / PI) * midpoint_integral(
        lambda x: math.cos(x)**2 / (math.cos(x)**2 + h*h), 0, PI / 3, 15000)


def root():
    lo, hi = .2, 4
    for _ in range(70):
        mid = (lo + hi) / 2
        val = fprime(mid) * (mid + C) - fg(mid)[0]
        if val > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def direct_crossing_count(h, normal, offset):
    verts = [(math.cos(2*PI*j/3), math.sin(2*PI*j/3), 0.)
             for j in range(3)] + [(0., 0., h), (0., 0., -h)]
    values = [sum(x*y for x,y in zip(normal, v)) - offset for v in verts]
    edges = [(i,j) for i in range(5) for j in range(i+1,5)
             if (i,j) != (3,4)]
    return sum((values[i] > 0) != (values[j] > 0) for i,j in edges)


def check():
    # Independent angle integrals verify the elementary closed formulas.
    for h in (.1, .3, .7, 1.0, 1.5, 3., 8.):
        f, g = fg(h)
        fi = 3/PI * midpoint_integral(
            lambda x: math.cos(x) * math.atan(h / math.cos(x)),
            0, PI/3)
        gi = 3/PI * midpoint_integral(
            lambda x: math.sin(x) * math.atan(math.sin(x)/h),
            0, PI/6)
        assert abs(f-fi) < 1.0e-9, (h, f, fi)
        assert abs(g-gi) < 1.0e-9, (h, g, gi)
        p = probs(h)
        assert all(-1e-11 <= x <= 1 + 1e-11 for x in p)
        assert abs(sum(p)-1.) < 1e-12
        assert abs(p[0]+p[2] - h/(h+C-f)) < 1e-12

    hstar = root()
    peak = probs(hstar)[2]
    assert abs(hstar-1.21144841358) < 1e-9, hstar
    assert abs(peak-.462970871315) < 1e-9, peak
    assert probs(hstar-.08)[2] < peak
    assert probs(hstar+.08)[2] < peak

    # Independent random normal and random section offset. Each sample
    # is weighted by its available offset interval (Crofton measure).
    rng = random.Random(20231124)
    for h in (.2, .9, 2.):
        nsamp = 140000
        totals = [0., 0., 0., 0.]
        widthtotal = 0.
        for _ in range(nsamp):
            z = 2*rng.random()-1
            ang = 2*PI*rng.random()
            radial = math.sqrt(1-z*z)
            u = (radial*math.cos(ang),radial*math.sin(ang),z)
            vals = [radial*math.cos(ang+2*PI*j/3) for j in range(3)]
            vals += [h*z, -h*z]
            lo, hi = min(vals), max(vals)
            width = hi-lo
            offset = lo + width*rng.random()
            sides = direct_crossing_count(h, u, offset)
            assert 3 <= sides <= 6
            totals[sides-3] += width
            widthtotal += width
        measured = [t/widthtotal for t in totals]
        expected = probs(h)
        assert max(abs(a-b) for a,b in zip(measured,expected)) < .009, (h,measured,expected)

    print('BIPYRAMID_AFFINE_SECTION_POLYGON_LAW_CHECKS_PASSED')
    print('optimal height %.12f; maximal pentagon probability %.12f' % (hstar, peak))

if __name__ == '__main__':
    check()
