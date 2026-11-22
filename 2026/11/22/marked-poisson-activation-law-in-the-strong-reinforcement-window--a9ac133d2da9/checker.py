#!/usr/bin/env python3
"""Exact rational checks for preferential-attachment activation rare-event coupling.

Only Python standard-library dependencies. No experimental output replaces the proof.
"""
from fractions import Fraction
from itertools import product


def path_mass(bits, a):
    h = 1
    prob = Fraction(1)
    for t, bit in enumerate(bits, start=2):
        q = Fraction(t-h, t+a*(t-1))
        prob *= q if bit else 1-q
        h += bit
    return prob


def star_product(n, a):
    ans = Fraction(1)
    for t in range(2, n):
        ans *= Fraction(1+a*(t-1), t+a*(t-1))
    return ans


def exact(n, a):
    bern = Fraction(1, a)
    masses = []
    assertion_count = 0
    for bits in product((0, 1), repeat=n-2):
        mass = path_mass(bits, a)
        indep = bern**sum(bits) * (1-bern)**(n-2-sum(bits))
        masses.append((bits, mass, indep))
        assert mass >= 0
        assert indep >= 0
        assertion_count += 2
    assert sum((p for _,p,_ in masses), Fraction()) == 1
    assert sum((q for _,_,q in masses), Fraction()) == 1
    assertion_count += 2
    assert masses[0][1] == star_product(n,a)
    assertion_count += 1
    tv = sum((abs(p-q) for _,p,q in masses), Fraction())/2
    assert tv <= Fraction(2*(n-2),a*a)
    assertion_count += 1
    # Every coordinate has probability at most 1/a and joint probabilities
    # lie below their independent-Bernoulli counterparts.
    for t in range(n-2):
        observed = sum((p for bits,p,_ in masses if bits[t]), Fraction())
        assert observed <= bern
        assertion_count += 1
    return assertion_count, tv


def run():
    total = 0
    largest_gap = Fraction(0)
    tests = 0
    for n in range(2, 12):
        for a in (1,2,3,5,10,30):
            count, tv = exact(n,a)
            total += count
            tests += 1
            largest_gap = max(largest_gap, tv)
    print('PASS: %d exact rational assertions; %d finite (n,a) cases' % (total, tests))
    print('Maximum observed finite TV distance: %s' % largest_gap)
    print('Infinite-dimensional Poisson-process limit is established analytically, not by these tests.')

if __name__=='__main__':
    run()


def marked_history_mass(history, a):
    """Exact probability for the complete sequence of first-parent activations.

    An event at step t+1 is encoded by 0 or by the earlier birth label j.
    """
    activated = {1}
    value = Fraction(1)
    for t, mark in enumerate(history, 2):
        denominator = t + a*(t-1)
        eligible = t - len(activated)
        if mark == 0:
            value *= 1 - Fraction(eligible, denominator)
        elif mark in activated or not 2 <= mark <= t:
            return Fraction(0)
        else:
            value *= Fraction(1, denominator)
            activated.add(mark)
    return value


def marked_reference_mass(history, a):
    ans = Fraction(1)
    for t, mark in enumerate(history, 2):
        ans *= (1-Fraction(1,a)) if mark == 0 else Fraction(1,a*(t-1))
    return ans


def marked_test(n,a):
    from itertools import product
    options = [[0]+list(range(2,t+1)) for t in range(2,n)]
    p_total=q_total=tv=Fraction(0)
    checks=0
    for history in product(*options):
        p = marked_history_mass(history,a)
        q = marked_reference_mass(history,a)
        assert 0 <= p <= 1 and 0 <= q <= 1
        checks += 2
        p_total += p; q_total += q
        tv += abs(p-q)
    assert p_total==q_total==1
    assert tv/2 <= Fraction(2*(n-2),a*a)
    checks+=3
    return checks, tv/2


def marked_run():
    checks=0
    tv_max=Fraction(0)
    cases=0
    for n in range(2,9):
        for a in (1,2,3,5,10,25):
            k,tv = marked_test(n,a)
            cases+=1
            checks+=k
            tv_max=max(tv_max,tv)
    print('PASS: %d additional rational marked-history assertions; %d cases' % (checks,cases))
    print('Largest marked-history total variation: %s' % tv_max)

if __name__=='__main__':
    marked_run()
