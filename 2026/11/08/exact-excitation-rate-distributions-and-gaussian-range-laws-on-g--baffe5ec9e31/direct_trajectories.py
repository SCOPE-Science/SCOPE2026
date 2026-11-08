#!/usr/bin/env python3
"""Independent complete functional-graph census of finite excitation dynamics."""
from collections import Counter, deque
from fractions import Fraction

# Expected frequencies computed by an exact independent path-integral algorithm.
EXPECTED = {
 (2,2,2): {'0':135,'3/4':108},
 (2,2,2,2): {'0':345,'3/4':384},
 (2,2,2,2,2): {'0':927,'3/4':1260},
 (3,3,3): {'0':2493,'1/2':3924,'1':144},
 (3,3,3,3): {'0':15471,'1/2':41268,'1':2310},
 (4,4,4): {'0':51543,'3/8':111240,'3/4':14364},
 (2,3,4): {'0':2529,'1/2':1584,'3/5':2286,'6/7':108,'1':54},
 (2,2,3,3): {'0':2241,'3/5':2322,'3/4':1944,'1':54},
 (2,3,3,4): {'0':15831,'1/2':9144,'3/5':31482,'6/7':1620,'1':972},
}

def graph(lengths):
    n = 2 + sum(k-1 for k in lengths)
    adj = [[] for _ in range(n)]
    next_vertex=2
    for k in lengths:
        path=[0]
        for j in range(k-1):
            path.append(next_vertex)
            next_vertex+=1
        path.append(1)
        for a,b in zip(path,path[1:]):
            adj[a].append(b);adj[b].append(a)
    return adj


def census(lengths, model):
    adj=graph(lengths)
    V=len(adj); total=3**V
    successors=[0]*total; increments=[0]*total; indegree=[0]*total
    for state in range(total):
        bits=[0]*V; t=state
        for i in range(V):bits[i]=t%3;t//=3
        dest=bits.copy()
        for i,c in enumerate(bits):
            if model=='GHM':
                if c>0 or (c==0 and any(bits[j]==1 for j in adj[i])):
                    dest[i]=(c+1)%3
            elif any(bits[j]==(c+1)%3 for j in adj[i]):
                dest[i]=(c+1)%3
        increments[state]=int(bits[0]==0 and dest[0]==1) if model=='GHM' else int(bits[0]!=dest[0])
        t=0
        for c in reversed(dest):t=3*t+c
        successors[state]=t; indegree[t]+=1
    boundary=deque(i for i,d in enumerate(indegree) if d==0)
    removed=[]
    while boundary:
        s=boundary.popleft();removed.append(s)
        nxt=successors[s];indegree[nxt]-=1
        if indegree[nxt]==0:boundary.append(nxt)
    rate=[None]*total
    for i in range(total):
        if indegree[i] and rate[i] is None:
            x=i; cyc=[]
            while rate[x] is None:
                rate[x]=Fraction(-1);cyc.append(x);x=successors[x]
            assert x==i
            activity=Fraction(sum(increments[x] for x in cyc),len(cyc))
            for x in cyc:rate[x]=activity
    for x in reversed(removed):rate[x]=rate[successors[x]]
    return Counter(rate)

if __name__=='__main__':
    cases=[(2,2,2),(2,2,2,2),(2,2,2,2,2),
           (3,3,3),(3,3,3,3),(4,4,4),(2,3,4),(2,2,3,3),(2,3,3,4)]
    for lengths in cases:
        ghm=census(lengths,'GHM')
        cca=census(lengths,'CCA')
        # Shared circulation structure forces a rate ratio of exactly three.
        assert Counter({3*k:v for k,v in ghm.items()})==cca
        if EXPECTED[lengths]:
            assert {str(k):v for k,v in sorted(cca.items())}==EXPECTED[lengths]
        assert sum(cca.values())==3**(2+sum(k-1 for k in lengths))
        print('DYNAMICS_OK',str(lengths),'states',sum(cca.values()),
              'CCA_counts',{str(k):v for k,v in sorted(cca.items())},
              'GHM_counts',{str(k):v for k,v in sorted(ghm.items())})
    print('ALL_DYNAMICS_CHECKS_OK')
