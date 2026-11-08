#!/usr/bin/env python3
"""Standalone exhaustive verifier for bouquet-of-cliques geodesic-transversal formulas.
No external packages required. All graphs small; computations are cross-checks, not an infinite proof.
"""
from collections import deque,Counter
from itertools import product,combinations
from math import prod

def graph(profile):
    sizes=list(profile); N=sum(sizes); V=range(N+1); hub=N
    part=[]; k=0
    for i,s in enumerate(sizes):
        part += [i]*s
    edges=[]; adj=[set() for _ in V]
    for u,v in combinations(V,2):
        if u==hub or v==hub or part[u]==part[v]:
            adj[u].add(v);adj[v].add(u); edges.append((u,v))
    return adj, part, hub

def paths_between(adj,s,t):
    dist={s:0}; q=deque([s]); ways={s:[(s,)]}
    while q:
        v=q.popleft()
        for w in adj[v]:
            if w not in dist:
                dist[w]=dist[v]+1;ways[w]=[];q.append(w)
            if dist[w]==dist[v]+1:
                ways[w]+=[p+(w,) for p in ways[v]]
    return ways[t]

def maximal_geodesics(adj):
    allpaths=[]
    for u,v in combinations(range(len(adj)),2):
        allpaths.extend(paths_between(adj,u,v))
    def proper_subpath(p,q):
        if len(p)>=len(q):return False
        for z in (p,p[::-1]):
            for a in range(len(q)-len(p)+1):
                if tuple(z)==q[a:a+len(p)]:return True
        return False
    return [p for p in allpaths if not any(proper_subpath(p,q) for q in allpaths)]

def gf2rank(columns):
    piv={}
    for v in columns:
        while v:
            j=v.bit_length()-1
            if j not in piv: piv[j]=v;break
            v^=piv[j]
    return len(piv)

def reduced_betti(faces):
    # faces are integer masks including 0, connectedness through H0 reduced differential
    maxdim=max(m.bit_count()-1 for m in faces)
    fs=[sorted(m for m in faces if m.bit_count()==k+1) for k in range(maxdim+1)]
    ranks=[]
    for k in range(1,maxdim+1):
        row={m:i for i,m in enumerate(fs[k-1])}
        vecs=[]
        for f in fs[k]:
            col=0
            for j in range(f.bit_length()):
                if f>>j&1: col^=1<<row[f^(1<<j)]
            vecs.append(col)
        ranks.append(gf2rank(vecs))
    betti=[]
    for k in range(maxdim+1):
        rlow=ranks[k-1] if k>0 else 1
        rhi=ranks[k] if k<maxdim else 0
        betti.append(len(fs[k])-rlow-rhi)
    return betti

def check(profile):
    adj,parts,hub=graph(profile); sz=len(adj); N=hub;r=len(profile)
    geods=maximal_geodesics(adj)
    observed={frozenset(p) for p in geods}
    expected=set()
    for i,s in enumerate(profile):
        vs=[j for j in range(N) if parts[j]==i]
        expected.update(frozenset(x) for x in combinations(vs,2))
    for x,y in combinations(range(N),2):
        if parts[x]!=parts[y]:expected.add(frozenset((x,hub,y)))
    assert observed==expected,(profile,observed^expected)
    forb=[sum(1<<v for v in h) for h in observed]
    valid=[m for m in range(1<<sz) if not any((m&e)==e for e in forb)]
    predicted=[m for m in range(1<<sz) if all(sum(bool(m>>x&1) for x in range(N) if parts[x]==i)<=1 for i in range(r)) and (not m>>hub&1 or sum(bool(m>>x&1) for x in range(N))<=1)]
    assert valid==predicted,(profile,'avoid')
    fset=set(valid)
    facets={m for m in valid if all(m | (1<<v) not in fset for v in range(sz) if not(m>>v&1))}
    fs=Counter((sz-m.bit_count()) for m in facets)
    assert fs==Counter({N+1-r:prod(profile),N-1:N}) if r!=2 else fs==Counter({N-1:prod(profile)+N})
    bet=Counter({1:N-1}); b=prod(s-1 for s in profile)
    if b:bet[r-1]+=b
    observed_b=Counter({i:x for i,x in enumerate(reduced_betti(valid)) if x})
    assert observed_b==bet,(profile, observed_b,bet)
    return sz,len(geods),len(valid),len(facets)

def main():
    out=[]
    for r in range(2,5):
        for profile in product(range(1,4),repeat=r):
            if sum(profile)>9:continue
            out.append((profile,check(profile)))
    print('VERIFY_OK profiles=%d masks=%d maximal_geodesics=PASS minimal_transversals=PASS face_complex=PASS mod2_homology=PASS' %(len(out),sum(1<<x[1][0] for x in out)))
if __name__=='__main__':main()
