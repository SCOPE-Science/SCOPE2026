from itertools import combinations
from math import comb


def span(generators):
    out = {0}
    for g in generators:
        out |= {x ^ g for x in tuple(out)}
    return out


def orbit_count(k, mode):
    pairs = list(combinations(range(k), 2))
    m = len(pairs)
    stars = []
    for v in range(k):
        mask = 0
        for i, pair in enumerate(pairs):
            if v in pair:
                mask |= 1 << i
        stars.append(mask)
    all_one = (1 << m) - 1
    generators = []
    if mode in ("switch", "both"):
        generators.extend(stars)
    if mode in ("global", "both") and k >= 2:
        generators.append(all_one)
    translations = span(generators)
    seen = set()
    count = 0
    for x in range(1 << m):
        if x in seen:
            continue
        count += 1
        seen |= {x ^ t for t in translations}
    return count


def expected(k, mode):
    m = comb(k, 2)
    if mode == "base":
        return 1 << m
    if mode == "global":
        return 1 if k <= 1 else 1 << (m - 1)
    if mode == "switch":
        return 1 if k == 0 else 1 << comb(k - 1, 2)
    if mode == "both":
        return 1 if k <= 2 else 1 << (comb(k - 1, 2) - 1)
    if mode == "sym":
        return 1
    raise ValueError(mode)


modes = ("base", "global", "switch", "both", "sym")
for k in range(7):
    for mode in modes:
        if mode in ("base", "sym"):
            got = expected(k, mode)
        else:
            got = orbit_count(k, mode)
        assert got == expected(k, mode), (k, mode, got, expected(k, mode))
    print(k, [expected(k, mode) for mode in modes])

S = [[0] * 8 for _ in range(8)]
S[0][0] = 1
for n in range(1, 8):
    for k in range(1, n + 1):
        S[n][k] = S[n - 1][k - 1] + k * S[n - 1][k]

for mode in modes:
    vals = [sum(S[n][k] * expected(k, mode) for k in range(n + 1)) for n in range(8)]
    print(mode, vals)

assert [sum(S[n][k] * expected(k, "base") for k in range(n + 1)) for n in range(5)] == [1, 1, 3, 15, 127]
assert [sum(S[n][k] * expected(k, "global") for k in range(n + 1)) for n in range(5)] == [1, 1, 2, 8, 64]
assert [sum(S[n][k] * expected(k, "switch") for k in range(n + 1)) for n in range(5)] == [1, 1, 2, 6, 28]
assert [sum(S[n][k] * expected(k, "both") for k in range(n + 1)) for n in range(5)] == [1, 1, 2, 5, 18]
assert [sum(S[n][k] * expected(k, "sym") for k in range(n + 1)) for n in range(5)] == [1, 1, 2, 5, 15]
print("VERIFY_OK")
