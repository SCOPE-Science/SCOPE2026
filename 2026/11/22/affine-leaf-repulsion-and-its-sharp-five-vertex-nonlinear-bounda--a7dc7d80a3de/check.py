"""Exact finite checks for leaf-survival identities in growing weighted trees.

Requires Python 3 and sympy. This script enumerates every parent choice for
small trees and verifies algebraic identities; the all-size proof is analytical.
"""
from fractions import Fraction
from itertools import combinations
import sympy as sp


def tree_degrees(n, weight):
    """Exact degree-vector law from a two-vertex initial edge."""
    states = {(1, 1): sp.S.One}
    for t in range(2, n):
        next_states = {}
        for degrees, probability in states.items():
            weights = [weight(k) for k in degrees]
            total = sum(weights)
            for i, w in enumerate(weights):
                child = list(degrees)
                child[i] += 1
                child.append(1)
                key = tuple(child)
                next_states[key] = next_states.get(key, 0) + probability*w/total
        states = next_states
    return states


def survival_all(subset, n, a, b):
    """Independent-category formula for simultaneous leaf events."""
    w = a+b
    answer = sp.S.One
    for t in range(2, n):
        m = sum(i < t for i in subset)
        total = 2*a*(t-1)+b*t
        answer *= 1-m*w/total
    return sp.cancel(answer)


def subset_prob(states, subset):
    return sp.cancel(sum(probability for degrees, probability in states.items()
                         if all(degrees[i] == 1 for i in subset)))


def exact_mask_probability(states, mask):
    return sp.cancel(sum(probability for degrees, probability in states.items()
                         if {i for i, deg in enumerate(degrees) if deg == 1} == set(mask)))


checks = 0
for a, b in [(sp.S.Zero, sp.S.One), (sp.S.One, sp.S.Zero),
             (sp.Rational(1, 2), sp.S.One),
             (sp.S(2), -sp.Rational(1, 2))]:
    assert a >= 0 and a+b > 0
    for n in range(2, 8):
        states = tree_degrees(n, lambda k: a*k+b)
        assert sp.simplify(sum(states.values())-1) == 0
        checks += 1
        for subsetmask in range(1 << n):
            subset = tuple(i for i in range(n) if subsetmask & (1 << i))
            assert sp.simplify(subset_prob(states, subset) - survival_all(subset, n, a, b)) == 0
            checks += 1
        for i, j in combinations(range(n), 2):
            pi = subset_prob(states, [i])
            pj = subset_prob(states, [j])
            pij = subset_prob(states, [i, j])
            assert sp.simplify(pij-pi*pj) <= 0
            checks += 1

# A completely enumerated five-vertex, degree-based nonlinear kernel.
g = sp.symbols('g', positive=True)
states = tree_degrees(5, lambda k: sp.S.One if k <= 2 else g)
assert len(states) == 14
checks += 1
assert sp.simplify(sum(states.values())-1) == 0
checks += 1
expected_cov = {
    (0, 1): -(7*g+17)**2/(576*(g+3)**2),
    (0, 2): -(g**2+46*g+145)/(288*(g+3)**2),
    (0, 3): (g**2-8*g-41)/(144*(g+3)**2),
    (1, 2): -(g**2+46*g+145)/(288*(g+3)**2),
    (1, 3): (g**2-8*g-41)/(144*(g+3)**2),
    (2, 3): (g**2-8*g-41)/(72*(g+3)**2),
}
for i, j in combinations(range(5), 2):
    pi = subset_prob(states, [i])
    pj = subset_prob(states, [j])
    pij = subset_prob(states, [i, j])
    asserted = expected_cov.get((i, j), sp.S.Zero)
    assert sp.cancel(pij-pi*pj-asserted) == 0
    checks += 1
assert sp.factor(g**2-8*g-41) == g**2-8*g-41
for value in [sp.Rational(1), sp.Rational(10), sp.Rational(12), sp.Rational(100)]:
    covariance = expected_cov[(2,3)].subs(g, value)
    assert (covariance > 0) == (value > 4+sp.sqrt(57))
    checks += 1
print('PASS: %d exact assertions; nonlinear threshold = 4+sqrt(57)' % checks)
