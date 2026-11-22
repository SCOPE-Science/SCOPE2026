#!/usr/bin/env python3
"""Independent automaton/path-counting computation, not a partition test."""
from collections import defaultdict, Counter

P = 'abbab'

def enumerate_by_automaton(A, B):
    # Counts paths of length a+b through the 6-state greedy subsequence DFA,
    # with exact counts of a,b and scattered ab. State 5 is accepting.
    layer = {(0, 0, 0, 0): 1}
    for _ in range(A+B):
        following = defaultdict(int)
        for (a, b, c, s), multiplicity in layer.items():
            if a < A:
                nxt = s + (s < len(P) and P[s] == 'a')
                following[a+1, b, c, nxt] += multiplicity
            if b < B:
                nxt = s + (s < len(P) and P[s] == 'b')
                following[a, b+1, c+a, nxt] += multiplicity
        layer = following
    good = Counter()
    all_words = Counter()
    for (a, b, c, s), multiplicity in layer.items():
        assert (a, b) == (A, B)
        all_words[c] += multiplicity
        if s < len(P):
            good[c] += multiplicity
    return good, all_words

def bounded_partitions(A, B):
    # Gaussian recursion based on the first letter, independent from DFA state.
    from functools import lru_cache
    @lru_cache(None)
    def rec(a, b):
        if not a or not b:
            return (1,)
        x = rec(a-1, b)
        y = rec(a, b-1)
        out = [0]*(a*b+1)
        for c, v in enumerate(x):
            out[c+b] += v
        for c, v in enumerate(y):
            out[c] += v
        return tuple(out)
    return rec(A,B)

def closed_count(A, B, C):
    if C == 0:
        return 1
    return min(A,C) - ((C + B - 1)//B) + 1

def run():
    cases = 0
    for A in range(13):
        for B in range(13):
            good, all_words = enumerate_by_automaton(A, B)
            gaussian = bounded_partitions(A, B)
            for C in range(A*B+1):
                n = closed_count(A,B,C)
                assert good[C] == n, (A,B,C,good[C],n)
                assert all_words[C] == gaussian[C], (A,B,C,all_words[C],gaussian[C])
                assert 0 < gaussian[C]
                cases += 1
            total = 1 + A + (B-1)*A*(A+1)//2 if A and B else 1
            assert sum(good.values()) == total, (A,B,sum(good.values()),total)
            mx = A - (A+B-1)//B + 1 if A and B else 1
            assert max(good.values()) == mx, (A,B,max(good.values()),mx)
    print('DYNAMIC_OK', 'classes', cases, 'compositions', 13*13)

if __name__ == '__main__':
    run()
