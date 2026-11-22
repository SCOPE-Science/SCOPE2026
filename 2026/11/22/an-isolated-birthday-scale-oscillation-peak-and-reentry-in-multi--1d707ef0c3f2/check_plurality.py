#!/usr/bin/env python3
"""Finite checker of plurality dynamics on complete bipartite graphs.

No external libraries. All states are enumerated independently of the
occupancy formula. This is a finite test, not the asymptotic proof.
"""
from itertools import product
from collections import Counter
from math import factorial


def winner(s, q):
    cnt = [0]*q
    for c in s: cnt[c] += 1
    high = max(cnt)
    return cnt.index(high) if cnt.count(high) == 1 else None


def step(state, m, q):
    a, b = state[:m], state[m:]
    # Each vertex explicitly observes the other shore's complete state.
    res=[]
    for v in range(2*m):
        nhood = b if v < m else a
        counts=[sum(x==c for x in nhood) for c in range(q)]
        leaders=[c for c in range(q) if counts[c]==max(counts)]
        res.append(leaders[0] if len(leaders)==1 else state[v])
    return tuple(res)


def first_entry(state, m, q):
    seen = {}
    s = state
    for t in range(5):
        if s in seen:
            return seen[s], t-seen[s]
        seen[s]=t
        s=step(s,m,q)
    raise AssertionError('Not periodic by time 3')


def counts_from_winners(m,q):
    seqs=list(product(range(q),repeat=m))
    U=sum(winner(s,q) is not None for s in seqs)
    B=q**m-U
    return U,B


def analytic_shells(m,q):
    U,B=counts_from_winners(m,q)
    return {
        (0,1):B*B+q,
        (0,2):q*(q-1),
        (1,1):U*U//q-q+2*q*B,
        (1,2):U*U*(q-1)//q-q*(q-1),
        (2,1):2*(U-q)*B,
    }


def check(m,q):
    pred=analytic_shells(m,q)
    brute=Counter()
    for s in product(range(q), repeat=2*m):
        brute[first_entry(s,m,q)] += 1
    assert dict(brute)=={k:v for k,v in pred.items() if v},(m,q,brute,pred)
    assert sum(brute.values())==q**(2*m)
    assert max(k[0] for k in brute)<=2
    assert set(k[1] for k in brute)<={1,2}
    U,B=counts_from_winners(m,q)
    return {'m':m,'q':q,'U':U,'B':B,'first_entry_period_counts':dict(sorted(brute.items()))}

if __name__=='__main__':
    for q in (2,3,4,5):
        for m in (1,2,3):
            print(check(m,q))
    print('ALL SMALL-STATE TESTS PASSED')
