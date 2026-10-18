from functools import lru_cache

@lru_cache(None)
def partitions(n, min_part=1):
    if n == 0:
        return [()]
    out = []
    for first in range(min_part, n+1):
        for tail in partitions(n-first, first):
            out.append((first,)+tail)
    return out

def multiplicity(part, ell):
    return sum(1 for x in part if x == ell)

for p in range(0, 13):
    parts = partitions(p)
    for ell in range(2, 13):
        observed = max((multiplicity(part, ell) for part in parts), default=0)
        expected = p // ell
        assert observed == expected, (p, ell, observed, expected)

vectors = [(0,1,2,3), (5,7), (2,9,10), (12,12,12)]
for vec in vectors:
    P = max(vec, default=0)
    for ell in range(2, P+1):
        observed = sum(max(multiplicity(part, ell) for part in partitions(p)) for p in vec)
        expected = sum(p // ell for p in vec)
        assert observed == expected, (vec, ell, observed, expected)

print('VERIFY_OK: max partition exponent is sum_j floor(p_j/ell) for all tested p_j <= 12.')
