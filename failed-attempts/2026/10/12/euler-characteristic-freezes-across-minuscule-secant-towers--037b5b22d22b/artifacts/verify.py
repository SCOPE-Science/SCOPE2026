from itertools import combinations, product
from math import comb

type_a_checks = spin_checks = quadric_checks = 0

for n in range(2, 13):
    coeffs = [2**i for i in range(n)]
    for k in range(1, n):
        vals = [sum(coeffs[i] for i in I) for I in combinations(range(n), k)]
        assert len(vals) == comb(n, k)
        assert len(set(vals)) == len(vals)
        type_a_checks += 1

for n in range(4, 11):
    coeffs = [3**i for i in range(n)]
    vals = []
    for signs in product((-1, 1), repeat=n):
        if sum(1 for s in signs if s < 0) % 2 == 0:
            vals.append(sum(s*c for s, c in zip(signs, coeffs)))
    assert len(vals) == 2**(n-1)
    assert len(set(vals)) == len(vals)
    spin_checks += 1

for n in range(3, 21):
    coeffs = [2**i for i in range(n)]
    vals = coeffs + [-c for c in coeffs]
    assert len(vals) == 2*n
    assert len(set(vals)) == len(vals)
    quadric_checks += 1

print("VERIFY_OK", type_a_checks, spin_checks, quadric_checks)
