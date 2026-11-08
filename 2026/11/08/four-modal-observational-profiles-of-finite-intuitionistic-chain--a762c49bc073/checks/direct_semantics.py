#!/usr/bin/env python3
"""Independent finite semantics enumeration for four modalities."""
from collections import Counter
from itertools import product

def signature(rows, n):
    ans=[]
    for k in range(n+1):
        U=set(range(k,n))
        for op in range(4):
            bits=0
            for s in range(n):
                if op==0:
                    truth=any(any(u in U for u in rows[t]) for t in range(s+1))
                elif op==1:
                    truth=all(all(u in U for u in rows[t]) for t in range(s,n))
                elif op==2:
                    truth=all(any(u in U for u in rows[t]) for t in range(s,n))
                else:
                    truth=any(all(u in U for u in rows[t]) for t in range(s+1))
                if truth: bits |= 1<<s
            ans.append(bits)
    return tuple(ans)

for n in (1,2,3,4):
    freq=Counter()
    subsets=[tuple(j for j in range(n) if (mask>>j)&1) for mask in range(1<<n)]
    for rows in product(subsets,repeat=n):
        freq[signature(rows,n)]+=1
    print('direct',n,'classes',len(freq),'total',sum(freq.values()),'max_fiber',max(freq.values()),'max_fiber_classes',sum(c==max(freq.values()) for c in freq.values()))
