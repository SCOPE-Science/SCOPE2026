#!/usr/bin/env python3
"""Independent transfer-series and exact enumerator checks."""
from collections import defaultdict
from itertools import product
from fractions import Fraction

def count_by_adjacent_runs(q,n):
    out=defaultdict(int)
    for word in product(range(q),repeat=n):
        prev=None;symbol=word[0];length=1;total=0
        for x in word[1:]:
            if x==symbol:length+=1
            else:
                if prev is not None and symbol==(prev^1):total+=length
                prev,symbol,length=symbol,x,1
        if prev is not None and symbol==(prev^1):total+=length
        out[total]+=1
    return dict(out)

def via_run_transfer(q,n):
    # DP over length and last run identity; its accumulated weight is the sum
    # of lengths of complementary-following runs.  Each complete run has weight.
    state={(a,0,0):1 for a in range(q)}  # (last letter, run count statistic, last run length)
    # The first symbol starts a run; store preceding run as separate dimension.
    state={(a,None,1,0):1 for a in range(q)}
    for _ in range(1,n):
        nxt=defaultdict(int)
        for (last,prev,r,c),cnt in state.items():
            for a in range(q):
                if a==last:
                    nxt[(last,prev,r+1,c)]+=cnt
                else:
                    new_c=c+(r if prev is not None and last==(prev^1) else 0)
                    nxt[(a,last,1,new_c)]+=cnt
        state=nxt
    output=defaultdict(int)
    for (last,prev,r,c),cnt in state.items():
        output[c+(r if prev is not None and last==(prev^1) else 0)]+=cnt
    return dict(output)

if __name__=='__main__':
    for q,max_n in ((2,9),(4,6),(6,5)):
        for n in range(1,max_n+1):
            x=count_by_adjacent_runs(q,n)
            y=via_run_transfer(q,n)
            assert x==y,(q,n,x,y)
            assert sum(x.values())==q**n
            assert x.get(0)==q*(q-1)**(n-1)
            if n>=2:assert x.get(n-1)==q*2**(n-2)
        print('PASS transfer',q,max_n)
