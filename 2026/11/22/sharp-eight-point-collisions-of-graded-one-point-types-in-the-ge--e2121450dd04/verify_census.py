#!/usr/bin/env python3
"""Complete low-order census of the predecessor/successor type fingerprint.

Pure Python 3 standard library.  A tuple ``below`` represents a finite
strict poset: below[v] is the bitmask of points strictly smaller than v.
The recurrence appends a new maximal point whose strict predecessors form
an ideal. Exact backtracking checks isomorphism, not hash equality.
"""
import json
from collections import Counter, defaultdict
from pathlib import Path

EXPECTED_COUNTS = [1, 1, 2, 5, 16, 63, 318, 2045, 16999]
EXPECTED_FIBRES = {2: 28, 3: 2, 4: 1}
WITNESS_A = (0, 0, 0, 0, 1, 2, 13, 19)
WITNESS_B = (0, 0, 0, 0, 1, 2, 7, 25)


def uppers(below):
    n = len(below)
    up = [0] * n
    for v, mask in enumerate(below):
        for w in range(n):
            if mask & (1 << w):
                up[w] |= 1 << v
    return tuple(up)


def invariant(below):
    up = uppers(below)
    return tuple(sorted((m.bit_count(), u.bit_count())
                        for m, u in zip(below, up)))


def isomorphic(a, b):
    """Exhaustively test all degree-preserving bijections by backtracking."""
    if len(a) != len(b) or invariant(a) != invariant(b):
        return False
    n = len(a)
    ua, ub = uppers(a), uppers(b)
    da = [(a[i].bit_count(), ua[i].bit_count()) for i in range(n)]
    db = [(b[j].bit_count(), ub[j].bit_count()) for j in range(n)]
    candidates = [[j for j in range(n) if da[i] == db[j]] for i in range(n)]
    order = sorted(range(n), key=lambda i: (len(candidates[i]), -sum(bool(a[i]&(1<<j) or a[j]&(1<<i)) for j in range(n))))
    mapping, used = {}, set()

    def dfs(t):
        if t == n:
            return True
        i = order[t]
        for j in candidates[i]:
            if j in used:
                continue
            if any(((a[i] >> i2) & 1) != ((b[j] >> j2) & 1)
                   or ((a[i2] >> i) & 1) != ((b[j2] >> j) & 1)
                   for i2, j2 in mapping.items()):
                continue
            mapping[i] = j
            used.add(j)
            if dfs(t + 1):
                return True
            used.remove(j)
            del mapping[i]
        return False

    return dfs(0)


def one_type_poly(below):
    n = len(below)
    up = uppers(below)
    ideals, filters = [], []
    for mask in range(1 << n):
        if all(not (mask & (1 << v)) or (below[v] & ~mask) == 0
               for v in range(n)):
            ideals.append(mask)
        if all(not (mask & (1 << v)) or (up[v] & ~mask) == 0
               for v in range(n)):
            filters.append(mask)
    counts = Counter()
    for low in ideals:
        for high in filters:
            if low & high:
                continue
            # A nonempty lower and upper side must satisfy all cross-relations.
            if any((up[v] & high) != high
                   for v in range(n) if low & (1 << v)):
                continue
            counts[(low.bit_count(), high.bit_count())] += 1
    return tuple(sorted((i, j, c) for (i, j), c in counts.items()))


def direct_type_poly(below):
    """Independent calculation: all ternary labellings, check order axioms."""
    n = len(below)
    out = Counter()
    for code in range(3 ** n):
        q, states = code, []
        for _ in range(n):
            states.append(q % 3)
            q //= 3
        # 0 = below new point, 1 = incomparable, 2 = above new point.
        if any(states[p] > states[v]
               for v, mask in enumerate(below)
               for p in range(n) if mask & (1 << p)):
            continue
        if any(states[p] == 0 and states[v] == 2
               and not (below[v] & (1 << p))
               for p in range(n) for v in range(n)):
            continue
        out[(states.count(0), states.count(2))] += 1
    return tuple(sorted((i, j, c) for (i, j), c in out.items()))


def build():
    posets = [()]
    summary = []
    output_fibres = []
    for n in range(1, 9):
        buckets = defaultdict(list)
        for old in posets:
            for low in range(1 << (n - 1)):
                if any((low & (1 << v)) and (old[v] & ~low)
                       for v in range(n - 1)):
                    continue
                candidate = old + (low,)
                signature = invariant(candidate)
                if not any(isomorphic(candidate, q) for q in buckets[signature]):
                    buckets[signature].append(candidate)
        posets = [p for family in buckets.values() for p in family]
        assert len(posets) == EXPECTED_COUNTS[n], (n, len(posets))
        fingerprints = defaultdict(list)
        for p in posets:
            fingerprints[one_type_poly(p)].append(p)
        fibres = [(poly, ps) for poly, ps in fingerprints.items() if len(ps) > 1]
        summary.append({"order": n, "posets": len(posets),
                        "distinct_fingerprints": len(fingerprints),
                        "collision_fibres": len(fibres)})
        if n < 8:
            assert not fibres, (n, len(fibres))
        else:
            lengths = Counter(len(ps) for _, ps in fibres)
            assert dict(lengths) == EXPECTED_FIBRES, lengths
            assert len(fingerprints) == 16964
            assert any(WITNESS_A in ps and WITNESS_B in ps
                       for _, ps in fibres)
            for poly, ps in sorted(fibres, key=lambda t: (len(t[1]), t[0])):
                output_fibres.append({"polynomial_coefficients": [list(v) for v in poly],
                                      "strict_predecessor_bitmasks": [list(p) for p in ps]})
        # Independent direct check, including all small posets and an evenly
        # spaced subset of the large census; witness checked separately.
        check = posets if n <= 5 else [posets[k] for k in
                    sorted(set(round(j*(len(posets)-1)/24) for j in range(25)))]
        for p in check:
            assert one_type_poly(p) == direct_type_poly(p), (n, p)
        print(f"order {n}: {len(posets)} posets, {len(fingerprints)} profiles, "
              f"{len(fibres)} non-singleton fibres, {len(check)} direct checks",
              flush=True)
    assert not isomorphic(WITNESS_A, WITNESS_B)
    assert one_type_poly(WITNESS_A) == one_type_poly(WITNESS_B)
    assert one_type_poly(WITNESS_A) == direct_type_poly(WITNESS_A)
    assert one_type_poly(WITNESS_B) == direct_type_poly(WITNESS_B)
    result = {"description": "All nontrivial equal-fingerprint fibres for strict posets of order eight",
              "unlabeled_poset_counts_by_order": EXPECTED_COUNTS,
              "summary": summary, "fibre_size_counts": {str(k): v for k,v in EXPECTED_FIBRES.items()},
              "witness_A": list(WITNESS_A), "witness_B": list(WITNESS_B),
              "collision_fibres": output_fibres}
    path = Path(__file__).with_name('census.json')
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n',encoding='utf-8')
    print('PASS exact census, exhaustive isomorphism, direct small-sample checks and witness')
    print('CENSUS',path.name,path.stat().st_size,'bytes')

if __name__ == '__main__':
    build()
