#!/usr/bin/env python3
"""Exact width-three all-on grid odd-domination polynomial via column chasing."""
from collections import Counter

def transition(column):
    return column ^ ((column << 1) & 7) ^ (column >> 1)

def weights(n):
    ans=Counter()
    for initial in range(8):
        prev, cur = 0, initial
        wt=0
        for _ in range(n):
            wt += cur.bit_count()
            prev,cur=cur,7^transition(cur)^prev
        if cur==0:ans[wt]+=1
    return ans

def prediction(n):
    q,r=divmod(n,6)
    return [Counter({10*q:1}),Counter({6*q+1:1}),Counter({6*q+2:2,6*q+4:2}),Counter({6*q+5:1}),Counter({10*q+10:1}),Counter({6*q+6:6,10*q+10:2})][r]

for n in range(1,301):
    result=weights(n)
    assert result==prediction(n),(n,result,prediction(n))
for initial in range(8):
    prev,cur=0,initial
    seq=[]
    for j in range(12):
        seq.append(cur)
        prev,cur=cur,7^transition(cur)^prev
    assert (prev,cur)==(seq[-1],initial), (initial,prev,cur)
    assert sum(z.bit_count() for z in seq[:6])==sum(z.bit_count() for z in seq[6:])
print('CHASE_PASS n=1..300 seeds=8 period12 and six-block weights checked')
for n in range(1,13):
    print('n=%d spectrum=%s'%(n,','.join('%d:%d'%(a,b) for a,b in sorted(weights(n).items()))))
