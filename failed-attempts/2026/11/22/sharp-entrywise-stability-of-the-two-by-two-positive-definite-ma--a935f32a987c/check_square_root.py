"""Supplementary checks for the two-by-two principal-square-root sensitivity theorem.

Run: python3 check_square_root.py
Requires only the Python standard library. Finite checks supplement, not replace, the proof.
"""
import math
import random

RNG = random.Random(20261115)
SQRT2 = math.sqrt(2.0)


def root2(a, b, d):
    q = math.sqrt(a * d - b * b)
    den = math.sqrt(a + d + 2.0 * q)
    return ((a + q) / den, b / den, (d + q) / den)


def spectral(u, v, theta):
    c, s = math.cos(theta), math.sin(theta)
    return (u*u*c*c + v*v*s*s, (u*u-v*v)*c*s,
            u*u*s*s + v*v*c*c)


def predicted(lower, upper):
    u, v = math.sqrt(lower), math.sqrt(upper)
    return ((3+2*SQRT2)/(8*u) - 1/(2*(u+v))
            + (3-2*SQRT2)/(8*v))


def frechet_sqrt(A, H):
    s00, s01, s11 = root2(*A)
    h00, h01, h11 = H
    den = s00 + s11 - s01*s01*(1/s00+1/s11)
    x01 = (h01 - s01*(h00/(2*s00)+h11/(2*s11))) / den
    return ((h00-2*s01*x01)/(2*s00), x01,
            (h11-2*s01*x01)/(2*s11))


def row_integral(u, v, angle):
    c, s = math.cos(angle), math.sin(angle)
    # Matrix sqrt has negative offdiagonal in this orientation.
    x1, y1 = c*c+c*s, s*s-c*s
    x2, y2 = s*s+c*s, c*c-c*s
    f = lambda x,y: x*x/(2*u)+2*x*y/(u+v)+y*y/(2*v)
    return max(f(x1,y1), f(x2,y2))


def diff_max(A,B):
    return max(abs(x-y) for x,y in zip(A,B))


def main():
    tests = 0
    for k in range(1500):
        a = 0.07+8*RNG.random()
        b = a*(1.001 + 999*RNG.random())
        u = math.sqrt(a)+(math.sqrt(b)-math.sqrt(a))*RNG.random()
        v = u+(math.sqrt(b)-u)*RNG.random()
        theta = math.pi*RNG.random()/2
        A = spectral(u,v,theta)
        L = predicted(a,b)
        # Induced derivative norm: exhaust all eight symmetric entrywise sign vertices.
        got = 0.
        for h0 in [-1.,1.]:
            for h1 in [-1.,1.]:
                for h2 in [-1.,1.]:
                    got = max(got, max(map(abs,frechet_sqrt(A,(h0,h1,h2)))))
                    tests += 1
        integral = row_integral(u,v,theta)
        assert abs(got-integral) < 5.e-10*max(1.,got), (got,integral)
        assert got <= L+1.e-9*max(1.,L), (got,L)
        tests += 2
        # Every finite segment stays in the spectral window, as does its midpoint.
        # Use independently sampled eigenvalues, ensuring both remain in the window.
        v1, v2 = sorted([math.sqrt(a)+(math.sqrt(b)-math.sqrt(a))*RNG.random() for _ in range(2)])
        B = spectral(v1,v2,RNG.random()*math.pi/2)
        RA, RB = root2(*A), root2(*B)
        assert diff_max(RA,RB) <= L*diff_max(A,B)+2.e-10*max(1.,L)
        tests += 1
    # Witness: nearly endpoint eigenvalues and perturbation H = all ones.
    for a,b in [(1.,4.),(.2,9.),(2.,2.1),(1.,10000.)]:
        for eps in [1.e-3,1.e-5]:
            lo = a+eps*a
            hi = b-eps*a
            A = spectral(math.sqrt(lo),math.sqrt(hi),math.pi/8)
            H = (1.,1.,1.)
            rate = max(map(abs,frechet_sqrt(A,H)))
            assert 0 <= predicted(a,b)-rate < 0.02*predicted(a,b)
            tests += 1
    # Closed form at the diagonal and high-contrast limit.
    for a in [.1,1.,7.]:
        assert abs(predicted(a,a) - 1/(2*math.sqrt(a))) < 1.e-14
        v = (3+2*SQRT2)/(8*math.sqrt(a))
        assert abs(predicted(a,1.e18) - v) < 1.e-8
        tests += 2
    # An explicit finite perturbation approaching the predicted value.
    a,b=1.,9.
    A=spectral(math.sqrt(a+1.e-4),math.sqrt(b-1.e-4),math.pi/8)
    H=(1.,1.,1.)
    h=1.e-5
    B=tuple(x+h*y for x,y in zip(A,H))
    observed=diff_max(root2(*B),root2(*A))/h
    assert 0 < predicted(a,b)-observed < 2.e-4, (observed,predicted(a,b))
    tests += 1
    print('PASS:',tests,'supplementary analytical-derivative, finite-difference, and window tests')

if __name__=='__main__':
    main()
