"""Finite check of odd-multiplicity reflection dichotomy for perfect necklaces.

Usage: python verify.py
"""
from itertools import product


def perfect(word, q, k, n):
    L = len(word)
    if L != n * q**k:
        return False
    found = {}
    for i in range(L):
        key = tuple(word[(i + j) % L] for j in range(k))
        found.setdefault(key, []).append(i % n)
    return len(found) == q**k and all(
        len(starts) == n and len(set(starts)) == n for starts in found.values()
    )


def axes(word):
    L = len(word)
    return [c for c in range(L) if all(word[i] == word[(c-i) % L] for i in range(L))]


def test():
    configurations = [(2, 1, n) for n in range(1, 6)]
    configurations += [(2, 2, n) for n in range(1, 4)]
    configurations += [(2, 3, n) for n in range(1, 3)]
    configurations += [(3, 1, n) for n in range(1, 3)]
    configurations += [(3, 2, 1), (4, 1, 1)]
    examined = 0
    perfect_count = 0
    symmetric_count = 0
    for q, k, n in configurations:
        L = n * q**k
        sym = 0
        for seq in product(range(q), repeat=L):
            examined += 1
            if not perfect(seq, q, k, n):
                continue
            perfect_count += 1
            ax = axes(seq)
            if ax:
                sym += 1
                symmetric_count += 1
                if n % 2 == 0:
                    assert all((c-k+1) % 2 == 1 for c in ax), (q,k,n,seq,ax)
                else:
                    assert q == 2 and k <= 2, (q,k,n,seq,ax)
        if n % 2 == 1:
            assert (sym > 0) == (q == 2 and k <= 2), (q,k,n,sym)
        print('q=%d k=%d n=%d L=%d symmetric_labeled=%d' % (q,k,n,L,sym))
    for n in range(1, 20, 2):
        for k, block in ((1, (0,1)), (2, (0,0,1,1))):
            seq = block*n
            assert perfect(seq, 2, k, n) and axes(seq), (n,k)
    even_witness = tuple(map(int, '0001011100111010'))
    assert perfect(even_witness,2,3,2) and axes(even_witness)
    print('VERIFY_OK configurations=%d words=%d perfect_labeled=%d symmetric_labeled=%d witnesses=21' % (
        len(configurations),examined,perfect_count,symmetric_count))


if __name__ == '__main__':
    test()
