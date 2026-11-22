#!/usr/bin/env python3
"""Exact finite-poset enumeration and small weak-core ambiguity boundary.
Only Python 3 standard library. Every poset is relabeled by a linear extension.
"""
import itertools
from collections import Counter, defaultdict


def posets(n):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    for mask in range(1 << len(pairs)):
        r = [1 << i for i in range(n)]
        for k, (i, j) in enumerate(pairs):
            if mask & (1 << k): r[i] |= 1 << j
        if all((r[i] | r[j]) == r[i] for i in range(n) for j in range(i+1,n) if r[i] & (1<<j)):
            yield r


def beat_reduced(r):
    nodes = list(range(len(r)))
    while True:
        found = None
        for a in nodes:
            ups=[b for b in nodes if b != a and r[a] & (1 << b)]
            downs=[b for b in nodes if b != a and r[b] & (1 << a)]
            if any(all(r[b] & (1 << x) for x in ups) for b in ups) or any(all(r[x] & (1 << b) for x in downs) for b in downs):
                found=a; break
        if found is None:break
        nodes.remove(found)
    return nodes


def component_count(r, nodes):
    found=set(); cc=0
    for a in nodes:
        if a in found:continue
        cc+=1; found.add(a);todo=[a]
        while todo:
            x=todo.pop()
            for y in nodes:
                if y not in found and ((r[x]>>y&1) or (r[y]>>x&1)):
                    found.add(y);todo.append(y)
    return cc


def core_type(r, nodes):
    k=len(nodes)
    if all(not (r[a]>>b&1) for a in nodes for b in nodes if a!=b):return 'discrete-'+str(k)
    if k==4 and component_count(r,nodes)==1:
        return 'square' if sum(r[a]>>b&1 for a in nodes for b in nodes if a!=b)==4 else 'other4'
    if k==5 and component_count(r,nodes)==2 and sum(r[a]>>b&1 for a in nodes for b in nodes if a!=b)==4:
        return 'square+point'
    if k==5 and component_count(r,nodes)==1:
        degs=[(sum(r[b]>>a&1 for b in nodes if a!=b),sum(r[a]>>b&1 for b in nodes if a!=b)) for a in nodes]
        if sorted(degs)==sorted([(0,3)]*2+[(2,0)]*3): return 'K23'
        if sorted(degs)==sorted([(0,2)]*3+[(3,0)]*2): return 'K32'
        return 'other5'
    return 'other'+str(k)


def quotient_type(r,a,b):
    n=len(r);groups=[(a,b)]+[(x,) for x in range(n) if x not in (a,b)]
    idx=[next(i for i,group in enumerate(groups) if x in group) for x in range(n)]
    k=n-1
    p=[1<<i for i in range(k)]
    for i in range(n):
        for j in range(n):
            if r[i] & (1<<j):p[idx[i]] |= 1<<idx[j]
    for j in range(k):
        for i in range(k):
            if p[i] & (1<<j):p[i]|=p[j]
    if any(i!=j and p[i] & (1<<j) and p[j] & (1<<i) for i in range(k) for j in range(k)):
        return None
    nodes=list(range(k))
    return core_type(p,nodes)


def canon(r):
    n=len(r);best=None
    for p in itertools.permutations(range(n)):
        sig=tuple(sum(1<<j for j in range(n) if r[p[i]] & (1<<p[j])) for i in range(n))
        if best is None or sig<best:best=sig
    return best


def main():
    for n in range(1,6):
        ct=Counter(); pc=0
        for r in posets(n):
            pc+=1;nodes=beat_reduced(r)
            ct[core_type(r,nodes)]+=1
        assert all(not k.startswith('other') for k in ct), (n,ct)
        print('size',n,'extension-labeled posets',pc,'Stong core types',dict(sorted(ct.items())))
    n=6; candidates=[];ct6=0
    for r in posets(n):
        ct6+=1
        pairs=itertools.combinations(range(n),2)
        qs={'K23':[],'K32':[]}
        for a,b in pairs:
            tp=quotient_type(r,a,b)
            if tp in qs:qs[tp].append((a,b))
        if qs['K23'] and qs['K32']:
            edges=[(i,j) for i in range(n) for j in range(n) if i!=j and r[i] & (1<<j)]
            # All such witnesses necessarily turn out bipartite; then H1 rank is |E|-|V|+1.
            assert all(not(r[i]&(1<<j) and r[j]&(1<<k) and i!=j and j!=k and i!=k) for i in range(n) for j in range(n) for k in range(n))
            assert component_count(r,list(range(n)))==1
            beta1=len(edges)-n+1
            candidates.append((r,qs,beta1,edges))
    cc=Counter((canon(r),b) for r,q,b,edges in candidates)
    assert ct6==4824,(ct6,)
    assert len(cc)==3,len(cc)
    betas=Counter({b:sum(m for (key,x),m in cc.items() if x==b) for b in (2,3,4)})
    assert betas=={2:22,3:10,4:1},betas
    winners=[(r,q,edges) for r,q,b,edges in candidates if b==2]
    assert len({canon(r) for r,q,edges in winners})==1
    for r,q,edges in winners:
        assert len(q['K23'])==len(q['K32'])==1
    print('size 6 posets',ct6,'both K23/K32 quotient: 33 linear-extension representatives')
    print('by rank 2,3,4:',dict(sorted(betas.items())))
    print('isomorphism types by rank:',{b:sum(1 for (k,x) in cc if x==b) for b in betas})
    print('rank-2 witness edges',edges,'quotient pairs',q)
    print('PASS')

if __name__=='__main__':main()
