"""Independent exact checks for Fourier projection onto spanning-tree vectors of cactus graphs.
Run: python3 cactus_fourier_checker.py. No external packages are needed.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def build_cactus(lengths, bridges):
    edges = []
    anchor = 0
    next_vertex = 1
    for i, length in enumerate(lengths):
        vertices = [anchor] + list(range(next_vertex, next_vertex + length - 1))
        next_vertex += length - 1
        edges.extend((vertices[j], vertices[(j + 1) % length]) for j in range(length))
        anchor = vertices[-1] if i % 2 == 0 else vertices[1]
    for _ in range(bridges):
        edges.append((anchor, next_vertex))
        anchor = next_vertex
        next_vertex += 1
    return next_vertex, edges


def spanning_tree_masks(n, edges):
    out = []
    for choices in combinations(range(len(edges)), n - 1):
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        acyclic = True
        for j in choices:
            a, b = edges[j]
            a, b = find(a), find(b)
            if a == b:
                acyclic = False
                break
            parent[a] = b
        if acyclic and len({find(v) for v in range(n)}) == 1:
            out.append(sum(1 << j for j in choices))
    return out


def transform_from_support(bits, edge_count):
    n = 1 << edge_count
    arr = [0] * n
    for bit in bits:
        arr[bit] = 1
    h = 1
    while h < n:
        for start in range(0, n, 2 * h):
            for i in range(start, start + h):
                u, v = arr[i], arr[i + h]
                arr[i], arr[i + h] = u + v, u - v
        h *= 2
    return arr


def closed_formula(lengths, bridges, freq):
    phase = 1
    p = 0
    for length in lengths:
        signs = [1 - 2 * ((freq >> (p + i)) & 1) for i in range(length)]
        phase *= (sum(signs) * __import__('math').prod(signs))
        p += length
    for i in range(bridges):
        phase *= 1 - 2 * ((freq >> (p + i)) & 1)
    return phase


def cycle_norm(length):
    return Fraction(sum(comb(length, k) * abs(length - 2 * k) for k in range(length+1)), 2 ** length)


def closed_norm(lengths):
    x = Fraction(1)
    for ell in lengths:
        x *= cycle_norm(ell)
    return x


def closed_rank(lengths, bridges):
    rank = 1 << bridges
    for ell in lengths:
        rank *= (1 << ell) - (comb(ell, ell // 2) if ell % 2 == 0 else 0)
    return rank


def alpha(m):
    return Fraction((2 * m + 1) * comb(2 * m, m), 4 ** m)


def extreme(n, r):
    if r == 0:
        return Fraction(1)
    k = (n - 1) // 2
    a, b = divmod(k, r)
    return alpha(a) ** (r - b) * alpha(a + 1) ** b


def configurations(n, r):
    def rec(left, slots, last):
        if slots == 0:
            yield ()
            return
        for ell in range(last, left - 2 * (slots-1)+2):
            if ell < 3:
                continue
            for tail in rec(left - (ell - 1), slots - 1, ell):
                yield (ell,) + tail
    yield from rec(n - 1, r, 3)


def main():
    cases = [([], 3), ([3], 0), ([4], 1), ([5], 0),
             ([3, 3], 0), ([3, 4], 0), ([3, 5], 1),
             ([4, 4], 0), ([3, 3, 3], 0), ([3, 4, 5], 0)]
    checked_coeffs = 0
    for lengths, bridges in cases:
        n, edges = build_cactus(lengths, bridges)
        assert len(edges) == sum(lengths) + bridges
        tree_masks = spanning_tree_masks(n, edges)
        assert len(tree_masks) == __import__('math').prod(lengths)
        vals = transform_from_support(tree_masks, len(edges))
        assert all(v == closed_formula(lengths, bridges, i) for i, v in enumerate(vals))
        assert sum(v != 0 for v in vals) == closed_rank(lengths, bridges)
        assert Fraction(sum(abs(v) for v in vals), len(vals)) == closed_norm(lengths)
        odd = all(x % 2 == 1 for x in lengths)
        if odd:
            assert min(abs(v) for v in vals) == 1
            assert max(abs(v) for v in vals) == __import__('math').prod(lengths)
        else:
            assert any(v == 0 for v in vals)
            assert min(abs(v) for v in vals if v) == 2 ** sum(x % 2 == 0 for x in lengths)
        checked_coeffs += len(vals)
    tested_partitions = 0
    for n in range(3, 25):
        k = (n - 1) // 2
        for r in range(1, k + 1):
            best = extreme(n, r)
            for lengths in configurations(n, r):
                tested_partitions += 1
                assert closed_norm(lengths) <= best
            assert best <= Fraction(3, 2) ** k
    for ell in range(3, 80):
        m = (ell - 1) // 2
        assert cycle_norm(ell) == alpha(m)
    print('CACTUS_FOURIER_ALL_EXACT_CHECKS_PASS')
    print('frequencies_checked=',checked_coeffs)
    print('extremal_integer_cycle_configurations_checked=',tested_partitions)

if __name__ == '__main__':
    main()
