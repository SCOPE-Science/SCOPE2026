"""Independent exhaustive grain-channel graph verification for n <= 9."""
from collections import Counter


def channel_ball(x, n):
    ans = {x}
    for j in range(1, n):
        if ((x >> j) ^ (x >> (j - 1))) & 1:
            ans.add(x ^ (1 << j))
    return ans


def degree_formula(x, n):
    if n == 1:
        return 0
    bits = [(x >> j) & 1 for j in range(n)]
    d = [bits[j] ^ bits[j + 1] for j in range(n - 1)]
    k = sum(d)
    boundaries = sum(d[j] != d[j + 1] for j in range(n - 2))
    return (n - 1) + k * (n - k) - d[0] - boundaries


if __name__ == '__main__':
    for n in range(1, 10):
        words = range(1 << n)
        balls = [channel_ball(x, n) for x in words]
        degrees = []
        for x in words:
            deg = sum(x != y and not balls[x].isdisjoint(balls[y])
                      for y in words)
            assert deg == degree_formula(x, n), (n, x, deg)
            degrees.append(deg)
        edges = sum(degrees) // 2
        expected_edges = ((n - 1) * (n + 2) * (1 << (n - 3))
                          if n >= 3 else (2 if n == 2 else 0))
        assert edges == expected_edges
        expected_max = n - 2 + n * n // 4 if n >= 3 else n - 1
        assert max(degrees) == expected_max
        expected_count = (2 if n % 2 == 0 else 4) if n >= 3 else (1 << n)
        assert degrees.count(expected_max) == expected_count
        print(f'length={n} vertices={1 << n} edges={edges} '
              f'max_degree={expected_max} maxima={expected_count} '
              f'degree_histogram={sorted(Counter(degrees).items())}')
    print('PASS: direct confusability-ball comparison, degree law and exact finite corollaries.')
