"""Reproduce exact free-spectrum counts for a six-element idempotent semiring.

Only finite checks: the proof in RESULT.md establishes arbitrary rank.
Run with: python verify_free_spectrum.py
"""
from itertools import combinations, product
from math import comb

INF, OMEGA, A, B, C, D = range(6)
LOWER = {(B, D), (C, A)}
PRODUCTS = {frozenset((A, B)), frozenset((B, C)), frozenset((C, D))}


def add(x, y):
    if x == y:
        return x
    if (x, y) in LOWER:
        return y
    if (y, x) in LOWER:
        return x
    return INF


def mul(x, y):
    return OMEGA if frozenset((x, y)) in PRODUCTS else INF


def bipartite(n, edges):
    adjacency = [set() for _ in range(n)]
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    color = {}
    for i in range(n):
        if i in color:
            continue
        color[i] = 0
        stack = [i]
        while stack:
            v = stack.pop()
            for w in adjacency[v]:
                if w not in color:
                    color[w] = color[v] ^ 1
                    stack.append(w)
                elif color[w] == color[v]:
                    return False
    return True


def direct_bipartite_counts(up_to=5):
    ans = []
    for n in range(up_to + 1):
        edges = list(combinations(range(n), 2))
        ans.append(sum(bipartite(n, [edges[j] for j in range(len(edges))
                                        if (mask >> j) & 1])
                       for mask in range(1 << len(edges))))
    return ans


def recurrent_bipartite_counts(up_to=8):
    # T(n): labelled bipartite graphs with a specified valid 2-coloring.
    # Their exponential generating function is the square of the EGF
    # of uncolored labelled bipartite graphs, because each connected
    # bipartite graph has exactly two proper colorings.
    Bvals = [1]
    for n in range(1, up_to + 1):
        t = sum(comb(n, k) * 2 ** (k * (n-k)) for k in range(n+1))
        conv = sum(comb(n, k) * Bvals[k] * Bvals[n-k]
                   for k in range(1, n))
        numerator = t - conv
        assert numerator % 2 == 0
        Bvals.append(numerator // 2)
    return Bvals


def scalar_signature(n, L, E):
    signature = bytearray()
    for assignment in product(range(6), repeat=n):
        value = None
        for u in L:
            value = assignment[u] if value is None else add(value, assignment[u])
        for u, v in E:
            term = mul(assignment[u], assignment[v])
            value = term if value is None else add(value, term)
        assert value is not None
        signature.append(value)
    return bytes(signature)


def check_normal_forms(n):
    # Enumerate every regular commutative scalar normal form, including
    # graph supports with odd cycles. Such graphs must all collapse to TOP.
    top = bytes([INF]) * 6**n
    seen = {top: ('TOP',)}
    tested = 0
    collapsed = 0
    for ell in range(n+1):
        for L in combinations(range(n), ell):
            remaining = tuple(v for v in range(n) if v not in L)
            all_edges = list(combinations(remaining, 2))
            for mask in range(1 << len(all_edges)):
                E = tuple(all_edges[i] for i in range(len(all_edges))
                          if (mask >> i) & 1)
                if not L and not E:
                    continue
                tested += 1
                s = scalar_signature(n, L, E)
                is_bip = bipartite(n, E)
                assert (s == top) == (not is_bip), (n, L, E)
                if is_bip:
                    assert s not in seen, (n, L, E, seen.get(s))
                    seen[s] = (L, E)
                else:
                    collapsed += 1
    return len(seen), tested, collapsed


def main():
    Bvals = recurrent_bipartite_counts(8)
    direct = direct_bipartite_counts(5)
    assert Bvals[:len(direct)] == direct
    assert Bvals[:9] == [1,1,2,7,41,376,5177,103237,2922446]
    scalar_expected = [2,5,17,86,677,8225,149102,3917681]
    matrix_expected = [3,21,567,67689,33887403,68921796861,
                       563431696713567,18451249599365935569]
    for r in range(1,9):
        scalar = sum(comb(r,ell) * Bvals[r-ell] for ell in range(r+1))
        matrix = sum(comb(r,ell) * 2**((r-ell)**2) for ell in range(r+1))
        assert scalar == scalar_expected[r-1], (r,scalar)
        assert matrix == matrix_expected[r-1], (r,matrix)
        if r <= 4:
            direct_count, tested, collapsed = check_normal_forms(r)
            assert direct_count == scalar, (r,direct_count,scalar)
            print(f'r={r}: scalar={scalar}; matrix={matrix}; tested={tested}; collapsed={collapsed}')
        else:
            print(f'r={r}: scalar={scalar}; matrix={matrix}')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
