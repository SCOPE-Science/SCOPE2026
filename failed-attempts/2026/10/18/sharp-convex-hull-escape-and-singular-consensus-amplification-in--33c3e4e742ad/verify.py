"""Auxiliary finite-arithmetic and numerical checks for the two-agent utility-weighted compromise theorem.
The analytic arguments in RESULT.md, not this program, establish infinite-time claims.
Run: python verify.py
"""
import math
from fractions import Fraction as Q


def shift(mu, eta, tol=1.e-15):
    """Consensus shift divided by initial gap for U(x)=exp(lambda*x), eta=lambda*gap/2."""
    assert 0 < mu < 1 and eta >= 0
    r = abs(1 - 2 * mu)
    s = 0.0
    p = 1.0
    while True:
        s += mu * p * math.tanh(eta * p)
        p *= r
        # Next and later terms bounded using tanh(z) <= z.
        rem = mu * eta * p * p / (1 - r * r)
        if rem < tol:
            return s, rem


def bisect(f, lo, hi, steps=90):
    assert f(lo) < 0 < f(hi)
    for _ in range(steps):
        mid = (lo + hi) / 2
        if f(mid) > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def main():
    assert 26 * 26 > 3 * 15 * 15  # sqrt(3) < 26/15
    assert 3 * 13**4 > 17**4       # 3^(1/4) > 17/13
    # Consequence: the first three positive mean drifts strictly exceed half the initial gap.
    # Exact strict inequalities: tanh(log(3)/4)>4/15; tanh(log(3)/8)>2/15.
    assert Q(3,4) * (Q(1,2) + Q(1,2)*Q(4,15) + Q(1,4)*Q(2,15)) == Q(1,2)
    eta = math.log(3)/2
    total, rem = shift(3/4, eta)
    assert total - rem > 0.5
    assert 0.509 < total < 0.510

    mu_star = bisect(lambda mu: shift(mu, eta)[0] - 0.5, 0.5, .999)
    eta_star = bisect(lambda a: shift(.75, a)[0] - .5, 0., 5.)
    assert .74 < mu_star < .75
    assert .53 < eta_star < .55
    print('fixed-utility mu_crit =',format(mu_star,'.12f'))
    print('fixed-learning eta_crit =',format(eta_star,'.12f'))
    print('mu=3/4 consensus (initial 0,1) =',format(.5+total,'.12f'),'tail<=',rem)

    x,y=0.,1.
    q=1-2*.75
    for t in range(60):
        d=y-x
        assert abs(d-q**t)<1e-10
        th=math.tanh(math.log(3)*d/2)
        x,y=x + .75*(1+th)*d, y - .75*(1-th)*d
    assert abs((x+y)/2-(.5+total)) < 3e-12
    assert abs(x-y)<1e-12

    # For fixed positive lambda*gap, the exact singular prefactor follows from a Riemann sum.
    coefficient=math.log(math.cosh(eta))/math.log(3)
    for mu in [.98,.99,.995,.999]:
        s,_=shift(mu,eta)
        rel=abs((1-mu)*s-coefficient)/coefficient
        print('mu',mu,'relative prefactor error',format(rel,'.6g'))
    assert abs(.001*shift(.999,eta)[0]-coefficient) < .001

    # The sharp crossing curve has two distinct end laws.
    for mu in [.505,.51,.6,.9,.99,.999]:
        a=bisect(lambda z:shift(mu,z)[0]-.5,1e-12,20.)
        print('mu',mu,'eta_crit',format(a,'.9g'))
    tiny=bisect(lambda z:shift(.999,z)[0]-.5,1e-12,2.)
    assert abs(tiny/(2*(1-.999))-1)<.005
    print('All deterministic finite checks passed.')

if __name__=='__main__':
    main()
