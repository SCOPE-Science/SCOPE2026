#!/usr/bin/env python3
"""Independent finite-state checks for cyclic/merging-letter reset costs.

Every search is on the complete reachable-subset power automaton.
A finite search corroborates, but does not prove, the all-n theorem.
"""
from collections import deque
from heapq import heappush, heappop


def neighbors(mask, n):
    universe = (1 << n) - 1
    via_a = ((mask << 1) | (mask >> (n - 1))) & universe
    via_b = (mask & ~(1 << (n - 1))) | ((mask >> (n - 1)) & 1)
    return via_a, via_b


def minimum_rotation_count(n):
    start = (1 << n) - 1
    queue = deque([start])
    dist = {start: 0}
    while queue:
        mask = queue.popleft()
        d = dist[mask]
        if mask.bit_count() == 1:
            return d
        na, nb = neighbors(mask, n)
        for nxt, cost in ((na, 1), (nb, 0)):
            nd = d + cost
            if nd < dist.get(nxt, 10**18):
                dist[nxt] = nd
                if cost:
                    queue.append(nxt)
                else:
                    queue.appendleft(nxt)
    raise AssertionError('not synchronizing')


def minimum_weight_and_count(n, ca, cb):
    start = (1 << n) - 1
    distances = {start: 0}
    counts = {start: 1}
    heap = [(0, start)]
    best = None
    answer_count = 0
    while heap:
        cost, mask = heappop(heap)
        if cost != distances[mask]:
            continue
        if best is not None and cost > best:
            break
        if mask.bit_count() == 1:
            best = cost
            answer_count += counts[mask]
            continue
        na, nb = neighbors(mask, n)
        for nxt, weight in ((na, ca), (nb, cb)):
            nd = cost + weight
            if nd < distances.get(nxt, 10**18):
                distances[nxt] = nd
                counts[nxt] = counts[mask]
                heappush(heap, (nd, nxt))
            elif nd == distances[nxt]:
                counts[nxt] += counts[mask]
    return best, answer_count


def explicit_reset(n):
    word = 'b' + ('a' * (n - 1) + 'b') * (n - 2)
    images = set(range(n))
    for ch in word:
        if ch == 'a':
            images = {(x + 1) % n for x in images}
        else:
            images = {0 if x == n-1 else x for x in images}
    assert images == {0}, (n, images)
    assert word.count('a') == (n - 1)*(n - 2)
    assert word.count('b') == n - 1


def main():
    tests = 0
    for n in range(2, 14):
        explicit_reset(n)
        assert minimum_rotation_count(n) == (n - 1)*(n - 2), n
        for ca, cb in ((1, 1), (1, 9), (9, 1), (3, 5), (17, 2)):
            cost, count = minimum_weight_and_count(n, ca, cb)
            expected = ca*(n - 1)*(n - 2) + cb*(n - 1)
            assert (cost, count) == (expected, 1), (n, ca, cb, cost, count, expected)
            tests += 1
    print('VERIFY_OK: 12 state sizes, 60 positive-cost searches, unique weighted optimum in each')

if __name__ == '__main__':
    main()
