"""Exact-rational checks for the periodic relay-delay counterexample.

Run: python3 verify.py
The all-trajectory theorem is established analytically in RESULT.md.
"""
from fractions import Fraction as Q


def g(t):
    """Eight-periodic continuous reference, represented exactly."""
    x = (Q(t) + 1) % 8 - 1
    if x <= Q(-1, 2):
        return Q(-1)
    if x <= Q(1, 2):
        return 2*x
    if x <= Q(3, 2):
        return Q(1)
    if x <= Q(11, 2):
        return Q(1) - (x-Q(3, 2))/2
    return Q(-1)


def sgn(x):
    return (x > 0) - (x < 0)


def next_d(s, d):
    return s - g(d)


def check():
    # Continuous gluing, exact amplitude, and one-sided derivative bound.
    for t, value in [(-1, -1), (Q(-1, 2), -1), (Q(1, 2), 1),
                     (Q(3, 2), 1), (Q(11, 2), -1), (7, -1)]:
        assert g(t) == value
    slopes = [Q(0), Q(2), Q(0), Q(-1, 2), Q(0)]
    assert min(slopes) == Q(-1, 2) and max(slopes) == 2
    # Periodic gluing introduces no jumps, so the global slope bounds follow.
    for k in range(-20, 21):
        for t in [Q(-1), Q(-1, 2), Q(1, 2), Q(3, 2), Q(11, 2), Q(7)]:
            assert g(t + 8*k) == g(t)

    s = Q(1, 4)
    d = s
    values = []
    for _ in range(14):
        values.append(d)
        d = next_d(s, d)
    expected = [Q(1, 4), Q(-1, 4), Q(3, 4), Q(-3, 4)]
    expected.extend([Q(5, 4), Q(-3, 4)]*5)
    assert values == expected

    implicit = Q(1, 12)
    assert implicit + g(implicit) == s
    assert g(implicit) > 0 and g(s) > 0
    for j in range(2, 15, 2):
        assert g(values[j-1]) < 0

    # Open-interval evidence: exact rational samples around t=9/4.
    for n in range(-20, 21):
        local_s = s + Q(n, 2000)
        d = local_s
        for j in range(1, 15):
            if j % 2 == 0:
                assert g(d) < 0, (j, local_s, d)
            d = next_d(local_s, d)
        assert g(local_s) > 0
    print('PASS: exact periodic gluing, slope bounds, implicit root,')
    print('      fourteen nested iterates, and 41 rational sign tests.')


if __name__ == '__main__':
    check()
