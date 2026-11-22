#!/usr/bin/env python3
"""Exact-rational spot checks for a Kalman packet-reliability ordering theorem.

The universal result rests on the algebraic proof, not these finite tests.
Only the Python standard library is required.
"""
from fractions import Fraction as F
from itertools import permutations, product


def update(x, precision):
    return x / (1 + precision * x)


def forecast(x, gain, noise):
    return gain * x + noise


def commutator(x, gain, noise, precision):
    return forecast(update(x, precision), gain, noise) - update(forecast(x, gain, noise), precision)


def algebraic_commutator(x, gain, noise, precision):
    n = (noise * noise
         + (precision * noise * noise + 2 * gain * noise) * x
         + gain * (precision * noise + gain - 1) * x * x)
    return precision * n / ((1 + precision * x) * (1 + precision * (gain * x + noise)))


def law(x, rates, gains, noises, precision):
    states = {x: F(1)}
    for j, p in enumerate(rates):
        updated = {}
        for v, w in states.items():
            for z, mass in [(update(v, precision), w * p), (v, w * (1-p))]:
                updated[z] = updated.get(z, F(0)) + mass
        states = updated
        if j < len(gains):
            states2 = {}
            for v, w in states.items():
                z = forecast(v, gains[j], noises[j]); states2[z] = states2.get(z, F(0)) + w
            states = states2
    return states


def increasing_cost(dist, func):
    return sum((w * func(v) for v,w in dist.items()), F(0))


def check():
    checks = 0
    # Verify commutator algebra on an exact rational grid.
    for gain in [F(1,5),F(1,2),F(1),F(3,2),F(3)]:
        for noise in [F(0),F(1,100),F(1,5),F(3,2)]:
            for precision in [F(1,3),F(1),F(5)]:
                for x in [F(1,100),F(1,4),F(1),F(10),F(100)]:
                    assert commutator(x,gain,noise,precision) == algebraic_commutator(x,gain,noise,precision)
                    checks += 1

    # Exact stable-model reversal and high-process-noise sorting.
    p_low,p_high=F(1,4),F(3,4)
    for x,noise,expected in [
        (F(1,4), F(1,10), F(-2,245)),
        (F(2), F(1,10), F(19,420)),
    ]:
        a = increasing_cost(law(x,(p_low,p_high),(F(1,2),),(noise,),F(1)),lambda y:y)
        b = increasing_cost(law(x,(p_high,p_low),(F(1,2),),(noise,),F(1)),lambda y:y)
        assert a-b == expected
        checks += 1
    for x in [F(1,10),F(1),F(10),F(100)]:
        assert commutator(x,F(1,2),F(1,2),F(1)) > 0
        assert commutator(x,F(1,2),F(0),F(1)) < 0
        checks += 2

    # Exhaustive schedules for fixed short horizons, exact conditional variances.
    # Per-interval gain + precision*noise >=1 in every case.
    scenarios = [
        (F(1,10),F(1),[F(1) for _ in range(4)],[F(0) for _ in range(4)]),
        (F(2),F(1),[F(1,2) for _ in range(4)],[F(1,2) for _ in range(4)]),
        (F(1,3),F(2),[F(1,5),F(3,2),F(4,5),F(1)],[F(2,5),F(0),F(1,10),F(0)]),
        (F(7,3),F(3),[F(3,5),F(1,3),F(6,5),F(2,3)],[F(2,15),F(2,9),F(0),F(1,9)]),
    ]
    for x,precision,gain_all,noise_all in scenarios:
        assert all(g+precision*n>=1 for g,n in zip(gain_all,noise_all))
        for n in (2,3,4,5):
            probs=[F(j,n+2) for j in range(1,n+1)]
            sorted_law=law(x,probs,gain_all[:n-1],noise_all[:n-1],precision)
            funcs=[lambda v:v,lambda v:v*v,lambda v:1-F(1)/(1+v)]
            costs=[increasing_cost(sorted_law,func) for func in funcs]
            for perm in permutations(probs):
                current=law(x,perm,gain_all[:n-1],noise_all[:n-1],precision)
                for func,best in zip(funcs,costs):
                    assert increasing_cost(current,func) >= best
                    checks+=1
                # finite support CDF test proves FOSD for these specific test instances
                for cutoff in sorted(set(current)|set(sorted_law)):
                    below_sorted=sum((prob for val,prob in sorted_law.items() if val<=cutoff),F(0))
                    below_current=sum((prob for val,prob in current.items() if val<=cutoff),F(0))
                    assert below_sorted>=below_current
                    checks += 1
    print(f'PASS: {checks} exact-rational identities, schedule comparisons, and finite CDF inequalities')


if __name__ == '__main__':
    check()
