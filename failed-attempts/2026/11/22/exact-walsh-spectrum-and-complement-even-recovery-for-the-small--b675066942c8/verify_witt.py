"""Exact finite verification of the small Witt hexad Walsh spectrum.

Python 3 standard library only; all calculations are integer arithmetic.
"""
from collections import Counter
from itertools import combinations, product
from math import comb

GENERATOR = (
    (1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1),
    (0, 1, 0, 0, 0, 0, 1, 0, 1, 2, 2, 1),
    (0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 2, 2),
    (0, 0, 0, 1, 0, 0, 1, 2, 1, 0, 1, 2),
    (0, 0, 0, 0, 1, 0, 1, 2, 2, 1, 0, 1),
    (0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 1, 0),
)
N = 12
FULL = (1 << N) - 1


def blocks():
    result = set()
    for coefficients in product(range(3), repeat=6):
        vector = [sum(coefficients[j] * GENERATOR[j][i] for j in range(6)) % 3
                  for i in range(N)]
        support = sum(1 << i for i, a in enumerate(vector) if a)
        if support.bit_count() == 6:
            result.add(support)
    return result


def predicted(mask, B):
    k = mask.bit_count()
    if k % 2:
        return 0
    k = min(k, 12-k)
    lambdas = (132, 66, 30, 12, 4, 1)
    total = sum((-2)**j * comb(k,j) * lambdas[j]
                for j in range(min(k,5)+1))
    if k == 6 and mask in B:
        total += 64
    return total


def fwht(vector):
    arr = list(vector)
    length = 1
    while length < len(arr):
        for pos in range(0,len(arr),2*length):
            for off in range(length):
                a, b = arr[pos+off], arr[pos+off+length]
                arr[pos+off] = a+b
                arr[pos+off+length] = a-b
        length *= 2
    return arr


def main():
    B = blocks()
    assert len(B) == 132
    assert all(FULL ^ x in B for x in B)
    incidence_counts = Counter()
    for five in combinations(range(N),5):
        mask = sum(1 << i for i in five)
        incidence_counts[sum(mask & b == mask for b in B)] += 1
    assert incidence_counts == {1: comb(12,5)}, incidence_counts
    for t in range(6):
        lam = comb(12-t,5-t) // comb(6-t,5-t)
        for I in combinations(range(N),t):
            mask = sum(1 << i for i in I)
            assert sum(b & mask == mask for b in B) == lam
    # Two independent exact transforms: direct character sums and FWHT.
    direct = [sum(1 if (s & b).bit_count() % 2 == 0 else -1 for b in B)
              for s in range(1 << N)]
    signal = [int(s in B) for s in range(1 << N)]
    fast = fwht(signal)
    assert direct == fast
    assert all(x == predicted(s, B) for s,x in enumerate(direct))
    observed = Counter(direct)
    assert observed == {-12:924,0:2048,4:990,52:132,132:2}, observed
    assert sum(observed[x] for x in observed if x > 0) == 1124
    assert sum(observed[x] for x in observed if x < 0) == 924
    assert min(abs(v) for v in direct if v) == 4
    assert max(abs(v) for v in direct) == 132
    assert all(direct[s] == direct[FULL ^ s] for s in range(1 << N))
    assert sum(m * (a*a) for a,m in observed.items()) == (1 << N) * 132
    print('PASS: S(5,6,12); 132 blocks; 4096 Walsh multipliers; '
          'spectrum -12:924, 0:2048, 4:990, 52:132, 132:2; '
          'rank 2048; nonzero gap 4; condition 33.')

if __name__ == '__main__':
    main()
