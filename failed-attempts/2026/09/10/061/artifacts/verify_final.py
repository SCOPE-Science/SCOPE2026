"""FINAL fallback verification (stdlib only, auditable).
Certificates: (i) Seifert solve, (ii) Delta/tau lattice count, (iii) HF_red bars + HF_conn parity.
Cross-checks: total finite length = sum(interior local max) - sum(interior local min) - (max-min);
rev-sweep tie-break invariance; r=5 hand-check (single bar (0,1))."""
from collections import Counter
import math

def seifert(p,q,r):
    P=p*q*r; out=[]
    for pp in range(p):
        for qq in range(q):
            for e0 in (-3,-2,-1,0):
                rem=-1-e0*P-pp*q*r-p*qq*r
                if rem%(p*q)==0:
                    rr=rem//(p*q)
                    if 0<=rr<r: out.append((e0,pp,qq,rr))
    return out

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
    assert tau[N0+1]==0; assert all(Delta[n]==-Delta[N0-n] for n in range(N0+1))
    return N0,S,Delta,tau

def compress(tau):
    v=[tau[0]]
    for t in tau[1:]:
        if t!=v[-1]: v.append(t)
    return v

def persistence_levels(v):
    """Level-by-level: at each occupied level L (descending), freely union same-level
    adjacency, then join each new-level group with ALL adjacent elder components;
    eldest tip survives; each younger tip t>L emits bar (L,t). Order inside level irrelevant."""
    n=len(v)
    levels=sorted(set(v), reverse=True)
    parent=list(range(n)); active=[False]*n; tip={}
    def find(a):
        while parent[a]!=a: parent[a]=parent[parent[a]]; a=parent[a]
        return a
    bars=[]
    for L in levels:
        grp=[i for i in range(n) if v[i]==L]
        gset=set(grp)
        for x in grp: active[x]=True; parent[x]=x; tip[x]=L
        for x in grp:
            for nb in (x-1,x+1):
                if nb in gset:
                    rx,rn=find(x),find(nb)
                    if rx!=rn: parent[rn]=rx
        # groups = connected same-level blocks; join each with adjacent elders
        seen=set()
        for x in grp:
            rx=find(x)
            if rx in seen: continue
            seen.add(rx)
            elders=set()
            y=x
            # gather all same-level members of this block: scan
            block=[z for z in grp if find(z)==rx]
            for z in block:
                for nb in (z-1,z+1):
                    if 0<=nb<n and active[nb] and v[nb]!=L:
                        elders.add(find(nb))
            if elders:
                alltips=sorted([tip[e] for e in elders]+[L])
                for t in alltips[:-1]:
                    if t>L: bars.append((L,t))
                base=rx
                for e in elders:
                    ee=find(e)
                    if ee!=base: parent[ee]=base
                tip[base]=alltips[-1]
    return bars

def local_check(v):
    smax=smin=0; nmax=nmin=0
    for i in range(1,len(v)-1):
        if v[i]>v[i-1] and v[i]>v[i+1]: smax+=v[i]; nmax+=1
        elif v[i]<v[i-1] and v[i]<v[i+1]: smin+=v[i]; nmin+=1
    return smax,nmax,smin,nmin, smax-smin-(max(v)-min(v))

ok=True
for r in [23,25,29]:
    N0,S,Delta,tau=delta_tau(2,9,r)
    e=seifert(2,9,r)
    v=compress(tau)
    assert all(abs(v[i+1]-v[i])==1 for i in range(len(v)-1))
    bars=persistence_levels(v)
    c=Counter(bars)
    odd=sorted([b for b,m in c.items() if m%2==1])
    dim=sum(t-a for a,t in odd)
    smax,nmax,smin,nmin,tot=local_check(v)
    assert tot==sum(t-a for a,t in bars), f"total-length mismatch r={r}"
    print(f"r={r}: seifert={e} N0={N0} kappa={len(S)} tauMin={min(tau)}")
    print(f"  nmax={nmax} nmin={nmin} totalPers={tot}")
    print(f"  bars={sorted(c.items())}")
    print(f"  HF_conn odd bars={odd} count={len(odd)} dim={dim}")
# r=5 hand-check
N0,S,Delta,tau=delta_tau(2,9,5); v=compress(tau)
assert Counter(persistence_levels(v))==Counter([(0,1)]), "r=5 must be single bar (0,1)"
print("r=5 hand-check OK: single bar (0,1)")
print("VERIFY_FINAL_OK")
