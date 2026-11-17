#!/usr/bin/env python3
"""Exact, self-contained integral-chain certificate for a projective-line word complex.

No nonstandard Python packages are required.  Words are cells, not unordered
simplices: deleting the j-th entry gives the incidence sign (-1)^j.
"""
from collections import Counter, defaultdict
from itertools import combinations, product

P = 5
POINTS = tuple(range(P)) + (P,)  # final label represents infinity
EXPECTED_CELLS = (6, 30, 120, 360, 300, 60)
EXPECTED_CANCELS = {6: 60, 5: 235, 4: 95, 3: 25, 2: 5}
EXPECTED_UNPAIRED = {1: 1, 2: 0, 3: 0, 4: 30, 5: 5, 6: 0}


def act(a, b, c, d, x):
    if x == P:
        return P if c == 0 else a * pow(c, -1, P) % P
    den = (c*x + d) % P
    return P if den == 0 else (a*x + b) * pow(den, -1, P) % P


def projective_group():
    group = set()
    square_determinant = set()
    for a, b, c, d in product(range(P), repeat=4):
        det = (a*d-b*c) % P
        if det not in (1, 4):
            continue
        perm = tuple(act(a, b, c, d, x) for x in POINTS)
        assert set(perm) == set(POINTS)
        square_determinant.add(perm)
        if det == 1:
            group.add(perm)
    # Every square-determinant matrix can be scaled to determinant one.
    assert group == square_determinant and len(group) == 60
    return group


def word_faces(group):
    faces = {}
    for k in range(1, 7):
        faces[k] = sorted({word for p in group for word in combinations(p, k)})
    assert tuple(len(faces[k]) for k in range(1, 7)) == EXPECTED_CELLS
    # There are no restrictions in lengths one through four.
    assert all(len(faces[k]) == 720 // __import__('math').factorial(6-k)
               for k in range(1, 5))
    return faces


def boundaries(faces):
    index = {k: {word: j for j, word in enumerate(faces[k])}
             for k in faces}
    out = {}
    for k in range(2, 7):
        columns = {}
        for j, word in enumerate(faces[k]):
            col = {}
            for h in range(k):
                tail = word[:h] + word[h+1:]
                row = index[k-1][tail]
                col[row] = col.get(row, 0) + (-1)**h
            assert len(col) == k and all(abs(v) == 1 for v in col.values())
            columns[j] = col
        out[k] = columns
    # Check the cellular chain-complex identity over the integers.
    for k in range(3, 7):
        for col in out[k].values():
            combined = {}
            for mid, v in col.items():
                for row, w in out[k-1][mid].items():
                    combined[row] = combined.get(row, 0) + v*w
            assert all(val == 0 for val in combined.values())
    return out


def exact_cancellations(columns, faces):
    """Cancel unit entries using integral basis operations, high degree first.

    A pivot entry +/-1 in d_k is a contractible two-generator summand.
    For each other column z with pivot-row coefficient t, replace z by
    z - (t/pivot) * pivot_column.  Delete the pivot column and row; also
    delete the associated lower-dimensional generator.  Because dimensions
    are processed from the top down, incoming differentials are already zero.
    All operations are integral unimodular basis changes.
    """
    active = {k: set(range(len(faces[k]))) for k in faces}
    cancelled = {}
    largest = 0
    for k in range(6, 1, -1):
        d = columns[k]
        count = 0
        while True:
            row_degrees = Counter(row for c in d.values() for row in c)
            choice = None
            for col_id, col in d.items():
                for row_id, coefficient in col.items():
                    if abs(coefficient) != 1:
                        continue
                    cost = ((len(col)-1)*(row_degrees[row_id]-1),
                            len(col)+row_degrees[row_id], col_id, row_id)
                    if choice is None or cost < choice[0]:
                        choice = (cost, col_id, row_id, coefficient)
            if choice is None:
                break
            _, col_id, row_id, pivot_sign = choice
            pivot_col = d[col_id]
            for other_id, other in d.items():
                if other_id == col_id:
                    continue
                val = other.get(row_id, 0)
                if val:
                    multiplier = val * pivot_sign  # pivot_sign = its own inverse
                    for r, w in pivot_col.items():
                        new = other.get(r, 0) - multiplier * w
                        if new:
                            other[r] = new
                            largest = max(largest, abs(new))
                        else:
                            other.pop(r, None)
                    assert row_id not in other
            del d[col_id]
            active[k].remove(col_id)
            active[k-1].remove(row_id)
            if k > 2:
                # Lower differential of the removed generator is omitted.
                columns[k-1].pop(row_id)
            count += 1
        assert not any(d.values()), (k, 'uncancelled nonzero differential')
        cancelled[k] = count
    assert cancelled == EXPECTED_CANCELS, cancelled
    assert {k: len(v) for k, v in active.items()} == EXPECTED_UNPAIRED
    assert all(not any(d.values()) for d in columns.values())
    return cancelled, {k: len(v) for k, v in active.items()}, largest


def rank_mod_prime(cols, prime):
    """A separate modular elimination cross-check of unreduced boundaries."""
    pivots = {}
    for col in cols.values():
        vector = {r: v % prime for r, v in col.items() if v % prime}
        while vector:
            r = max(vector)
            if r not in pivots:
                inv = pow(vector[r], -1, prime)
                pivots[r] = {u: (z*inv) % prime for u, z in vector.items()}
                break
            fac = vector[r]
            for u, z in pivots[r].items():
                v = (vector.get(u, 0) - fac*z) % prime
                if v:
                    vector[u] = v
                else:
                    vector.pop(u, None)
    return len(pivots)


def main():
    group = projective_group()
    faces = word_faces(group)
    raw = boundaries(faces)
    for prime in (2, 3, 5, 7):
        ranks = {k: rank_mod_prime(raw[k], prime) for k in range(2, 7)}
        assert ranks == EXPECTED_CANCELS, (prime, ranks)
    # Reconstruct so this exact calculation uses new integer dictionaries.
    collapsed, active, max_coefficient = exact_cancellations(boundaries(faces), faces)
    assert sum((-1)**(k-1) * len(faces[k]) for k in range(1, 7)) == -24
    assert sum((-1)**(k-1) * active[k] for k in range(1, 7)) == -24
    print('GROUP_ORDER', len(group))
    print('WORD_CELL_COUNTS', EXPECTED_CELLS)
    print('INTEGRAL_UNIT_PIVOTS', collapsed)
    print('REMAINING_ZERO_DIFFERENTIAL_CHAIN_GROUPS', active)
    print('MAX_ABSOLUTE_INTERMEDIATE_COEFFICIENT', max_coefficient)
    print('REDUCED_INTEGRAL_HOMOLOGY', {3: 'Z^30', 4: 'Z^5'})
    print('MODULAR_RANK_CHECKS', 'PASS for primes 2,3,5,7')
    print('PSL5_WORD_INTEGRAL_CERTIFICATE_PASS')


if __name__ == '__main__':
    main()
