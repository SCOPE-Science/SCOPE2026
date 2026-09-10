"""Fallback verification: compressed-tau superlevel bars -> HF_red -> HF_conn (HHL parity).
Same-level adjacency unions are free (no bar); zero-length bars discarded."""
import math
from collections import Counter
import itertools

def semigroup_S(p,q,r):
    pq,pr,qr=p*q,p*r,q*r
    N0=p*q*r-p*q-p*r-q*r
    reach=[False]*(N0+1); reach[0]=True
    for n in range(1,N0+1):
        for g in (pq,pr,qr):
            if n-g>=0 and reach[n-g]: reach[n]=True; break
    S=[n for n in range(N0+1) if reach[n]]
    return N0,S,set(S)

def delta_tau(p,q,r):
    N0,S,Sset=semigroup_S(p,q,r)
    Delta=[1 if n in Sset else (-1 if (N0-n) in Sset else 0) for n in range(N0+1)]
    tau=[0]*(N0+2)
    for n in range(N0+1): tau[n+1]=tau[n]+Delta[n]
    assert tau[N0+1]==0, "closure fail"
    assert all(Delta[n]==-Delta[N0-n] for n in range(N0+1)), "symmetry fail"
    return N0,S,Delta,tau

def compress(tau):
    v=[tau[0]]
    for t in tau[1:]:
        if t!=v[-1]: v.append(t)
    return v

def persistence(v):
    n=len(v)
    order=sorted(range(n), key=lambda i:(-v[i],i))
    parent=list(range(n)); active=[False]*n; tip={}
    def find(a):
        while parent[a]!=a: parent[a]=parent[parent[a]]; a=parent[a]
        return a
    bars=[]
    for level,grp in itertools.groupby(order, key=lambda i:v[i]):
        grp=list(grp)
        for i in grp: active[i]=True; parent[i]=i; tip[i]=level
        # free union within level
        for i in grp:
            for nb in (i-1,i+1):
                if 0<=nb<n and active[nb] and v[nb]==level:
                    ri=find(i); rn=find(nb)
                    if ri!=rn: parent[rn]=ri
        # merge with older (higher-born) components
        for i in grp:
            for nb in (i-1,i+1):
                if 0<=nb<n and active[nb] and v[nb]>level:
                    ri=find(i); rn=find(nb)
                    if ri!=rn:
                        t_new=tip[ri] if tip[ri]==level else tip[ri]
                        # dying tip = min birth; base = level
                        d=min(tip[ri],tip[rn])
                        if d>level: bars.append((level,d))
                        # union keep max birth
                        if tip[ri]>=tip[rn]: parent[rn]=ri; tip[ri]=max(tip[ri],tip[rn])
                        else: parent[ri]=rn; tip[rn]=max(tip[ri],tip[rn])
    return bars

for r in [23,25,29]:
    N0,S,Delta,tau=delta_tau(2,9,r)
    v=compress(tau)
    assert all(abs(v[i+1]-v[i])==1 for i in range(len(v)-1)), "non-unit step"
    bars=persistence(v)
    c=Counter(bars)
    odd=sorted([b for b,m in c.items() if m%2==1])
    dim=sum(t-b for b,t in odd)
    print(f"r={r} N0={N0} kappa={len(S)} tauMin={min(tau)} len(v)={len(v)} nBars={len(bars)}")
    print(f"   bar mult: {sorted(c.items())}")
    print(f"   HF_conn odd bars: {odd} count={len(odd)} totaldim={dim}")
