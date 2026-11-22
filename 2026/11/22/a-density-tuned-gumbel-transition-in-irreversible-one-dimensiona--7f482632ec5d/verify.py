"""Reproducibility checks for the one-dimensional saturated spin-flip ordering-time theorem.

Requires Python 3, numpy, scipy, sympy. This is not an infinite-size proof.
"""
import math
import numpy as np
import sympy as sp
from scipy.linalg import expm


def exact_tail(p, t):
    if abs(p - 0.5) < 1e-13:
        return math.exp(-t) * (1.0 + 0.5 * t)
    return (p * math.exp(-t) - (1-p) * math.exp(-2*p*t)) / (2*p-1)


def conditional_domain_tail(k, t):
    if k == 1:
        return math.exp(-t)
    Q = np.zeros((k, k))
    for n in range(1, k+1):
        rate = min(2, n)
        i = n-1
        Q[i, i] = -rate
        if n > 1:
            Q[i, i-1] = rate
    # row generator, initial stage k; column of all ones
    return float(expm(Q*t)[k-1, :].sum())


def centering(L, p):
    if p < 0.5:
        return (math.log(L) + math.log(p*(1-p)**2/(1-2*p)))/(2*p), 2*p
    if p > 0.5:
        return math.log(L) + math.log(p*p*(1-p)/(2*p-1)), 1.0
    return math.log(L) + math.log(math.log(L)) - math.log(8), 1.0


def simulate_ring(L, p, rng):
    spins = rng.random(L) < p
    if not spins.any():
        return math.inf
    plus = np.flatnonzero(spins)
    down_lengths = np.diff(np.r_[plus, plus[0]+L])-1
    down_lengths = down_lengths[down_lengths > 0]
    if down_lengths.size == 0:
        return 0.0
    durations = rng.exponential(size=down_lengths.size)
    mask = down_lengths > 1
    durations[mask] += rng.gamma(shape=down_lengths[mask]-1, scale=0.5)
    return float(durations.max())


def direct_ctmc_on_ring(initial, rng):
    spins = np.array(initial, dtype=bool)
    L = len(spins)
    elapsed = 0.0
    if not spins.any():
        return math.inf
    while not spins.all():
        enabled = np.flatnonzero((~spins) & (np.roll(spins,1) | np.roll(spins,-1)))
        if not len(enabled):
            raise AssertionError('unexpected stuck nonuniform state')
        elapsed += float(rng.exponential(scale=1.0/len(enabled)))
        spins[rng.choice(enabled)] = True
    return elapsed


def main():
    p, s, t = sp.symbols('p s t', real=True, positive=True)
    laplace = sp.factor((p*(s+2))/((s+2*p)*(s+1)))
    weighted = sp.factor(p/(s+1)+(1-p)*2*p/((s+2*p)*(s+1)))
    assert sp.simplify(laplace-weighted) == 0
    tail = (p*sp.exp(-t)-(1-p)*sp.exp(-2*p*t))/(2*p-1)
    assert sp.simplify(sp.limit(tail,p,sp.Rational(1,2)) - sp.exp(-t)*(1+t/2)) == 0
    assert sp.simplify(tail.subs(t,0)-1)==0  # exact survival normalization
    for density in (0.2, 0.35, 0.5, 0.8):
        for time in (0.25, 1.0, 3.0, 6.0):
            # Infinite mixture of geometric run lengths, with exact phase-type tails
            weighted_sum = sum(density*(1-density)**(k-1)*conditional_domain_tail(k,time) for k in range(1,105))
            assert abs(weighted_sum-exact_tail(density,time)) < 2e-9, (density,time,weighted_sum,exact_tail(density,time))
    for density in (0.25, 0.5, 0.75):
        for L in (100000, 100000000):
            b, rate = centering(L, density)
            expected_count = L*density*(1-density)*exact_tail(density,b)
            assert 0.6 < expected_count < 1.7, (L,density,expected_count)
    # Critical detuning intensity is evaluated in log space to avoid enormous L.
    for z in (1000., 10000.):
        for a in (-2., -1., 0., 1., 2.):
            q = 0.5 + a/z
            w = -math.expm1(-2*a)/(2*a) if a else 1.
            b = z + math.log(z) - math.log(8.) + math.log(w)
            if a:
                scaled_tail = math.exp(z-b) * (q-(1-q)*math.exp(-(2*q-1)*b))/(2*q-1)
            else:
                scaled_tail = math.exp(z-b)*(1+b/2)
            assert abs(q*(1-q)*scaled_tail-1.) < 0.04, (a,z,scaled_tail)
    rng = np.random.default_rng(20261117)
    # Independent stochastic state updates vs. exact product of pure-death laws.
    initial = [True, False, False, True, False, False, False, True, False, True, True, True]
    domain_lens = [2,3,1]
    at = 2.0
    pred = 1.0-np.prod([1-conditional_domain_tail(k,at) for k in domain_lens])
    sims = np.array([direct_ctmc_on_ring(initial,rng) for _ in range(12500)])
    empirical = float((sims > at).mean())
    assert abs(empirical-pred) < 0.018, (empirical, pred)
    print('direct finite-cycle CTMC tail:',round(empirical,5),'vs independent-domain prediction',round(pred,5))
    # Genuine Bernoulli rings, not a prefabricated independent-run sample.
    for density in (0.3,0.5,0.8):
        L = 3000
        b, rate = centering(L,density)
        samples = np.array([simulate_ring(L,density,rng) for _ in range(1100)])
        empirical = float((rate*(samples-b) <= 0).mean())
        reference = math.exp(-1)
        # Slow finite-size convergence is expected at density 1/2.
        assert abs(empirical-reference) < 0.13, (density,empirical,reference)
        print('Bernoulli ring density',density,'CDF at Gumbel center',round(empirical,4),'limit',round(reference,4))
    print('PASS: symbolic identity, exact domain law, direct CTMC, finite Bernoulli rings')


if __name__ == '__main__':
    main()
