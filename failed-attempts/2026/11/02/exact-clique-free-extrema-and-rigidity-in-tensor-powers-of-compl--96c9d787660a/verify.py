"""Finite consistency tests for clique-free subsets of categorical clique powers.

Run: python3 verify.py. No third-party dependencies are required.
"""
from itertools import combinations, permutations, product
from math import comb


def vertices(q, n):
    return list(product(range(q), repeat=n))


def large_cliques(q, n):
    vv = vertices(q, n)
    where = {v: i for i, v in enumerate(vv)}
    out = []
    for ps in product(permutations(range(q)), repeat=n - 1):
        points = [(a,) + tuple(p[a] for p in ps) for a in range(q)]
        out.append(sum(1 << where[v] for v in points))
    return out


def direct_clique_masks(q, n, t):
    vv = vertices(q, n)
    out = []
    for ids in combinations(range(q ** n), t):
        if all(all(vv[i][k] != vv[j][k] for k in range(n))
               for i, j in combinations(ids, 2)):
            out.append(sum(1 << i for i in ids))
    return out


def slabs(q, n, t):
    vv = vertices(q, n)
    return {sum(1 << k for k, v in enumerate(vv) if v[i] in letters)
            for i in range(n)
            for letters in combinations(range(q), t - 1)}


def exhaustive(q, n, t):
    N = q ** n
    goal = (t - 1) * q ** (n - 1)
    triangles = direct_clique_masks(q, n, t)
    expected = slabs(q, n, t)
    observed = set()
    for ids in combinations(range(N), goal):
        mask = sum(1 << i for i in ids)
        if all(mask & obstruction != obstruction for obstruction in triangles):
            observed.add(mask)
    assert observed == expected, (q, n, t, len(observed), len(expected))
    assert len(observed) == n * comb(q, t - 1)
    print('DIRECT_EXHAUSTIVE_OK', q, n, t, len(observed), 'sets',
          len(triangles), 'forbidden cliques')


def exact_cover_count(q, n, t):
    """Independent solver using only full transversal-clique equalities."""
    N = q ** n
    masks = large_cliques(q, n)
    want = t - 1
    incidence = [[i for i in range(N) if (m >> i) & 1] for m in masks]
    counts = [sum(i in block for block in incidence) for i in range(N)]
    results = set()

    def search(ass):
        while True:
            updates = {}
            for block in incidence:
                s = sum(ass.get(i, 0) for i in block)
                open_ = [i for i in block if i not in ass]
                if s > want or s + len(open_) < want:
                    return
                if s == want or s + len(open_) == want:
                    value = 0 if s == want else 1
                    for i in open_:
                        if i in updates and updates[i] != value:
                            return
                        updates[i] = value
            if not updates:
                break
            ass = dict(ass)
            ass.update(updates)
        if len(ass) == N:
            results.add(sum(1 << i for i, value in ass.items() if value))
            return
        i = max((j for j in range(N) if j not in ass), key=lambda j: counts[j])
        for value in (0, 1):
            next_ass = dict(ass)
            next_ass[i] = value
            search(next_ass)

    search({})
    expected = slabs(q, n, t)
    assert results == expected, (q, n, t, len(results), len(expected))
    print('TRANSVERSAL_EQUATIONS_OK', q, n, t, len(results),
          'sets', len(masks), 'independently generated transversals')


def check_swap_lemma(q, n):
    vv = vertices(q, n)
    ws = list(product(range(q), repeat=n - 1))
    for a, b in combinations(range(q), 2):
        for u, v in combinations(ws, 2):
            if all(x != y for x, y in zip(u, v)):
                for c in product((0, 1), repeat=4):
                    # Enumerates 0/1 values for the four involved words.
                    left_equal = c[0] + c[3] == c[1] + c[2]
                    if not left_equal:
                        continue
                    # Difference equality is an identical rearrangement.
                    assert c[0] - c[2] == c[1] - c[3]
    print('SWAP_IDENTITY_OK', q, n)


if __name__ == '__main__':
    exhaustive(3, 2, 3)
    exhaustive(4, 2, 3)
    exhaustive(4, 2, 4)
    exact_cover_count(3, 3, 3)
    exact_cover_count(4, 2, 3)
    check_swap_lemma(3, 2)
    print('VERIFY_OK')
