#!/usr/bin/env python3
"""Finite-state proof checker for paired three-colour automata on GP(5,k)."""
from collections import Counter, deque
import json

N = 3**10


def graph(k):
    edges = set()
    for i in range(5):
        for a,b in ((i, (i+1)%5), (i,5+i), (5+i,5+(i+k)%5)):
            edges.add(tuple(sorted((a,b))))
    assert len(edges) == 15
    neighbours = [tuple(j for j in range(10) if tuple(sorted((i,j))) in edges) for i in range(10)]
    assert all(len(a)==3 for a in neighbours)
    return neighbours


def next_state(state, neighbours, model):
    trits = []
    for i in range(10):
        trits.append(state % 3)
        state //= 3
    assert state == 0
    new = []
    for i, c in enumerate(trits):
        if model == 'CCA':
            nxt=(c+1)%3
            new.append(nxt if any(trits[j] == nxt for j in neighbours[i]) else c)
        else:
            new.append((1 if any(trits[j] == 1 for j in neighbours[i]) else 0)
                       if c == 0 else ((c+1)%3))
    return sum(c*3**i for i,c in enumerate(new))


def all_periods(neighbours, model):
    f = [next_state(x, neighbours, model) for x in range(N)]
    indegree = [0]*N
    for target in f:indegree[target]+=1
    queue = deque(i for i,d in enumerate(indegree) if d==0)
    removed=[]
    while queue:
        x=queue.popleft()
        removed.append(x)
        indegree[f[x]]-=1
        if indegree[f[x]]==0:queue.append(f[x])
    p=[0]*N
    t=[-1]*N
    for s in range(N):
        if indegree[s]==0 or p[s]:continue
        cycle=[s]
        z=f[s]
        while z != s:
            assert indegree[z]>0
            cycle.append(z)
            z=f[z]
        for z in cycle:p[z]=len(cycle);t[z]=0
    for s in reversed(removed):
        p[s]=p[f[s]]
        t[s]=t[f[s]]+1
    assert all(v>0 for v in p) and all(v>=0 for v in t)
    return f,p,t


def main():
    output={}
    for k in (1,2):
        adj=graph(k)
        cf,cp,ct=all_periods(adj, 'CCA')
        gf,gp,gt=all_periods(adj, 'GHM')
        pairs=Counter(zip(cp,gp))
        output['GP(5,%d)'%k]={
            'joint_eventual_periods':{f'{a}/{b}':v for (a,b),v in sorted(pairs.items())},
            'CCA_max_first_periodic_entry':max(ct),
            'GHM_max_first_periodic_entry':max(gt),
            'period_mismatch_total':sum(v for (a,b),v in pairs.items() if a!=b),
        }
        assert sum(pairs.values())==N
        assert (k!=1 or all(a==b for a,b in pairs))
        if k==2:
            assert pairs[(8,4)]==4800
            assert all(a==b or (a,b)==(8,4) for a,b in pairs)
            example=421
            assert cp[example]==8 and gp[example]==4 and ct[example]==0
            output['GP(5,%d)'%k]['witness']={
                'base3_integer':example,
                'color_string':''.join(str((example//3**i)%3) for i in range(10)),
                'CCA_first_entry':ct[example],
                'GHM_first_entry':gt[example],
            }
    print(json.dumps(output, indent=2, sort_keys=True))

if __name__=='__main__':main()
