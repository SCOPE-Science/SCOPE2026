#!/usr/bin/env python3
"""Reproduce the graded singleton-type reconstruction cutoff for finite posets.
Python >=3.10, standard library only. Run: python3 checker.py
Optionally provide collision_pairs.json in the same directory for certificate replay.
"""
import collections
import hashlib
import itertools
import json
from pathlib import Path


def canonical_key(n, edges):
    """Isomorphism-complete signature by degree-refined relabelling."""
    ed = set(edges)
    degree = []
    for i in range(n):
        degree.append((sum((j, i) in ed for j in range(n)),
                       sum((i, j) in ed for j in range(n))))
    clusters = [[i for i in range(n) if degree[i] == k]
                for k in sorted(set(degree))]
    parts = [list(itertools.permutations(c)) for c in clusters]
    best = None
    for choices in itertools.product(*parts):
        order = tuple(itertools.chain.from_iterable(choices))
        code = 0
        for i in order:
            for j in order:
                code = (code << 1) | int((i, j) in ed)
        if best is None or code < best:
            best = code
    return tuple((len(c), degree[c[0]]) for c in clusters), best


def ideals(n, edges):
    predecessors = [0] * n
    for i, j in edges:
        predecessors[j] |= 1 << i
    result = []
    for mask in range(1 << n):
        if all((mask & predecessors[j]) == predecessors[j]
               for j in range(n) if mask & (1 << j)):
            result.append(mask)
    return result


def generate_posets(max_n=7):
    items = [frozenset()]
    yield 0, items
    for n in range(1, max_n + 1):
        unique = {}
        for old in items:
            for lower in ideals(n - 1, old):
                edges = old | frozenset((i, n - 1)
                                        for i in range(n - 1)
                                        if lower & (1 << i))
                key = canonical_key(n, edges)
                unique.setdefault(key, edges)
        items = list(unique.values())
        yield n, items


def type_rank_direct(n, edges):
    """Directly enumerate compatible lower ideals and upper filters."""
    successors = [0] * n
    for i, j in edges:
        successors[i] |= 1 << j
    lower_ideals = ideals(n, edges)
    # U is an upper filter iff its complement is an ideal.
    filters = [((1 << n) - 1) ^ low for low in lower_ideals]
    rank = [0] * (2 * n + 1)
    for low in lower_ideals:
        allowed_upper = (1 << n) - 1
        for i in range(n):
            if low & (1 << i):
                allowed_upper &= successors[i]
        for up in filters:
            if up & allowed_upper == up:
                rank[low.bit_count() + n - up.bit_count()] += 1
    return tuple(rank)


def type_bivariate_direct(n, edges):
    """Joint old-predecessor/old-successor profile, for comparison only."""
    successors = [0] * n
    for i, j in edges:
        successors[i] |= 1 << j
    lower_ideals = ideals(n, edges)
    filters = [((1 << n) - 1) ^ low for low in lower_ideals]
    profile = collections.Counter()
    for low in lower_ideals:
        allowed_upper = (1 << n) - 1
        for i in range(n):
            if low & (1 << i):
                allowed_upper &= successors[i]
        for up in filters:
            if up & allowed_upper == up:
                profile[(low.bit_count(), up.bit_count())] += 1
    return tuple(sorted(profile.items()))


def type_rank_doubled(n, edges):
    """Independent order-ideal traversal on an explicit 2n-point poset."""
    strict = set(edges)
    predecessors = [0] * (2 * n)
    for i, j in strict:
        predecessors[j] |= 1 << i
        predecessors[j + n] |= 1 << (i + n)
    for p in range(n):
        for q in range(n):
            if (p, q) not in strict:
                predecessors[p + n] |= 1 << q
    layer = {0}
    counts = [1]
    for size in range(1, 2 * n + 1):
        following = set()
        for subset in layer:
            for v in range(2 * n):
                if (subset >> v) & 1 == 0 and (
                    subset & predecessors[v]) == predecessors[v]:
                    following.add(subset | (1 << v))
        counts.append(len(following))
        layer = following
    assert counts[-1] == 1
    return tuple(counts)


def cover_edges(n, edges):
    e = set(edges)
    return sorted([list(pair) for pair in e
                   if not any((pair[0], k) in e and (k, pair[1]) in e
                              for k in range(n))])


def run():
    totals = {}
    groups = None
    for n, posets in generate_posets(7):
        totals[n] = len(posets)
        if n == 0:
            continue
        profiles = collections.defaultdict(list)
        bivar_profiles = set()
        for edges in posets:
            polynomial = type_rank_direct(n, edges)
            assert polynomial == type_rank_doubled(n, edges), (n, edges)
            profiles[polynomial].append(edges)
            joint = type_bivariate_direct(n, edges)
            assert sum(v for _, v in joint) == sum(polynomial)
            if n == 7:
                assert joint not in bivar_profiles, "bivariate-profile collision at seven"
                bivar_profiles.add(joint)
        colliding = [t for t in profiles.values() if len(t) > 1]
        if n <= 6:
            assert not colliding, n
        else:
            assert len(colliding) == 6 and all(len(t) == 2 for t in colliding)
            assert len(bivar_profiles) == 2045
            groups = []
            for pair in colliding:
                a, b = pair
                ca = cover_edges(n, a)
                cb = cover_edges(n, b)
                left, right = sorted((ca, cb), key=lambda x: json.dumps(x))
                groups.append({"covers_a": left, "covers_b": right,
                               "rank_coefficients": list(type_rank_direct(n, a))})
            groups.sort(key=lambda x: (x['rank_coefficients'],
                                        x['covers_a'], x['covers_b']))
    assert totals == {0:1, 1:1, 2:2, 3:5, 4:16, 5:63, 6:318, 7:2045}
    canonical = json.dumps(groups, ensure_ascii=False, sort_keys=True,
                           separators=(',', ':')).encode('utf8')
    digest = hashlib.sha256(canonical).hexdigest()
    print('poset_isomorphism_counts=' + json.dumps(totals, sort_keys=True))
    print('first_rank_collision_order=7; collision_pairs=6; involved_classes=12')
    print('bivariate_profiles_at_seven=2045; rank_profiles_at_seven=2039')
    print('collision_certificate_sha256=' + digest)
    reference = Path(__file__).with_name('collision_pairs.json')
    if reference.exists():
        expected = json.loads(reference.read_text(encoding='utf8'))
        assert groups == expected, 'collision certificate mismatch'
        print('collision_certificate=PASS')
    else:
        reference.write_text(json.dumps(groups, indent=2) + '\n', encoding='utf8')
        print('collision_certificate=CREATED')
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
