"""Independent row-pattern enumerator for three pencil-balanced 5x5 masks.

Run: python3 line_incidence_checker.py
Only integer operations are used. Each selected row pattern is a subset of
five columns; column and broken-diagonal sums are checked directly.
"""
from itertools import combinations, permutations, product
from math import comb

P = 5
assert 5 == P
for k, want_pair, want_triple in ((1, 120, 15), (2, 2040, 130)):
    choices = [tuple(c) for c in combinations(range(P), k)]
    pairs = triples = 0
    for selected in product(choices, repeat=P):
        columns = [0] * P
        diagonals = [0] * P
        for x, ys in enumerate(selected):
            for y in ys:
                columns[y] += 1
                diagonals[(x + y) % P] += 1
        if all(z == k for z in columns):
            pairs += 1
            if all(z == k for z in diagonals):
                triples += 1
    print(f'weight={5*k} two fixed balanced directions={pairs} three={triples}')
    assert (pairs, triples) == (want_pair, want_triple)

# For a fixed subset of t parallel pencils, use 3-transitivity of PGL(2,5).
# The following complete intersection counts apply to any t-pencil set.
N = {
    5:  [comb(25, 5), 5**5, 120, 15, 10, 5, 0],
    10: [comb(25, 10), comb(5, 2)**5, 2040, 130, 20, 10, 0],
}

def exact_hist(w):
    a = N[w]
    return {25 - 4*k: sum((-1)**(t-k)*comb(t,k)*comb(6,t)*a[t]
                              for t in range(k, 7)) for k in range(7)}

for w in (5,10):
    hist = exact_hist(w)
    print(f'weight={w} ranks:', {r: c for r,c in sorted(hist.items()) if c})
    assert sum(hist.values()) == comb(25, w)

combined = {r: 2*(exact_hist(5)[r] + exact_hist(10)[r])
            for r in exact_hist(5)}
not_divisible_5 = 2**25 - sum(comb(25, w) for w in range(0,26,5))
combined[25] += not_divisible_5
combined[1] = 1  # the full 25-point mask
combined[0] = 1  # the zero mask
expected = {0:1,1:1,5:180,13:4000,17:51000,21:1122600,25:32376650}
assert {r:c for r,c in sorted(combined.items()) if c} == expected
print('complete rank census:', expected)
print('total:', sum(expected.values()))
assert sum(expected.values()) == 2**25
