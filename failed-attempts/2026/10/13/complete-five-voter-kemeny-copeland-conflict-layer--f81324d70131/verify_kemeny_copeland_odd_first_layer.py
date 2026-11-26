#!/usr/bin/env python3
from itertools import permutations, product
from math import factorial
from collections import Counter

CANDS = (0,1,2)
BALLOTS = tuple(permutations(CANDS))

def pairwise_from_profile(profile):
    s = [[0]*3 for _ in range(3)]
    for ballot in profile:
        pos = {c:i for i,c in enumerate(ballot)}
        for a in CANDS:
            for b in CANDS:
                if a != b and pos[a] < pos[b]:
                    s[a][b] += 1
    return s

def pairwise_from_counts(counts):
    s = [[0]*3 for _ in range(3)]
    for mult, ballot in zip(counts, BALLOTS):
        pos = {c:i for i,c in enumerate(ballot)}
        for a in CANDS:
            for b in CANDS:
                if a != b and pos[a] < pos[b]:
                    s[a][b] += mult
    return s

def kemeny_pairwise(profile):
    s = pairwise_from_profile(profile)
    score = {}
    best = None
    for order in BALLOTS:
        val = sum(s[order[i]][order[j]] for i in range(3) for j in range(i+1,3))
        score[order] = val
        best = val if best is None else max(best, val)
    return frozenset(o[0] for o,v in score.items() if v == best), score

def kendall_distance(a,b):
    pos = {x:i for i,x in enumerate(b)}
    d = 0
    for i in range(3):
        for j in range(i+1,3):
            if pos[a[i]] > pos[a[j]]:
                d += 1
    return d

def kemeny_distance(profile):
    dist = {}
    best = None
    for order in BALLOTS:
        val = sum(kendall_distance(order,b) for b in profile)
        dist[order] = val
        best = val if best is None else min(best, val)
    return frozenset(o[0] for o,v in dist.items() if v == best), dist

def kemeny_counts(counts):
    s = pairwise_from_counts(counts)
    best = None
    tops = set()
    for order in BALLOTS:
        val = sum(s[order[i]][order[j]] for i in range(3) for j in range(i+1,3))
        if best is None or val > best:
            best = val
            tops = {order[0]}
        elif val == best:
            tops.add(order[0])
    return frozenset(tops)

def copeland_from_matrix(s):
    vals = []
    for a in CANDS:
        v = 0
        for b in CANDS:
            if a == b:
                continue
            if s[a][b] > s[b][a]:
                v += 1
            elif s[a][b] == s[b][a]:
                v += 0.5
        vals.append(v)
    best = max(vals)
    return frozenset(a for a,v in enumerate(vals) if v == best), tuple(vals)

def copeland_profile(profile):
    return copeland_from_matrix(pairwise_from_profile(profile))

def copeland_counts(counts):
    return copeland_from_matrix(pairwise_from_counts(counts))

def maximin_profile(profile):
    s = pairwise_from_profile(profile)
    vals = tuple(min(s[a][b] for b in CANDS if b != a) for a in CANDS)
    best = max(vals)
    return frozenset(a for a,v in enumerate(vals) if v == best), vals

def margins_from_matrix(s):
    return (s[0][1]-s[1][0], s[0][2]-s[2][0], s[1][2]-s[2][1])

def compositions(total, parts, prefix=()):
    if parts == 1:
        yield prefix + (total,)
    else:
        for x in range(total+1):
            yield from compositions(total-x, parts-1, prefix+(x,))

def multinomial(counts):
    n = sum(counts)
    ans = factorial(n)
    for x in counts:
        ans //= factorial(x)
    return ans

def relabel_counts(counts, perm):
    # Transform every ballot by candidate relabeling and accumulate in BALLOTS order.
    index = {b:i for i,b in enumerate(BALLOTS)}
    out = [0]*len(BALLOTS)
    for mult, ballot in zip(counts, BALLOTS):
        rb = tuple(perm[x] for x in ballot)
        out[index[rb]] += mult
    return tuple(out)

def canonical_counts(counts):
    return min(relabel_counts(counts,p) for p in permutations(CANDS))

# First engine: all labeled odd-electorate profiles for n = 1,3,5.
labeled_hist = {}
divergent_profiles = []
for n in (1,3,5):
    hist = Counter()
    for profile in product(BALLOTS, repeat=n):
        K1, ks = kemeny_pairwise(profile)
        K2, kd = kemeny_distance(profile)
        assert K1 == K2
        assert all(ks[o] + kd[o] == 3*n for o in BALLOTS)

        X, cop_scores = copeland_profile(profile)
        M, _ = maximin_profile(profile)

        # Published three-candidate equivalence, checked here independently
        # throughout the complete finite domains used in the claim.
        assert K1 == M

        relation = "equal" if K1 == X else "kemeny_strict_subset_copeland"
        if K1 != X:
            assert K1 < X
            divergent_profiles.append(profile)
        hist[(relation, len(K1), len(X))] += 1
    labeled_hist[n] = hist

assert labeled_hist[1] == Counter({("equal",1,1):6})
assert labeled_hist[3] == Counter({
    ("equal",1,1):204,
    ("equal",3,3):12,
})
assert labeled_hist[5] == Counter({
    ("equal",1,1):7236,
    ("equal",3,3):360,
    ("kemeny_strict_subset_copeland",2,3):180,
})
assert len(divergent_profiles) == 180

# Every divergence is a 3-cycle with absolute majority margins {1,1,3}.
for profile in divergent_profiles:
    s = pairwise_from_profile(profile)
    assert tuple(sorted(abs(x) for x in margins_from_matrix(s))) == (1,1,3)

# Second engine: all 252 anonymous five-voter profiles, weighted back to labeled profiles.
anonymous_divergent = []
weighted_divergence = 0
anonymous_hist = Counter()
for counts in compositions(5,6):
    K = kemeny_counts(counts)
    X, _ = copeland_counts(counts)
    relation = "equal" if K == X else "kemeny_strict_subset_copeland"
    anonymous_hist[(relation, len(K), len(X))] += 1
    if K != X:
        assert K < X
        anonymous_divergent.append(counts)
        weighted_divergence += multinomial(counts)

assert sum(anonymous_hist.values()) == 252
assert anonymous_hist == Counter({
    ("equal",1,1):240,
    ("equal",3,3):6,
    ("kemeny_strict_subset_copeland",2,3):6,
})
assert len(anonymous_divergent) == 6
assert weighted_divergence == 180

# All six anonymous divergent profiles are one candidate-relabeling orbit.
canonical = Counter(canonical_counts(c) for c in anonymous_divergent)
assert len(canonical) == 1
canon_counts = next(iter(canonical))
assert canonical[canon_counts] == 6

# Canonical anonymous representative:
# BALLOTS are (012),(021),(102),(120),(201),(210).
assert canon_counts == (0,1,2,0,0,2)

# Its six candidate relabelings are exactly the six anonymous divergences.
orbit = {relabel_counts(canon_counts,p) for p in permutations(CANDS)}
assert len(orbit) == 6
assert orbit == set(anonymous_divergent)

# Each anonymous profile has multiplicities 2,2,1 and therefore 5!/(2!2!) = 30
# labeled realizations, giving 6*30 = 180.
assert {multinomial(c) for c in anonymous_divergent} == {30}
assert 6*30 == 180

# Exact incidences.
from fractions import Fraction
assert Fraction(180,6**5) == Fraction(5,216)
assert Fraction(6,252) == Fraction(1,42)

# Representative winner sets and margins.
rep_profile = (
    (0,1,2),(0,1,2),
    (1,2,0),(1,2,0),
    (2,0,1),
)
K,_ = kemeny_pairwise(rep_profile)
X,_ = copeland_profile(rep_profile)
s = pairwise_from_profile(rep_profile)
assert K == frozenset({0,1})
assert X == frozenset({0,1,2})
assert margins_from_matrix(s) == (1,-1,3)

print("VERIFY_OK")
for n in (1,3,5):
    print("n",n,"labeled_hist",dict(labeled_hist[n]))
print("anonymous_n5_hist",dict(anonymous_hist))
print("divergent_labeled",180,"of",6**5,"=", "5/216")
print("divergent_anonymous",6,"of",252,"=", "1/42")
print("anonymous_classes",len(canonical))
print("canonical_counts",canon_counts)
print("candidate_orbit_size",len(orbit))
print("labeled_weight_per_anonymous",30)
print("representative_margins",margins_from_matrix(s))
print("representative_K",sorted(K))
print("representative_Copeland",sorted(X))
