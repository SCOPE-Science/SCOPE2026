"""Finite, exact verification of the four-card adhesive-riffle quotient.

Run: python3 check_four_card.py. Standard library only.
The finite checks support, but do not prove, the singular-time-scale limit.
"""
from fractions import Fraction as F
from itertools import permutations, product
from collections import defaultdict
from math import comb, exp

CARDS = (1, 2, 3, 4)
STATES = list(permutations(CARDS))
N = len(CARDS)

def orbit(deck):
    return min(deck[r:] + deck[:r] for r in range(N))

CLASSES = sorted({orbit(s) for s in STATES})
CLASS_INDEX = {c: i for i, c in enumerate(CLASSES)}
OPPOSITES = {(0, 5), (1, 3), (2, 4)}
RATES = {'C': F(9, 64), 'B': F(7, 48), 'I': F(7, 16)}


def partition(seq, mask):
    """Split m-card packet at exactly gaps flagged in mask."""
    m = len(seq)
    if not m:
        return []
    starts = [0] + [i + 1 for i, flag in enumerate(mask) if flag]
    ends = starts[1:] + [m]
    return [(tuple(seq[a:b]), F(a + b, 2 * m)) for a, b in zip(starts, ends)]


def merge(left, right, mode):
    out = defaultdict(F)
    if mode == 'I':
        groups = defaultdict(lambda: [[], []])
        for x in left:
            groups[x[1]][0].append(x[0])
        for x in right:
            groups[x[1]][1].append(x[0])
        choices = []
        for key in sorted(groups):
            ls, rs = groups[key]
            assert len(ls) <= 1 and len(rs) <= 1
            if ls and rs:
                choices.append([(ls[0], rs[0]), (rs[0], ls[0])])
            else:
                choices.append([(ls[0],) if ls else (rs[0],)])
        for picks in product(*choices):
            flattened = tuple(c for pair in picks for block in pair for c in block)
            out[flattened] += F(1, 2 ** sum(len(x) == 2 for x in choices))
        return out

    def rec(l, r, prefix, prob):
        if not l and not r:
            out[tuple(prefix)] += prob
            return
        if not r:
            rec(l[1:], r, prefix + list(l[0][0]), prob)
            return
        if not l:
            rec(l, r[1:], prefix + list(r[0][0]), prob)
            return
        if mode == 'B':
            left_prob = F(len(l), len(l) + len(r))
        else:
            left_prob = F(sum(len(s) for s, _ in l), sum(len(s) for s, _ in l + r))
        rec(l[1:], r, prefix + list(l[0][0]), prob * left_prob)
        rec(l, r[1:], prefix + list(r[0][0]), prob * (1 - left_prob))

    rec(left, right, [], F(1))
    return out


def transition(deck, mode, q, derivative=False):
    """One-round law, or rare-one-break probability coefficients."""
    out = defaultdict(F)
    for cut in range(N + 1):
        cut_prob = F(comb(N, cut), 2 ** N)
        if cut in (0, N):
            if not derivative:
                out[deck] += cut_prob
            continue
        left, right = deck[:cut], deck[cut:]
        choices = []
        for flags_l in product((0, 1), repeat=cut - 1):
            for flags_r in product((0, 1), repeat=N - cut - 1):
                breaks = sum(flags_l) + sum(flags_r)
                if derivative:
                    if breaks != 1:
                        continue
                    weight = cut_prob
                else:
                    weight = cut_prob * q ** breaks * (1 - q) ** (N - 2 - breaks)
                choices.append((flags_l, flags_r, weight))
        for ml, mr, weight in choices:
            for perm, v in merge(partition(left, ml), partition(right, mr), mode).items():
                out[perm] += weight * v
    return out


def quotient(mode):
    mat = [[F(0) for _ in CLASSES] for _ in CLASSES]
    for i, c in enumerate(CLASSES):
        for j in range(N):
            deck = c[j:] + c[:j]
            for perm, prob in transition(deck, mode, F(0), derivative=True).items():
                target = CLASS_INDEX[orbit(perm)]
                if target != i:
                    mat[i][target] += prob / N
        mat[i][i] = -sum(mat[i])
    return mat


def get_full_matrix(mode, q):
    return [[transition(s, mode, q).get(t, F(0)) for t in STATES] for s in STATES]


def exact_checks():
    assertions = 0
    assert len(STATES) == 24 and len(CLASSES) == 6
    assertions += 1
    for mode in 'CBI':
        rate = RATES[mode]
        mat = quotient(mode)
        for i in range(6):
            for j in range(6):
                expected = (-4 * rate if i == j else F(0) if tuple(sorted((i,j))) in OPPOSITES else rate)
                assert mat[i][j] == expected, (mode, i, j, mat[i][j], expected)
                assertions += 1
        for q in [F(0), F(1, 10), F(1, 3)]:
            P = get_full_matrix(mode, q)
            for i in range(24):
                assert sum(P[i]) == 1
                assertions += 1
                for j in range(24):
                    assert P[i][j] >= 0
                    assertions += 1
            for j in range(24):
                assert sum(P[i][j] for i in range(24)) == 1
                assertions += 1
        P0 = get_full_matrix(mode, F(0))
        for i, s in enumerate(STATES):
            for j, t in enumerate(STATES):
                assert (P0[i][j] != 0) == (orbit(s) == orbit(t)) or P0[i][j] == 0
                if orbit(s) != orbit(t):
                    assert P0[i][j] == 0
                assertions += 1
        for k, c in enumerate(CLASSES):
            assert set(c[j:] + c[:j] for j in range(N)) == {s for s in STATES if orbit(s) == c}
            assertions += 1
    return assertions


def profile(a, t):
    return .5 * exp(-4 * float(a) * t) + exp(-6 * float(a) * t) / 3


def numerical_checks():
    data = []
    for mode in 'CBI':
        for q in [F(1, 50), F(1, 100)]:
            P = [[float(x) for x in row] for row in get_full_matrix(mode, q)]
            for t in [.5, 2., 4.]:
                vec = [0.] * 24
                vec[0] = 1.
                for _ in range(int(t / float(q))):
                    vec = [sum(vec[i] * P[i][j] for i in range(24)) for j in range(24)]
                tv = .5 * sum(abs(v - 1 / 24) for v in vec)
                predicted = profile(RATES[mode], t)
                data.append((mode, str(q), t, round(tv, 7), round(predicted, 7), round(abs(tv - predicted), 7)))
                assert abs(tv - predicted) < .045, data[-1]
    return data


if __name__ == '__main__':
    num = exact_checks()
    data = numerical_checks()
    print('Exact rational assertions:', num)
    print('Finite-q convergence checks:', len(data))
    for item in data:
        print(*item)
