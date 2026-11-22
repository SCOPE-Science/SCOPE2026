#!/usr/bin/env python3
"""Independent direct enumeration of inclusion-minimal dominating sets on cycles.
Uses bitmasks, direct set-removal minimality, and full expansion/contraction neighbors.
No third-party packages required. Run: python verify_exhaustive.py
"""
from collections import Counter


def data(n):
    full = (1 << n) - 1
    adj = [(1 << ((i - 1) % n)) | (1 << ((i + 1) % n)) for i in range(n)]
    closed = [a | (1 << i) for i, a in enumerate(adj)]
    dominated = [0] * (1 << n)
    for s in range(1, 1 << n):
        bit = s & -s
        j = bit.bit_length() - 1
        dominated[s] = dominated[s ^ bit] | closed[j]
    bases = set()
    for s in range(1, 1 << n):
        if dominated[s] != full:
            continue
        if all(dominated[s ^ (1 << j)] != full for j in range(n) if s & (1 << j)):
            bases.add(s)
    degree = Counter()
    edge_count = 0
    for s in bases:
        neighbors = set()
        for v in range(n):
            if s & (1 << v):  # expansion: remove v and add 1 or 2 vacant neighbors
                avail = adj[v] & ~s
                t = avail
                while t:
                    target = (s ^ (1 << v)) | t
                    if target in bases:
                        neighbors.add(target)
                    t = (t - 1) & avail
            else:  # contraction: add v and remove 1 or 2 occupied neighbors
                avail = adj[v] & s
                t = avail
                while t:
                    target = (s | (1 << v)) ^ t
                    if target in bases:
                        neighbors.add(target)
                    t = (t - 1) & avail
        degree.update([len(neighbors)])
        edge_count += len(neighbors)
        if not neighbors:
            expected = n >= 8 and n % 4 == 0 and any(
                all(((s >> i) & 1) == (((0b0011) >> ((i - shift) % 4)) & 1)
                    for i in range(n)) for shift in range(4)
            )
            assert expected, (n, s, 'unexpected frozen configuration')
    expected_count = 4 if n >= 8 and n % 4 == 0 else 0
    assert degree[0] == expected_count, (n, degree[0], expected_count)
    return len(bases), edge_count // 2, degree[0]


def main():
    for n in range(3, 19):
        size, edges, isolated = data(n)
        print(f'n={n}: minimal_sets={size}, edges={edges}, isolated={isolated}')
    print('PASS: all 16 cycle orders, full move rule, all frozen states classified')


if __name__ == '__main__':
    main()
