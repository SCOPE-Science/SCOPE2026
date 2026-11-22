"""Standalone numerical checks for the symmetric slab deposition comparison.
Only supplementary tests; the all-parameter proof is analytic in RESULT.md.
"""
from math import cosh, sinh, sqrt, exp, log, isclose
from random import Random

def evaluate(D, r, kappa, L, Q):
    assert min(D, r, kappa, L, Q) > 0
    k=sqrt(r/D); a=k*L/2; t=kappa/k
    S=sinh(a)+t*cosh(a)
    B=S/(a+t)
    F=lambda x:cosh(k*x)+t*sinh(k*x)
    threshold=log((B+sqrt(B*B+t*t-1))/(1+t))/k
    C=Q/(2*D*k*S)
    bulk=Q/(L*(r+2*D*kappa/L))
    avg=C*(sinh(a)+t*(cosh(a)-1))/a
    assert 1 < B < F(L/2)
    assert 0 < threshold < L/2
    assert C < bulk < C*F(L/2)
    assert avg > bulk
    assert isclose(C*F(threshold),bulk,rel_tol=2e-12,abs_tol=1e-12)
    assert isclose(2*D*k*S*C,Q,rel_tol=2e-13)
    assert isclose(D*kappa*C,D*k*C*t,rel_tol=2e-13)
    assert isclose(r*L*avg+2*D*kappa*C,Q,rel_tol=1e-12)
    for pos in (0,0.25*threshold, 0.75*threshold): assert C*F(pos) < bulk
    for pos in ((threshold+L/2)/2,L/2): assert C*F(pos)>bulk
    return threshold

if __name__=='__main__':
    exact=evaluate(1,1,1,2,1)
    assert isclose(exact,1-log(2),rel_tol=5e-15)
    assert isclose(0.5/exp(1),0.18393972058572117)
    for vals in ((1,1,0.1,2,1),(1,1,10,2,1),(0.5,0.3,0.2,0.9,2),(9,0.5,1.1,3,0.3)):
        evaluate(*vals)
    rng=Random(502)
    for i in range(500):
        # moderate exponents avoid numerical cancellation/overflow
        D=exp(rng.uniform(-1,1)); r=exp(rng.uniform(-2,1))
        kappa=exp(rng.uniform(-2,1)); L=exp(rng.uniform(-1,1))
        Q=exp(rng.uniform(-1,1))
        evaluate(D,r,kappa,L,Q)
    print('PASS: exact example and 504 positive-parameter numerical tests, including Robin flux and mass balance')
