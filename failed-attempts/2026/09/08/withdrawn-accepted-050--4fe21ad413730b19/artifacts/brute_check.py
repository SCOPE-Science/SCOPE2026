#!/usr/bin/env python3
"""Independent brute-force 2-abelian-cube checker (stdlib only, no prefix sums).

Direct definition check: for every end position e and arm length m, compare the
three consecutive blocks via first/last letters and explicit digram Counters.
Intentionally O(n^2*m) with no prefix-sum machinery, so it shares no code path
with verify.c. Usage: brute_check.py WORDFILE [MAXLEN]
Exit 0 + "OK ..." if cube-free; exit 3 + "CUBE at s=.. m=.." for first cube.
"""
import sys
from collections import Counter


def digram_counter(block):
    return Counter(block[i:i + 2] for i in range(len(block) - 1))


def first_cube(w):
    n = len(w)
    for e in range(3, n + 1):
        for m in range(1, e // 3 + 1):
            s = e - 3 * m
            A, B, C = w[s:s + m], w[s + m:s + 2 * m], w[s + 2 * m:e]
            if not (A[0] == B[0] == C[0]):
                continue
            if not (A[-1] == B[-1] == C[-1]):
                continue
            if m == 1:
                return (s, m)
            if digram_counter(A) == digram_counter(B) == digram_counter(C):
                return (s, m)
    return None


def main():
    with open(sys.argv[1]) as f:
        w = ''.join(ch for ch in f.read() if ch in '01')
    if len(sys.argv) > 2:
        w = w[:int(sys.argv[2])]
    r = first_cube(w)
    if r is None:
        print("OK: length %d 2-abelian-cube-free (brute force)" % len(w))
        return 0
    print("CUBE at s=%d m=%d (brute force)" % r)
    return 3


if __name__ == '__main__':
    sys.exit(main())
