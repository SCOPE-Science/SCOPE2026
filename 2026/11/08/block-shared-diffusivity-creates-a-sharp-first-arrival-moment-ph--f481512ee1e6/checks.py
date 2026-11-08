#!/usr/bin/env python3
"""Numerical diagnostics for the block-shared Brownian search law.

Requires mpmath 1.3 or later; all tests deterministic.  These are checks,
not substitutes for the limiting arguments in the proof.
"""
from mpmath import mp

mp.dps = 45


def s(u, a=1):
    if u <= 0:
        return mp.mpf(1)
    return mp.erf(mp.mpf(a) / (2 * mp.sqrt(u)))


def block_survival(t, alpha, k, a=1):
    # If U is uniform(0,1), U^(1/alpha) is Beta(alpha,1).
    # Split at the natural crossover U~t^(-alpha).
    t, alpha = mp.mpf(t), mp.mpf(alpha)
    split = min(mp.mpf(1), t ** (-alpha))
    f = lambda u: s(t * u ** (1 / alpha), a) ** k if u > 0 else mp.mpf(1)
    return mp.quad(f, [0, split, 1]) if split < 1 else mp.quad(f, [0,1])


def tail_constant(alpha, k, a=1):
    # E[H_k^alpha]=alpha*int_0^infty u^(alpha-1) erf(a/(2sqrt u))^k du.
    alpha = mp.mpf(alpha)
    assert alpha < mp.mpf(k) / 2
    fun = lambda u: alpha * u ** (alpha-1) * s(u, a) ** k
    return mp.quad(fun, [0, 1, mp.inf])


def close(x, y, rel=mp.mpf('0.000000001')):
    assert abs(x-y) <= rel*max(1,abs(x),abs(y)), (str(x),str(y))


def run():
    assertions = 0
    c = 1 / mp.sqrt(mp.pi)
    # One-walker Mellin constant agrees with the gamma integral for alpha<1/2.
    for alpha in ['0.2','0.3','0.4']:
        x = mp.mpf(alpha)
        theoretical = mp.mpf('0.25')**x * mp.gamma(mp.mpf('0.5')-x) / mp.sqrt(mp.pi)
        close(tail_constant(x,1), theoretical, mp.mpf('1e-4'))
        assertions += 1
    # Exact group survival; larger shared blocks are stochastically slower at fixed N.
    for alpha in ['0.4','1.0','1.75']:
        for t in ['0.03','0.5','4','100']:
            values = [block_survival(t,alpha,k)**(6//k) for k in (1,2,3,6)]
            for a,b in zip(values,values[1:]):
                assert b > a, (str(t),str(alpha),str(a),str(b))
                assertions += 1
    # Asymptotic constants in the strict alpha<k/2 regime for groups of 2,3,6.
    for alpha in ['0.2','0.4','0.7']:
        for k in [2,3,6]:
            aa=mp.mpf(alpha)
            if aa < mp.mpf(k)/2:
                t=mp.mpf('1e7')
                ratio=t**aa*block_survival(t,aa,k)/tail_constant(aa,k)
                assert abs(ratio-1)<mp.mpf('0.025'), (alpha,k,str(ratio))
                assertions += 1
    # Alpha > k/2 regime: constant is alpha c^k/(alpha-k/2).
    for alpha,k in [('1.1',1),('1.7',2),('2.5',3)]:
        aa=mp.mpf(alpha)
        goal=aa*c**k/(aa-mp.mpf(k)/2)
        ratio=mp.mpf('1e8')**(mp.mpf(k)/2)*block_survival('1e8',aa,k)/goal
        assert abs(ratio-1)<mp.mpf('0.012'), (alpha,k,str(ratio))
        assertions += 1
    # Critical logarithm coefficients, t very large so additive term is relatively small.
    for alpha,k in [('0.5',1),('1',2)]:
        aa=mp.mpf(alpha)
        t=mp.mpf('1e18')
        target=aa*c**k
        ratio=(t**aa*block_survival(t,aa,k)/mp.log(t))/target
        assert abs(ratio-1)<mp.mpf('0.09'), (alpha,k,str(ratio))
        assertions += 1
    # Finite-vs-infinite mean for 6 particles and alpha=2/5:
    # k=1,2 have tail exponent >1, while k=3,6 have exponent <=1.
    alpha=mp.mpf(2)/5
    thresholds = [ (6//k) * min(alpha,mp.mpf(k)/2) for k in (1,2,3,6)]
    for got, expected in zip(thresholds, ['2.4','1.2','0.8','0.4']):
        close(got, mp.mpf(expected), mp.mpf('1e-30'))
    assertions += 1
    print(f"PASS: {assertions} deterministic numerical / symbolic assertions")
    print("Example alpha=2/5, N=6 group k=1,2,3,6 tail exponents:", [str(x) for x in thresholds])
    print("Example t=100, grouped survival:", [mp.nstr(block_survival(100,alpha,k)**(6//k), 10) for k in (1,2,3,6)])


if __name__ == '__main__':
    run()
