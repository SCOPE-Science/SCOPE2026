"""Independent optimal adaptive signed-transcript gap on small permutation boards."""
from functools import lru_cache
from itertools import permutations
from math import factorial

for n in range(2, 5):
    perms = list(permutations(range(n)))
    signs = [1 if sum(p[i] > p[j] for i in range(n) for j in range(i+1, n)) % 2 == 0 else -1 for p in perms]
    qbits = []
    for i in range(n):
        for j in range(n):
            qbits.append(sum((1 << k) for k, p in enumerate(perms) if p[i] == j))
    full = (1 << len(perms)) - 1
    @lru_cache(None)
    def score(h, d):
        imbalance = abs(sum(signs[k] for k in range(len(perms)) if h >> k & 1))
        if d == 0:
            return imbalance
        out = imbalance
        for bit in qbits:
            a = h & bit
            b = h & ~bit
            if a and b:
                out = max(out, score(a, d-1) + score(b, d-1))
        return out
    assert score(full, n-2) == 0
    signed_total = score(full, n-1)
    assert signed_total == 2**(n-1), (n, signed_total)
    # Total variation is signed_total/factorial(n): each parity has n!/2 members.
    print(f'ADAPTIVE_n={n} depth_before={n-2} signed_total_before=0 depth_threshold={n-1} signed_total={signed_total} tv={signed_total}/{factorial(n)} PASS')
print('ADAPTIVE_ALL_PASS')
