"""Exact binomial-weighted orbit census from two-class population representatives.

Run: python3 code/weighted_profiles.py
The permutation action within the clique and within the independent set
makes every (k,j) representative account for comb(c,k)*comb(s,j)
labelled initial configurations. This is separate from adjacency enumeration.
"""
from math import comb


def step(state, c, s):
    full_clique = (1 << c) - 1
    k = (state & full_clique).bit_count()
    j = (state >> c).bit_count()
    h = k + j
    n = c + s
    if 2 * h < n:
        core = 0
    elif 2 * h > n:
        core = full_clique
    else:
        core = (state ^ full_clique) & full_clique
    if 2 * k < c:
        leaf = 0
    elif 2 * k > c:
        leaf = (1 << s) - 1
    else:
        leaf = state >> c
    return core | (leaf << c)


def expected(c, s):
    first = int(s >= c)
    second = comb(c, (c - s) // 2) if c > s and (c - s) % 2 == 0 else 0
    third = comb(c, c // 2) * comb(s, s // 2) // 2 if (c % 2 == s % 2 == 0) else 0
    return 2, first + second + third


cases = checked_profiles = 0
for c in range(1, 31):
    for s in range(1, 31):
        fixed = periodic2 = 0
        for k in range(c + 1):
            for j in range(s + 1):
                x = (1 << k) - 1 | (((1 << j) - 1) << c)
                y = step(x, c, s)
                z = step(y, c, s)
                weight = comb(c, k) * comb(s, j)
                fixed += weight * (x == y)
                periodic2 += weight * (x == z)
                checked_profiles += 1
        assert (fixed, (periodic2 - fixed) // 2) == expected(c, s), (c, s, fixed, periodic2)
        cases += 1

# Independent explicit trajectory check for the three-update witness.
witnesses = 0
for c in range(4, 100):
    for s in range(3, c):
        if (c - s) % 2:
            continue
        k = (c - s) // 2 + 1
        j = s - 1
        start = ((1 << k) - 1) | (((1 << j) - 1) << c)
        chain = [start]
        for _ in range(5):
            chain.append(step(chain[-1], c, s))
        assert all(chain[t] != chain[t + 2] for t in range(3)), (c,s,chain)
        assert chain[3] == chain[4] == chain[5], (c,s,chain)
        witnesses += 1

print(f"PASS weighted canonical profiles: {cases} parameter pairs, {checked_profiles} exact population profiles")
print(f"PASS explicit sharp-three-step witnesses: {witnesses} parameter pairs")
