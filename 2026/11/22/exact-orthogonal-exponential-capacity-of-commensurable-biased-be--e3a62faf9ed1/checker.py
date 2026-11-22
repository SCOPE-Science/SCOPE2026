"""Exact finite checks for orthogonal exponential capacity of biased Bernoulli sums.

Standard library only. Rational grid and exhaustive clique search; the
all-size theorem is proved analytically in RESULT.md, not by enumeration.
"""
from fractions import Fraction
from itertools import product
from collections import Counter


def v2(n):
    assert n > 0
    result = 0
    while n % 2 == 0:
        n //= 2
        result += 1
    return result


def mod1(x):
    return x - x.numerator // x.denominator


def zeros_mod_one(steps, balanced):
    z = set()
    for a, is_balanced in zip(steps, balanced):
        if is_balanced:
            z.update(Fraction(2*k+1, 2*a) for k in range(a))
    return z


def max_clique_for_zero_set(z):
    # Any orthogonal frequency set can be translated to contain 0; all its
    # other points then lie in z modulo 1, since all steps are integers.
    vertices = sorted(z)
    n = len(vertices)
    adj = [0] * n
    for i, a in enumerate(vertices):
        for j in range(i+1, n):
            b = vertices[j]
            if mod1(a-b) in z:
                adj[i] |= (1 << j)
                adj[j] |= (1 << i)
    # Include 0, then search maximum clique in the remaining graph.
    best = 0
    def expand(candidates, size):
        nonlocal best
        if size + candidates.bit_count() <= best:
            return
        if candidates == 0:
            best = max(best, size)
            return
        while candidates:
            if size + candidates.bit_count() <= best:
                break
            bit = candidates & -candidates
            i = bit.bit_length() - 1
            candidates ^= bit
            expand(candidates & adj[i], size+1)
    expand((1 << n) - 1, 0)
    return best+1


def exact_constructed_frequencies(steps, balanced):
    representatives = {}
    for a,b in zip(steps,balanced):
        if b:
            representatives[v2(a)] = a
    freqs = {sum((Fraction(bit, 2**(s+1)) for bit,s in zip(bits,sorted(representatives))),Fraction(0))
             for bits in product((0,1),repeat=len(representatives))}
    z = zeros_mod_one(steps,balanced)
    assert len(freqs) == 2**len(representatives)
    assert all(mod1(x-y) in z for x in freqs for y in freqs if x!=y)
    return len(freqs)


def main():
    tests = 0
    cases = [(a,) for a in range(1,9)]
    cases += list(product(range(1,7),repeat=2))
    cases += list(product(range(1,5),repeat=3))
    cases += [(1,2,4,8),(1,1,2,4),(3,5,7,9),(1,2,3,4),(2,4,6,8),
              (1,3,5,7),(1,1,1,1),(1,4,8,16),(1,3,7,15)]
    for steps in cases:
        for balanced in product((False,True),repeat=len(steps)):
            r=len({v2(a) for a,b in zip(steps,balanced) if b})
            expected=2**r
            z=zeros_mod_one(steps,balanced)
            actual=max_clique_for_zero_set(z)
            constructed=exact_constructed_frequencies(steps,balanced)
            assert actual==expected==constructed,(steps,balanced,actual,expected)
            tests+=1
    print(f'PASS {tests} finite masks: exhaustive rational-grid cliques, construction, and 2-adic formula')


if __name__=='__main__':
    main()
