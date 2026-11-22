#!/usr/bin/env python3
"""Independent arithmetic checks for Fibonacci-shifted semigroup gap-run formula.

Pure standard Python 3; run: python3 verify.py.
Finite tests are evidence only, not an infinite proof.
"""
from collections import Counter

F = [0, 1]
for _ in range(30):
    F.append(F[-1] + F[-2])


def zeckendorf_weight(x):
    weight = 0
    for index in range(len(F) - 1, 1, -1):
        if x >= F[index]:
            x -= F[index]
            weight += 1
    assert x == 0
    return weight


def predicted(a):
    count = Counter({F[a] - 1: 1})
    for j in range(3, a - 1):
        count[F[j] - 1] += F[a - j - 1]
    return count


def actual_semigroup(a):
    m = F[a]
    conductor = ((a - 1) // 2) * m
    limit = conductor + m
    generators = [m] + [m + F[j] for j in range(2, a)]
    member = bytearray(limit + 1)
    member[0] = 1
    for gen in generators:
        for n in range(gen, limit + 1):
            if member[n - gen]:
                member[n] = 1
    # Ensure this is the complete gap set (the last modulus row is filled).
    assert all(member[conductor:])
    runs = Counter()
    start = None
    for n in range(1, limit + 2):
        gap = n <= limit and not member[n]
        if gap and start is None:
            start = n
        if not gap and start is not None:
            runs[n - start] += 1
            start = None
    # Independent membership computation through Zeckendorf Apéry heights.
    for n in range(limit + 1):
        z = (n // m >= zeckendorf_weight(n % m))
        if z != bool(member[n]):
            raise AssertionError(('threshold failure', a, n, z, member[n]))
    return runs, limit + 1


def check_word_recursion(a):
    m = F[a]
    B = [zeckendorf_weight(x) for x in range(m)]
    X = [zeckendorf_weight(x) for x in range(F[a - 1])]
    Y = [zeckendorf_weight(x) + 1 for x in range(F[a - 2])]
    assert B == X + Y
    return len(B)


def main():
    tested_memberships = 0
    tested_heights = 0
    tested_blocks = 0
    for a in range(5, 25):
        tested_heights += check_word_recursion(a)
        obs, n = actual_semigroup(a)
        exp = predicted(a)
        if obs != exp:
            raise AssertionError(('histogram mismatch', a, obs, exp))
        assert sum(obs.values()) == F[a - 2]
        assert obs[1] == F[a - 4]
        assert sum(k * v for k, v in obs.items()) == sum((F[a - j - 1] * (F[j] - 1) for j in range(3, a - 1))) + F[a] - 1
        tested_memberships += n
        tested_blocks += sum(obs.values())
        if a in (5, 10, 16, 20, 24):
            print('a=%d multiplicity=%d run_count=%d histogram=%s' % (a, F[a], sum(obs.values()), sorted(obs.items())))
    print('PASS: a=5..24; %d direct membership decisions; %d word entries; %d gap blocks.'
          % (tested_memberships, tested_heights, tested_blocks))


if __name__ == '__main__':
    main()
