#!/usr/bin/env python3
"""Independent bounded-gap enumeration and explicit edge-pivot connectivity."""
from itertools import combinations, product
from collections import deque

def weak_compositions(total, parts):
    if parts == 1:
        yield (total,)
    else:
        for x in range(total + 1):
            for rest in weak_compositions(total - x, parts - 1):
                yield (x,) + rest

def all_states(n):
    k, r = divmod(n, 4)
    states = set()
    for longs in range(min(k, r) + 1):
        for long_places in combinations(range(k), longs):
            lengths = tuple(2 if i in long_places else 1 for i in range(k))
            for gaps in weak_compositions(r - longs, k):
                for origin in range(n):
                    pos = origin
                    matching = []
                    for length, extra in zip(lengths, gaps):
                        matching.append(tuple(sorted((pos % n, (pos + length) % n))))
                        pos += length + 3 + extra
                    assert pos == origin + n
                    states.add(frozenset(matching))
    return states

def is_induced(n, matching):
    endpoints = list(matching)
    for i in range(len(endpoints)):
        for j in range(i + 1, len(endpoints)):
            if any((x-y) % n in (0, 1, 2, n-1, n-2)
                   for x in endpoints[i] for y in endpoints[j]):
                return False
    return True

def connected_components(n, states):
    remaining = set(states)
    sizes = []
    for root in list(states):
        if root not in remaining:
            continue
        q = deque([root]); remaining.remove(root); total = 0
        while q:
            cur = q.popleft(); total += 1
            for a, b in cur:
                for fixed in (a, b):
                    for shift in (1, 2, -1, -2):
                        new = (fixed + shift) % n
                        if new == fixed:
                            continue
                        candidate_edge = tuple(sorted((fixed, new)))
                        if candidate_edge == (a, b):
                            continue
                        dest = (cur - {(a, b)}) | {candidate_edge}
                        if dest in remaining:
                            remaining.remove(dest)
                            q.append(dest)
        sizes.append(total)
    return sorted(sizes)

def expected(n):
    k, r = divmod(n, 4)
    return (4, 2*n, 2*k*n, n*(4*k*k+2)//3)[r]

if __name__ == '__main__':
    for n in range(5, 48):
        states = all_states(n)
        count = expected(n)
        assert len(states) == count, (n, len(states), count)
        assert all(is_induced(n, state) for state in states)
        cc = connected_components(n, states)
        assert cc == ([1]*4 if n % 4 == 0 else [count]), (n,cc)
        print(f'n={n}: states={count}; components={len(cc)}')
    print('GAP_ENUMERATION_AND_PIVOT_OK')
