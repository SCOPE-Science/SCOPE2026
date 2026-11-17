#!/usr/bin/env python3
"""Finite independent checks for two length-two shortcuts in directed cycles.
Only ordinary combinatorial and chain-complex algorithms are used.
"""
from itertools import combinations
from collections import Counter


def faces_of_arcs(n, d, count):
    arcs = [(i, (i + 1) % n) for i in range(n)]
    if count >= 1:
        arcs.append((0, 2))
    if count >= 2:
        arcs.append((d, (d + 2) % n))
    m = len(arcs)
    faces = []
    for mask in range(1 << m):
        next_vertex = {}
        incoming = set()
        valid = True
        for j, (src, dst) in enumerate(arcs):
            if not ((mask >> j) & 1):
                continue
            if src in next_vertex or dst in incoming:
                valid = False
                break
            next_vertex[src] = dst
            incoming.add(dst)
        if not valid:
            continue
        for src in next_vertex:
            seen = set()
            cur = src
            while cur in next_vertex:
                if cur in seen:
                    valid = False
                    break
                seen.add(cur)
                cur = next_vertex[cur]
            if not valid:
                break
        if valid:
            faces.append(mask)
    return set(faces)


def expected_link(n, d):
    W = set(range(n)) - {d, d + 1}
    R = set(range(n)) - {0, 1, d, d + 1}
    Wmask = sum(1 << j for j in W)
    Rmask = sum(1 << j for j in R)
    ans = set()
    for mask in range(1 << n):
        if mask & ~Wmask or mask == Wmask:
            continue
        ans.add(mask)
        if not (mask & ~Rmask) and (d == 1 or mask != Rmask):
            ans.add(mask | (1 << n))
    return ans


def rank_mod_p(columns, p):
    pivots = {}
    for col in columns:
        col = dict(col)
        while col:
            k = max(col)
            if k not in pivots:
                inv = pow(col[k], -1, p)
                pivots[k] = {i: (v * inv) % p for i, v in col.items() if v % p}
                break
            fac = col[k]
            for i, v in pivots[k].items():
                new = (col.get(i, 0) - fac * v) % p
                if new:
                    col[i] = new
                else:
                    col.pop(i, None)
    return len(pivots)


def bettis_mod_p(faces, p):
    f = {}
    for mask in faces:
        f.setdefault(mask.bit_count(), []).append(mask)
    ranks = {}
    for size in range(1, max(f) + 1):
        to_index = {x: i for i, x in enumerate(f.get(size-1, []))}
        cols = []
        for mask in f.get(size, []):
            col = {}
            a = mask
            pos = 0
            while a:
                bit = a & -a
                a -= bit
                col[to_index[mask-bit]] = 1 if pos % 2 == 0 else p-1
                pos += 1
            cols.append(col)
        ranks[size] = rank_mod_p(cols, p)
    ranks[max(f)+1] = 0
    return {size-1: len(f[size]) - ranks[size] - ranks[size+1]
            for size in f if size > 0 and len(f[size]) - ranks[size] - ranks[size+1]}


def expected(n, d, count):
    if count == 0:
        return {n-2: 1}
    if count == 1:
        return {n-2: 1, n-3: 1}
    if d == 1:
        return {n-2: 1, n-3: 2}
    return {n-2: 1, n-3: 2, n-4: 1}


def main():
    ntests = 0
    ptests = 0
    total_faces = 0
    for n in range(6, 13):
        for d in range(1, n // 2 + 1):
            k0 = faces_of_arcs(n, d, 0)
            k1 = faces_of_arcs(n, d, 1)
            k2 = faces_of_arcs(n, d, 2)
            # Check both inclusions and exact links, without relying on rank calculations.
            assert k0 <= k1 <= k2
            actual_link = {m & ~(1 << (n+1)) for m in k2 if m & (1 << (n+1))}
            assert actual_link == expected_link(n, d), (n, d, "link")
            for count, complex_faces in enumerate((k0, k1, k2)):
                expected_chi = sum(((-1) ** i) * num for i, num in expected(n, d, count).items())
                actual_chi = sum((-1) ** (m.bit_count() - 1) for m in complex_faces)
                # Include empty face (dimension -1) and compare reduced Euler numbers.
                assert actual_chi == expected_chi, (n, d, count, actual_chi)
                ntests += 1
                total_faces += len(complex_faces)
            # More expensive independent boundary reductions for small cycles.
            if n <= 10:
                for count, complex_faces in enumerate((k0, k1, k2)):
                    for p in (2, 3):
                        assert bettis_mod_p(complex_faces, p) == expected(n, d, count), (n,d,count,p)
                        ptests += 1
    print(f"VERIFY_OK independent face/links/Euler cases={ntests}; modular boundary cases={ptests}; faces_examined={total_faces}")

if __name__ == "__main__":
    main()
