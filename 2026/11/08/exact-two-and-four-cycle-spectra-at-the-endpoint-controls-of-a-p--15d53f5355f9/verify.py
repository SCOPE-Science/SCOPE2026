"""Exact finite consistency tests for the endpoint skew-tent hybrid cycle theorem.

The general theorem is proved symbolically in RESULT.md; finite tests are auxiliary.
"""
from collections import Counter


def skew(z: int, a: int, n: int) -> int:
    assert 0 < a < n and 0 <= z < n
    if z < a:
        return (n * (z + 1) + a - 1) // a - 1
    return n * (n - 1 - z) // (n - a)


def hybrid(z: int, a: int, n: int) -> int:
    return skew(z, a if z % 2 == 0 else n - a, n)


def cycle_census(a: int, n: int) -> Counter:
    unseen = set(range(n))
    counts = Counter()
    while unseen:
        start = min(unseen)
        z = start
        length = 0
        while z in unseen:
            unseen.remove(z)
            length += 1
            z = hybrid(z, a, n)
        assert z == start, (a, n, start, z)
        counts[length] += 1
    return counts


def verify() -> None:
    checked = 0
    for m in range(2, 15):
        n = 1 << m
        assert sorted(skew(z, 1, n) for z in range(n)) == list(range(n))
        assert sorted(skew(z, n - 1, n) for z in range(n)) == list(range(n))
        for z in range(n):
            assert skew(z, 1, n) == n - 1 - z
            assert skew(z, n - 1, n) == (z + 1) % n
        for a in (1, n - 1):
            orbit_counts = cycle_census(a, n)
            wanted = (Counter({2: 2, 4: (n - 4) // 4}) if a == 1
                      else Counter({4: n // 4}))
            assert orbit_counts == wanted, (m, a, orbit_counts, wanted)
            assert sum(k * v for k, v in orbit_counts.items()) == n
            for z in range(n):
                nxt = hybrid(z, a, n)
                assert nxt % 2 != z % 2
                twice = hybrid(nxt, a, n)
                expected_twice = ((-z if z % 2 == 0 else -2 - z) % n
                                  if a == 1 else
                                  ((-2 - z if z % 2 == 0 else -z) % n))
                assert twice == expected_twice
                four = z
                for _ in range(4):
                    four = hybrid(four, a, n)
                assert four == z
                checked += 1
            for t in range(1, 13):
                lhs = sum(1 for z in range(n)
                          if iterate(z, a, n, t) == z)
                rhs = sum(k * count for k, count in wanted.items() if t % k == 0)
                assert lhs == rhs
    print(f"VERIFY_OK m=2..14 endpoint_controls=26 checked_states={checked} "+
          "cycle_counts_and_fixed_point_spectra=exact")


def iterate(z: int, a: int, n: int, t: int) -> int:
    for _ in range(t):
        z = hybrid(z, a, n)
    return z


if __name__ == "__main__":
    verify()
