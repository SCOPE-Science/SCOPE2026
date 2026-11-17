#!/usr/bin/env python3
"""Reproducibility checks for the exact lollipop colour-refinement round formula.
Uses only the Python standard library. Its finite checks complement a symbolic proof.
"""
from functools import lru_cache


def lollipop(m, ell):
    assert m >= 3 and ell >= 1
    n = m + ell
    adj = [set() for _ in range(n)]
    edges = [(i, (i + 1) % m) for i in range(m)]
    edges += [(0, m)] + [(i, i + 1) for i in range(m, m + ell - 1)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return tuple(tuple(sorted(vs)) for vs in adj)


def wl(adj):
    n = len(adj)
    coloring = (0,) * n
    states = [coloring]
    while True:
        sigs = [(coloring[v], tuple(sorted(coloring[w] for w in adj[v]))) for v in range(n)]
        palette = {s: i for i, s in enumerate(sorted(set(sigs)))}
        new = tuple(palette[s] for s in sigs)
        if len(set(new)) == len(set(coloring)):
            return len(states) - 1, states
        coloring = new
        states.append(coloring)


def claimed(m, ell):
    return max(m // 2, min(m, ell), (ell + 1) // 2)


def orbit_label(m, ell, v):
    if v >= m:
        return (1, v - m + 1)
    return (0, min(v, m - v))


def degree_cover_code(adj, root, depth):
    """Independent computation tree: degree marks and backtrack-free unrolling."""
    @lru_cache(None)
    def unfold(v, parent, d):
        if d == 0:
            return (len(adj[v]),)
        return (len(adj[v]), tuple(sorted((unfold(w, v, d - 1) for w in adj[v] if w != parent))))
    return unfold(root, -1, depth)


def main():
    cases = 0
    for m in range(3, 45):
        for ell in range(1, 66):
            adj = lollipop(m, ell)
            steps, states = wl(adj)
            assert steps == claimed(m, ell), (m, ell, steps, claimed(m, ell))
            assert len(set(states[-1])) == ell + 1 + m // 2, (m, ell)
            seen = {}
            for v, c in enumerate(states[-1]):
                lab = orbit_label(m, ell, v)
                assert c not in seen or seen[c] == lab, (m, ell, c, v)
                seen[c] = lab
            assert len(seen) == ell + 1 + m // 2
            cases += 1
    print(f'WL_FORMULA_OK {cases} parameter pairs (3<=m<=44, 1<=ell<=65)')
    # Structurally independent universal-cover tests on small parameters.
    cover_cases = 0
    for m in range(3, 13):
        for ell in range(1, 17):
            adj = lollipop(m, ell)
            steps, states = wl(adj)
            for t, state in enumerate(states):
                view_codes = [degree_cover_code(adj, v, t - 1) if t > 0 else (0,)
                              for v in range(len(adj))]
                for u in range(len(adj)):
                    for v in range(u + 1, len(adj)):
                        assert (state[u] == state[v]) == (view_codes[u] == view_codes[v]), (m, ell, t, u, v)
            cover_cases += 1
    print(f'UNFOLDING_EQUIVALENCE_OK {cover_cases} parameter pairs (3<=m<=12, 1<=ell<=16)')
    for m, ell in [(3, 1), (3, 7), (8, 4), (7, 5), (10, 11), (20, 50)]:
        print(f'SAMPLE m={m} ell={ell} rounds={wl(lollipop(m, ell))[0]} formula={claimed(m, ell)}')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
