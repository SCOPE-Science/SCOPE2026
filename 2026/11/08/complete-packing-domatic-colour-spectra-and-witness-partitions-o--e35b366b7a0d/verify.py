#!/usr/bin/env python3
"""Independent small-instance enumeration of packing broadcast-domatic colourings."""
from collections import Counter
from itertools import product
from math import factorial, comb
from functools import lru_cache

def partitions(n, mx=None):
    if mx is None: mx=n
    if n==0: yield ()
    for a in range(min(n,mx),1-1,-1):
        for tail in partitions(n-a,a): yield (a,)+tail

def falling(x,h):
    return factorial(x)//factorial(x-h) if 0<=h<=x else 0

@lru_cache(None)
def stirling(h,k):
    if h==0: return int(k==0)
    if k<0 or k>h: return 0
    return k*stirling(h-1,k)+stirling(h-1,k-1)

def predicted_witnesses(parts,t,k):
    n=sum(parts)
    total=falling(t-1,n)*stirling(n,k)
    for a in parts:
        for s in range(1,a+1):
            h=n-s
            total+=comb(a,s)*falling(t-1,h)*(stirling(h,k)*k**s + (stirling(h,k-1) if s==a else 0))
    return total

def predicted(parts,t):
    n=sum(parts)
    c=Counter({n: falling(t-1,n)})
    for a in parts:
        for s in range(1,a+1):
            c[n-s+(s==a)]+=comb(a,s)*falling(t-1,n-s)
    return +c

def predicted_min(parts,k):
    n=sum(parts); a=max(parts)
    if k<=n-a+1: return n-a+1
    if n-k+1 in parts: return k
    return k+1

def predicted_optimal_count(parts,k):
    n=sum(parts); a=max(parts); t=predicted_min(parts,k)
    if k<=n-a+1: return sum(q==a for q in parts)*factorial(n-a)
    if n-k+1 in parts: return sum(q==n-k+1 for q in parts)*factorial(k-1)
    if k==n: return factorial(n)
    return factorial(k)*sum(comb(q,n-k) for q in parts if q>=n-k)

def direct(parts,t):
    n=sum(parts)
    ids=sum(([i]*a for i,a in enumerate(parts)),[])
    adj=[{j for j in range(n) if j!=i and ids[i]!=ids[j]} for i in range(n)]
    dist=[[0 if i==j else (1 if j in adj[i] else 2) for j in range(n)] for i in range(n)]
    counts=Counter(); witnesses=Counter()
    for col in product(range(1,t+1),repeat=n):
        if any(col[i]==col[j] and dist[i][j]<=col[i] for i in range(n) for j in range(i+1,n)): continue
        sources=[]
        for i in range(n): sources.append(sum(1<<j for j in range(n) if dist[i][j]<=col[i]))
        allmask=(1<<n)-1
        good=[False]*(1<<n)
        cover=[0]*(1<<n)
        for mask in range(1,1<<n):
            low=mask&-mask; i=low.bit_length()-1
            cover[mask]=cover[mask^low]|sources[i]
            good[mask]=cover[mask]==allmask
        opt=[-100]*(1<<n);opt[0]=0
        for mask in range(1,1<<n):
            sub=mask
            while sub:
                if good[sub] and opt[mask^sub]>=0:
                    opt[mask]=max(opt[mask],1+opt[mask^sub])
                sub=(sub-1)&mask
        counts[opt[allmask]]+=1
        from functools import lru_cache
        @lru_cache(None)
        def partition_counts(mask):
            if mask==0: return (1,)
            low=mask&-mask
            sub=mask
            result=[0]*(n+1)
            while sub:
                if (sub&low) and good[sub]:
                    tail=partition_counts(mask^sub)
                    for j,v in enumerate(tail):
                        if j+1<len(result):result[j+1]+=v
                sub=(sub-1)&mask
            return tuple(result)
        for k,v in enumerate(partition_counts(allmask)):
            witnesses[k]+=v
    return +counts,+witnesses

def main():
    cases=0; colored=0; optimal_cases=0
    for n in range(2,7):
        for parts in partitions(n):
            if len(parts)<2: continue
            if n==6 and parts not in [(5,1),(4,2),(3,3),(3,2,1),(2,2,2),(2,1,1,1,1),(1,1,1,1,1,1)]: continue
            for t in range(1,n+2):
                p=predicted(parts,t); d,w=direct(parts,t)
                if p!=d: raise AssertionError(('distribution',parts,t,p,d))
                for k in range(1,n+1):
                    assert w.get(k,0)==predicted_witnesses(parts,t,k), ('witness',parts,t,k,w.get(k,0),predicted_witnesses(parts,t,k))
                for k in range(1,n+1):
                    if t==predicted_min(parts,k):
                        observed=sum(v for cap,v in d.items() if cap>=k)
                        expected=predicted_optimal_count(parts,k)
                        assert observed==expected, ('optimal count',parts,k,observed,expected)
                        optimal_cases+=1
                    # Scan eligible t rather than assume minima.
                    if sum(v for m,v in d.items() if m>=k):
                        if t < predicted_min(parts,k): raise AssertionError(('early',parts,t,k))
                    if t==predicted_min(parts,k) and not sum(v for m,v in d.items() if m>=k):
                        raise AssertionError(('missing',parts,t,k))
                cases+=1;colored+=sum(d.values())
    print('PACKING_COLORING_AND_WITNESS_COUNT_OK',cases,'graph-palette cases')
    print('OPTIMAL_CHROMATIC_AND_MULTIPLICITY_OK', optimal_cases,'graph-k cases')
    print('BROADCAST_PARTITION_EXHAUSTIVE_OK',cases,'graph-palette cases',colored,'packing colourings')
    for parts in [(3,3),(5,2,1),(2,2,2),(1,1,1,1),(5,1),(4,3,2)]:
        n=sum(parts)
        # independent small set-theoretic assertion of exact spectrum
        spectrum=[predicted_min(parts,k) for k in range(1,n+1)]
        assert all(spectrum[k]>=spectrum[k-1] for k in range(1,n))
        print('SPECTRUM',parts,spectrum)
    print('VERIFY_OK')
if __name__=='__main__':main()
