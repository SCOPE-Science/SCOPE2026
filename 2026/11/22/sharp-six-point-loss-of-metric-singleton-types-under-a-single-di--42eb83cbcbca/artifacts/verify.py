"""Independent direct Katetov-distance vector checks for the six-site witnesses.
Run: python3 artifacts/verify.py
"""
from itertools import combinations, product

REPRESENTATIVES = (
    "111222211111111",
    "111222211111112",
    "111222211211112",
)


def type_counts(encoded):
    edges = list(combinations(range(6), 2))
    assert len(encoded) == len(edges)
    before = {(i, j): int(v) for (i, j), v in zip(edges, encoded)}
    after = dict(before)
    after[0, 1] = 3

    def is_metric(dist):
        for a, b, c in combinations(range(6), 3):
            x, y, z = dist[a, b], dist[a, c], dist[b, c]
            if max(x, y, z) > x + y + z - max(x, y, z):
                return False
        return True

    assert is_metric(before) and is_metric(after)

    def admissible(values, dist):
        return all(abs(values[i] - values[j]) <= d <= values[i] + values[j]
                   for (i, j), d in dist.items())

    total_before = sum(admissible(values, before)
                       for values in product((1, 2, 3), repeat=6))
    total_after = sum(admissible(values, after)
                      for values in product((1, 2, 3), repeat=6))
    old11 = sum(admissible((1, 1) + values, before)
                for values in product((1, 2, 3), repeat=4))
    new13 = sum(admissible((1, 3) + values, after)
                for values in product((1, 2, 3), repeat=4))
    new31 = sum(admissible((3, 1) + values, after)
                for values in product((1, 2, 3), repeat=4))
    assert total_after - total_before == new13 + new31 - old11
    return total_before, total_after, (old11, new13, new31)


for signature in REPRESENTATIVES:
    before, after, local = type_counts(signature)
    print(f"{signature} before={before} after={after} delta={after-before} "
          f"local={local[0]},{local[1]},{local[2]}")
    assert after - before == -2 and local == (16, 7, 7)

for p in range(1, 7):
    for q in range(1, 7):
        delta = 2 * (2**p + 2**q - 1) - 2**(p + q)
        assert delta == 2 - (2**p - 2) * (2**q - 2)
        assert (delta < 0) == (p >= 2 and q >= 2)
print("VERIFY_OK")
