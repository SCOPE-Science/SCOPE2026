#!/usr/bin/env python3
"""Independent exact recursion versus Dyck-end decomposition for all short binary words."""
from functools import lru_cache
from itertools import product

def is_dyck(word):
    h=0
    for c in word:
        h += 1 if c=='a' else -1
        if h<0: return False
    return h==0

def end_counts(word):
    h=k=left_end=0
    for i,c in enumerate(word):
        h += 1 if c=='a' else -1
        if h<0: break
        if h==0:
            k += 1
            left_end=i+1
    h=l=right_len=0
    for i,c in enumerate(reversed(word)):
        h += 1 if c=='b' else -1
        if h<0: break
        if h==0:
            l += 1
            right_len=i+1
    return k,l,left_end,right_len

@lru_cache(maxsize=None)
def grundy(word):
    options=set()
    for j in range(2,len(word)+1,2):
        if is_dyck(word[:j]):
            options.add(grundy(word[j:]))
        if is_dyck(word[-j:]):
            options.add(grundy(word[:-j]))
    g=0
    while g in options: g+=1
    return g

checks=0
for n in range(18):
    hist={}
    for letters in product('ab',repeat=n):
        w=''.join(letters)
        k,l,i,j=end_counts(w)
        pred=k if is_dyck(w) else (k^l)
        actual=grundy(w)
        assert pred==actual, (w,pred,actual)
        if not is_dyck(w):
            assert i+j<len(w), (w,i,j)
            assert (i==0 or is_dyck(w[:i])) and (j==0 or is_dyck(w[-j:]))
            core=w[i:len(w)-j if j else len(w)]
            assert core
            assert all(not is_dyck(core[:t]) and not is_dyck(core[-t:])
                       for t in range(2,len(core)+1,2))
        hist[actual]=hist.get(actual,0)+1
        checks += 1
    print(f'length={n} positions={2**n} losing={hist.get(0,0)} max_grundy={max(hist)}')
print('PASS total_exact_positions=',checks)
