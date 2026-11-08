"""Exact rational consistency checks for a two-state diffusing-diffusivity tail law.

The infinite-parameter assertions follow from the analytic proof, not these finite tests.
"""
from fractions import Fraction as F
from random import Random


def check(J, lo, hi, beta, t):
    mean = beta * lo + (1 - beta) * hi
    slow = J / hi
    fast = J / mean
    q = slow + t * (fast - slow)
    assert 0 < lo < mean < hi and 0 < beta < 1 and slow < q < fast
    A = 1 + q
    B = J - lo*q
    C = hi*q - J
    H = J - mean*q
    P = A * B * C
    P1 = B*C - A*lo*C + A*B*hi
    P2 = 2*(-lo*C + B*hi + A*(-lo)*hi)
    mu = P / H
    mu1 = (P1*H + mean*P) / H**2
    mu2 = P2/H + 2*mean*P1/H**2 + 2*mean**2*P/H**3
    rem = (1 + J/mean)*J**2*(mean-lo)*(hi-mean)/mean**2
    mu2_independent = 2*lo*hi/mean + 2*mean**2*rem/H**3
    assert mu > 0 and mu1 > 0 and mu2 > 0 and mu2 == mu2_independent
    alpha = q+1
    Flow = alpha*(J-q*lo)
    Fhigh = alpha*(J-q*hi)
    delta = Flow*Fhigh + mu*alpha*(J-q*mean)
    assert delta == 0
    slow_slope = beta/(J+hi)
    p0 = (1+slow)*(J-lo*slow)*hi
    h0 = J-mean*slow
    assert h0 / p0 == slow_slope
    K = (1+fast)*J**2*beta*(1-beta)*(hi-lo)**2/mean**3
    assert rem/mean == K
    return mu, mu1, mu2


def main():
    rng=Random(20261105)
    n=0
    for _ in range(480):
        J=F(rng.randint(1,80),rng.randint(1,30))
        lo=F(rng.randint(1,35),rng.randint(1,40))
        hi=lo+F(rng.randint(1,60),rng.randint(1,30))
        beta=F(rng.randint(1,99),100)
        t=F(rng.randint(1,99),100)
        a=check(J,lo,hi,beta,t)
        assert a[0]>0 and a[1]>0 and a[2]>0
        n+=1
    for t in [F(1,100000), F(1,4), F(1,2), F(3,4), F(99999,100000)]:
        check(F(1),F(3,25),F(11,10),F(18,25),t)
        n+=1
    print('PASS: '+str(n)+' exact-rational parameter samples; determinant, inverse, curvature, limits')

if __name__ == '__main__':
    main()
