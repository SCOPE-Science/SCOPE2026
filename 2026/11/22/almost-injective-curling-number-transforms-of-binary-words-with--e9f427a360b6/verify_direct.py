"""Direct suffix-power verification of an exact sparse curling transform theorem.
Run with Python 3, no third-party dependencies.
"""
from collections import defaultdict
from math import comb


def curling_number(prefix):
    n = len(prefix)
    best = 1
    for period in range(1, n // 2 + 1):
        copies = 1
        while (copies + 1) * period <= n and (
            prefix[n - (copies + 1) * period:n - copies * period]
            == prefix[n - period:n]
        ):
            copies += 1
        best = max(best, copies)
    return best


def observed(a, b, c):
    word = '0' * a + '1' + '0' * b + '1' + '0' * c
    return tuple(curling_number(word[:i]) for i in range(1, len(word) + 1))


def predicted(a, b, c):
    v = list(range(1, a + 1)) + [1] + list(range(1, b + 1))
    v.append(2 if a >= b else 1)
    if c:
        v.append(2 if b >= 1 and a >= b - 1 else 1)
        v.extend(range(2, c + 1))
    return tuple(v)


def exception_fibers(n):
    if n == 4:
        return {
            frozenset([(0, 0, 2), (2, 0, 0)]),
            frozenset([(0, 1, 1), (1, 1, 0)]),
            frozenset([(0, 2, 0), (1, 0, 1)]),
        }
    if n == 5:
        return {frozenset([(0, 1, 2), (1, 1, 1)])}
    if n == 6:
        return {frozenset([(2, 1, 1), (2, 2, 0)])}
    if n >= 7:
        return {
            frozenset([(n - 4, 1, 1), (n - 4, 2, 0)]),
            frozenset([(n - 5, 1, 2), (n - 5, 2, 1)]),
        }
    return set()


def run():
    checked = 0
    total_collisions = 0
    for n in range(2, 41):
        fibers = defaultdict(list)
        for a in range(n - 1):
            for b in range(n - 1 - a):
                c = n - 2 - a - b
                x = observed(a, b, c)
                y = predicted(a, b, c)
                assert x == y, (n, a, b, c, x, y)
                fibers[x].append((a, b, c))
                checked += 1
        collisions = {frozenset(v) for v in fibers.values() if len(v) > 1}
        assert collisions == exception_fibers(n), (n, collisions)
        expected_count = {2: 1, 3: 3, 4: 3, 5: 9, 6: 14}.get(n, comb(n, 2) - 2)
        assert len(fibers) == expected_count, n
        assert max(map(len, fibers.values())) <= 2
        total_collisions += len(collisions)
    print('PASS direct suffix-power implementation; n=2..40')
    print(f'inputs={checked}; doubleton_fibers={total_collisions}; all_fibers_leq_two=True')
    print('special_image_counts={2:1,3:3,4:3,5:9,6:14}; for n>=7 count=binom(n,2)-2')


if __name__ == '__main__':
    run()
