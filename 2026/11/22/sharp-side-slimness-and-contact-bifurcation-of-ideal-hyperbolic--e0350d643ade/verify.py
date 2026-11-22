#!/usr/bin/env python3
"""Independent direct-geodesic sample checks for ideal quadrilateral slimness.

Standard library only. These numerical checks supplement, not replace, the
exact proof and its unrestricted quantifiers.
"""
import math


def h_dist(x1, y1, x2, y2):
    assert y1 > 0 and y2 > 0
    return math.acosh(1.0 + ((x1 - x2)**2 + (y1 - y2)**2)/(2.0*y1*y2))


def semicircle_distance(y, a, b):
    """Minimise actual point-to-point hyperbolic distance, NOT the claimed formula."""
    assert 0 <= a < b
    center, radius = (a + b)/2, (b - a)/2
    def cost(t):
        theta = 2*math.atan(math.exp(t))
        xx = center + radius*math.cos(theta)
        yy = radius*math.sin(theta)
        return h_dist(0, y, xx, yy)
    # golden section in logarithmic half-angle; covers both cusp limits
    lo, hi = -19.0, 19.0
    phi = (math.sqrt(5)-1)/2
    c = hi - phi*(hi-lo); d = lo + phi*(hi-lo)
    fc, fd = cost(c), cost(d)
    for _ in range(155):
        if fc < fd:
            hi, d, fd = d, c, fc
            c = hi - phi*(hi-lo); fc = cost(c)
        else:
            lo, c, fc = c, d, fd
            d = lo + phi*(hi-lo); fd = cost(d)
    return min(fc, fd)


def independent_distance(y, lam):
    return min(semicircle_distance(y, 0, 1),
               math.asinh(lam/y),
               semicircle_distance(y, 1, lam))


def formula_distance(y, lam):
    return math.asinh(min(y, lam/y, (lam+y*y)/((lam-1)*y)))


def one_side_peak(lam):
    return math.sqrt(lam) if lam <= 3 else math.sqrt(lam/(lam-2))


def global_peak(lam):
    kappa = max(lam, lam/(lam-1))
    return math.sqrt(kappa if kappa <= 3 else kappa/(kappa-2))


def check():
    total = 0
    for lam in (1.12,1.4,1.5,1.9,2,2.5,2.99,3,3.01,4,5,10,30):
        for scale in (.16,.32,.6,1,1.35,2.1,4.2):
            y = scale*math.sqrt(lam)
            direct, formula = independent_distance(y,lam),formula_distance(y,lam)
            assert abs(direct-formula) < 1e-8,(lam,y,direct,formula)
            total += 1
        roots=[math.sqrt(lam)] if lam <= 3 else [math.sqrt(lam/(lam-2)), math.sqrt(lam*(lam-2))]
        for y in roots:
            v=math.sinh(independent_distance(y,lam))
            assert abs(v-one_side_peak(lam))<1e-8,(lam,y,v)
            total+=1
        assert global_peak(lam)>=one_side_peak(lam)-1e-13
        for lx in (lam, lam/(lam-1)):
            for i in range(201):
                x = math.exp((i-100)*.11)
                y = x*math.sqrt(lx)
                assert math.sinh(formula_distance(y,lx)) <=global_peak(lam)+1e-12
                total += 1
    for lam in (1.5,2,3,10,500):
        assert abs(global_peak(lam) - global_peak(lam/(lam-1)))<1e-12
    assert abs(global_peak(3) - math.sqrt(3))<1e-12
    assert abs(global_peak(2) - math.sqrt(2))<1e-12
    print(f'PASS: {total} direct/analytic checks, 5 symmetry comparisons, phase endpoints')

if __name__=='__main__': check()
