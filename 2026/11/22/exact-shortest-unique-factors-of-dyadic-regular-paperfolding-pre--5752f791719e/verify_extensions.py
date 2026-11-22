#!/usr/bin/env python3
"""Independent parity-recursive generation and neighboring-suffix-LCP tests."""
from collections import Counter

def pf_recursive(n):
    w=bytearray(n)
    for i in range(n):
        w[i]=w[i//2] if i%2 else 1-((i//2)%2)
    return bytes(w)

def sus_by_suffix_neighbors(w):
    sorted_indices=sorted(range(len(w)),key=lambda i:w[i:])
    def common(i,j):
        k=0
        while i+k<len(w) and j+k<len(w) and w[i+k]==w[j+k]:k+=1
        return k
    out=[]
    for t,i in enumerate(sorted_indices):
        need=1+max(common(i,sorted_indices[t-1]) if t else 0,
                   common(i,sorted_indices[t+1]) if t+1<len(w) else 0)
        if i+need<=len(w):out.append((need,i))
    best=min(n for n,i in out)
    return best,sorted(i for n,i in out if n==best)

for k in range(8,13):
    w=pf_recursive(1<<k)
    predicted=(2**(k-4)+1,[11*2**(k-4)-1,12*2**(k-4)-1])
    result=sus_by_suffix_neighbors(w)
    assert result==predicted,(k,result,predicted)
    r=predicted[0]-1
    # The suffix count is the boundary invariant in the induction.
    suffix=w[-r:]
    suffix_count=sum(w[i:i+r]==suffix for i in range(len(w)-r+1))
    assert suffix_count>=3,(k,suffix_count)
    print(f'order={k} shortest={result[0]} starts={result[1]} suffix_len={r} suffix_multiplicity={suffix_count}')
print('EXTENSION_CHECK_PASS')
