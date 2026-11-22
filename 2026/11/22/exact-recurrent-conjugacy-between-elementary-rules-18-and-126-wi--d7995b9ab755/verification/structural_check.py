#!/usr/bin/env python3
"""Truth-table and recurrence-conjugacy assertions for ECA 18/126."""
from collections import Counter, defaultdict


def bit(x, i, n):
    return (x >> (i % n)) & 1


def original(x, n, code):
    y = 0
    for i in range(n):
        a,b,c=bit(x,i-1,n),bit(x,i,n),bit(x,i+1,n)
        y |= ((code >> (4*a+2*b+c)) & 1) << i
    return y


def D(x,n):
    return sum((bit(x,i,n)^bit(x,i+1,n))<<i for i in range(n))


def H(w,n):
    return sum((bit(w,i-1,n)|bit(w,i,n))<<i for i in range(n))


def functional_graph(n,code):
    N=1<<n
    succ=[original(x,n,code) for x in range(N)]
    indeg=[0]*N
    for v in succ: indeg[v]+=1
    queue=[v for v in range(N) if not indeg[v]]
    for v in queue:
        w=succ[v];indeg[w]-=1
        if indeg[w]==0: queue.append(w)
    cycles={};labels=[-1]*N
    for x in range(N):
        if indeg[x] and labels[x]==-1:
            walk=[];v=x
            while labels[v]==-1:
                labels[v]=-2;walk.append(v);v=succ[v]
            assert v==x or v in walk
            label=min(walk)
            cycles[label]=tuple(walk)
            for u in walk:labels[u]=label
    for v in reversed(queue):labels[v]=labels[succ[v]]
    basins=Counter(labels)
    assert sum(basins.values())==N
    return succ,cycles,basins


def main():
    for a in (0,1):
        for b in (0,1):
            for c in (0,1):
                f126=((a^b)|(b^c))
                f18=((1-b)&(a^c))
                assert f126==((126>>(4*a+2*b+c))&1)
                assert f18==((18>>(4*a+2*b+c))&1)
    for n in range(1,17):
        N=1<<n
        nxt18,cyc18,bas18=functional_graph(n,18)
        nxt126,cyc126,bas126=functional_graph(n,126)
        assert len(cyc18)==len(cyc126)
        for x in range(N):
            assert original(x,n,126)==H(D(x,n),n)
            assert original(x,n,18)==D(H(x,n),n)
            assert D(nxt126[x],n)==nxt18[D(x,n)]
        for lab,orbit in cyc126.items():
            trans=[D(x,n) for x in orbit]
            assert len(set(trans))==len(orbit)
            other=min(trans)
            assert other in cyc18 and set(trans)==set(cyc18[other])
            assert all(nxt18[D(x,n)]==D(nxt126[x],n) for x in orbit)
        # Independently compare per-attractor basin sizes, not only total counts.
        even_counts=Counter()
        for w in range(N):
            if w.bit_count()%2==0:
                # Use reverse-forest basin labels, rebuilt with own array.
                v=w;seen=set()
                while v not in seen and not any(v in c for c in cyc18.values()):
                    seen.add(v);v=nxt18[v]
                dest=next(l for l,c in cyc18.items() if v in c)
                even_counts[dest]+=1
        for lab,orbit in cyc126.items():
            other=min(D(x,n) for x in orbit)
            assert bas126[lab]==2*even_counts[other]
        if n in (4,8,11,16):
            lens=Counter(len(c) for c in cyc126.values())
            print('n',n,'cycles',dict(sorted(lens.items())),'image pair',len(set(nxt18)),len(set(nxt126)))
    print('STRUCTURAL_OK')

if __name__=='__main__':main()
