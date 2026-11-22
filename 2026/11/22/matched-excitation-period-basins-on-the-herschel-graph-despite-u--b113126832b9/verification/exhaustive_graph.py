#!/usr/bin/env python3
"""Exhaustive functional graph proof for two ternary dynamics on the Herschel graph.

Uses topological indegree peeling; no finite graph samples or stochastic estimates.
"""
import json
from collections import Counter, deque
from pathlib import Path

# Vertex numbering 1..11 follows the Herschel graph illustrated at
# https://faculty.washington.edu/moishe/hanoi-2011/DO-2011/Week-8/Supplements/Herschel%20Graph.pdf
NEIGHBORS_1BASED = (
    (2,4,5), (1,3,6,7), (2,4,8), (1,3,9,10), (1,6,10),
    (2,5,11), (2,8,11), (3,7,9), (4,8,11), (4,5,11), (6,7,9,10)
)
NVERT=11
NEIGH=[tuple(j-1 for j in nbrs) for nbrs in NEIGHBORS_1BASED]
POWERS=[3**i for i in range(NVERT)]
TOTAL=3**NVERT
assert sum(len(x) for x in NEIGH)==36
assert all(i in NEIGH[j] for i in range(NVERT) for j in NEIGH[i])

def transition(value, kind):
    symbols=[]
    for i in range(NVERT): symbols.append((value//POWERS[i])%3)
    result=0
    for i,color in enumerate(symbols):
        if kind=='GHM':
            nxt = (color+1)%3 if color else int(any(symbols[j]==1 for j in NEIGH[i]))
        else:
            nxt = (color+1)%3 if any(symbols[j]==(color+1)%3 for j in NEIGH[i]) else color
        result += POWERS[i]*nxt
    return result

def classify(kind):
    nxt=[transition(s,kind) for s in range(TOTAL)]
    degree=[0]*TOTAL
    for dest in nxt:degree[dest]+=1
    waiting=deque(s for s,d in enumerate(degree) if d==0)
    peeled=[]
    while waiting:
        s=waiting.popleft();peeled.append(s)
        v=nxt[s];degree[v]-=1
        if degree[v]==0:waiting.append(v)
    depth=[-1]*TOTAL;period=[0]*TOTAL
    for s in range(TOTAL):
        if degree[s]==0 or depth[s]>=0:continue
        cyc=[];v=s
        while depth[v]<0:
            cyc.append(v);depth[v]=0;v=nxt[v]
        assert v==s
        p=len(cyc)
        for v in cyc:period[v]=p
    for v in reversed(peeled):
        depth[v]=1+depth[nxt[v]]
        period[v]=period[nxt[v]]
    assert all(v>=0 for v in depth)
    cells=Counter((depth[s],period[s]) for s in range(TOTAL))
    assert sum(cells.values())==TOTAL
    return nxt, depth, period, cells

def main():
    c=classify('CCA');h=classify('GHM')
    assert c[2]==h[2], 'pointwise period equality fails'
    assert max(c[1])==8 and max(h[1])==10
    for name,v,expected in [
        ('CCA',c,{1:3,3:3060,4:4752}),
        ('GHM',h,{1:1,3:3060,4:1200})
    ]:
        recurrent={p:sum(a for (t,q),a in v[3].items() if t==0 and q==p) for p in [1,3,4]}
        assert recurrent==expected,(name,recurrent)
    basins={p:sum(1 for v in c[2] if v==p) for p in (1,3,4)}
    assert basins=={1:17397,3:23346,4:136404}
    assert sum(basins.values())==TOTAL
    for p in (3,4):
        src={s for s in range(TOTAL) if h[1][s]==0 and h[2][s]==p}
        dest={s for s in range(TOTAL) if c[1][s]==0 and c[2][s]==p}
        assert src<=dest
        assert all(h[0][s]==c[0][s] for s in src)
        if p==3:assert src==dest
    assert sum(1 for s in range(TOTAL) if c[2][s]!=h[2][s])==0
    assert sum(1 for s in range(TOTAL) if c[1][s]==8 and c[2][s]==3)==108
    assert sum(1 for s in range(TOTAL) if h[1][s]==10 and h[2][s]==3)==36
    report={
        'graph':'Herschel graph, 11 vertices, 18 edges',
        'states':TOTAL,
        'basins':{str(k):v for k,v in basins.items()},
        'CCA':{'max_first_entry':max(c[1]),'recurrent_states':{str(p):sum(a for (t,q),a in c[3].items() if t==0 and q==p) for p in [1,3,4]},'entry_period_counts':[[t,p,a] for (t,p),a in sorted(c[3].items())]},
        'GHM':{'max_first_entry':max(h[1]),'recurrent_states':{str(p):sum(a for (t,q),a in h[3].items() if t==0 and q==p) for p in [1,3,4]},'entry_period_counts':[[t,p,a] for (t,p),a in sorted(h[3].items())]},
        'matched_periods':TOTAL,
        'shared_recurrent_three_states':3060,
        'shared_recurrent_four_states':1200,
        'shared_transitions_on_GHM_recurrent_states':True
    }
    print(json.dumps(report,sort_keys=True,indent=2))
    print('HERSCHEL_EXHAUSTIVE_OK')
if __name__=='__main__':main()
