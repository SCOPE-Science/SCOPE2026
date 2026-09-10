"""Correct superlevel persistence for compressed tau (strict +-1 alternation).
Rule per activation group at level L: union same-level adjacency freely (tip L),
then join ALL adjacent higher components + self; keep eldest tip; emit (L,t) for each younger t>L."""
from verify_fallback import delta_tau, compress
from collections import Counter
import math

def persistence(v, rev=False):
    n=len(v)
    order=sorted(range(n), key=lambda i:((-v[i] if not rev else v[i]), (i if not rev else -i)))
    parent=list(range(n)); active=[False]*n; tip={}
    def find(a):
        while parent[a]!=a: parent[a]=parent[parent[a]]; a=parent[a]
        return a
    bars=[]; i=0
    while i<n:
        j=i
        L=v[order[i]]
        grp=[]
        while j<n and v[order[j]]==L: grp.append(order[j]); j+=1
        gset=set(grp)
        for x in grp: active[x]=True; parent[x]=x; tip[x]=L
        for x in grp:  # same-level unions
            for nb in (x-1,x+1):
                if nb in gset:
                    rx,rn=find(x),find(nb)
                    if rx!=rn: parent[rn]=rx
        # collect adjacent higher components
        roots=set()
        for x in grp:
            for nb in (x-1,x+1):
                if 0<=nb<n and active[nb] and v[nb]!=L:
                    roots.add(find(nb))
        if roots:
            selfr=find(grp[0])
            alltips=sorted([tip[r] for r in roots]+[L])
            eldest=alltips[-1]
            for t in alltips[:-1]:
                if t>L: bars.append((L,t))
            # union all into one with eldest tip
            base=selfr
            for r in roots:
                rr=find(r)
                if rr!=base: parent[rr]=base
            tip[base]=eldest
        i=j
    return bars

for r in [5,7,11,13,17,19,23,25,29,31,37]:
    if math.gcd(r,18)!=1: continue
    N0,S,Delta,tau=delta_tau(2,9,r)
    v=compress(tau)
    b1=Counter(persistence(v)); b2=Counter(persistence(v,rev=True))
    assert b1==b2, f"TIE-DEPENDENCE at r={r}: {b1} vs {b2}"
    odd=sorted([b for b,m in b1.items() if m%2==1])
    dim=sum(t-a for a,t in odd)
    tot=sum(t-a for a,t in b1.elements())
    print(f"r={r} N0={N0} kap={len(S)} tmin={min(tau)} nbars={sum(b1.values())} totLen={tot}")
    print(f"   mult={sorted(b1.items())}")
    print(f"   HF_conn odd={odd} count={len(odd)} dim={dim}  [tie-break independent]")
