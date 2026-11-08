#!/usr/bin/env python3
"""Independent finite checks for a cyclic-automaton extension theorem.

No third-party packages are needed. These checks are finite, not a proof for
all n; the proof uses a structural invariant of inverse transitions.
"""
from collections import Counter, deque
from itertools import product


def image(n, state, letter):
    if letter == 'a':
        return (state + 1) % n
    if letter == 'b':
        return 0 if state == n - 1 else state
    raise ValueError(letter)


def inverse(n, subset, word):
    # Compute from the full word's forward action, not via the proof's rules.
    return frozenset(
        q for q in range(n)
        if (lambda r: r in subset)(apply(n, q, word))
    )


def apply(n, state, word):
    for letter in word:
        state = image(n, state, letter)
    return state


def first_boundary(n, subset):
    return min(i for i in subset if (i - 1) % n not in subset)


def shortest_bfs(n, subset):
    """BFS in reverse-image subset graph, without using the proposed formula."""
    start = frozenset(subset)
    queue = deque([(start, 0)])
    visited = {start}
    while queue:
        s, depth = queue.popleft()
        if len(s) > len(start):
            return depth
        for letter in ('a', 'b'):
            nextset = frozenset(q for q in range(n) if image(n, q, letter) in s)
            if nextset not in visited:
                visited.add(nextset)
                queue.append((nextset, depth + 1))
    raise AssertionError('No extending word')


def test():
    bfs_cases = 0
    unique_cases = 0
    hist_cases = 0
    for n in range(3, 12):
        histogram = Counter()
        for mask in range(1, (1 << n) - 1):
            subset = frozenset(q for q in range(n) if mask & (1 << q))
            r = first_boundary(n, subset)
            target_len = r + 1
            assert shortest_bfs(n, subset) == target_len, (n, subset)
            assert len(inverse(n, subset, 'b' + 'a' * r)) > len(subset)
            histogram[target_len] += 1
            bfs_cases += 1
            if n <= 8:
                optimal = [
                    ''.join(word) for word in product('ab', repeat=target_len)
                    if len(inverse(n, subset, word)) > len(subset)
                ]
                assert optimal == ['b' + 'a' * r], (n, subset, optimal)
                unique_cases += 1
        for t in range(1, n + 1):
            expected = t * 2 ** (n - t - 1) if t < n else n - 1
            assert histogram[t] == expected, (n, t, histogram[t], expected)
            hist_cases += 1
    print('VERIFY_OK')
    print(f'bfs_exact_cases={bfs_cases}')
    print(f'unique_shortest_word_cases={unique_cases}')
    print(f'histogram_coefficients={hist_cases}')


if __name__ == '__main__':
    test()
