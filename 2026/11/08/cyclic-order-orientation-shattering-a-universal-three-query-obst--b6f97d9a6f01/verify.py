#!/usr/bin/env python3
"""Exhaustive verifier for cyclic triple-orientation query shattering on six labels.
Uses Python's standard library only; run `python3 verify.py` from the package folder.
"""
import itertools
import json
from collections import Counter
from pathlib import Path

N = 6
LABELS = tuple(range(N))
QUERIES = tuple(itertools.combinations(LABELS, 3))
QINDEX = {triple: i for i, triple in enumerate(QUERIES)}


def cyclic_rows():
    output = {}
    for tail in itertools.permutations(range(1, N)):
        cycle = (0,) + tail
        pos = {x: i for i, x in enumerate(cycle)}
        flags = 0
        for idx, (a, b, c) in enumerate(QUERIES):
            if (pos[b] - pos[a]) % N < (pos[c] - pos[a]) % N:
                flags |= 1 << idx
        assert flags not in output
        output[flags] = list(cycle)
    assert len(output) == 120
    return output


def cocycle_rows():
    # Independent enumeration, using binary quadrangle identities from
    # Abram--Chapelier-Laget--Reutenauer, Theorem 21 (2020 preprint).
    quad_relations = []
    for a, b, c, d in itertools.combinations(LABELS, 4):
        quad_relations.append(tuple(QINDEX[t] for t in
                                    ((a, b, c), (a, c, d), (a, b, d), (b, c, d))))
    output = set()
    for candidate in range(1 << len(QUERIES)):
        for i, j, k, ell in quad_relations:
            if ((candidate >> i) & 1) + ((candidate >> j) & 1) != \
               ((candidate >> k) & 1) + ((candidate >> ell) & 1):
                break
        else:
            output.add(candidate)
    assert len(output) == 120
    return output


def shattering_faces(rows):
    # Exhaust all relevant supports. Seven queries require at least 128
    # hypotheses, but there are only 120 cyclic orders.
    true_rows = list(rows)
    wordmask = (1 << len(true_rows)) - 1
    ones = [sum(((r >> i) & 1) << j for j, r in enumerate(true_rows))
            for i in range(len(QUERIES))]
    zeros = [wordmask ^ x for x in ones]
    levels = {}
    for k in range(7):
        accepted = set()
        for support in itertools.combinations(range(len(QUERIES)), k):
            slices = [wordmask]
            for idx in support:
                new_slices = []
                for s in slices:
                    left = s & zeros[idx]
                    right = s & ones[idx]
                    if not left or not right:
                        break
                    new_slices.extend((left, right))
                else:
                    slices = new_slices
                    continue
                break
            else:
                accepted.add(sum(1 << idx for idx in support))
        levels[k] = accepted
    return levels


def facets(levels):
    result = {}
    for k in range(1, 7):
        supersets = levels.get(k + 1, set())
        covered = {x & ~(1 << j) for x in supersets
                   for j in range(len(QUERIES)) if x & (1 << j)}
        result[k] = levels[k] - covered
    return result


def query_actions():
    result = []
    for p in itertools.permutations(LABELS):
        result.append(tuple(QINDEX[tuple(sorted(p[v] for v in tri))]
                            for tri in QUERIES))
    return result


def action(mask, transform):
    new = 0
    for idx in range(len(QUERIES)):
        if mask & (1 << idx):
            new |= 1 << transform[idx]
    return new


def orbit_table(facet_levels):
    actions = query_actions()
    table = []
    for k in sorted(facet_levels, reverse=True):
        remaining = set(facet_levels[k])
        while remaining:
            chosen = min(remaining)
            orbit = {action(chosen, t) for t in actions}
            assert orbit <= facet_levels[k]
            remaining -= orbit
            canonical = min(orbit)
            table.append({"support_size": k,
                          "representative_indices": [i for i in range(20) if canonical & (1 << i)],
                          "orbit_size": len(orbit)})
    table.sort(key=lambda r: (-r["support_size"], r["orbit_size"], r["representative_indices"]))
    return table


def three_query_obstruction_nine_labels():
    # A family of three distinct triple queries uses at most nine labels.
    # Restricting and extending circular orders proves that it suffices to
    # test all supports on nine labels for the universal statement.
    n = 9
    triples = tuple(itertools.combinations(range(n), 3))
    index = {t: i for i, t in enumerate(triples)}
    predicates = [0] * len(triples)
    total_cycles = 0
    for tail in itertools.permutations(range(1, n)):
        position = [0] * n
        for j, value in enumerate((0,) + tail):
            position[value] = j
        for i, (a, b, c) in enumerate(triples):
            if (position[b] - position[a]) % n < (position[c] - position[a]) % n:
                predicates[i] |= 1 << total_cycles
        total_cycles += 1
    assert total_cycles == 40320
    full = (1 << total_cycles) - 1
    opposite = [full ^ v for v in predicates]
    failures = set()
    tested = 0
    for a, b, c in itertools.combinations(range(len(triples)), 3):
        tested += 1
        traces_all = True
        for aa in (predicates[a], opposite[a]):
            for bb in (predicates[b], opposite[b]):
                if not (aa & bb & predicates[c]) or not (aa & bb & opposite[c]):
                    traces_all = False
                    break
            if not traces_all:
                break
        if not traces_all:
            failures.add((a, b, c))
    expected = set()
    for quad in itertools.combinations(range(n), 4):
        four = [index[t] for t in itertools.combinations(quad, 3)]
        expected.update(itertools.combinations(four, 3))
    assert tested == 95284
    assert len(expected) == 504
    assert failures == expected
    return {"n": 9, "cyclic_orders": total_cycles,
            "queried_triples": len(triples), "supports_tested": tested,
            "nonshattered_supports": len(failures),
            "exception": "Three of the four triples of a four-element set"}


def small_case_checks():
    data = {}
    for n in (3, 4, 5):
        queries = tuple(itertools.combinations(range(n), 3))
        rows = []
        for tail in itertools.permutations(range(1, n)):
            position = {v: j for j, v in enumerate((0,) + tail)}
            rows.append(sum(((position[b] - position[a]) % n <
                             (position[c] - position[a]) % n) << i
                            for i, (a, b, c) in enumerate(queries)))
        all_faces = {0: {frozenset()}}
        for k in range(1, len(queries) + 1):
            accepted = set()
            for inds in itertools.combinations(range(len(queries)), k):
                patterns = {tuple((row >> i) & 1 for i in inds) for row in rows}
                if len(patterns) == (1 << k):
                    accepted.add(frozenset(inds))
            all_faces[k] = accepted
        maximal = Counter()
        for k in range(1, len(queries) + 1):
            for face in all_faces[k]:
                if not any(face < sup for sup in all_faces.get(k + 1, set())):
                    maximal[k] += 1
        data[str(n)] = {"coefficients": [len(all_faces[k]) for k in range(len(queries) + 1)],
                        "facet_sizes": dict(sorted(maximal.items()))}
    assert data == {"3": {"coefficients": [1, 1], "facet_sizes": {1: 1}},
                    "4": {"coefficients": [1, 4, 6, 0, 0], "facet_sizes": {2: 6}},
                    "5": {"coefficients": [1, 10, 45, 100, 10, 0, 0, 0, 0, 0, 0],
                          "facet_sizes": {3: 60, 4: 10}}}
    return data


def main():
    small_cases = small_case_checks()
    universal_three = three_query_obstruction_nine_labels()
    rows = cyclic_rows()
    oracle = cocycle_rows()
    assert set(rows) == oracle, 'Permutation and quadrangle models disagree'
    levels = shattering_faces(rows)
    expected = [1, 20, 190, 1080, 3420, 1680, 30]
    assert [len(levels[k]) for k in range(7)] == expected
    fl = facets(levels)
    assert [len(fl[k]) for k in range(1, 7)] == [0, 0, 0, 840, 1500, 30]
    table = orbit_table(fl)
    assert len(table) == 10
    assert [(k, sorted(x["orbit_size"] for x in table if x["support_size"] == k))
            for k in [4, 5, 6]] == [(4, [120, 360, 360]),
                                    (5, [60, 180, 180, 360, 360, 360]),
                                    (6, [30])]
    top = next(t for t in table if t["support_size"] == 6)
    selected = top["representative_indices"]
    witnesses = {}
    for flags, cycle in sorted(rows.items()):
        pattern = sum(((flags >> i) & 1) << j for j, i in enumerate(selected))
        witnesses.setdefault(str(pattern), cycle)
    assert len(witnesses) == 64 and set(witnesses) == {str(i) for i in range(64)}
    certificate = {"query_indexing": "0-based lexicographic order of 3-subsets of {0,1,2,3,4,5}",
                   "query_triples": [list(t) for t in QUERIES],
                   "facet_orbits": table,
                   "three_query_obstruction": universal_three,
                   "smaller_cases": small_cases,
                   "top_support_indices": selected,
                   "top_support_witnesses": {str(k): witnesses[str(k)] for k in range(64)}}
    target = Path(__file__).parent / 'certificates.json'
    if target.exists():
        assert json.loads(target.read_text(encoding='utf-8')) == json.loads(json.dumps(certificate))
    else:
        target.write_text(json.dumps(certificate, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print('CIRCULAR_TRIPLE_SHATTER_PASS 95284_three_query_supports 504_quadruple_obstructions 120_cyclic_orders 120_cocycles 60460_six_label_supports 6421_faces 2370_facets 10_orbits 64_witnesses')


if __name__ == '__main__':
    main()
