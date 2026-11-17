#!/usr/bin/env python3
"""Exact space-time transfer for majority dynamics on generalized Petersen GP(n,2).
Pure Python 3 standard library. No files or prior results are required.
"""
from collections import Counter


def majority(x,y,z):
    return (x+y+z)>=2


def pair_edges():
    N=1<<16
    ed=[[] for _ in range(N)]
    for state in range(N):
        a=(state>>12)&15; b=(state>>8)&15
        c=(state>>4)&15; d=state&15
        ou=lambda q:q&1
        iv=lambda q:(q>>1)&1
        pu=lambda q:(q>>2)&1
        qv=lambda q:(q>>3)&1
        if majority(ou(b),ou(d),iv(c)) != pu(c): continue
        if majority(pu(b),pu(d),qv(c)) != ou(c): continue
        for e in range(16):
            if majority(iv(a),iv(e),ou(c)) != qv(c):continue
            if majority(qv(a),qv(e),pu(c)) != iv(c):continue
            ed[state].append(((state<<4)&65535)|e)
    return ed


def fixed_edges():
    N=256
    ed=[[] for _ in range(N)]
    for state in range(N):
        a=(state>>6)&3;b=(state>>4)&3;c=(state>>2)&3;d=state&3
        if majority(b&1,d&1,(c>>1)&1)!=(c&1):continue
        for e in range(4):
            if majority((a>>1)&1,(e>>1)&1,c&1)!=((c>>1)&1):continue
            ed[state].append(((state<<2)&255)|e)
    return ed


def strongly_connected_components(ed):
    """Iterative Kosaraju, including singleton components; no recursion limit risk."""
    n=len(ed)
    reverse=[[] for _ in range(n)]
    for v,row in enumerate(ed):
        for w in row:reverse[w].append(v)
    visited=bytearray(n); order=[]
    for v in range(n):
        if visited[v]:continue
        visited[v]=1;stack=[(v,0)]
        while stack:
            x,j=stack[-1]
            if j==len(ed[x]):
                order.append(x);stack.pop()
            else:
                stack[-1]=(x,j+1)
                y=ed[x][j]
                if not visited[y]:
                    visited[y]=1;stack.append((y,0))
    comps=[];labels=[-1]*n
    for v in reversed(order):
        if labels[v]!=-1:continue
        cid=len(comps);labels[v]=cid;stack=[v];comp=[]
        while stack:
            x=stack.pop();comp.append(x)
            for y in reverse[x]:
                if labels[y]==-1:labels[y]=cid;stack.append(y)
        comps.append(comp)
    assert all(x>=0 for x in labels)
    return comps,labels


def recurring_components(ed):
    comps,lab=strongly_connected_components(ed)
    return [comp for comp in comps if len(comp)>1 or any(x in ed[x] for x in comp)]


def subgraph(ed,nodes):
    lookup={v:i for i,v in enumerate(nodes)}
    return [[lookup[w] for w in ed[v] if w in lookup] for v in nodes]


def trace_power(ed,k):
    """Count length-k closed walks, with exact Python integers."""
    n=len(ed);total=0
    for start in range(n):
        v=[0]*n;v[start]=1
        for _ in range(k):
            nextv=[0]*n
            for i,neighbors in enumerate(ed):
                a=v[i]
                if a:
                    for j in neighbors:nextv[j]+=a
            v=nextv
        total+=v[start]
    return total


def integer_collatz_certificate(ed,lower,upper,power=80,den=100000):
    """Check rho in (lower/den,upper/den) with exact integers.
    The block must be strongly connected and the vector strictly positive.
    """
    v=[1]*len(ed)
    for _ in range(power):
        v=[sum(v[j] for j in neighbors) for neighbors in ed]
    assert min(v)>0
    w=[sum(v[j] for j in neighbors) for neighbors in ed]
    assert all(lower*vi < den*wi < upper*vi for vi,wi in zip(v,w))
    return (len(v),len(str(max(v))),min(v)>0)


def main():
    pair=pair_edges(); one=fixed_edges()
    for name,ed,sz,edcount,giant,giant_edges,lo,hi in [
        ('two-step',pair,1<<16,102400,778,2202,264157,264158),
        ('fixed',one,256,320,24,36,156485,156486),
    ]:
        assert len(ed)==sz and sum(map(len,ed))==edcount
        comps=recurring_components(ed)
        assert sorted(map(len,comps))==[1,1,giant]
        big=max(comps,key=len);small=[c for c in comps if len(c)==1]
        assert all(ed[c[0]].count(c[0])==1 for c in small)
        block=subgraph(ed,big)
        assert sum(map(len,block))==giant_edges
        assert any(i in row for i,row in enumerate(block)), 'aperiodicity certificate'
        cert=integer_collatz_certificate(block,lo,hi)
        print(f'{name}: states={sz} edges={edcount} recurrent_sccs={sorted(map(len,comps))} giant_edges={giant_edges} rho_interval=({lo}/100000,{hi}/100000) vector={cert}')
        if name=='two-step':pair_block=block
        else:fixed_block=block
    # Each full graph has two isolated one-loop components.
    for n in range(5,12):
        two=2+trace_power(pair_block,n)
        one=2+trace_power(fixed_block,n)
        assert (two-one)%2==0
        print(f'n={n} fixed={one} two_step={two} primitive_two_orbits={(two-one)//2}')


def prism_pair_edges():
    ed=[[] for _ in range(256)]
    for state in range(256):
        a=(state>>4)&15; b=state&15
        for c in range(16):
            if majority(a&1,c&1,(b>>1)&1)!=(b>>2)&1:continue
            if majority((a>>2)&1,(c>>2)&1,(b>>3)&1)!=(b&1):continue
            if majority((a>>1)&1,(c>>1)&1,b&1)!=(b>>3)&1:continue
            if majority((a>>3)&1,(c>>3)&1,(b>>2)&1)!=(b>>1)&1:continue
            ed[state].append(((state<<4)&255)|c)
    return ed


def prism_fixed_edges():
    ed=[[] for _ in range(16)]
    for state in range(16):
        a=(state>>2)&3;b=state&3
        for c in range(4):
            if majority(a&1,c&1,(b>>1)&1)!=(b&1):continue
            if majority((a>>1)&1,(c>>1)&1,b&1)!=((b>>1)&1):continue
            ed[state].append(((state<<2)&15)|c)
    return ed


def prism_report():
    one=prism_fixed_edges();two=prism_pair_edges()
    for name,graph in [('one',one),('two',two)]:
        cs=recurring_components(graph)
        major=max(cs,key=len)
        main=subgraph(graph,major)
        print('prism',name,'states',len(graph),'edges',sum(map(len,graph)),
            'components',sorted(map(len,cs)),'main_edges',sum(map(len,main)))
        if name=='one':f=graph
        else:t=graph
    for n in range(5,12):
        a=trace_power(f,n);b=trace_power(t,n)
        print('prism',n,a,b,(b-a)//2)

if __name__ == "__main__":
    main()
    prism_report()
