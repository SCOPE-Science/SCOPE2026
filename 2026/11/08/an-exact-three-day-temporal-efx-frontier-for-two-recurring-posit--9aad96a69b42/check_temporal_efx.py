"""Self-contained exact checker for temporal two-good EFX phase diagram.

Run: python check_temporal_efx.py. All arithmetic is rational; this script is
finite evidence, and does not replace the all-real-parameter proof.
"""
from fractions import Fraction
from itertools import product
from math import sqrt


def alpha_for_bundles(a, b):
    # a and b are tuples of exact rational item values.
    caps = [Fraction(1)]
    for own, other in ((a, b), (b, a)):
        for item in other:
            rem = sum(other) - item
            if rem:
                caps.append(sum(own) / rem)
    return min(caps)


def direct_score(H, L, schedule):
    A, B = [], []
    worst = Fraction(1)
    for decision in schedule:
        for g, receiver in zip((H, L), decision):
            (A if receiver == 0 else B).append(g)
        worst = min(worst, alpha_for_bundles(A, B))
    return worst


def brute_opt(H, L, days):
    best = Fraction(-1)
    argmax = []
    for schedule in product(product((0, 1), repeat=2), repeat=days):
        score = direct_score(H, L, schedule)
        if score > best:
            best, argmax = score, [schedule]
        elif score == best:
            argmax.append(schedule)
    return best, argmax


def closed_form(H, L):
    h = H / L
    if h <= 2:
        return Fraction(1)
    return max((H + 2*L)/(2*H), H/(H+L))


def prefix_states(H, L, T):
    states = {(0, 0)}
    sizes = []
    for t in range(1, T+1):
        new = set()
        for x, y in states:
            for u, v in product((0,1), repeat=2):
                xx, yy = x+u, y+v
                A = (H,)*xx + (L,)*yy
                B = (H,)*(t-xx) + (L,)*(t-yy)
                if alpha_for_bundles(A, B) == 1:
                    new.add((xx, yy))
        states = new
        sizes.append(len(states))
    return sizes


def main():
    test_ratios = [Fraction(x) for x in (1, 2, 3, 4, 5, 10, 100)]
    test_ratios += [Fraction(11, 10), Fraction(3, 2), Fraction(19,10),
                    Fraction(2001,1000), Fraction(201,100), Fraction(5,2),
                    Fraction(31,10), Fraction(35,10), Fraction(356,100),
                    Fraction(357,100), Fraction(7,2), Fraction(15,4),
                    Fraction(9,2), Fraction(1001,100)]
    comparisons = 0
    for h in test_ratios:
        best, paths = brute_opt(h, Fraction(1), 3)
        expected = closed_form(h, Fraction(1))
        assert best == expected, (h, best, expected)
        comparisons += 64
        assert len(paths) >= 1
        if h <= 2:
            assert best == 1
        else:
            assert best < 1
        sizes = prefix_states(h, Fraction(1), 9)
        assert all(x > 0 for x in sizes[:2]), (h, sizes)
        if h <= 2:
            assert all(x > 0 for x in sizes), (h, sizes)
        else:
            assert all(x == 0 for x in sizes[2:]), (h, sizes)
    # Independent case enumeration at the switching point and exact inequalities.
    # The root satisfies h^2-3h-2=0 and lies strictly between 3 and 4.
    def q(h):
        return h*h - 3*h - 2
    assert q(Fraction(3)) < 0 and q(Fraction(4)) > 0
    assert closed_form(Fraction(3), Fraction(1)) == Fraction(5,6)
    assert closed_form(Fraction(4), Fraction(1)) == Fraction(4,5)
    assert abs((sqrt(17)-1)/4 - 0.7807764064044151) < 1e-14
    print('PASS: %d exact three-day allocation paths at %d distinct rational ratios' % (comparisons, len(test_ratios)))
    print('PASS: %d nine-day dynamic EFX reachability comparisons' % (len(test_ratios)))
    print('PASS: crossing polynomial, endpoints, and algebraic constant checks')

if __name__ == '__main__':
    main()
