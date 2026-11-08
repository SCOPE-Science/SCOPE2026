"""Self-contained exact certificate for the three-type six-candidate PAV theorem.

No external packages are required. Run: python verify_triangle.py
The two implementations independently use (i) aggregated seat counts and
(ii) explicit subsets of six labeled candidates with rational voter scores.
"""
from fractions import Fraction
from itertools import combinations

H12 = (0, 12, 18, 22, 25)
H = tuple(Fraction(j, 12) for j in H12)
# Candidate indices 0,1 belong to A, 2,3 to B, 4,5 to C.
APPROVALS = ((0, 1, 2, 3), (0, 1, 4, 5), (2, 3, 4, 5))
ALL_CANDIDATES = tuple(range(6))


def coarse_score(state, weights):
    a, b, c = state
    x, z, y = weights
    return x * H12[a + b] + z * H12[a + c] + y * H12[b + c]


def aggregated_greedy(weights):
    frontier = {(0, 0, 0)}
    for _ in range(4):
        new = set()
        for state in frontier:
            choices = []
            for j in range(3):
                if state[j] < 2:
                    nxt = tuple(state[i] + int(i == j) for i in range(3))
                    choices.append((coarse_score(nxt, weights), nxt))
            best = max(score for score, _ in choices)
            new.update(s for score, s in choices if score == best)
        frontier = new
    return frontier


def aggregated_optima(weights):
    choices = {(a, b, 4-a-b) for a in range(3) for b in range(3)
               if 0 <= 4-a-b <= 2}
    best = max(coarse_score(s, weights) for s in choices)
    return {s for s in choices if coarse_score(s, weights) == best}


def explicit_score(committee, weights):
    return sum(Fraction(weight) * H[len(set(committee).intersection(APPROVALS[i]))]
               for i, weight in enumerate(weights))


def signature(committee):
    return tuple(sum(c // 2 == i for c in committee) for i in range(3))


def explicit_greedy(weights):
    frontier = {frozenset()}
    for _ in range(4):
        nxt = set()
        for committee in frontier:
            choices = [(explicit_score(committee | {c}, weights),
                        committee | {c}) for c in ALL_CANDIDATES
                       if c not in committee]
            best = max(q for q, _ in choices)
            nxt.update(x for q, x in choices if q == best)
        frontier = nxt
    return {signature(c) for c in frontier}


def explicit_optima(weights):
    committees = list(combinations(ALL_CANDIDATES, 4))
    scores = {c: explicit_score(c, weights) for c in committees}
    best = max(scores.values())
    return {signature(c) for c in committees if scores[c] == best}


def sorted_weights(total):
    for a in range(1, total + 1):
        for b in range(a, total + 1):
            c = total - a - b
            if c >= b:
                yield (a, b, c)


def verify():
    count = 0
    robust_before_17 = []
    robust_at_17 = []
    any_failure_before_17 = []
    for total in range(3, 18):
        for weights in sorted_weights(total):
            count += 1
            g = aggregated_greedy(weights)
            o = aggregated_optima(weights)
            eg = explicit_greedy(weights)
            eo = explicit_optima(weights)
            assert g == eg, (weights, g, eg)
            assert o == eo, (weights, o, eo)
            for committee in combinations(ALL_CANDIDATES, 4):
                assert coarse_score(signature(committee), weights) == (
                    12 * explicit_score(committee, weights))
            if not (g & o):
                (robust_before_17 if total < 17 else robust_at_17).append(weights)
            if total < 17 and (g - o):
                any_failure_before_17.append(weights)
    assert count == 147, count
    assert robust_before_17 == [], robust_before_17
    assert robust_at_17 == [(5, 5, 7)], robust_at_17
    assert any_failure_before_17 == [(2, 2, 3), (4, 4, 6)]
    assert aggregated_greedy((5,5,7)) == {(1,2,1), (1,1,2)}
    assert aggregated_optima((5,5,7)) == {(0,2,2)}
    assert Fraction(coarse_score((0,2,2),(5,5,7)),12) == Fraction(355,12)
    assert Fraction(coarse_score((1,2,1),(5,5,7)),12) == Fraction(59,2)

    # Analytic one-parameter phase claim at all critical ratios and dense rationals.
    ratios = {Fraction(n, d) for d in range(1, 43) for n in range(1, 105)}
    ratios |= {Fraction(1,2), Fraction(2,3), Fraction(1),
               Fraction(4,3), Fraction(3,2)}
    for ratio in ratios:
        weights = (ratio.denominator, ratio.denominator, ratio.numerator)
        g = aggregated_greedy(weights)
        o = aggregated_optima(weights)
        W = {(2,1,1)}
        V = {(1,2,1), (1,1,2)}
        U = {(0,2,2)}
        if ratio < 1:
            expected_g, expected_o = W, W
        elif ratio == 1:
            expected_g, expected_o = W|V, W|V
        elif ratio < Fraction(4,3):
            expected_g, expected_o = V, V
        elif ratio == Fraction(4,3):
            expected_g, expected_o = V, V|U
        elif ratio < Fraction(3,2):
            expected_g, expected_o = V, U
        elif ratio == Fraction(3,2):
            expected_g, expected_o = V|U, U
        else:
            expected_g, expected_o = U, U
        assert (g,o) == (expected_g,expected_o), (ratio, g, o, expected_g,expected_o)
    print('PASS: 147 nondecreasing positive integer triples through 17 voters')
    print('PASS: aggregated and direct six-candidate exact committee/greedy checks')
    print('PASS: 123 triples below 17 have no robust discrepancy')
    print('PASS: only (5,5,7) among 24 size-17 triples has robust discrepancy')
    print('PASS: entire one-parameter phase diagram on',len(ratios),'rational ratios')
    print('PASS: 17-voter scores: optimum 355/12, sequential 59/2, gap 1/12')

if __name__ == '__main__':
    verify()
