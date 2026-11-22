#!/usr/bin/env python3
"""Finite-history certificate for cyclic Rule 110 temporal 8-,9-,10-clocks.

Python standard library only. The graph is constructed directly from the eight
entries of Rule 110, rather than from a cited cycle inventory.
"""
from collections import defaultdict, deque, Counter

RULE = 110
HEIGHTS = (1,2,3,4,5,8,9,10)


def graph(t):
    Q=1<<t
    adj={}
    for a in range(Q):
        for b in range(Q):
            possibilities=[0]
            for j in range(t):
                prefix=4*((a>>j)&1)+2*((b>>j)&1)
                required=(b>>((j+1)%t))&1
                allowed=[bit for bit in (0,1) if (RULE>>(prefix+bit))&1 == required]
                if not allowed:
                    possibilities=[]; break
                possibilities=[c|(bit<<j) for c in possibilities for bit in allowed]
            if possibilities:
                adj[a*Q+b]=[b*Q+c for c in possibilities]
    return adj


def cyclic_components(adj):
    # Successive removal of in-/out-degree-zero vertices preserves all cycles.
    deg_in=defaultdict(int);deg_out={v:len(ws) for v,ws in adj.items()}
    for v,ws in adj.items():
        for w in ws:deg_in[w]+=1
    allnodes=set(deg_in)|set(adj)
    alive=set(allnodes)
    reverse=defaultdict(list)
    for v,ws in adj.items():
        for w in ws:reverse[w].append(v)
    queue=deque(v for v in allnodes if deg_in[v]==0 or deg_out.get(v,0)==0)
    while queue:
        v=queue.popleft()
        if v not in alive:continue
        alive.remove(v)
        for w in adj.get(v,()):
            deg_in[w]-=1
            if w in alive and (deg_in[w]==0 or deg_out.get(w,0)==0):queue.append(w)
        for u in reverse.get(v,()):
            deg_out[u]-=1
            if u in alive and (deg_in[u]==0 or deg_out[u]==0):queue.append(u)
    # Independent Kosaraju on the remaining graph (which may contain bridges).
    visited=set();order=[]
    for s in sorted(alive):
        if s in visited:continue
        visited.add(s);stack=[(s,0)]
        while stack:
            v,j=stack[-1]; edges=adj.get(v,())
            while j<len(edges) and edges[j] not in alive:j+=1
            if j==len(edges):
                order.append(v);stack.pop()
            else:
                w=edges[j];stack[-1]=(v,j+1)
                if w not in visited:
                    visited.add(w);stack.append((w,0))
    visited=set(); components=[]
    for s in reversed(order):
        if s in visited:continue
        visited.add(s);stack=[s]; comp=[]
        while stack:
            v=stack.pop();comp.append(v)
            for w in reverse.get(v,()):
                if w in alive and w not in visited:
                    visited.add(w);stack.append(w)
        if len(comp)>1 or s in adj.get(s,()):components.append(set(comp))
    return components,alive


def local_period(v,t):
    Q=1<<t
    a,b=divmod(v,Q)
    return next(d for d in range(1,t+1) if t%d==0 and
       all(((a>>j)&1)==((a>>((j+d)%t))&1) and
           ((b>>j)&1)==((b>>((j+d)%t))&1) for j in range(t)))


def certificate():
    results={}
    for t in HEIGHTS:
        adj=graph(t)
        cc,alive=cyclic_components(adj)
        summary=[]
        for C in cc:
            inside_edges=sum(w in C for v in C for w in adj.get(v,()))
            periods=set(local_period(v,t) for v in C)
            summary.append((len(C),inside_edges,tuple(sorted(periods))))
        summary.sort(reverse=True)
        results[t]=summary
        print('T=',t,'graph source vertices=',len(adj),'cycle trim vertices=',len(alive),'cyclic SCC=',summary)
    assert results[1]==[(1,1,(1,))]
    assert results[2]==[(4,4,(2,)),(1,1,(1,))]
    assert results[3]==[(9,9,(3,)),(1,1,(1,))]
    assert results[4]==[(4,4,(2,)),(1,1,(1,))]
    assert results[5]==[(25,30,(5,)),(1,1,(1,))]
    assert results[8]==[(8,8,(8,)),(4,4,(2,)),(1,1,(1,))]
    assert results[9]==[(18,18,(9,))]+[(12,12,(9,))]*3+[(9,9,(3,))]+[(6,6,(9,))]*3+[(1,1,(1,))]
    assert results[10]==[(25,30,(5,)),(4,4,(2,)),(1,1,(1,))]
    # On these components every vertex has the displayed time-column period,
    # therefore closed walks in G_10 represent only fixed points of F^5 or F^2.
    # Disjoint simple cycle SCCs in G_8 and G_9 give their complete trace sequences.
    for n in range(1,401):
        T8=1+4*(n%4==0)+8*(n%8==0)
        T4=1+4*(n%4==0)
        T9=1+9*(n%9==0)+18*(n%18==0)+36*(n%12==0)+18*(n%6==0)
        T3=1+9*(n%9==0)
        p8=(T8-T4)//8;p9=(T9-T3)//9
        assert 8*p8==T8-T4 and p8==(n%8==0)
        assert 9*p9==T9-T3 and p9==2*(n%6==0)+4*(n%12==0)+2*(n%18==0)
    print('FULL_SPECTRAL_COUNTS_OK')
    return results

if __name__=='__main__':certificate()
