"""Finite arithmetic checks for Caputo SIR critical-incidence Taylor identities.

The theorem is proved in RESULT.md; this script only checks algebraic instances.
"""
from math import gamma, pi, isclose
from fractions import Fraction
from random import Random


def coeffs(alpha, N, beta, recovery, I0):
    """First three normalized coefficients in powers t^(k alpha)/Gamma(1+k alpha)."""
    S0 = N-I0
    c = beta/N
    H2 = gamma(1+2*alpha)/gamma(1+alpha)**2
    H3 = gamma(1+3*alpha)/(gamma(1+alpha)*gamma(1+2*alpha))
    x0 = c*S0*I0
    s1, i1 = -x0, x0-recovery*I0
    x1 = c*(s1*I0+S0*i1)
    s2, i2 = -x1, x1-recovery*i1
    x2 = c*(s2*I0+S0*i2+H2*s1*i1)
    s3, i3 = -x2, x2-recovery*i2
    x3 = c*(s3*I0+S0*i3+H3*(s1*i2+s2*i1))
    return (x0,x1,x2,x3), (i1, i2), (H2,H3)


def check():
    # Critical instance: N=3, beta=3, recovery=1, I0=1.
    for alpha in [0.03,0.1,0.25,0.5,0.75,0.95,1.0]:
        (x0,x1,x2,x3),(i1,i2),(H2,H3) = coeffs(alpha,3.,3.,1.,1.)
        assert abs(x0-2)<1e-13 and abs(x1)<1e-13
        assert abs(i1-1.)<1e-13 and abs(i2+1.)<1e-13
        assert isclose(x2, -(2+2*H2),rel_tol=1e-12,abs_tol=1e-12)
        assert isclose(x3,2*(H3-H2),rel_tol=1e-10,abs_tol=1e-10)
        assert x2<0 and x3>0 and H3>H2
    (_,_,x2,x3), _, (H2,H3) = coeffs(.5,3.,3.,1.,1.)
    assert isclose(x2,-2-8/pi,rel_tol=1e-13)
    assert isclose(x3,3-8/pi,rel_tol=1e-13)

    rng = Random(83916)
    ntested=0
    for alpha in [0.13,0.3,0.5,0.9,1.0]:
        for _ in range(100):
            N = rng.uniform(2.0,10.0)
            I0 = rng.uniform(.01*N,.49*N)
            S0=N-I0
            beta=rng.uniform(.1,10)
            recovery=beta*(S0-I0)/N
            (x0,x1,x2,x3),(i1,i2),(H2,H3)=coeffs(alpha,N,beta,recovery,I0)
            c=beta/N
            assert abs(x1)<1e-10*max(1,x0)
            assert isclose(i1,c*I0**2,rel_tol=1e-12)
            assert isclose(x2,-c*i1*(recovery*S0+H2*x0),rel_tol=1e-11)
            assert isclose(x3,c*i1*recovery*x0*(H3-H2),rel_tol=1e-9,abs_tol=1e-11)
            assert x2<0 and x3>0
            ntested+=1
    print(f"PASS: {ntested} critical parameter cases and the exact resonant half-order example")

if __name__ == '__main__': check()
