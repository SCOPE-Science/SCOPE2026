#!/usr/bin/env python3
from itertools import permutations, product
from fractions import Fraction
from collections import Counter
from math import factorial


def antichains(n):
    """All nonempty antichains of nonempty subsets of [n]."""
    subs = list(range(1, 1 << n))
    comparable = {
        s: {t for t in subs if t != s and (((s & t) == s) or ((s & t) == t))}
        for s in subs
    }
    out = []
    def rec(cands, chosen):
        if not cands:
            if chosen:
                out.append(tuple(sorted(chosen)))
            return
        s = min(cands)
        rec(cands - {s}, chosen)
        rec((cands - {s}) - comparable[s], chosen + (s,))
    rec(set(subs), ())
    return tuple(out)


def value(fam, S):
    return int(any((m & S) == m for m in fam))


def proper(n, fam):
    N = (1 << n) - 1
    return all(not (value(fam, S) and value(fam, N ^ S)) for S in range(1 << n))


def deegan_packel_formula(n, fam):
    m = len(fam)
    return tuple(
        sum((Fraction(1, S.bit_count()) for S in fam if (S >> i) & 1), Fraction(0)) / m
        for i in range(n)
    )


def deegan_packel_split(n, fam):
    acc = [Fraction(0) for _ in range(n)]
    for S in fam:
        share = Fraction(1, S.bit_count())
        for i in range(n):
            if (S >> i) & 1:
                acc[i] += share
    return tuple(x / len(fam) for x in acc)


def shapley_swing_formula(n, fam):
    nf = factorial(n)
    out = []
    for i in range(n):
        z = Fraction(0)
        for S in range(1 << n):
            if (S >> i) & 1:
                continue
            if value(fam, S | (1 << i)) != value(fam, S):
                k = S.bit_count()
                z += Fraction(factorial(k) * factorial(n-k-1), nf)
        out.append(z)
    return tuple(out)


def shapley_pivotal_permutations(n, fam):
    pivots = [0] * n
    for p in permutations(range(n)):
        S = 0
        for i in p:
            before = value(fam, S)
            S |= 1 << i
            after = value(fam, S)
            if not before and after:
                pivots[i] += 1
                break
    nf = factorial(n)
    return tuple(Fraction(x, nf) for x in pivots)


def weak_order(v):
    return tuple(
        (v[i] > v[j]) - (v[i] < v[j])
        for i in range(len(v)) for j in range(i + 1, len(v))
    )


def relabel_family(fam, p, n):
    out = []
    for S in fam:
        T = 0
        for i in range(n):
            if (S >> i) & 1:
                T |= 1 << p[i]
        out.append(T)
    return tuple(sorted(out))


def canonical_family(fam, n):
    return min(relabel_family(fam, p, n) for p in permutations(range(n)))


def relation_type(a, b):
    reversals = a_refines_b_tie = b_refines_a_tie = changed = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            ca = (a[i] > a[j]) - (a[i] < a[j])
            cb = (b[i] > b[j]) - (b[i] < b[j])
            if ca == cb:
                continue
            changed += 1
            if ca * cb == -1:
                reversals += 1
            elif cb == 0:
                a_refines_b_tie += 1
            elif ca == 0:
                b_refines_a_tie += 1
    return reversals, a_refines_b_tie, b_refines_a_tie, changed


def weighted_rep(n, fam, maxw=5):
    truth = [value(fam, S) for S in range(1 << n)]
    for w in product(range(maxw + 1), repeat=n):
        if not any(w):
            continue
        total = sum(w)
        for q in range(1, total + 1):
            ok = True
            for S in range(1 << n):
                sw = sum(w[i] for i in range(n) if (S >> i) & 1)
                if int(sw >= q) != truth[S]:
                    ok = False
                    break
            if ok:
                return q, w
    return None


proper_counts = {}
class_counts = {}
divergence_counts = {}
relation_hist = Counter()
relation_class_hist = Counter()
divergent = {}
dummy_free_proper5 = 0
dummy_free_divergent5 = 0

for n in range(1, 6):
    classes = Counter(canonical_family(f, n) for f in antichains(n) if proper(n, f))
    proper_counts[n] = sum(classes.values())
    class_counts[n] = len(classes)
    div = 0
    for c, orbit in classes.items():
        dp1 = deegan_packel_formula(n, c)
        dp2 = deegan_packel_split(n, c)
        sh1 = shapley_swing_formula(n, c)
        sh2 = shapley_pivotal_permutations(n, c)
        assert dp1 == dp2
        assert sh1 == sh2
        assert sum(dp1) == 1
        assert sum(sh1) == 1

        if n == 5 and all(x > 0 for x in dp1):
            dummy_free_proper5 += orbit

        if weak_order(dp1) != weak_order(sh1):
            div += orbit
            if n == 5:
                typ = relation_type(dp1, sh1)
                relation_hist[typ] += orbit
                relation_class_hist[typ] += 1
                divergent[c] = (orbit, dp1, sh1, typ)
                if all(x > 0 for x in dp1):
                    dummy_free_divergent5 += orbit
    divergence_counts[n] = div

assert proper_counts == {1: 1, 2: 3, 3: 11, 4: 80, 5: 2645}
assert class_counts == {1: 1, 2: 2, 3: 5, 4: 14, 5: 86}
assert divergence_counts == {1: 0, 2: 0, 3: 0, 4: 0, 5: 460}
assert len(divergent) == 9
assert sum(v[0] for v in divergent.values()) == 460
assert relation_hist == Counter({
    (1,0,0,1): 300,
    (2,0,0,2): 120,
    (3,0,0,3): 40,
})
assert relation_class_hist == Counter({
    (1,0,0,1): 4,
    (2,0,0,2): 3,
    (3,0,0,3): 2,
})
# Every first-layer difference is a genuine strict reversal; there are no tie-only changes.
assert all(t[0] == t[3] and t[1] == 0 and t[2] == 0 for t in relation_hist)
assert dummy_free_proper5 == 2330
assert dummy_free_divergent5 == 460

expected = {
    (3,5,14,22): (30, (7,(4,3,3,1,1))),
    (3,13,14,21): (120, (9,(5,4,3,2,1))),
    (3,13,14,21,22): (30, (6,(3,3,2,1,1))),
    (3,13,14,21,22,25): (60, (9,(5,4,3,2,2))),
    (3,13,14,21,25): (60, (7,(4,3,2,2,1))),
    (3,13,21): (60, (8,(5,3,2,1,1))),
    (3,13,21,25): (20, (6,(4,2,1,1,1))),
    (3,13,21,25,30): (20, (5,(3,2,1,1,1))),
    (3,13,21,30): (60, (7,(4,3,2,1,1))),
}
assert set(divergent) == set(expected)
for c, (orbit, wr) in expected.items():
    assert divergent[c][0] == orbit
    assert weighted_rep(5, c) == wr

# Clean strict-reversal witness: minimal winners {AB, ACD, ACE}.
witness = (3,13,21)
assert divergent[witness] == (
    60,
    (Fraction(7,18), Fraction(1,6), Fraction(2,9), Fraction(1,9), Fraction(1,9)),
    (Fraction(37,60), Fraction(1,5), Fraction(7,60), Fraction(1,30), Fraction(1,30)),
    (1,0,0,1),
)
# DP ranks C above B; Shapley-Shubik ranks B above C.
assert divergent[witness][1][2] > divergent[witness][1][1]
assert divergent[witness][2][1] > divergent[witness][2][2]

print("VERIFY_OK")
print("proper_counts", proper_counts)
print("proper_isomorphism_classes", class_counts)
print("divergence_counts", divergence_counts)
print("five_player_divergent_labeled", 460, "of", 2645, "=", "92/529")
print("five_player_divergent_classes", len(divergent))
print("relation_hist", dict(relation_hist))
print("relation_class_hist", dict(relation_class_hist))
print("dummy_free_proper5", dummy_free_proper5, "divergent", dummy_free_divergent5)
for c in sorted(expected):
    orbit, dpv, shv, typ = divergent[c]
    print("class", c, "orbit", orbit, "DP", dpv, "SSI", shv, "relation", typ, "weighted", expected[c][1])
