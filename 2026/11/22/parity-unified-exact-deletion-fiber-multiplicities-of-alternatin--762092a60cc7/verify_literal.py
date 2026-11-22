"""Literal independent enumeration of alternating-prefix subsequence deletions.

Run: python3 verify_literal.py
Uses only Python's standard library.
"""
from collections import Counter
from itertools import product
from math import comb


def h(n):
    return ''.join(str(i % 2) for i in range(n))


def theorem_distribution(n, d):
    r = n - d
    ell = r // 2
    p = d % 2
    result = {}
    for bits in product((0, 1), repeat=ell):
        v = ''.join('10' if x else '01' for x in bits)
        if r % 2:
            v += str(p)
        chain = (0,) + bits + (p,)
        t = sum(chain[i] != chain[i+1] for i in range(len(chain)-1))
        mult = comb(ell + (d-t)//2, ell) if t <= d else 0
        if mult:
            result[v] = mult
    return result


def direct_all_n(n):
    host = h(n)
    table = [Counter() for _ in range(n+1)]
    for mask in range(1 << n):
        u = []
        v = []
        for i, letter in enumerate(host):
            (u if mask >> i & 1 else v).append(letter)
        d = len(u)
        if ''.join(u) == host[:d]:
            table[d][''.join(v)] += 1
    return table


def main():
    cases = 0
    distinct = 0
    positional = 0
    for n in range(19):
        direct = direct_all_n(n)
        for d in range(n+1):
            predicted = theorem_distribution(n, d)
            assert direct[d] == predicted, (n, d, direct[d], predicted)
            ell = (n-d)//2
            assert len(predicted) == sum(comb(ell, j) for j in range(min(d, ell)+1)), (n,d)
            cases += 1
            distinct += len(predicted)
            positional += sum(predicted.values())
    print('VERIFY_LITERAL_OK n=0..18 cases=%d distinct_cells=%d positional_embeddings=%d' % (cases, distinct, positional))


if __name__ == '__main__':
    main()
