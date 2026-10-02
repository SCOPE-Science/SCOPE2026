#!/usr/bin/env python3
"""Exhaustive small-case verification for connected mutual visibility in rook graphs."""

CASES = [(2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]


def c4_free(mask, m, n):
    for i in range(m):
        for k in range(i + 1, m):
            common = 0
            for j in range(n):
                if ((mask >> (i*n + j)) & 1) and ((mask >> (k*n + j)) & 1):
                    common += 1
                    if common >= 2:
                        return False
    return True


def rook_connected(mask, m, n):
    cells = [(i, j) for i in range(m) for j in range(n)
             if (mask >> (i*n + j)) & 1]
    if len(cells) <= 1:
        return True
    seen = {cells[0]}
    stack = [cells[0]]
    while stack:
        i, j = stack.pop()
        for k, ell in cells:
            if (k, ell) not in seen and (i == k or j == ell):
                seen.add((k, ell))
                stack.append((k, ell))
    return len(seen) == len(cells)


def maximal_c4_free(mask, m, n):
    if not c4_free(mask, m, n):
        return False
    for bit in range(m*n):
        if not ((mask >> bit) & 1) and c4_free(mask | (1 << bit), m, n):
            return False
    return True


def direct_mutual_visibility(mask, m, n):
    cells = [(i, j) for i in range(m) for j in range(n)
             if (mask >> (i*n + j)) & 1]
    selected = set(cells)
    for a in range(len(cells)):
        i, j = cells[a]
        for b in range(a + 1, len(cells)):
            k, ell = cells[b]
            if i == k or j == ell:
                continue
            if (i, ell) in selected and (k, j) in selected:
                return False
    return True


def verify_case(m, n):
    ordinary = 0
    connected = 0
    maximal_count = 0
    disconnected_maximal = 0
    maximum_count = 0
    connected_maximum_count = 0

    good = []
    for mask in range(1 << (m*n)):
        c4 = c4_free(mask, m, n)
        mv = direct_mutual_visibility(mask, m, n)
        assert c4 == mv
        if not c4:
            continue
        e = mask.bit_count()
        ordinary = max(ordinary, e)
        if rook_connected(mask, m, n):
            connected = max(connected, e)
        if maximal_c4_free(mask, m, n):
            maximal_count += 1
            if not rook_connected(mask, m, n):
                disconnected_maximal += 1
        good.append(mask)

    for mask in good:
        if mask.bit_count() == ordinary:
            maximum_count += 1
            if rook_connected(mask, m, n):
                connected_maximum_count += 1

    assert ordinary == connected
    assert disconnected_maximal == 0
    assert maximum_count == connected_maximum_count
    return (ordinary, connected, maximal_count,
            disconnected_maximal, maximum_count, connected_maximum_count)


def main():
    print("m n  mu  mu_c  maximal  disconnected_maximal  maximum  connected_maximum")
    for m, n in CASES:
        vals = verify_case(m, n)
        print(m, n, *vals)
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
