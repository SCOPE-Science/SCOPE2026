"""Numerical diagnostics for an exact projective-phase geometric-completeness theorem.

Run with Python 3 and its standard library: python VERIFY.py.
These finite tests are not a proof of the universal statements in RESULT.md.
"""
from math import acos, asin, cos, pi, sin, sqrt


def miss(gaps, threshold, subdivisions=16000):
    assert 0 < threshold < 1
    assert len(gaps) >= 2
    assert all(x >= 0 for x in gaps)
    assert abs(sum(gaps)-pi) < 1e-10
    assert subdivisions % 2 == 0
    h=sqrt(1-threshold*threshold)
    step=threshold/subdivisions
    def integrand(z):
        b=asin(min(1, h/sqrt(1-z*z)))
        return sum(max(0, x-2*b) for x in gaps)
    total=integrand(0)+integrand(threshold)
    for k in range(1,subdivisions):
        total+=(4 if k%2 else 2)*integrand(k*step)
    return step*total/(3*pi)


def edge_coefficient(m):
    angle=pi/(2*m)
    return 4*m*sqrt(2*cos(angle))/(3*pi*sin(angle)**2)


def run():
    checks=0
    for m in range(3,9):
        tc=cos(pi/(2*m))
        uniform=[pi/m]*m
        for factor in (0.15,0.6,0.999):
            threshold=tc*factor
            assert miss(uniform,threshold)<2e-10
            checks+=1
        for threshold in (tc+0.02*(1-tc),tc+0.2*(1-tc),tc+0.8*(1-tc)):
            base=miss(uniform,threshold)
            assert base>0
            checks+=1
            for delta in (0.03,0.09,0.17):
                gaps=uniform[:]
                gaps[0]*=(1-delta)
                gaps[-1]+=pi/m*delta
                assert miss(gaps,threshold)>base+1e-12
                checks+=1
        for gap in (0.04,0.01):
            threshold=tc+gap*(1-tc)
            actual=miss(uniform,threshold)
            asym=edge_coefficient(m)*(threshold-tc)**1.5
            assert abs(actual/asym-1)<0.08
            checks+=1
    m=3
    threshold=0.92
    u=miss([pi/3]*3,threshold)
    a=miss([pi/6,pi/3,pi/2],threshold)
    assert abs(u-0.10286909)<3e-6
    assert abs(a-0.19408187)<3e-6
    checks+=2
    print('PASS',checks,'quadrature, gap and edge-onset diagnostic assertions')


if __name__=='__main__':
    run()
