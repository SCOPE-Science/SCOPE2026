#!/usr/bin/env python3
"""Independent exhaustive state-space check of majority dynamics on paired cliques."""
from math import comb


def step(bits, n):
    # Update using independently specified open-neighbor masks.
    output = 0
    for v in range(2 * n):
        partner = v + n if v < n else v - n
        start = 0 if v < n else n
        neighbor_mask = (((1 << n) - 1) << start) ^ (1 << v) ^ (1 << partner)
        plus = (bits & neighbor_mask).bit_count()
        old = (bits >> v) & 1
        new = 1 if 2 * plus > n else (0 if 2 * plus < n else old)
        output |= new << v
    return output


def expected(n):
    if n % 2 == 0:
        z = comb(n, n // 2)
        return (4 + z, z * (z - 1), z * (z - 1), 1 if n == 2 else 2)
    return (4, (n + 3) * comb(n, (n - 1) // 2), (n + 3) * comb(n, (n - 1) // 2) + 2 * n * (n - 1) * comb(n - 2, (n - 3) // 2), 2 if n == 3 else 3)


def run():
    tested = 0
    for n in range(2, 9):
        fixed = two = eventual_two = 0
        max_entry = 0
        for z in range(1 << (2 * n)):
            tested += 1
            a = z
            entry = None
            for t in range(5):
                if step(step(a, n), n) == a:
                    entry = t
                    break
                a = step(a, n)
            assert entry is not None, (n, z, 'unexpected long transient')
            max_entry = max(max_entry, entry)
            if step(a, n) != a:
                eventual_two += 1
                assert entry <= 1, (n, z, entry, 'late oscillation')
            if entry == 0:
                if step(z, n) == z:
                    fixed += 1
                else:
                    two += 1
        goal = expected(n)
        assert (fixed, two, eventual_two, max_entry) == goal, (n, (fixed, two, eventual_two, max_entry), goal)
        print(f'n={n}: fixed={fixed}, primitive_two={two}, eventual_two={eventual_two}, max_entry={max_entry} OK')
    print(f'PASS; {tested} initial configurations checked exhaustively')

if __name__ == '__main__':
    run()
