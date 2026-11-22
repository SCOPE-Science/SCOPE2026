"""Exact rational checks for one-step fair-spin laws of a noisy three-site automaton.

Run with Python 3.9+; no third-party packages are needed. This tests finite
rings and rational parameter values. The all-size proof is in RESULT.md.
"""
from fractions import Fraction
from itertools import combinations, product


def conditional_mean(spins, i, p, r):
    """Exact expected output spin at site i, given input spins (+/-1)."""
    n = len(spins)
    a, b, c = spins[(i - 1) % n], spins[i], spins[(i + 1) % n]
    if a == c:
        return (2*r - 1) * a
    return (2*p - 1) * b


def moment(n, sites, p, r):
    """Unconditional output-spin product moment, with fair independent inputs."""
    total = Fraction(0)
    for spins in product((-1, 1), repeat=n):
        v = Fraction(1)
        for i in sites:
            v *= conditional_mean(spins, i, p, r)
        total += v
    return total / (1 << n)


def check():
    cases = 0
    params = [(Fraction(1, 5), Fraction(7, 10)),
              (Fraction(4, 5), Fraction(1, 2)),
              (Fraction(1, 2), Fraction(3, 5)),
              (Fraction(1, 2), Fraction(1, 2)),
              (Fraction(0), Fraction(1)),
              (Fraction(1), Fraction(0))]
    for n in range(1, 11):
        for p, r in params:
            u, v = 2*p-1, 2*r-1
            for i in range(n):
                assert moment(n, (i,), p, r) == 0
                cases += 1
            if n == 3:
                for i in range(n):
                    assert moment(n, (i, (i+1)%n), p, r) == (u+v)**2/4
                    cases += 1
            if n >= 4:
                for i in range(n):
                    assert moment(n, (i, (i+1)%n), p, r) == u*v/2
                    assert moment(n, (i, (i+2)%n), p, r) == v*v/(2 if n == 4 else 4)
                    cases += 2
            if n >= 4 and r == Fraction(1, 2):
                # Every subset of at most three distinct output sites has zero spin moment.
                for k in range(1, 4):
                    for subset in combinations(range(n), k):
                        assert moment(n, subset, p, r) == 0
                        cases += 1
                # The first dependence witness has order exactly four.
                four = moment(n, (0,1,2,3), p, r)
                assert four == u**4 / (4 if n == 4 else 16)
                cases += 1
            if n == 2:
                assert moment(n, (0,1), p, r) == 0
                cases += 1
    # Four-symbol distribution reconstructed from the spin moments.
    for n in (4, 5, 7):
        p, r = Fraction(4,5), Fraction(1,2)
        theta = (2*p-1)**4 / (4 if n == 4 else 16)
        for word in product((-1,1), repeat=4):
            probability = Fraction(0)
            for spins in product((-1,1), repeat=n):
                prod_probability = Fraction(1)
                for i,y in enumerate(word):
                    prod_probability *= (1+y*conditional_mean(spins,i,p,r))/2
                probability += prod_probability
            probability /= 1 << n
            expected = (1+theta*word[0]*word[1]*word[2]*word[3])/16
            assert probability == expected
            cases += 1
    print('PASS: %d exact checks; n=1..10; six rational parameter pairs; four-block law checked.' % cases)

if __name__ == '__main__':
    check()
