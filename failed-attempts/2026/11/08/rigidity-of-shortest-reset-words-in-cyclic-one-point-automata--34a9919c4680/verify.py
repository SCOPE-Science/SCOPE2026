#!/usr/bin/env python3
"""Check the unique-shortest-reset-word theorem for finite parameter ranges."""
from collections import deque
from math import gcd


def step(n, r, subset, letter):
    mask = (1 << n) - 1
    if letter == 'a':
        return ((subset << 1) & mask) | (subset >> (n - 1))
    if letter == 'b':
        return (subset & ~1) | ((1 << r) if subset & 1 else 0)
    raise ValueError(letter)


def shortest_reset_statistics(n, r):
    """Independent breadth-first subset search, with shortest-path multiplicity."""
    full = (1 << n) - 1
    queue = deque([full])
    distance = {full: 0}
    multiplicity = {full: 1}
    while queue:
        s = queue.popleft()
        for symbol in 'ab':
            t = step(n, r, s, symbol)
            if t not in distance:
                distance[t] = distance[s] + 1
                multiplicity[t] = multiplicity[s]
                queue.append(t)
            elif distance[t] == distance[s] + 1:
                multiplicity[t] += multiplicity[s]
    goals = [s for s in distance if s.bit_count() == 1]
    if not goals:
        return None, 0
    best = min(distance[s] for s in goals)
    return best, sum(multiplicity[s] for s in goals if distance[s] == best)


def replay_optimal(n, r):
    full = (1 << n) - 1
    current = full
    for j in range(n - 1):
        current = step(n, r, current, 'b')
        if j < n - 2:
            for _ in range(n - r):
                current = step(n, r, current, 'a')
    return current


def main():
    count = 0
    for n in range(2, 13):
        for r in range(1, n):
            length, ways = shortest_reset_statistics(n, r)
            if gcd(n, r) == 1:
                expected = (n - 1) + (n - 2) * (n - r)
                assert (length, ways) == (expected, 1), (n, r, length, ways)
                assert replay_optimal(n, r) == (1 << r), (n, r)
            else:
                assert (length, ways) == (None, 0), (n, r, length, ways)
            count += 1
    large = 0
    for n in range(2, 51):
        for r in range(1, n):
            if gcd(n, r) == 1:
                assert replay_optimal(n, r) == (1 << r)
                large += 1
    print(f'VERIFY_OK BFS={count} witness_replays={large}')


if __name__ == '__main__':
    main()
