"""Standalone verifier: Gram-rank hull cert + full 2^k tally + MacWilliams + Griesmer widths + syndrome spot check.
Usage: python3 verify.py  (reads witnesses.json in same dir)
stdlib only."""
import json, os, sys
from collections import Counter
from math import comb
from itertools import combinations
here = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(here,"witnesses.json")))
def wt(x): return bin(x).count("1")
def rank(rows,nc):
    R=list(rows); r=0
    for c in range(nc):
        p=None
        for i in range(r,len(R)):
            if (R[i]>>c)&1: p=i; break
        if p is None: continue
        R[r],R[p]=R[p],R[r]
        for i in range(len(R)):
            if i!=r and ((R[i]>>c)&1): R[i]^=R[r]
        r+=1
    return r
def griesmer_ub(n,k):
    for d in range(1,n+1):
        if sum((d+(1<<i)-1)//(1<<i) for i in range(k))>n: return d-1
    return n
def kraw(n,j,i): return sum(((-1)**t)*comb(i,t)*comb(n-i,j-t) for t in range(max(0,i+j-n),min(i,j)+1))
def dual_basis(G,n,k):
    A=[[ (G[i]>>c)&1 for c in range(n)] for i in range(k)]
    pivs=[]; r=0
    for c in range(n):
        p=None
        for i in range(r,k):
            if A[i][c]: p=i; break
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        for i in range(k):
            if i!=r and A[i][c]:
                for j in range(c,n): A[i][j]^=A[r][j]
        pivs.append(c); r+=1
        if r==k: break
    free=[c for c in range(n) if c not in pivs]
    H=[]
    for f in free:
        v=(1<<f)
        for ri,pc in enumerate(pivs):
            if A[ri][f]: v|=(1<<pc)
        H.append(v)
    return H,pivs,free
def tally(rows,n):
    C=Counter()
    for mask in range(1<<len(rows)):
        cw=0
        for i in range(len(rows)):
            if (mask>>i)&1: cw^=rows[i]
        C[wt(cw)]+=1
    return C
fails=0
gaps={}
for key in sorted(D,key=lambda s:list(map(int,s.split(",")))):
    v=D[key]; n,k,ht=v["n"],v["k"],v["hull_target"]; G=v["G_ints"]
    assert len(G)==k and rank(G,n)==k, f"{key}: generator rank deficient"
    A=tally(G,n)
    assert sum(A.values())==1<<k, f"{key}: tally sum"
    d=min(w for w in A if w>0)
    M=[]
    for i in range(k):
        row=0
        for j in range(k):
            if wt(G[i]&G[j])&1: row|=(1<<j)
        M.append(row)
    rk=rank(M,k); h=k-rk
    H,_,_=dual_basis(G,n,k)
    assert len(H)==n-k
    B=tally(H,n)
    Av=[A.get(i,0) for i in range(n+1)]; Bv=[B.get(i,0) for i in range(n+1)]
    mac=all(sum(Av[i]*kraw(n,j,i) for i in range(n+1))==(1<<k)*Bv[j] for j in range(n+1))
    ub=griesmer_ub(n,k)
    s_ok=(d==v["d"] and h==v["h"]==ht and mac)
    # syndrome distinct-error check for n<=20
    syn="skip(n>20)"
    if n<=20:
        t=(d-1)//2
        def syn_e(e):
            s=0
            for j,hh in enumerate(H):
                if wt(e&hh)&1: s|=(1<<j)
            return s
        seen={}; ok=True
        for w in range(t+1):
            for cb in combinations(range(n),w):
                e=0
                for c in cb: e|=(1<<c)
                s=syn_e(e)
                if s in seen: ok=False
                seen[s]=e
        syn=("PASS" if ok else "FAIL"); s_ok=s_ok and ok
    gaps.setdefault((n,k),{})[ht]=d
    print(f"[{n},{k}] h={ht}: d={d} hull={h} rank={rk} MacW={'PASS' if mac else 'FAIL'} GriesUB={ub} width={ub-d} synd={syn} -> {'OK' if s_ok else 'FAIL'}")
    if not s_ok: fails+=1
print("--- gaps d_LCD-d_one per cell ---")
for (n,k),dd in sorted(gaps.items()):
    print(f"[{n},{k}]: d_LCD={dd[0]} d_one={dd[1]} achieved-gap={dd[0]-dd[1]}")
print("VERIFY_OK" if fails==0 else "VERIFY_FAIL")
sys.exit(1 if fails else 0)
