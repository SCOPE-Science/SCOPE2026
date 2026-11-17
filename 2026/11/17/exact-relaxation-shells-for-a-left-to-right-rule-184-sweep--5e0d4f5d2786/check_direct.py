"""Direct bitwise Rule 184 scan versus the closed run clock; standard library only."""
from collections import Counter

def sweep(x, n):
    a = [(x >> i) & 1 for i in range(n)]
    for i in range(n):
        left, center, right = a[(i - 1) % n], a[i], a[(i + 1) % n]
        a[i] = right if center else left
    return sum(bit << i for i, bit in enumerate(a))

def clock_from_runs(x, n):
    a = [(x >> i) & 1 for i in range(n)]
    if all(a) or not any(a):
        return 0
    runs = []
    i = 0
    while i < n:
        j = i + 1
        while j < n and a[j] == a[i]:
            j += 1
        if a[i]:
            runs.append((i, j, j - i))
        i = j
    if a[0] and a[-1]:
        return max([runs[0][2] + runs[-1][2] - 1]
                   + [r[2] for r in runs[1:-1]])
    if not(a[0] == 0 and a[-1] == 1):
        return max(r[2] for r in runs)
    if len(runs) == 1:
        return 1
    return max([runs[0][0] + runs[0][2] + runs[-1][2] - 1]
               + [r[2] for r in runs[1:-1]])

def trajectory_clock(x, n):
    current = x
    for t in range(n + 2):
        after = sweep(current, n)
        if after == current:
            assert current in (0, (1 << n) - 1)
            return t, current
        current = after
    raise AssertionError('unanticipated long transient')

if __name__ == '__main__':
    total = 0
    for n in range(3, 17):
        depths = Counter()
        targets = Counter()
        top_words = []
        for x in range(1 << n):
            expected = clock_from_runs(x, n)
            depth, target = trajectory_clock(x, n)
            assert depth == expected, (n, x, depth, expected)
            depths[depth] += 1
            targets[target] += 1
            if depth == n - 1:
                top_words.append(x)
            total += 1
        assert targets[(1 << n) - 1] == n
        assert targets[0] == (1 << n) - n
        assert top_words == [(1 << (n - 1)) - 1]
        assert depths[0] == 2
        print(f'n={n} basin_one={n} worst={n-1} extremizers={len(top_words)} '
              f'shells={",".join(str(depths[t]) for t in range(n))}')
    print(f'PASS direct states={total}')
