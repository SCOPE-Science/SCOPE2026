"""Finite quotient-cell checks for complete-graph Hom complexes.

The program checks the explicit oriented product-cell incidences, consecutive
boundary compositions, and the two-term difference-chain differential.
No external dependencies are required.
"""
from collections import defaultdict
from itertools import combinations, product
from math import comb


def compositions(total, parts):
    if parts == 1:
        if total >= 1:
            yield (total,)
        return
    for first in range(1, total - parts + 2):
        for tail in compositions(total - first, parts - 1):
            yield (first,) + tail


def branch(supports, n):
    lengths = [s[-1] for s in supports]
    return (sum(lengths) <= n - 2 or
            any(any(j not in s for j in range(1, s[-1]))
                for s in supports))


def quotient_cells(m, n):
    cells = defaultdict(list)
    for total in range(m, n + 1):
        for lengths in compositions(total, m):
            row_lists = []
            for ell in lengths:
                row_lists.append([s for k in range(1, ell + 1)
                                  for s in combinations(range(1, ell + 1), k)
                                  if s[-1] == ell])
            for supports in product(*row_lists):
                degree = sum(len(s) - 1 for s in supports)
                parities = (0,) if branch(supports, n) else (0, 1)
                for parity in parities:
                    cells[degree].append((supports, parity))
    return cells


def boundary(cell, n):
    supports, parity = cell
    lengths = [s[-1] for s in supports]
    row_offset = 0
    for i, s in enumerate(supports):
        if len(s) > 1:
            for j in range(len(s)):
                face = supports[:i] + (s[:j] + s[j + 1:],) + supports[i + 1:]
                if branch(face, n):
                    next_parity = 0
                else:
                    flip = sum(lengths[i + 1:]) % 2 if j == len(s) - 1 else 0
                    next_parity = parity ^ flip
                yield (face, next_parity), (-1) ** (row_offset + j)
        row_offset += len(s) - 1


def sparse_rank_modp(columns, p):
    pivots = {}
    for column in columns:
        current = {i: a % p for i, a in column.items() if a % p}
        while current:
            lead = max(current)
            if lead not in pivots:
                inverse = pow(current[lead], -1, p)
                pivots[lead] = {i: a * inverse % p for i, a in current.items()}
                break
            multiplier = current[lead]
            for i, a in pivots[lead].items():
                value = (current.get(i, 0) - multiplier * a) % p
                if value:
                    current[i] = value
                else:
                    current.pop(i, None)
    return len(pivots)


def check(m, n):
    cells = quotient_cells(m, n)
    d = n - m
    incidence = {}
    ranks = {2: {}, 3: {}, 5: {}}
    for k in range(1, d + 1):
        index = {c: j for j, c in enumerate(cells[k - 1])}
        cols = []
        for c in cells[k]:
            col = defaultdict(int)
            for f, sign in boundary(c, n):
                assert f in index, (m, n, c, f)
                col[index[f]] += sign
            cols.append({r: v for r, v in col.items() if v})
        incidence[k] = cols
        for p in ranks:
            ranks[p][k] = sparse_rank_modp(cols, p)
    for k in range(2, d + 1):
        for col in incidence[k]:
            comp = defaultdict(int)
            for j, a in col.items():
                for i, b in incidence[k - 1][j].items():
                    comp[i] += a * b
            assert all(v == 0 for v in comp.values()), (m, n, k, comp)
    expected_rank = comb(n - 2, m - 2)
    for p in ranks:
        betti = [len(cells[k]) - ranks[p].get(k, 0)
                 - ranks[p].get(k + 1, 0) for k in range(d + 1)]
        wanted = [1] + [0] * (d - 1) + [expected_rank]
        assert betti == wanted, (m, n, p, betti, wanted)
    # Independent combinatorial check of the signed unbranched relative matrix.
    # Exactly one unit pivot per (n-1)-composition occurs by increasing last part;
    # sorting rows by the last part makes this a triangular square submatrix.
    upper = list(compositions(n, m))
    lower = list(compositions(n - 1, m))
    rows = {b: i for i, b in enumerate(lower)}
    columns = []
    for a in upper:
        entries = {}
        for i in range(m):
            if a[i] > 1:
                b = tuple(a[j] - (j == i) for j in range(m))
                entries[rows[b]] = (-1) ** (sum(a[:i]) - i + a[i] - 1 +
                                              sum(a[i + 1:]))  # sign is a unit
        columns.append(entries)
    assert len(upper) - len(lower) == expected_rank
    ordered_lower = sorted(lower, key=lambda b: (b[-1], b))
    chosen_columns = [tuple(b[i] + (i == m - 1) for i in range(m))
                      for b in ordered_lower]
    assert len(set(chosen_columns)) == len(lower)
    row_order = {b: j for j, b in enumerate(ordered_lower)}
    for j, a in enumerate(chosen_columns):
        col = columns[upper.index(a)]
        assert col[rows[ordered_lower[j]]] in (-1, 1)
        assert all(row_order[lower[r]] >= j for r in col), (m, n, j)
    # This selected square submatrix is triangular over Z, with determinant +/-1.
    return len(cells), sum(len(v) for v in cells.values()), expected_rank


def main():
    tested = 0
    for m in range(2, 6):
        for n in range(m + 1, min(m + 5, 9)):
            degrees, cells, rank = check(m, n)
            print(f"m={m} n={n} degrees={degrees} quotient_cells={cells} top_rank={rank}")
            tested += 1
    print(f"HOM_ALTERNATING_QUOTIENT_BOUNDARY_PASS cases={tested}")


if __name__ == '__main__':
    main()
