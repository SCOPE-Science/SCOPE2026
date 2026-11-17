"""Finite verification of single-pass critical-mass orbits for complete bipartite graphs."""
from collections import Counter
from math import comb, factorial

def stirling(n,k):
    return sum((-1)**(k-j)*comb(k,j)*j**n for j in range(k+1))//factorial(k)

def compositions(total, slots):
    if slots == 1:
        yield (total,)
        return
    for a in range(total+1):
        for tail in compositions(total-a,slots-1):
            yield (a,)+tail

def step(x,m,n):
    L=x[:m]; R=x[m:]; FL=[int(a>=n) for a in L]; FR=[int(b>=m) for b in R]
    return tuple(a-n*f+sum(FR) for a,f in zip(L,FL))+tuple(b-m*f+sum(FL) for b,f in zip(R,FR))

def count(m,n):
    # All configurations (not just bounded ones) of critical total mass are enumerated.
    mass=m*n
    memo={}
    counts=Counter()
    for s in compositions(mass,m+n):
        if s not in memo:
            walk=[]; seen={}; v=s
            while v not in memo and v not in seen:
                seen[v]=len(walk);walk.append(v);v=step(v,m,n)
            if v in seen:
                entry=seen[v];period=len(walk)-entry
                for i,z in enumerate(walk):memo[z]=(period,max(0,entry-i))
            else:
                period,tail=memo[v]
                for i,z in enumerate(reversed(walk),1):memo[z]=(period,tail+i)
        period,tail=memo[s]
        if tail==0 and period>1:
            v=s;fires=[0]*(m+n)
            for _ in range(period):
                for i,a in enumerate(v):
                    if a >= (n if i<m else m):fires[i]+=1
                v=step(v,m,n)
            assert v==s
            if all(a==1 for a in fires):counts[period]+=1
    expected={2*k:2*factorial(k)**2*stirling(m,k)*stirling(n,k) for k in range(1,min(m,n)+1)}
    assert dict(counts)==expected,(m,n,counts,expected)
    print('K_{%d,%d}: states=%d, single-pass counts=%s'%(m,n,len(memo),dict(sorted(counts.items()))))

for m,n in [(1,1),(1,5),(2,2),(2,3),(2,5),(3,3),(3,4),(3,5),(4,4)]:count(m,n)
print('PASS: all critical-mass configurations in nine graphs independently enumerated')
