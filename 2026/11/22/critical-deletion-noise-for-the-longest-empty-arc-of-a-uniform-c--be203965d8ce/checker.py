"""Finite checks and an illustrative simulation for circular-point thinning.

Python 3 standard library only. The limiting theorem is proved analytically
in RESULT.md, not by the simulation or these finite assertions.
Run: python3 checker.py
"""
from fractions import Fraction
from math import exp, log
from random import Random


def block_lengths(keep):
    n = len(keep)
    retained = [i for i, b in enumerate(keep) if b]
    if not retained:
        return []
    if len(retained) == 1:
        return [n]
    return [(retained[(j+1) % len(retained)]-retained[j]) % n
            for j in range(len(retained))]


def exact_checks():
    count = 0
    for n in range(3, 10):
        for eps in (Fraction(1, 4), Fraction(2, 5), Fraction(3, 4)):
            q = 1-eps
            totals = [Fraction(0)]*(n+1)
            total_blocks = Fraction(0)
            for mask in range(1 << n):
                keep = [bool(mask & (1 << i)) for i in range(n)]
                weight = q**sum(keep) * eps**(n-sum(keep))
                lengths = block_lengths(keep)
                total_blocks += weight*len(lengths)
                for length in lengths:
                    totals[length] += weight
            assert total_blocks == n*q
            count += 1
            for k in range(1, n):
                assert totals[k] == n*q*q*eps**(k-1), (n, eps, k)
                count += 1
            assert totals[n] == n*q*eps**(n-1)
            count += 1

    # The geometric mixture of Erlang(k,1) variables has Exp(q) law.
    # This is its Laplace-transform identity for rational arguments.
    for eps in (Fraction(1, 4), Fraction(1, 3), Fraction(3, 5)):
        q = 1-eps
        for s in (Fraction(1, 3), Fraction(2), Fraction(7, 5)):
            partial = sum((q*eps**(k-1)*(1+s)**(-k)
                           for k in range(1, 101)), Fraction(0))
            assert abs(float(partial-q/(q+s))) < 1e-14
            count += 1
    return count


def simulation(n=5000, tau=0.7, trials=2000, seed=271828):
    random = Random(seed)
    eps = tau/log(n)
    equal = joint00 = joint01 = 0
    for _ in range(trials):
        e = [random.expovariate(1) for _ in range(n)]
        S = sum(e)
        keep = [random.random() >= eps for _ in range(n)]
        retained = [i for i, b in enumerate(keep) if b]
        if not retained:
            continue
        prefix = [0.0]
        for value in e:
            prefix.append(prefix[-1] + value)
        merged = []
        for j, i in enumerate(retained):
            if j+1 < len(retained):
                merged.append(prefix[retained[j+1]]-prefix[i])
            else:
                merged.append(prefix[n]-prefix[i]+prefix[retained[0]])
        X = n*max(e)/S-log(n)
        Y = n*max(merged)/S-log(n)
        equal += abs(Y-X) < 1e-8
        joint00 += (X <= 0 and Y <= 0)
        joint01 += (X <= 0 and Y <= 1)
    empirical = (equal/trials, joint00/trials, joint01/trials)
    expected = (exp(-tau), exp(-exp(tau)),
                exp(-1-(exp(tau)-1)*exp(-1)))
    for observed, target in zip(empirical, expected):
        assert abs(observed-target) < 0.12, (observed, target)
    return empirical, expected

if __name__ == '__main__':
    count = exact_checks()
    observed, expected = simulation()
    print('PASS', count, 'exact finite assertions and 3 illustrative simulation bounds')
    print('Monte Carlo: n=5000, tau=0.7, 2000 fixed-seed trials')
    print('Metrics: unchanged maximum, joint CDF at (0,0) and (0,1)')
    print('Observed:', tuple(round(x, 5) for x in observed))
    print('Limit:', tuple(round(x, 5) for x in expected))
    print('Finite simulations do not certify an asymptotic law.')
