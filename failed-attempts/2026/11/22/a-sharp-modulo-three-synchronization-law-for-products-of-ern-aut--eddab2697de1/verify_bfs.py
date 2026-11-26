"""Independent finite subset-graph BFS for common reset thresholds.
Run: python3 verify_bfs.py. No external packages.
"""
from collections import deque


def step(mask, size, letter):
    result = 0
    for state in range(size):
        if mask & (1 << state):
            if letter == 0:  # cyclic rotation
                target = (state + 1) % size
            else:  # one-point collapse
                target = 0 if state == size - 1 else state
            result |= 1 << target
    return result


def exact_threshold(n):
    start = ((1 << n) - 1, 7)
    queue = deque([(start, 0)])
    seen = {start}
    while queue:
        (x, y), dist = queue.popleft()
        if x.bit_count() == y.bit_count() == 1:
            return dist, len(seen)
        for letter in (0, 1):
            z = (step(x, n, letter), step(y, 3, letter))
            if z not in seen:
                seen.add(z)
                queue.append((z, dist + 1))
    raise AssertionError('Expected a synchronizing word')


def expected(n):
    return (n - 1) ** 2 + (n % 3 != 0)


def main():
    rows = []
    for n in range(4, 17):
        threshold, visited = exact_threshold(n)
        assert threshold == expected(n), (n, threshold, expected(n))
        rows.append((n, threshold, visited))
    print('BFS_OK', rows)


if __name__ == '__main__':
    main()
