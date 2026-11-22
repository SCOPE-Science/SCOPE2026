"""Reproducible numerical checks for normalized fractional-integral BV error.
Requires scipy and numpy. All infinite-order assertions are analytical, not certified by these tests.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import lambertw


def critical_integral(a, s):
    if a >= 50:
        q = a*s
        return quad(lambda z: math.exp((a-1)*math.log1p(-z/a))/z if z < a else 0.0,
                    q, a, epsabs=1e-12, limit=200)[0]
    v = 1-s
    return v**a/a + quad(lambda u: u**a/(1-u), 0.0, v, epsabs=1e-12)[0]


def optimizer(a):
    return brentq(lambda s: a*critical_integral(a,s)-1,
                  1e-7, 1-1e-7, xtol=1e-14)


def h_numeric(a,s):
    return quad(lambda x: -math.expm1(a*math.log1p(-s/x)),
                s,1,epsabs=1e-12)[0]


def step_residual(a,s,x):
    if x < s: return 0.0
    return -math.expm1(a*math.log1p(-s/x))


def signed_jump_error(a, jumps, amplitudes):
    bounds = sorted([0,1]+list(jumps))
    return sum(quad(lambda x: abs(sum(c*step_residual(a,s,x) for s,c in zip(jumps,amplitudes))),
                    l,r,epsabs=1e-11)[0] for l,r in zip(bounds[:-1],bounds[1:]))


def main():
    rng=np.random.default_rng(20261119)
    tests=0
    for a in [0.15,0.5,1.0,2.0,4.0,10.0,100.0,1000.0,10000.0]:
        s=optimizer(a)
        C=1-(1-s)**a
        assert abs(a*critical_integral(a,s)-1) < 3e-8, (a,s)
        assert abs(h_numeric(a,s)-C)<2e-9, (a,s,C)
        for offset in [-0.14,-0.03,0.03,0.13]:
            t=min(1-1e-9,max(1e-9,s+offset))
            assert h_numeric(a,t) <= C+1e-10,(a,t)
            tests+=1
        if a<=100:
            for _ in range(25):
                count=int(rng.integers(1,5))
                jumps=sorted(rng.uniform(0.01,0.99,count))
                coeff=rng.uniform(-2,2,count)
                lhs=signed_jump_error(a,jumps,coeff)
                assert lhs <= C*sum(abs(coeff))+1e-10,(a,lhs,C)
                tests+=1
    assert abs(optimizer(1)-math.exp(-1))<1e-12
    assert abs((1-(1-optimizer(0.001))**0.001)/0.001-math.log(2)) < 0.002
    for a in [100.0,1000.0,10000.0]:
        s=optimizer(a)
        q=a*s
        W=float(lambertw(a).real)
        assert abs(q-W)<0.4
        assert abs(a*(1-s)**a-(W+1))<0.75
    print('FRACTIONAL_BV_CHECK_PASS',tests,'critical-parameter and multi-jump tests')

if __name__=='__main__':main()
