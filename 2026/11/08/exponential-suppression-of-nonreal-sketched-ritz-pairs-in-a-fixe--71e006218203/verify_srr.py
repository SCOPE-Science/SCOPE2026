"""Standalone reproducibility checks for the Gaussian-sketch nonreal-pair law.

Python 3 standard library only. Numerical tests supplement, not replace, the proof.
"""
from fractions import Fraction
from math import cos, sqrt, pi, exp, log1p, isfinite
from random import Random


def exact_discriminant(a, d, t, v1, v2):
    m11 = a + t*v1
    m12 = t*v1
    m21 = t*v2
    m22 = a + d + t*v2
    return (m11+m22)**2 - 4*(m11*m22-m12*m21)


def angular_probability(s, h, intervals=12000):
    assert s >= 3 and isinstance(s, int) and h > 0
    assert intervals % 2 == 0
    def integrand(i):
        phi = (pi/4)*i/intervals
        c = cos(phi)
        z = sqrt(max(0.0, cos(2*phi)))
        near = 2*h/(c+z)
        far = 2*h/(c-z) if c > z else float('inf')
        e = (s-1)/2
        near_part = exp(-e*log1p(near*near))
        far_part = exp(-e*log1p(far*far)) if isfinite(far) else 0.0
        return near_part-far_part
    total = integrand(0)+integrand(intervals)
    total += 4*sum(integrand(i) for i in range(1,intervals,2))
    total += 2*sum(integrand(i) for i in range(2,intervals,2))
    return total/(12*intervals)


def gaussian_event(rng, s, h):
    # Independent columns of the s x 3 Gaussian matrix; solve G^T G v=G^T w.
    g11 = g12 = g22 = c1 = c2 = 0.0
    for _ in range(s):
        x, y, z = rng.gauss(0,1), rng.gauss(0,1), rng.gauss(0,1)
        g11 += x*x; g12 += x*y; g22 += y*y
        c1 += x*z; c2 += y*z
    det = g11*g22-g12*g12
    v1 = (g22*c1-g12*c2)/det
    v2 = (g11*c2-g12*c1)/det
    u = (v1+v2)/sqrt(2)
    b = (v1-v2)/sqrt(2)
    parabola = b > h + u*u/(4*h)
    # t=1, delta=2 sqrt(2) h. Identical algebraic criterion.
    d = 2*sqrt(2)*h
    matrix_event = exact_discriminant(1.0, d, 1.0, v1, v2) < 0
    assert parabola == matrix_event
    return parabola


def run():
    checks=0
    rng=Random(20261107)
    for _ in range(3000):
        a=Fraction(rng.randint(1,8),rng.randint(1,5))
        d=Fraction(rng.randint(1,8),rng.randint(1,5))
        t=Fraction(rng.randint(1,8),rng.randint(1,5))
        v1=Fraction(rng.randint(-15,15),rng.randint(1,7))
        v2=Fraction(rng.randint(-15,15),rng.randint(1,7))
        target = d*d-2*d*t*(v1-v2)+t*t*(v1+v2)**2
        assert exact_discriminant(a,d,t,v1,v2)==target
        checks+=1
    # A=[[1,0,1],[0,2,1],[1,1,2]] is SPD; a full-rank 3x3 sketch
    # has first two columns e1,e2 and third column (1,-1,1).
    assert exact_discriminant(Fraction(1),Fraction(1),Fraction(1),Fraction(1),Fraction(-1)) == -3
    checks+=1
    h=1/(2*sqrt(2))
    p3=angular_probability(3,h)
    assert abs(p3 - 0.1924500897) < 0.000002
    checks+=1
    # Direct Monte Carlo on the original Gaussian sketch, independent
    # of the one-dimensional angular quadrature.
    for s in (3,4,8,16):
        analytic = angular_probability(s,h)
        trials=14000
        count=sum(gaussian_event(rng,s,h) for _ in range(trials))
        observed=count/trials
        tolerance=7*sqrt(analytic*(1-analytic)/trials)+0.003
        assert abs(observed-analytic) < tolerance, (s,observed,analytic)
        checks += trials+1
    q=1+h*h
    ratios=[]
    for s in (40,80,160,320,640):
        p=angular_probability(s,h)
        leading=(q/h)/sqrt(3*pi*s)*q**(-s/2)
        ratios.append(p/leading)
        assert 0 < p < 0.5
        checks+=2
    assert all(a<b for a,b in zip(ratios,ratios[1:]))
    assert abs(ratios[-1]-1)<0.03
    checks+=2
    print('VERIFIED:',checks,'supplementary assertions; p_3=',p3,
          '; asymptotic ratios=',[round(x,6) for x in ratios])


if __name__=='__main__':
    run()
