#!/usr/bin/env python3
"""Finite checks of cyclic factor-class inflation in sparse-marker fixed points."""
from collections import defaultdict


def fixed_point_prefix(k, size):
    w = "0"
    while len(w) < size:
        w = "".join("0" * (k-1) + ("1" if a == "0" else "0") for a in w)
    return w


def morph(k, u):
    return "".join("0" * (k-1) + ("1" if a == "0" else "0") for a in u)


def representative(u):
    return min(u[i:] + u[:i] for i in range(len(u)))


def classes(prefix, length, positions):
    out = defaultdict(set)
    for i in range(positions):
        u = prefix[i:i+length]
        if len(u) == length:
            out[representative(u)].add(u)
    return out


def main():
    for k in range(2, 7):
        prefix = fixed_point_prefix(k, 30000)
        for n in range(1, 15):
            source = classes(prefix, n, 8000)
            target = classes(prefix, k*n, 8000)
            induced = {representative(morph(k, u)): u for u in source}
            assert len(induced) == len(source), (k, n, "injective")
            assert set(induced) == set(target), (k, n, "surjective")
            for target_rep, source_rep in induced.items():
                expected_size = (1 if n == 1 and source_rep == "1"
                                 else k*len(source[source_rep]))
                assert len(target[target_rep]) == expected_size, (k,n,source_rep)
                assert target_rep.count("1") == n - source_rep.count("1")
        print("PASS k=", k, " n<=14", sep="")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
