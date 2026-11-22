"""Exhaustive literal-word BFS for a rotation letter and a defect-one letter.

This checker uses bitmask power automata and a three-state monitor that
forbids any occurrence of three consecutive rotation letters.
No external packages are required. Run: python verify_full_bfs.py
"""
from collections import deque


def shortest(n):
    full = (1 << n) - 1
    # (image mask, terminal run of rotation letters)
    queue = deque([(full, 0, 0)])
    seen = {(full, 0)}
    while queue:
        mask, run, length = queue.popleft()
        if mask.bit_count() == 1:
            return length
        # a rotates every state by one.
        if run < 2:
            image_a = ((mask << 1) & full) | (mask >> (n - 1))
            key = (image_a, run + 1)
            if key not in seen:
                seen.add(key)
                queue.append((image_a, run + 1, length + 1))
        # b fixes all but n-1, which moves to 0.
        image_b = (mask & ~(1 << (n - 1))) | (1 if (mask >> (n - 1)) & 1 else 0)
        key = (image_b, 0)
        if key not in seen:
            seen.add(key)
            queue.append((image_b, 0, length + 1))
    raise AssertionError('No admissible reset word')


def formula(n):
    return (3 * n * n - 8 * n + 6) // 2


if __name__ == '__main__':
    for n in range(3, 15):
        actual = shortest(n)
        expected = formula(n)
        assert actual == expected, (n, actual, expected)
    print('PASS: literal subset/constraint BFS, all n=3..14')
