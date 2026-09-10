#!/usr/bin/env python3
"""Lane-486 TARGET probe P2: best single-vertex non-neighborhood factor in PRIME P5-free n<=6.
For each prime P5-free G: f(G)=max_v |M_v|/n (M_v = non-neighbours of v, excl. v).
Report min f over primes (worst case = densest prime) + the extremal graphs.
Also min dominating-clique size and max-degree window stats.
Stdlib only.
"""
import itertools
LOG=[]
def log(s): LOG.append(s); print(s, flush=True)
def all_adjs(n):
    m=n*(n-1)//2; pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    for bits in range(1<<m):
        adj=[0]*n
        for k,(i,j) in enumerate(pairs):
            if (bits>>k)&1: adj[i]|=(1<<j); adj[j]|=(1<<i)
        yield adj
def popcount(x): return bin(x).count("1")
def hasP5(adj, n):
    verts=list(range(n))
    for sub in itertools.combinations(verts,5):
        mask=0
        for v in sub: mask|=(1<<v)
        if sum(popcount(adj[v]&mask) for v in sub)//2!=4: continue
        seen={sub[0]}; stack=[sub[0]]
        while stack:
            v=stack.pop()
            for u in sub:
                if u not in seen and (adj[v]>>u)&1: seen.add(u); stack.append(u)
        if len(seen)!=5: continue
        if all(popcount(adj[v]&mask)<=2 for v in sub): return True
    return False
def prime(adj,n):
    if n<=2: return False
    full=(1<<n)-1; comp=[full^(1<<v)^adj[v] for v in range(n)]
    for A in (adj,comp):
        seen={0}; stack=[0]
        while stack:
            v=stack.pop()
            for u in range(n):
                if u not in seen and (A[v]>>u)&1: seen.add(u); stack.append(u)
        if len(seen)!=n: return False
    for r in range(2,n):
        for sub in itertools.combinations(range(n),r):
            s=set(sub); ok=True
            for x in range(n):
                if x in s: continue
                d=sum(1 for v in sub if (adj[x]>>v)&1)
                if d not in (0,r): ok=False; break
            if ok: return False
    return True
for n in range(4,7):
    minf=2.0; minex=None; mindom=n+1; maxdeg_min=n
    cnt=0
    for adj in all_adjs(n):
        if n>=5 and hasP5(adj,n): continue
        if not prime(adj,n): continue
        cnt+=1
        full=(1<<n)-1
        f=max(popcount(full^(1<<v)^adj[v]) for v in range(n))/n
        if f<minf-1e-12: minf=f; minex=adj[:]
        # dominating clique number (min over? report max? we want min dominating clique size)
        best=n+1
        for r in range(1,n+1):
            done=False
            for K in itertools.combinations(range(n),r):
                mask=0
                for v in K: mask|=(1<<v)
                if sum(popcount(adj[v]&mask) for v in K)//2!=r*(r-1)//2: continue
                s=set(K)
                if all(x in s or any((adj[x]>>v)&1 for v in K) for x in range(n)):
                    best=r; done=True; break
            if done: break
        mindom=min(mindom,best)
        maxdeg_min=min(maxdeg_min,max(popcount(a) for a in adj))
    log(f"n={n}: primes={cnt} min_v_max|M_v|/n={minf:.4f} extremal_adj={minex} min_dom_clique={mindom} min_possible_maxdeg={maxdeg_min}")
    # stall threshold with this f at c=1/8,k=1: N=(1/(1-f^c))^8
    c=1/8
    N=(1/(1-minf**c))**8
    log(f"   one-step stall N(f={minf:.4f},c=1/8,k=1) = {N:.3g} (argument dies past this n)")
log("P2PROBE_OK")
with open("output/artifacts/p2probe.log","w") as f: f.write("\n".join(LOG)+"\n")
