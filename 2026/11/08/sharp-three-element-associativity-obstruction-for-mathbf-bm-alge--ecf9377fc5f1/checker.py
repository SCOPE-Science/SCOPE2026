#!/usr/bin/env python3
"""Exact finite census of B/M combinatory algebras on at most three elements.

Uses only Python's standard library. Run: python3 checker.py
Every binary operation table on a fixed n-element set is enumerated; the
marked elements B and M are part of the structure and preserved by isomorphism.
"""
from itertools import permutations, product


def square_row(table, n):
    return tuple(table[i*n+i] for i in range(n))


def satisfies_b(table, n, b):
    # ((b*x)*y)*z = x*(y*z) for all x,y,z
    return all(table[table[table[b*n+x]*n+y]*n+z] ==
               table[x*n+table[y*n+z]]
               for x, y, z in product(range(n), repeat=3))


def satisfies_m(table, n, m):
    return all(table[m*n+x] == table[x*n+x] for x in range(n))


def associative(table, n):
    return all(table[table[x*n+y]*n+z] == table[x*n+table[y*n+z]]
               for x, y, z in product(range(n), repeat=3))


def transport(table, n, b, m, p):
    # Relabel x to p[x], including the two named constants.
    inv = [p.index(i) for i in range(n)]
    t = tuple(p[table[inv[i]*n+inv[j]]] for i in range(n) for j in range(n))
    return t, p[b], p[m]


def generated_by_marks(table, n, b, m):
    closure = {b, m}
    while True:
        enlarged = closure | {table[x*n+y] for x in closure for y in closure}
        if enlarged == closure:
            return len(closure) == n
        closure = enlarged


def census(n):
    group = tuple(permutations(range(n)))
    marked = []
    all_magmas_examined = 0
    for table in product(range(n), repeat=n*n):
        all_magmas_examined += 1
        # Independent direct tests of each distinguished symbol.
        bs = tuple(b for b in range(n) if satisfies_b(table, n, b))
        if not bs:
            continue
        ms = tuple(m for m in range(n) if satisfies_m(table, n, m))
        if not ms:
            continue
        assoc = associative(table, n)
        for b in bs:
            for m in ms:
                marked.append((table, b, m, assoc))
    assert all_magmas_examined == n**(n*n)
    canon = {}
    generated_keys = set()
    generated_labelled = 0
    generated_nonassoc_labelled = 0
    fixed = [0]*len(group)
    fixed_nonassoc = [0]*len(group)
    for table, b, m, assoc in marked:
        images = [transport(table, n, b, m, p) for p in group]
        key = min(images)
        if key in canon:
            assert canon[key] == assoc
        else:
            canon[key] = assoc
        if generated_by_marks(table, n, b, m):
            generated_keys.add(key)
            generated_labelled += 1
            generated_nonassoc_labelled += int(not assoc)
        for j, image in enumerate(images):
            if image == (table, b, m):
                fixed[j] += 1
                if not assoc:
                    fixed_nonassoc[j] += 1
    assert sum(fixed) == len(group)*len(canon)  # independent Burnside check
    nonassoc_keys = tuple(sorted(key for key, is_assoc in canon.items() if not is_assoc))
    assert sum(fixed_nonassoc) == len(group)*len(nonassoc_keys)
    return marked, canon, nonassoc_keys, fixed, fixed_nonassoc, (generated_labelled, len(generated_keys), generated_nonassoc_labelled, sum(not canon[k] for k in generated_keys)), sorted(k for k in generated_keys if not canon[k])


expected = {
  1: (1, 1, 0, 0),
  2: (14, 7, 0, 0),
  3: (204, 36, 36, 6),
}
results = {}
for n in (1, 2, 3):
    marked, canon, nonassoc_keys, fixed, fixed_nonassoc, gen_counts, gen_bad_keys = census(n)
    result = (len(marked), len(canon), sum(not a for _, _, _, a in marked), len(nonassoc_keys))
    assert result == expected[n], (n, result)
    expected_gen = {1:(1,1,0,0), 2:(8,4,0,0), 3:(42,7,6,1)}
    assert gen_counts == expected_gen[n], (n, gen_counts)
    results[n] = result
    print(f'n={n} labelled={result[0]} marked_isomorphism_classes={result[1]} '
          f'nonassociative_labelled={result[2]} nonassociative_classes={result[3]} '
          f'generated={gen_counts} fixed={fixed} fixed_nonassoc={fixed_nonassoc}')

# Canonical marked structures, by the B- and M-preserving symmetric-group action.
expected_canon = (
    ((0, 0, 0, 0, 0, 0, 0, 2, 0), 0, 0),
    ((0, 0, 0, 0, 0, 0, 0, 2, 0), 0, 1),
    ((0, 0, 0, 0, 0, 0, 0, 2, 0), 1, 0),
    ((0, 0, 0, 0, 0, 0, 0, 2, 0), 1, 1),
    ((0, 0, 0, 0, 0, 1, 0, 0, 1), 0, 1),
    ((0, 0, 0, 0, 0, 1, 0, 0, 1), 0, 2),
)
assert census(3)[2] == expected_canon
assert census(3)[6] == [expected_canon[5]]
for table, b, m in expected_canon:
    assert satisfies_b(table, 3, b) and satisfies_m(table, 3, m)
    assert not associative(table, 3)
    # In these minimal obstructions, 0 is an absorbing element and there
    # is no left identity (in agreement with finite BI rigidity).
    assert all(table[x] == 0 and table[3*x] == 0 for x in range(3))
    assert not any(all(table[3*i+j] == j for j in range(3)) for i in range(3))
    # The same algebra nevertheless contains a Y-element, as in the source theorem.
    assert any(all(table[3*y+x] == table[3*x+table[3*y+x]] for x in range(3))
               for y in range(3))

# Distinct underlying nonassociative magma types, disregarding marked symbols.
underlying = {row[0] for row in expected_canon}
assert len(underlying) == 2
canonical_unmarked = {
    min(tuple(p[table[p.index(i)*3+p.index(j)]]
              for i in range(3) for j in range(3))
        for p in permutations(range(3)))
    for table in underlying
}
assert len(canonical_unmarked) == 2  # the two shapes are not isomorphic even unmarked
for table in underlying:
    automorphisms = [p for p in permutations(range(3))
                    if all(p[table[i*3+j]] == table[p[i]*3+p[j]]
                           for i in range(3) for j in range(3))]
    assert automorphisms == [(0, 1, 2)]
print('BM_MINIMAL_NONASSOCIATIVE_CENSUS_OK')
