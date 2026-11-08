"""Exact finite cross-checks for the two-overlapping-hyperedge majority theorem.

Run: python3 verify.py. Standard library only. All probabilities use Fraction.
"""
from fractions import Fraction
from itertools import product
from math import comb


def majority(edge, state):
    return int(sum(state[i] for i in edge) * 2 > len(edge))


def active(edge, state):
    k = sum(state[i] for i in edge)
    return 0 < k < len(edge)


def updated(edge, state):
    val = majority(edge, state)
    result = list(state)
    for i in edge:
        result[i] = val
    return tuple(result)


def exact_from_transition_graph(a, b, s, initial):
    """Follow each possible first event, then all forced effective transitions."""
    e = tuple(range(a))
    f = tuple(range(a-s, a+b-s))
    active_first = [h for h in (e, f) if active(h, initial)]
    if not active_first:
        return Fraction(0)
    trapping_first = 0
    for first in active_first:
        state = updated(first, initial)
        visited = set()
        for step in range(8):
            if len(set(state)) == 1:
                break
            if state in visited:
                trapping_first += 1
                break
            visited.add(state)
            possible = [h for h in (e, f) if active(h, state)]
            if not possible:
                assert len(set(state)) == 1
                break
            # Immediately after a firing, at most the other edge is active.
            assert len(possible) == 1, (a, b, s, initial, state)
            state = updated(possible[0], state)
        else:
            raise AssertionError('Unclassified transition cycle')
    return Fraction(trapping_first, len(active_first))


def exact_from_formula(a, b, s, initial):
    e = tuple(range(a))
    f = tuple(range(a-s, a+b-s))
    act = [h for h in (e, f) if active(h, initial)]
    if not act or 2*s >= min(a, b):
        return Fraction(0)
    successes = 0
    for current, other in ((e, f), (f, e)):
        if not active(current, initial):
            continue
        c = majority(current, initial)
        after = updated(current, initial)
        successes += int(majority(other, after) != c)
    return Fraction(successes, len(act))


def binomial_tail(n, threshold):
    return Fraction(sum(comb(n, k) for k in range(threshold, n+1)), 2**n)


def iid_formula(a, b, s):
    if 2*s >= min(a, b):
        return Fraction(0)
    ta = binomial_tail(a-s, (a+1)//2)
    tb = binomial_tail(b-s, (b+1)//2)
    return (ta+tb)/2


def main():
    full_state_count = 0
    configurations = 0
    for a in (3, 5, 7):
        for b in (3, 5, 7):
            for s in range(1, min(a,b)):
                if a+b-s > 12:
                    continue
                configurations += 1
                for state in product((0, 1), repeat=a+b-s):
                    lhs = exact_from_transition_graph(a,b,s,state)
                    rhs = exact_from_formula(a,b,s,state)
                    assert lhs == rhs, (a,b,s,state,lhs,rhs)
                    full_state_count += 1
    print('Exact initial-state comparisons:', full_state_count,
          'across', configurations, 'hypergraph structures')
    iid_cases = 0
    for a in (3,5,7,9):
        for b in (3,5,7,9):
            for s in range(1,min(a,b)):
                if a+b-s>12:
                    continue
                distribution = sum((exact_from_transition_graph(a,b,s,state)
                                    for state in product((0,1), repeat=a+b-s)),
                                    Fraction(0)) / 2**(a+b-s)
                predicted = iid_formula(a,b,s)
                assert distribution == predicted, (a,b,s,distribution,predicted)
                iid_cases += 1
    assert iid_formula(3,3,1) == Fraction(1,4)
    assert iid_formula(5,5,1) == Fraction(5,16)
    assert iid_formula(5,5,2) == Fraction(1,8)
    assert iid_formula(3,5,1) == Fraction(9,32)
    print('Exact fair-initialization comparisons:',iid_cases)
    print('PASS')


if __name__ == '__main__':
    main()
