#!/usr/bin/env python3
"""Exhaustive scattered-subsequence signatures of binary palindromes."""
from itertools import product, combinations
from collections import defaultdict

def palindrome_words(n):
    h=(n+1)//2
    for u in product('01',repeat=h):
        p=''.join(u)
        yield p + (p[::-1] if n%2==0 else p[:-1][::-1])

def direct_signature(word):
    result=[]
    for k in (1,2,3):
        targets=[''.join(x) for x in product('01',repeat=k)]
        tally=dict.fromkeys(targets,0)
        for positions in combinations(range(len(word)),k):
            key=''.join(word[i] for i in positions)
            tally[key]+=1
        result.extend(tally[t] for t in targets)
    return tuple(result)

def census():
    for n in range(1,15):
        fibers=defaultdict(list)
        for w in palindrome_words(n):
            fibers[direct_signature(w)].append(w)
        sizes=sorted(len(v) for v in fibers.values() if len(v)>1)
        print(f'{n}: words={2**((n+1)//2)} signatures={len(fibers)} collisions={sizes}')
        if n<14: assert not sizes
        else:
            assert sizes==[2]*6
            for v in sorted(v for v in fibers.values() if len(v)>1): print('PAIR',*v)
if __name__=='__main__': census()
