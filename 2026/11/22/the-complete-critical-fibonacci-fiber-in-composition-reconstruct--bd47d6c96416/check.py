#!/usr/bin/env python3
"""Independent finite checks of a critical composition-deck fiber.
Only standard Python; theoretical all-k proof is in RESULT.md.
"""
from collections import defaultdict, Counter
from functools import lru_cache
from itertools import combinations

@lru_cache(maxsize=None)
def descendants(w, k):
    if k == 0:
        return frozenset((w,))
    values = set()
    for i, a in enumerate(w):
        u = w[:i] + ((a-1,) if a>1 else ()) + w[i+1:]
        values.update(descendants(u, k-1))
    return frozenset(values)

def compositions(n):
    for mask in range(1 << (n-1)):
        out, run = [], 1
        for i in range(n-1):
            if mask>>i & 1:
                out.append(run)
                run=1
            else:
                run += 1
        yield tuple(out+[run])

def family(k):
    return { (1,2)*i + (2,1)*(k-i) for i in range(k+1)}

def min_absent_weight(w):
    # Greedy subsequence automaton over 1 and 2, shortest missing total weight.
    d=[0]*(len(w)+1)
    d[-1]=1
    for p in range(len(w)-1, -1,-1):
        nxt = next((j for j in range(p,len(w)) if w[j]==2), None)
        d[p] = min(1+d[p+1], 2+(d[nxt+1] if nxt is not None else 0))
    return d[0]

def direct_contains(u,w):
    i=0
    for a in w:
        if i < len(u) and a >= u[i]: i+=1
    return i==len(u)

def main():
    for k in range(1,6):
        n=3*k
        F=frozenset(x for x in compositions(2*k) if max(x)<=2)
        observed=[]
        # exhaustive all source compositions of 3k, with literal complete k-decks
        for w in compositions(n):
            if descendants(w,k)==F: observed.append(w)
        assert set(observed)==family(k), (k,observed)
        print(f'EXHAUSTIVE n={n} k={k}: {len(observed)} preimages, deck {len(F)} compositions')
        descendants.cache_clear()
    for k in range(1,14):
        for w in family(k):
            assert min_absent_weight(w)==2*k+1,(k,w)
        print(f'GREEDY k={k}: shortest missing weight {2*k+1} for {k+1} witnesses')
    for k in range(2,9):
        for slots in combinations(range(2*k),k):
            s=set(slots)
            w=tuple(2 if i in s else 1 for i in range(2*k))
            if w in family(k):continue
            # find two zero 1-gaps, and the explicit obstruction of weight 2k
            a=[0]*(k+1)
            j=0
            for z in w:
                if z==2:j+=1
                else:a[j]+=1
            zeros=[j for j,x in enumerate(a) if x==0]
            assert len(zeros)>=2
            p,q=zeros[0],zeros[1]
            missing=(2,)*p+(1,)+(2,)*(q-p-1)+(1,)+(2,)*(k-q)
            assert sum(missing)==2*k
            assert not direct_contains(missing,w),(k,w,missing)
        print(f'OBSTRUCTION k={k}: all balanced nonfamily sources checked')
    print('VERIFY_OK')
if __name__=='__main__':main()
