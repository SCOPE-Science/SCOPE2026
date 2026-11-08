#!/usr/bin/env python3
"""Independent exhaustive cyclic-word census and difference-word checks.

Uses Python standard library only. The numerical tests do not replace the proof.
"""
from collections import Counter


def rotations(w):
    return [w[j:] + w[:j] for j in range(len(w))]


def cyclic_windows(w, m):
    L = len(w)
    return [tuple(w[(i+j) % L] for j in range(m)) for i in range(L)]


def all_binary_cycles(n):
    L = (1 << (n-1)) - 1
    nwin_mask = (1 << n) - 1
    cycles = set()
    words = 0
    for v in range(1 << L):
        w = tuple((v >> j) & 1 for j in range(L))
        patterns = [sum(w[(i+j)%L] << (n-1-j) for j in range(n)) for i in range(L)]
        canonical = [min(p, p ^ nwin_mask) for p in patterns]
        if 0 in canonical or len(set(canonical)) != L:
            continue
        words += 1
        allc = rotations(w) + rotations(tuple(1-x for x in w))
        cycles.add(min(allc))
        d = tuple(w[j] ^ w[(j+1)%L] for j in range(L))
        assert sum(d) == (1 << (n-2))
        assert set(cyclic_windows(d, n-1)) == {
            tuple((x >> (n-2-j)) & 1 for j in range(n-1))
            for x in range(1, 1 << (n-1))
        }
    return words, len(cycles)


def main():
    for n in range(3, 6):
        words, cycles = all_binary_cycles(n)
        L = (1 << (n-1))-1
        predicted = 1 << ((1 << (n-2))-(n-1))
        assert cycles == predicted, (n, cycles, predicted)
        assert words == 2*L*cycles, (n,words, cycles)
        print(f'n={n} rooted_words={words} rotation_complement_classes={cycles} expected={predicted}')
    print('DIRECT_CENSUS_OK')


if __name__ == '__main__':
    main()
