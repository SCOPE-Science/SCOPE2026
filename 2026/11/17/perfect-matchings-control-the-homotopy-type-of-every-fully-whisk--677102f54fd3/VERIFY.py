#!/usr/bin/env python3
"""Exhaustive finite tests of the matching complex of a leaf-extension graph.
All graph inputs are labeled; mathematical proof is independent of these tests.
"""
from itertools import combinations
from collections import defaultdict, deque

def edges(n,mask):
    pairs=list(combinations(range(n),2))
    return [pairs[i] for i in range(len(pairs)) if mask>>i&1]

def pm_count(n,base):
    if n%2: return 0
    adj={v:[] for v in range(n)}
    for u,v in base:
        adj[u].append(v);adj[v].append(u)
    def count(unmatched):
        if not unmatched:return 1
        i=min(unmatched)
        return sum(count(unmatched-{i,j}) for j in adj[i] if j in unmatched)
    return count(set(range(n)))

def faces(n,base):
    # each face as (base-edge index bitset, pendant-edge index bitset)
    b=len(base); inc=[(1<<u)|(1<<v) for u,v in base]
    ans=set()
    def extend(i,bits,used):
        if i==b:
            available=[v for v in range(n) if not used>>v&1]
            for mask in range(1<<len(available)):
                pend=sum(1<<v for j,v in enumerate(available) if mask>>j&1)
                ans.add((bits,pend))
            return
        extend(i+1,bits,used)
        if not used & inc[i]: extend(i+1,bits | (1<<i),used|inc[i])
    extend(0,0,0)
    return ans

def paired(n,base,F):
    inc=[(1<<u)|(1<<v) for u,v in base]
    lower={}; higher={}; critical=[]
    for b,p in F:
        used=0
        for j,uv in enumerate(inc):
            if b>>j&1: used|=uv
        available=[v for v in range(n) if not used>>v&1]
        if not available:
            critical.append((b,p));continue
        pivot=available[0]; k=(b,p^(1<<pivot))
        if p>>pivot&1: higher[k]=(b,p)
        else: lower[(b,p)]=k
    assert lower==higher
    assert len(critical)==pm_count(n,base)
    assert all(p==0 and b.bit_count()*2==n for b,p in critical)
    return lower, critical

def check_acyclic(n,base,F,match):
    # directed Forman Hasse diagram: matched arrows up; all other arrows down.
    b=len(base); nodes=list(F); out={f:[] for f in nodes};indeg={f:0 for f in nodes}
    def arrow(x,y):out[x].append(y);indeg[y]+=1
    for f in nodes:
        bm,pm=f
        for i in range(b):
            if bm>>i&1:
                g=(bm^(1<<i),pm)
                assert g in F
                arrow(f,g)
        for j in range(n):
            if pm>>j&1:
                g=(bm,pm^(1<<j))
                assert g in F
                if match.get(g)==f:arrow(g,f)
                else:arrow(f,g)
    dq=deque(f for f in nodes if indeg[f]==0); seen=0
    while dq:
        f=dq.popleft();seen+=1
        for g in out[f]:
            indeg[g]-=1
            if indeg[g]==0:dq.append(g)
    assert seen==len(F),(n,base,len(F)-seen)

def ranks_mod2(n,base,F):
    grades=defaultdict(list)
    for b,p in F:grades[b.bit_count()+p.bit_count()-1].append((b,p))
    ranks={}
    for d in sorted(grades):
        if d<0:continue
        lower={f:i for i,f in enumerate(grades[d-1])}
        pivots={};rank=0
        for b,p in grades[d]:
            x=0
            for j in range(len(base)):
                if b>>j&1:x ^= 1<<lower[(b^(1<<j),p)]
            for j in range(n):
                if p>>j&1:x ^= 1<<lower[(b,p^(1<<j))]
            while x:
                bit=x.bit_length()-1
                if bit in pivots:x^=pivots[bit]
                else:pivots[bit]=x;rank+=1;break
        ranks[d]=rank
    return {d:len(grades[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in grades if d>=0}

def run():
    examples=0;acyclic=0;rank_tests=0
    # Every labeled graph on at most four vertices.
    for n in range(1,6):
        for mask in range(1<< (n*(n-1)//2)):
            base=edges(n,mask);F=faces(n,base);matching,crit=paired(n,base,F)
            check_acyclic(n,base,F,matching);acyclic+=1
            pm=pm_count(n,base)
            if n>=2:
                betti=ranks_mod2(n,base,F)
                pred={d:(pm if n%2==0 and d==n//2-1 else 0) for d in betti}
                assert betti==pred,(n,base,betti,pred)
                rank_tests+=1
            examples+=1
    for n in (6,7,8):
        allmask=(1<<(n*(n-1)//2))-1
        masks=[0,allmask]
        for kind in ('path','cycle','star'):
            ed=[]
            if kind in ('path','cycle'):ed=[(i,i+1) for i in range(n-1)]
            if kind=='cycle':ed.append((0,n-1))
            if kind=='star':ed=[(0,i) for i in range(1,n)]
            pairs=list(combinations(range(n),2))
            masks.append(sum(1<<pairs.index(tuple(sorted(e))) for e in ed))
        for mask in masks:
            base=edges(n,mask);F=faces(n,base);pair,crit=paired(n,base,F)
            if n<=6:
                check_acyclic(n,base,F,pair);acyclic+=1
            if n<=6:
                betti=ranks_mod2(n,base,F)
                pred={d:(pm_count(n,base) if n%2==0 and d==n//2-1 else 0) for d in betti}
                assert betti==pred,(n,base,betti,pred);rank_tests+=1
            examples+=1
    print('VERIFIED_GRAPH_INPUTS',examples)
    print('EXPLICIT_ACYCLIC_HASSE_CHECKS',acyclic)
    print('INDEPENDENT_MOD2_HOMOLOGY_CHECKS',rank_tests)
    print('SUNLET_CYCLE_N4_TO_N8',[(n,pm_count(n,[(i,(i+1)%n) for i in range(n)])) for n in range(4,9)])
    print('VERIFY_OK')
if __name__=='__main__':run()
