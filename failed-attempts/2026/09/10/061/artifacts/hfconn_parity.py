import math
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
    Delta=[]
    for n in range(N0+1):
        inS=n in Sset; inQ=(N0-n) in Sset
        Delta.append(1 if inS else (-1 if inQ else 0))
    tau=[0]*(N0+2)
    for n in range(N0+1): tau[n+1]=tau[n]+Delta[n]
    return N0,S,Delta,tau

def bars_from_tau(tau):
    """Superlevel merge on tau (birth at local maxima/high, merge at minima/low).
    Each merge of comps with tips t1,t2 at base b produces a bar [b, min(t1,t2)) (upward).
    Returns list of (base, tip)."""
    n=len(tau)
    order=sorted(range(n), key=lambda i:(-tau[i],i))
    parent=list(range(n)); active=[False]*n; tip={}
    def find(a):
        while parent[a]!=a: parent[a]=parent[parent[a]]; a=parent[a]
        return a
    import itertools
    bars=[]
    for level,grp in itertools.groupby(order, key=lambda i:tau[i]):
        grp=list(grp)
        for i in grp: active[i]=True; parent[i]=i; tip[i]=level
        for i in grp:
            for nb in (i-1,i+1):
                if 0<=nb<n and active[nb]:
                    ri=find(i); rn=find(nb)
                    if ri!=rn:
                        t1=tip[ri]; t2=tip[rn]
                        bars.append((level, min(t1,t2)))
                        parent[rn]=ri; tip[ri]=max(t1,t2)
    return bars

def hfconn(tau):
    bars=bars_from_tau(tau)
    from collections import Counter
    c=Counter(bars)
    odd=[b for b,m in c.items() if m%2==1]
    return bars,c,odd

for r in [5,7,11,13,17,19,23,25,29,31,37]:
    if math.gcd(r,18)!=1: continue
    N0,S,Delta,tau=delta_tau(2,9,r)
    bars,c,odd=hfconn(tau)
    print(f"r={r} N0={N0} tauMin={min(tau)} nBars={len(bars)} distinct={len(c)}")
    print(f"   bar mult: {sorted(c.items())}")
    print(f"   ODD (HF_conn survivors): {sorted(odd)}")
