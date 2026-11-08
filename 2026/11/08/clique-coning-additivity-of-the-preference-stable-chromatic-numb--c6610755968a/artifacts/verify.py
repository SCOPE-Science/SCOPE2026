#!/usr/bin/env python3
"""Finite, supplementary spot checks for the clique-coning theorem.
The theorem's proof applies to all finite nonempty graphs; these checks
only test small examples and the lower-bound lifting construction.
"""
from itertools import permutations, product


def cone(edges, n):
    return n + 1, edges | {tuple(sorted((i, n))) for i in range(n)}


def all_colorings(n, edges, k):
    return [p for p in product(range(k), repeat=n)
            if all(p[a] != p[b] for a, b in edges)]


def stable(coloring, pref, edges):
    n = len(coloring)
    arcs = [[] for _ in range(n)]
    for a, b in edges:
        if pref[a].index(coloring[b]) < pref[a].index(coloring[a]):
            arcs[a].append(b)
        if pref[b].index(coloring[a]) < pref[b].index(coloring[b]):
            arcs[b].append(a)
    seen = [0] * n
    def visit(v):
        if seen[v] == 1:
            return False
        if seen[v] == 2:
            return True
        seen[v] = 1
        for w in arcs[v]:
            if not visit(w):
                return False
        seen[v] = 2
        return True
    return all(visit(v) for v in range(n) if not seen[v])


def check_all_profiles(n, edges, k):
    cands = all_colorings(n, edges, k)
    ranks = list(permutations(range(k)))
    count = 0
    bad_profile = None
    for p in product(ranks, repeat=n):
        count += 1
        if not any(stable(c, p, edges) for c in cands):
            bad_profile = p
            break
    return bad_profile is None, count, bad_profile


def check_lift(n, edges, k, profile):
    # Witness profile on k-1 colors, extended by color k-1 as worst;
    # new apex ranks the newly added color first.
    assert profile is not None
    n1, e1 = cone(edges, n)
    new = k - 1
    pp = [tuple(p) + (new,) for p in profile]
    pp.append((new,) + tuple(range(k - 1)))
    proper = all_colorings(n1, e1, k)
    assert all(not stable(c, pp, e1) for c in proper)
    return len(proper)


def main():
    tests = [
        ("isolated vertex", 1, set(), 1),
        ("two independent vertices", 2, set(), 1),
        ("single edge", 2, {(0, 1)}, 2),
        ("three-vertex path", 3, {(0, 1), (1, 2)}, 2),
        ("four-vertex path", 4, {(0, 1), (1, 2), (2, 3)}, 3),
    ]
    for name, n, edges, chi in tests:
        edges = {tuple(sorted(e)) for e in edges}
        if chi > 1:
            ok, np, witness = check_all_profiles(n, edges, chi-1)
            assert not ok, (name, "wrong lower bound")
            nc = check_lift(n, edges, chi, witness)
        else:
            nc = 'edge bound'
        if n <= 3:  # full preference universality for small graphs
            ok, np, _ = check_all_profiles(n, edges, chi)
            assert ok, (name, "wrong upper bound")
            if chi <= 2:
                cn, ce = cone(edges, n)
                ok, nr, _ = check_all_profiles(cn, ce, chi + 1)
                assert ok, (name, "wrong cone upper bound")
        print("CASE_OK", name, "base_chi", chi, "lifted_proper_assignments", nc)
    # Exhaustive proper coloring + preference profile on a genuinely non-bipartite cone.
    n, edges = cone({(0, 1), (1, 2)}, 3)
    assert check_all_profiles(n, edges, 3)[0]
    print("CONE_P3_ALL_1296_PROFILES_OK")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
