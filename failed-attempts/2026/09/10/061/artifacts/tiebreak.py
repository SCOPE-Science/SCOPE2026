"""Obviously-correct O(n^2) bars: each interior strict local min b kills the younger
of the two adjacent superlevel components; dying tip = min of side-tips."""
from verify_fallback import delta_tau, compress
from collections import Counter
import math

def bars_bruteforce(v):
    n=len(v)
    bars=[]
    for j in range(1,n-1):
        if not (v[j]<v[j-1] and v[j]<v[j+1]): continue
        b=v[j]
        # left tip: max of v on (i0..j-1) where i0 = last index left with v<=b, exclusive
        i0=j-1
        while i0>=0 and v[i0]>b: i0-=1
        TL=max(v[i0+1:j])
        k0=j+1
        while k0<n and v[k0]>b: k0+=1
        TR=max(v[j+1:k0])
        bars.append((b,min(TL,TR)))
    return bars

for r in [5,7,23,25,29]:
    if math.gcd(r,18)!=1: continue
    N0,S,Delta,tau=delta_tau(2,9,r)
    v=compress(tau)
    bars=bars_bruteforce(v)
    c=Counter(bars)
    odd=sorted([b for b,m in c.items() if m%2==1])
    dim=sum(t-b for b,t in odd)
    tot=sum(t-b for b,t in bars)
    print(f"r={r} nBars={len(bars)} totalLen={tot}")
    print(f"   mult: {sorted(c.items())}")
    print(f"   HF_conn odd: {odd} count={len(odd)} dim={dim}")
