#!/usr/bin/env python3
"""Independent finite tests of the induced-matching enumerators for clique blowups."""
from collections import Counter
from itertools import combinations
from math import comb, ceil, floor

def base_edges(n, mask=None):
    if mask is None:
        return {(i, (i+1)%n) if i < (i+1)%n else ((i+1)%n, i) for i in range(n)}
    all_edges=list(combinations(range(n),2))
    return {edge for k,edge in enumerate(all_edges) if (mask>>k)&1}

def blowup(n, m, bedges):
    N=n*m
    adj=[set() for _ in range(N)]
    for u in range(N):
        for v in range(u+1,N):
            x,y=u//m,v//m
            if x==y or ((min(x,y),max(x,y)) in bedges):
                adj[u].add(v);adj[v].add(u)
    es=[(u,v) for u in range(N) for v in sorted(adj[u]) if u<v]
    return adj,es

def direct_enumerators(n, m, bedges):
    adj,es=blowup(n,m,bedges)
    E=len(es)
    compat=[0]*E
    for i,(u,v) in enumerate(es):
        cmask=0
        for j,(x,y) in enumerate(es):
            if i!=j and len({u,v,x,y})==4 and x not in adj[u] and y not in adj[u] and x not in adj[v] and y not in adj[v]:
                cmask |= 1<<j
        compat[i]=cmask
    allcounts=Counter(); maxcounts=Counter()
    def visit(chosen, candidates, upper):
        k=len(chosen)
        allcounts[k]+=1
        # Extendability tested against every edge, including earlier indexed edges.
        maxable=True
        for j in range(E):
            if j in chosen:continue
            if all((compat[i]>>j)&1 for i in chosen):
                maxable=False;break
        if maxable:maxcounts[k]+=1
        while candidates:
            bit=candidates & -candidates
            j=bit.bit_length()-1
            candidates ^= bit
            visit(chosen+(j,), candidates & compat[j], j+1)
    visit(tuple(), (1<<E)-1, 0)
    return allcounts,maxcounts

def projected_enumerators(n,m,bedges):
    a=comb(m,2); b=m*m
    adj=[set() for _ in range(n)]
    for i,j in bedges:adj[i].add(j);adj[j].add(i)
    allc=Counter();maxc=Counter()
    for mask in range(1<<n):
        S=[i for i in range(n) if mask>>i&1]
        deg=[len(adj[i].intersection(S)) for i in S]
        if any(d>1 for d in deg):continue
        c1=sum(d==0 for d in deg); c2=sum(d==1 for d in deg)//2
        k=c1+c2
        weight=a**c1*b**c2
        allc[k]+=weight
        if all(i in S or any(j in S for j in adj[i]) for i in range(n)):
            maxc[k]+=weight
    return allc,maxc

def transfer_trace(n,m,maximal):
    # 2-bit de Bruijn automaton; polynomial coefficient lists, no symbolic dependency.
    states=[(0,0),(0,1),(1,0),(1,1)]
    a,b=comb(m,2),m*m
    trans=[]
    for i,(u,v) in enumerate(states):
        for j,(v2,w) in enumerate(states):
            if v!=v2 or (u==v==w==1) or (maximal and (u==v==w==0)):continue
            if v==1 and w==0:
                trans.append((i,j,1,b if u==1 else a))
            else:
                trans.append((i,j,0,1))
    result=Counter()
    for start in range(4):
        v={(start,0):1}
        for _ in range(n):
            out=Counter()
            for (state,k),cnt in v.items():
                for i,j,degree,wt in trans:
                    if i==state:out[(j,k+degree)]+=cnt*wt
            v=out
        for (state,k),cnt in v.items():
            if state==start:result[k]+=cnt
    return result

def formula_max(n,m):
    a,b=comb(m,2),m*m
    out=Counter()
    for k in range(ceil(n/4),floor(n/2)+1):
        numerator=0
        for p in range(max(0,n-3*k),min(k,n-2*k)+1):
            q=n-2*k-p
            numerator+=comb(k,p)*comb(k,q)*a**(k-p)*b**p
        assert (n*numerator)%k==0
        out[k]=n*numerator//k
    return out

def main():
    total=cases=0
    for n in range(1,5):
        for mask in range(1<<comb(n,2)):
            for m in (2,3):
                e=base_edges(n,mask)
                got=direct_enumerators(n,m,e)
                expected=projected_enumerators(n,m,e)
                assert got==expected,(n,m,mask,got,expected)
                total+=sum(got[0].values());cases+=1
    cyc=0
    for n in range(3,10):
        for m in ((2,3) if n<=6 else (2,)):
            e=base_edges(n)
            direct=direct_enumerators(n,m,e)
            proj=projected_enumerators(n,m,e)
            ta=transfer_trace(n,m,False)
            tm=transfer_trace(n,m,True)
            fm=formula_max(n,m)
            assert direct==(ta,tm)==proj==(proj[0],fm),(n,m,direct,proj,ta,tm,fm)
            assert set(tm)==set(range(ceil(n/4),floor(n/2)+1))
            cyc+=1;total+=sum(direct[0].values())
    # Independent arithmetic for all n <= 64, m <= 8
    test=0
    for n in range(3,65):
        for m in range(2,9):
            assert transfer_trace(n,m,True)==formula_max(n,m)
            test+=1
    print(f"VERIFY_OK base_profiles={cases} cycle_profiles={cyc} independent_edge_matchings={total} transfer_formula_cases={test} direct_all_and_maximal=PASS maximal_spectrum=PASS")

if __name__=="__main__":
    main()
