#!/usr/bin/env python3
"""Independent functional-digraph decomposition, LCF graph and Boolean majority."""
import json
from collections import deque

N = 12
LCF = (-5,-2,-4,2,5,-2,2,5,-2,-5,4,2)
# Canonical labelled graph to the LCF Hamiltonian labelling:
RELABELLING = (5,3,2,1,0,7,6,4,10,11,8,9)

def graph():
    adj = [set() for _ in range(N)]
    for i in range(N):
        for j in ((i+1)%N,(i+LCF[i])%N):
            adj[i].add(j)
            adj[j].add(i)
    return tuple(tuple(sorted(a)) for a in adj)

def table(g, omitted):
    # In the cubic graph majority is median of three neighboring bits.
    # With one bond removed, its endpoints replace the old neighbor by SELF;
    # this is exactly the original tie-retaining update on the degree-two graph.
    ans = [0] * (1 << N)
    for x in range(1 << N):
        new = 0
        for i in range(N):
            nb = list(g[i]); assert len(nb) == 3
            if omitted is not None and i in omitted:
                other = omitted[0] if omitted[1] == i else omitted[1]
                nb[nb.index(other)] = i
            a,b,c = (((x >> v) & 1) for v in nb)
            new |= ((a&b) | (a&c) | (b&c)) << i
        ans[x] = new
    return ans

def classify(f):
    total = len(f)
    incoming = [[] for _ in range(total)]
    indeg = [0] * total
    for x,y in enumerate(f):
        indeg[y] += 1
        incoming[y].append(x)
    Q = deque(x for x in range(total) if indeg[x] == 0)
    removed = [False] * total
    while Q:
        x=Q.popleft();removed[x]=True
        y=f[x];indeg[y]-=1
        if indeg[y]==0:Q.append(y)
    distance=[-1]*total
    cls=[-1]*total  # 0 or ALL or other
    period=[0]*total
    q=deque()
    done=set()
    for x in range(total):
        if removed[x] or x in done:continue
        cycle=[];y=x
        while y not in done:
            done.add(y);cycle.append(y);y=f[y]
        assert y==x and len(cycle) in (1,2)
        typ=0 if cycle==[0] else (1 if cycle==[total-1] else 2)
        for y in cycle:
            distance[y]=0;cls[y]=typ;period[y]=len(cycle);q.append(y)
    while q:
        x=q.popleft()
        for y in incoming[x]:
            if distance[y]<0:
                distance[y]=distance[x]+1;cls[y]=cls[x];period[y]=period[x];q.append(y)
    assert min(distance)==0
    hist=[distance.count(i) for i in range(max(distance)+1)]
    return dict(unanimity=cls.count(0)+cls.count(1),zero_basin=cls.count(0),
                one_basin=cls.count(1),fixed_points=sum((distance[x]==0 and period[x]==1) for x in range(total)),
                temporal_two_states=sum((distance[x]==0 and period[x]==2) for x in range(total)),
                maximum_entry=max(distance),max_count=hist[-1],entry_histogram=hist), tuple(c in (0,1) for c in cls)

def main():
    g=graph(); assert len(g)==12 and all(len(row)==3 for row in g)
    edges=sorted((i,j) for i in range(N) for j in g[i] if i<j)
    assert len(edges)==18
    reference_edges = sorted(tuple(sorted((RELABELLING.index(i),RELABELLING.index(j)))) for i,j in edges)
    base,base_flags=classify(table(g,None))
    out={'graph':'Frucht in independent LCF labelling','vertices':N,
         'edges_lcf':edges,'edges_original_labels':reference_edges,'runs':[]}
    out['runs'].append({'deleted_edge':None,'delta_unanimity':0,
                       'new_consensus_initials':0,'lost_consensus_initials':0,**base})
    for a,b in reference_edges:
        c,d=RELABELLING[a],RELABELLING[b]
        st,flags=classify(table(g,(c,d)))
        gain=sum(b and not a for a,b in zip(base_flags,flags))
        loss=sum(a and not b for a,b in zip(base_flags,flags))
        assert gain-loss==st['unanimity']-base['unanimity']
        out['runs'].append({'deleted_edge':[a,b],'delta_unanimity':gain-loss,
                            'new_consensus_initials':gain,'lost_consensus_initials':loss,**st})
    print(json.dumps(out,sort_keys=True,separators=(',',':')))
if __name__ == '__main__':main()
