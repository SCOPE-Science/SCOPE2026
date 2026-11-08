#!/usr/bin/env python3
"""Independently enumerate synchronous dynamics and count root excitation rates.
All state spaces named in CASES are explored without trajectory samples.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from exact_formula import cactus_counts

CASES=([3,3],0),([4,4],0),([5,5],0),([3,4],1),([3,3,3],0),([4,4,4],0)

def make_graph(lengths, bridges):
    # Cycles joined at common root and a path of 'bridges' pendant edges.
    adj=[set()]
    for n in lengths:
        vv=[0]+list(range(len(adj),len(adj)+n-1))
        adj.extend(set() for _ in range(n-1))
        for i in range(n):
            u,v=vv[i],vv[(i+1)%n]
            adj[u].add(v);adj[v].add(u)
    for _ in range(bridges):
        u=len(adj)-1
        v=len(adj)
        adj.append({u});adj[u].add(v)
    return [sorted(a) for a in adj]

def update(state,adj,model):
    ans=[]
    for i,s in enumerate(state):
        if model=='CCA':
            adv=any(state[j]==(s+1)%3 for j in adj[i]);ans.append((s+int(adv))%3)
        else:
            ans.append((s+1)%3 if s in (1,2) else int(any(state[j]==1 for j in adj[i])))
    return tuple(ans)

def measure_one(x,adj,model):
    seen={}
    seq=[]
    for tick in range(500):
        if x in seen:
            j=seen[x]; period=len(seq)-j
            events=0
            for i in range(j,len(seq)):
                a=seq[i][0];b=seq[(i+1) if (i+1)<len(seq) else j][0]
                events+=(b==(a+1)%3) if model=='CCA' else (a==0 and b==1)
            return Fraction(events,period)
        seen[x]=len(seq);seq.append(x)
        x=update(x,adj,model)
    raise AssertionError('no eventual cycle found')

def main():
    for lengths,bridges in CASES:
        adj=make_graph(lengths,bridges)
        predicted=cactus_counts(lengths,bridges)
        observed={}
        for model in ['CCA','GHM']:
            count=defaultdict(int)
            for state in product(range(3),repeat=len(adj)):
                alpha=measure_one(state,adj,model)
                if model=='GHM':alpha*=3
                count[alpha]+=1
            assert dict(count)==predicted,(lengths,bridges,model,dict(count),predicted)
            observed[model]=sum(count.values())
        print('PASS',lengths,'bridges',bridges,'vertices',len(adj), 'states_per_model',len(range(3))**len(adj),
              'CCA_and_3GHM_histogram',','.join(f'{k}:{v}' for k,v in sorted(predicted.items())))
    print('ALL_COMPLETE_GRAPH_STATES_PASS')
if __name__=='__main__':main()
