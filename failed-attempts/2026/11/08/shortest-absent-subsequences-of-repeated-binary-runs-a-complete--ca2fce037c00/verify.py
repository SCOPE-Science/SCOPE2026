#!/usr/bin/env python3
"""Checks a classification of shortest absent subsequences of repeated binary runs.

Run: python3 verify.py
No dependencies outside Python's standard library.
"""
from itertools import product, groupby
from functools import lru_cache


def subsequence(u, w):
    at = 0
    for letter in u:
        at = w.find(letter, at)
        if at < 0:
            return False
        at += 1
    return True


def run_index(u, a, b):
    blocks = [(c, len(tuple(g))) for c, g in groupby(u)]
    return int(blocks[0][0] == '1') + len(blocks)-1 + 2*sum(
        (length+((a if c == '0' else b)-1)) // (a if c == '0' else b) - 1
        for c, length in blocks
    )


def expected(u, a, b, m):
    if a == b == 1:
        return (len(u) == m + 1 and '01' not in u)
    if a == 1:
        return len(u) == m + 1 and (u == '0'*(m+1) or u == '1'+'0'*m)
    if b == 1:
        return len(u) == m + 1 and (u == '1'*(m+1) or u == '1'*m+'0')
    if len(u) != 2*m or not u.startswith('1'):
        return False
    return all((length % 2 == 1 if (a if c == '0' else b) == 2 else length == 1)
               for c, length in ((c, len(tuple(g))) for c, g in groupby(u)))


def fibonacci(n):
    x, y = 0, 1
    for _ in range(n):
        x, y = y, x+y
    return x


def expected_count(a, b, m):
    if a == b == 1:
        return m+2
    if min(a, b) == 1:
        return 2
    if a == b == 2:
        return fibonacci(2*m)
    if min(a, b) == 2:
        return 2**(m-1)
    return 1


def count_dp(w, k):
    # Deterministic greedy-subsequence automaton, one state per prefix length.
    nxt = [[len(w)]*2 for _ in range(len(w)+1)]
    for p in range(len(w)-1,-1,-1):
        nxt[p] = nxt[p+1][:]
        nxt[p][int(w[p])] = p
    dp={0:1}
    for _ in range(k):
        nd={}
        for p, count in dp.items():
            for c in (0, 1):
                v=nxt[p][c]
                if v < len(w):
                    nd[v+1]=nd.get(v+1, 0)+count
        dp=nd
    return (1 << k)-sum(dp.values())


def main():
    small_cases=0
    patterns=0
    for a in range(1,6):
        for b in range(1,6):
            for m in range(1,8):
                word=('0'*a+'1'*b)*m
                k=m+1 if min(a,b)==1 else 2*m
                missing=[]
                for n in range(k):
                    # Every shorter word must occur (index of universality).
                    if n == k-1:
                        for p in product('01', repeat=n):
                            assert subsequence(''.join(p), word), (a,b,m,n,p)
                for tup in product('01', repeat=k):
                    u=''.join(tup)
                    absent=not subsequence(u,word)
                    by_runs=run_index(u,a,b)>2*m-1
                    by_theorem=expected(u,a,b,m)
                    assert absent == by_runs == by_theorem, (a,b,m,u,absent,by_runs,by_theorem)
                    if absent: missing.append(u)
                    patterns += 1
                assert len(missing)==expected_count(a,b,m),(a,b,m,len(missing))
                assert count_dp(word,k)==len(missing),(a,b,m)
                small_cases += 1
    # Dynamic verification at larger exponents without exhaustive enumeration.
    large_cases=0
    for a,b in [(1,1),(1,3),(4,1),(2,2),(2,5),(5,2),(3,4)]:
        for m in (8,10,12,16,20,30,40):
            word=('0'*a+'1'*b)*m
            k=m+1 if min(a,b)==1 else 2*m
            assert count_dp(word,k)==expected_count(a,b,m),(a,b,m)
            large_cases += 1
    print('RUN_BLOCK_SAS_VERIFY_OK',small_cases,patterns,large_cases)


if __name__=='__main__':
    main()
