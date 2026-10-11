#!/usr/bin/env python3
"""Finite stress test for the complete-multipartite TxGraffiti equality theorem."""

def integer_partitions(n, max_part=None):
    if n == 0:
        yield ()
        return
    if max_part is None or max_part > n:
        max_part = n
    for first in range(max_part, 0, -1):
        for tail in integer_partitions(n-first, first):
            yield (first,) + tail


def degree_multiset(part_sizes):
    n = sum(part_sizes)
    d = []
    for s in part_sizes:
        d.extend([n-s] * s)
    return sorted(d)


def annihilation_number(degrees):
    edge_count = sum(degrees) // 2
    total = 0
    ans = 0
    for d in sorted(degrees):
        if total + d <= edge_count:
            total += d
            ans += 1
        else:
            break
    return ans


def havel_hakimi_residue(degrees):
    seq = sorted(degrees, reverse=True)
    while seq and seq[0] > 0:
        d = seq.pop(0)
        if d > len(seq):
            raise AssertionError("nongraphic sequence")
        for i in range(d):
            seq[i] -= 1
            if seq[i] < 0:
                raise AssertionError("nongraphic reduction")
        seq.sort(reverse=True)
    return len(seq)


def canonical_name(part_sizes):
    p = tuple(sorted(part_sizes, reverse=True))
    if p == (2,1): return "P3"
    if p == (1,1,1): return "K3"
    if p == (2,2): return "C4"
    if p == (1,1,1,1): return "K4"
    return None


def main():
    total_types = 0
    equality = []
    for n in range(2, 21):
        for p in integer_partitions(n):
            if len(p) < 2:
                continue
            total_types += 1
            deg = degree_multiset(p)
            a = annihilation_number(deg)
            R = havel_hakimi_residue(deg)
            alpha = max(p)
            Delta = max(deg)
            if a > Delta:
                raise AssertionError(("a>Delta", p, a, Delta))
            if Delta >= 2:
                eq = Delta * alpha == a + R
                expected = canonical_name(p) is not None
                if eq != expected:
                    raise AssertionError(("classification mismatch", p, alpha, a, R, Delta, eq, expected))
                if eq:
                    equality.append(p)
    if len(equality) != 4:
        raise AssertionError(("wrong equality count", equality))
    print(f"ALL CHECKS PASSED; multipartite_types={total_types}; max_order=20; equality_types={len(equality)}")

if __name__ == '__main__':
    main()
