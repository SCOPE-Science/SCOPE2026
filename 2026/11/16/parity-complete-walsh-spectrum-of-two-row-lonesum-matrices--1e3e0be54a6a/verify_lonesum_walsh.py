#!/usr/bin/env python3
"""Exact reproducibility checks for the 2-by-n binary lonesum Walsh theorem.

Only built-in Python integers are used.  Finite tests corroborate the proof,
but the all-n statement is established algebraically in RESULT.md.
"""

from collections import Counter
from math import comb


def is_lonesum_columns(word, n):
    seen_01 = seen_10 = False
    for j in range(n):
        a, b = (word >> (2*j)) & 1, (word >> (2*j+1)) & 1
        seen_01 |= (a, b) == (0, 1)
        seen_10 |= (a, b) == (1, 0)
    return not (seen_01 and seen_10)


def directed_acyclic(word, n):
    # The independent graph-theoretic test: topological elimination.
    # Two left vertices 0,1 and n right vertices 2,...,n+1.
    N = n + 2
    incoming = [0] * N
    edges = [[] for _ in range(N)]
    for j in range(n):
        for i in range(2):
            v = (word >> (2*j+i)) & 1
            src, dst = (i, j+2) if v else (j+2, i)
            edges[src].append(dst)
            incoming[dst] += 1
    stack = [i for i in range(N) if incoming[i] == 0]
    removed = 0
    while stack:
        src = stack.pop()
        removed += 1
        for dst in edges[src]:
            incoming[dst] -= 1
            if incoming[dst] == 0:
                stack.append(dst)
    return removed == N


def fwht(a):
    a = a[:]
    step = 1
    while step < len(a):
        for start in range(0, len(a), step*2):
            for i in range(start, start+step):
                x, y = a[i], a[i+step]
                a[i], a[i+step] = x+y, x-y
        step *= 2
    return a


def formula(freq, n):
    c00 = c01 = c10 = c11 = 0
    for j in range(n):
        a, b = (freq >> (2*j)) & 1, (freq >> (2*j+1)) & 1
        if (a,b) == (0,0): c00 += 1
        elif (a,b) == (0,1): c01 += 1
        elif (a,b) == (1,0): c10 += 1
        else: c11 += 1
    return 3**c00 * ((-1)**c10+(-1)**c01) - (2**n if c01+c10==0 else 0)


def histogram(n):
    # Includes zeros, and counts exact signed values without evaluating a transform.
    answer = Counter()
    for c00 in range(n+1):
        for c01 in range(n-c00+1):
            for c10 in range(n-c00-c01+1):
                c11 = n-c00-c01-c10
                multiplicity = comb(n,c00)*comb(n-c00,c01)*comb(n-c00-c01,c10)
                v = 3**c00*((-1)**c10+(-1)**c01)-(2**n if c01+c10==0 else 0)
                answer[v] += multiplicity
    return answer


def main():
    total_pairs=0
    for n in range(1,9):
        N = 1<<(2*n)
        indicator = [int(is_lonesum_columns(x,n)) for x in range(N)]
        if n<=5:
            for x in range(N):
                assert bool(indicator[x]) == directed_acyclic(x,n), (n,x)
        assert sum(indicator)==2*3**n-2**n
        coeff=fwht(indicator)
        assert Counter(coeff) == histogram(n)
        for b,w in enumerate(coeff):
            total_pairs+=1
            assert w == formula(b,n), (n,b,w,formula(b,n))
            if n >= 2:
                assert (w!=0) == ((b.bit_count()%2)==0), (n,b,w)
                if w: assert abs(w)>=2
            else:
                assert (w!=0)==(b==0)
        if n>=2:
            assert sum(w!=0 for w in coeff) == N//2
            assert min(abs(w) for w in coeff if w)!=0
            assert min(abs(w) for w in coeff if w)==2
            assert max(abs(w) for w in coeff)==2*3**n-2**n
    # Algebraic formula parity/support checks far beyond feasible full transforms.
    for n in (9,10,15,31,50,100):
        frequencies = [0, 3, (1<<(2*n))-1, 5, 10, 15, (1<<(2*n-1))|3]
        frequencies += [sum(1<<(2*j) for j in range(n))]
        for b in frequencies:
            w=formula(b,n)
            assert (w != 0) == (b.bit_count()%2==0)
    print(f"LONESUM_WALSH_EXACT_PASS n=1..8; {total_pairs} exact Walsh coefficients; graph cycle checks n<=5")

if __name__ == '__main__': main()
