#!/usr/bin/env python3
"""Reproduce exact singleton-extension counts and extremal shuffles.

The parameter poset is the disjoint union of two nonempty chains A and B.
A word in A,B specifies its distinguished linear extension.
"""
from itertools import combinations, product
from math import comb


def type_count_formula(word, a, b):
    i = j = 0
    total = 0
    for symbol in (None, *word):
        if symbol == 'A':
            i += 1
        elif symbol == 'B':
            j += 1
        d = i - j
        total += (a + 1) * (b + 1) + (a - b) * d - d*d
    return total


def type_count_direct(word):
    """Enumerate all ternary new-point relations and test every transitivity condition."""
    n = len(word)
    # Old strict order: positions sharing the same chain are comparable.
    old = [[i < j and word[i] == word[j] for j in range(n)]
           for i in range(n)]
    total = 0
    for gap in range(n + 1):
        for status in product((-1, 0, 1), repeat=n):
            # -1: old vertex below x; 0: incomparable; +1: x below old.
            if any((status[k] == -1 and k >= gap) or
                   (status[k] == 1 and k < gap) for k in range(n)):
                continue
            order = [[False]*(n + 1) for _ in range(n + 1)]
            for x in range(n):
                for y in range(n):
                    order[x][y] = old[x][y]
                if status[x] == -1:
                    order[x][n] = True
                if status[x] == 1:
                    order[n][x] = True
            if all(not (order[x][y] and order[y][z]) or order[x][z]
                   for x in range(n + 1)
                   for y in range(n + 1)
                   for z in range(n + 1)):
                total += 1
    return total


def q_positions(word):
    count = 0
    q = []
    for s in word:
        if s == 'A':
            count += 1
        else:
            q.append(count)
    return q


def type_count_defect(word, a, b):
    q = q_positions(word)
    n = a + b
    baseline = comb(n + 3, 3) + a*b
    return (baseline + 2*sum(t*(a-t) for t in q)
            + 2*sum(q[j]-q[i] for i in range(b) for j in range(i+1,b)))


def bounds(a, b):
    if a < b:
        a, b = b, a
    d = a-b
    n = a+b
    low = comb(n+3, 3) + a*b
    gap = b*(3*d*d+6*d*b+4*b*b-(4 if d%2==0 else 1))//6
    return low, low+gap


def expected_max(word, a, b):
    if a < b:
        word = ''.join('A' if x=='B' else 'B' for x in word)
        a, b = b, a
    d=a-b
    q=q_positions(word)
    if d%2:
        return all(2*q[j] == d-1+2*(j+1) for j in range(b))
    return all(abs(2*q[j]-(d-1+2*(j+1)))==1 for j in range(b))


def words(a,b):
    n=a+b
    for pos in combinations(range(n), a):
        mark=set(pos)
        yield ''.join('A' if t in mark else 'B' for t in range(n))


if __name__ == '__main__':
    words_total = 0
    direct_total = 0
    max_total = 0
    profiles = 0
    for a in range(1, 9):
        for b in range(1, 9):
            profiles += 1
            lo, hi = bounds(a,b)
            assert lo == type_count_formula('A'*a+'B'*b, a, b)
            assert lo == type_count_formula('B'*b+'A'*a, a, b)
            values=[]
            for w in words(a,b):
                t=type_count_formula(w,a,b)
                assert t == type_count_defect(w,a,b), (a,b,w,t)
                if a+b <= 7:
                    assert t == type_count_direct(w), (a,b,w,t)
                    direct_total += 1
                values.append((t,w))
                words_total += 1
            actual_lo=min(t for t,w in values)
            actual_hi=max(t for t,w in values)
            assert (actual_lo, actual_hi) == (lo,hi), (a,b,lo,hi,actual_lo,actual_hi)
            m=[w for t,w in values if t==lo]
            assert set(m)=={'A'*a+'B'*b, 'B'*b+'A'*a}
            h=[w for t,w in values if t==hi]
            assert all(expected_max(w,a,b) == (t==hi) for t,w in values)
            expected_count=(2**min(a,b)) if abs(a-b)%2==0 else 1
            assert len(h)==expected_count,(a,b,len(h),expected_count)
            max_total+=len(h)
    for m in range(1,100):
        lo,hi=bounds(m,m)
        assert hi-lo==2*m*(m*m-1)//3
    print('word_profiles:',profiles)
    print('shuffles_checked:',words_total)
    print('direct_ternary_cross_checks:',direct_total)
    print('maximizing_words_checked:',max_total)
    print('balanced_gap_formula: 1<=m<100')
    print('VERIFY_OK')
