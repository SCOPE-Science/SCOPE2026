#!/usr/bin/env python3
"""Finite checks for exact partition-cell action multiplicity."""
from collections import Counter
from itertools import product


def partitions(n):
    if n == 0:
        return
    def extend(seq, maximum):
        if len(seq) == n:
            yield tuple(seq)
        else:
            for a in range(maximum + 2):
                yield from extend(seq + [a], max(maximum, a))
    yield from extend([0], 0)


def verified_frame(parts):
    k = len(parts)
    r = len(parts[0])
    counts = [1 + max(p) for p in parts]
    cells = {}
    for x in range(r):
        key = tuple(p[x] for p in parts)
        cells.setdefault(key, []).append(x)
    if len(cells) != __import__('math').prod(counts):
        return None
    return cells


def needed(t, k):
    m = 1
    while m ** (k - 1) < t:
        m += 1
    return m


def check_frame(parts, cells):
    k = len(parts)
    t = max(map(len, cells.values()))
    m = needed(t, k)
    assert m ** (k - 1) >= t
    assert m == 1 or (m - 1) ** (k - 1) < t
    actions = [[(b, u) for b in range(max(p) + 1)
                for u in range(m)] for p in parts]
    observed = [{action: set() for action in acts} for acts in actions]
    for profile in product(*actions):
        key = tuple(action[0] for action in profile)
        members = cells[key]
        digits = [((profile[i][1] - profile[-1][1]) % m)
                  for i in range(k - 1)]
        code = 0
        for digit in digits:
            code = code * m + digit
        outcome = members[code % len(members)]
        for i, action in enumerate(profile):
            observed[i][action].add(outcome)
    for i, acts in enumerate(actions):
        for b, u in acts:
            expected = {x for x, v in enumerate(parts[i]) if v == b}
            assert observed[i][(b, u)] == expected, (parts, i, b, u)
    return m, t


def check_two_agent_coordinate_minima(parts, cells):
    assert len(parts) == 2
    pa, pb = parts
    a_blocks = 1 + max(pa)
    b_blocks = 1 + max(pb)
    row_need = [max(len(cells[(i, j)]) for j in range(b_blocks))
                for i in range(a_blocks)]
    col_need = [max(len(cells[(i, j)]) for i in range(a_blocks))
                for j in range(b_blocks)]
    row_actions = [(i, u) for i in range(a_blocks) for u in range(row_need[i])]
    col_actions = [(j, v) for j in range(b_blocks) for v in range(col_need[j])]
    r_seen = {a: set() for a in row_actions}
    c_seen = {b: set() for b in col_actions}
    for a, b in product(row_actions, col_actions):
        members = cells[(a[0], b[0])]
        outcome = members[(a[1] + b[1]) % len(members)]
        r_seen[a].add(outcome)
        c_seen[b].add(outcome)
    for i, u in row_actions:
        assert r_seen[(i, u)] == {x for x, v in enumerate(pa) if v == i}
    for j, v in col_actions:
        assert c_seen[(j, v)] == {x for x, u in enumerate(pb) if u == j}
    assert all(row_need[i] >= len(cells[(i, j)])
               for i in range(a_blocks) for j in range(b_blocks))
    assert all(col_need[j] >= len(cells[(i, j)])
               for i in range(a_blocks) for j in range(b_blocks))
    return sum(row_need), sum(col_need)


def main():
    total = 0
    saved = []
    for k, r_max in ((2, 6), (3, 5), (4, 4)):
        for r in range(1, r_max + 1):
            ps = list(partitions(r))
            good = 0
            for parts in product(ps, repeat=k):
                cells = verified_frame(parts)
                if cells is None:
                    continue
                check_frame(parts, cells)
                if k == 2:
                    check_two_agent_coordinate_minima(parts, cells)
                good += 1
            total += good
            saved.append((k, r, good))
    print('partition_cases', saved)
    print('valid_frames_checked', total)
    print('ALL_CHECKS_OK')


if __name__ == '__main__':
    main()
