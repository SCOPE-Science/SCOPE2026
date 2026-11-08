"""Exact checks of the two-edge geometric contact clock.

Uses Python's standard library only. It checks finite arithmetic identities;
the almost-sure asymptotic is proved analytically in RESULT.md.
"""
from fractions import Fraction
from math import comb


def moments(delta, initial_bad_weight, n):
    assert 0 < delta < 1 and 0 < initial_bad_weight <= 1 and n >= 1
    mean = Fraction(0)
    variance = Fraction(0)
    for k in range(n):
        w = initial_bad_weight * delta ** k
        p = w / (1 + w)
        mean += 1 / p
        variance += (1 - p) / (p * p)
    return mean, variance


def closed_form(delta, b, n):
    first = sum((delta ** (-k) for k in range(n)), Fraction(0))
    second = sum((delta ** (-2*k) for k in range(n)), Fraction(0))
    return n + first / b, second / (b*b) + first / b


def exact_dp_first_hit(delta, b, n, horizon):
    """Exact probability of reaching n negative contacts by given horizon."""
    dist = [Fraction(0) for _ in range(n+1)]
    dist[0] = Fraction(1)
    hist = []
    for _ in range(horizon):
        new = [Fraction(0) for _ in range(n+1)]
        new[n] = dist[n]
        for k in range(n):
            w = b*delta**k
            p = w/(1+w)
            new[k] += dist[k]*(1-p)
            new[k+1] += dist[k]*p
        dist = new
        hist.append(dist[n])
        assert sum(dist) == 1
    return hist


def check():
    tests = 0
    for delta in (Fraction(1, 2), Fraction(2, 3), Fraction(1, 4)):
        for b in (Fraction(1), Fraction(1, 3), Fraction(3, 4)):
            for n in range(1, 12):
                assert moments(delta,b,n) == closed_form(delta,b,n)
                tests += 1
    assert moments(Fraction(1, 2), Fraction(1), 1) == (2,2)
    assert moments(Fraction(1, 2), Fraction(1), 2) == (5,8)
    assert moments(Fraction(1, 2), Fraction(1), 3) == (10,28)
    # Independent exact Markov-chain DP: the first bad contact is geometric(p=1/2).
    hist = exact_dp_first_hit(Fraction(1, 2), Fraction(1), 1, 20)
    for t, p in enumerate(hist, start=1):
        assert p == 1 - Fraction(1,2)**t
        tests += 1
    # Two-contact clock: sum of independent geometric(1/2) + geometric(1/3).
    hist = exact_dp_first_hit(Fraction(1,2), Fraction(1), 2, 18)
    for t in range(1,19):
        ref = sum((Fraction(1,2)**(j-1)*Fraction(1,2) *
                   (1-Fraction(2,3)**(t-j)) for j in range(1,t+1)), Fraction(0))
        assert hist[t-1] == ref
        tests += 1
    print('PASS:', tests, 'exact rational identities and finite-horizon probabilities')

if __name__ == '__main__':
    check()
