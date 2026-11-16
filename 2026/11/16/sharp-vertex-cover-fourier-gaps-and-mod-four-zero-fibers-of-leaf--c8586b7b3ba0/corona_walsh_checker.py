#!/usr/bin/env python3
"""Exact integer tests of leaf-corona Walsh spectra and signed path continuants."""
from itertools import combinations, product


def adjacent_independent(S, edges):
    return all(not ((S >> i) & (S >> j) & 1) for i, j in edges)


def walsh_spectrum_of_corona(n, edges):
    N = 1 << (2 * n)
    a = [0] * N
    for x in range(1 << n):
        if not adjacent_independent(x, edges):
            continue
        admissible = ((1 << n) - 1) ^ x
        y = admissible
        while True:
            a[x | (y << n)] = 1
            if y == 0:
                break
            y = (y - 1) & admissible
    for step in (1 << k for k in range(2 * n)):
        for i in range(0, N, 2 * step):
            for j in range(i, i + step):
                u, v = a[j], a[j + step]
                a[j], a[j + step] = u + v, u - v
    return a


def independence_poly_signed(n, edges, signs):
    return sum((1 << (n - I.bit_count())) * (-1 if (I & signs).bit_count() % 2 else 1)
               for I in range(1 << n) if adjacent_independent(I, edges))


def closed_neighborhood(n, edges, B):
    N = 0
    for i, j in edges:
        if B >> i & 1:
            N |= 1 << j
        if B >> j & 1:
            N |= 1 << i
    return B | N


def formula_general(n, edges, a, b):
    if not adjacent_independent(b, edges):
        return 0
    closed = closed_neighborhood(n, edges, b)
    rem = [i for i in range(n) if not (closed >> i & 1)]
    renumber = {v: j for j, v in enumerate(rem)}
    rem_edges = [(renumber[i], renumber[j]) for i, j in edges if i in renumber and j in renumber]
    signs = sum(((a >> v) & 1) << j for j, v in enumerate(rem))
    nb = (closed ^ b).bit_count()
    return (-1 if (a & b).bit_count() % 2 else 1) * (1 << nb) * independence_poly_signed(len(rem), rem_edges, signs)


def p(s):
    if not s:
        return 1
    x, y = 1, 2 + s[0]
    for t in s[1:]:
        x, y = y, 2 * y + 2 * t * x
    return y


def v2(x):
    assert x != 0
    return (abs(x) & -abs(x)).bit_length() - 1


def test():
    graph_tests = 0
    coeffs = 0
    for n in range(1, 5):
        all_edges = list(combinations(range(n), 2))
        for edge_mask in range(1 << len(all_edges)):
            edges = [e for k, e in enumerate(all_edges) if (edge_mask >> k) & 1]
            spec = walsh_spectrum_of_corona(n, edges)
            alpha = max(I.bit_count() for I in range(1 << n) if adjacent_independent(I, edges))
            gap = 1 << (n - alpha)
            nz = [abs(w) for w in spec if w]
            assert min(nz) == gap
            assert all(w % gap == 0 for w in spec)
            for b in range(1 << n):
                for a in range(1 << n):
                    assert spec[a | (b << n)] == formula_general(n, edges, a, b)
                    coeffs += 1
            graph_tests += 1
    path_counts = []
    for n in range(1, 9):
        edges = [(i, i + 1) for i in range(n - 1)]
        spectrum = walsh_spectrum_of_corona(n, edges)
        rank = sum(w != 0 for w in spectrum)
        path_counts.append((n, rank))
        for b in range(1 << n):
            closed = closed_neighborhood(n, edges, b)
            rem = [i for i in range(n) if not (closed >> i & 1)]
            runs = []
            if rem:
                run = [rem[0]]
                for i in rem[1:]:
                    if i == run[-1] + 1:
                        run.append(i)
                    else:
                        runs.append(run)
                        run = [i]
                runs.append(run)
            valid_b = adjacent_independent(b, edges)
            resonant = any(len(run) % 4 == 2 for run in runs)
            nz = [spectrum[a | (b << n)] != 0 for a in range(1 << n)]
            if not valid_b:
                assert not any(nz)
            elif resonant:
                assert any(nz) and not all(nz)
            else:
                assert all(nz)
                common = (closed ^ b).bit_count() + sum(len(run) // 2 for run in runs)
                assert all(v2(spectrum[a | (b << n)]) == common for a in range(1 << n))
    pchecks = 0
    for length in range(0, 17):
        for s in product((-1, 1), repeat=length):
            v = p(s)
            if length % 4 != 2:
                assert v != 0 and v2(v) == length // 2
            else:
                assert v == 0 or v2(v) >= length // 2 + 1
            if s == (-1,) * length:
                assert (v == 0) == (length % 4 == 2)
            pchecks += 1
    print('LEAF_CORONA_WALSH_EXACT_PASS', 'graphs=', graph_tests,
          'graph_coefficients=', coeffs, 'signed_continuants=', pchecks,
          'path_ranks=', path_counts)

if __name__ == '__main__':
    test()
