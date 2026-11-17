"""Construct explicit optimal cyclic k-path-cover token-slide paths.

Run: python3 verify_geodesic_constructor.py
Deterministic pseudorandom test cases, including orders much larger than enumeration.
"""
from random import Random


def feasible(n, k, x):
    return all(1 <= x[(j+1) % len(x)] + (n if j == len(x)-1 else 0)-x[j] <= k for j in range(len(x)))


def sample_cover(n, k, t, rng):
    gaps = [1]*t
    extra = n-t
    while extra:
        j=rng.randrange(t)
        if gaps[j] < k:
            gaps[j]+=1
            extra-=1
    origin=rng.randrange(n)
    positions=[origin]
    for g in gaps[:-1]:positions.append(positions[-1]+g)
    return {(v%n) for v in positions}


def optimal_route(n,k,S,T):
    pref=0
    levels=[]
    for i in range(n):
        pref += (i in S)-(i in T)
        levels.append(pref)
    med=sorted(levels)[n//2]
    lower_bound=sum(abs(x-med) for x in levels)
    cut=next(i for i in range(n) if levels[i]==med)
    lo=cut+1
    def lift(U):
        return sorted(lo+(p-lo)%n for p in U)
    x=lift(S);y=lift(T)
    z=[max(a,b) for a,b in zip(x,y)]
    assert feasible(n,k,x) and feasible(n,k,y) and feasible(n,k,z)
    count=0
    # A coordinate increment/decrement changes exactly one token via a cycle edge.
    for target,direction in ((z,+1),(y,-1)):
        while x!=target:
            moved=False
            for j in range(len(x)):
                if direction*(target[j]-x[j])<=0:continue
                nxt=x.copy();nxt[j]+=direction
                if min(nxt)<lo or max(nxt)>=lo+n:continue
                if feasible(n,k,nxt):
                    x=nxt; count+=1;moved=True;break
            if not moved:
                raise AssertionError(('stuck', n,k,S,T,x,target))
    if count!=lower_bound:
        raise AssertionError(('wrong length',n,k,S,T,count,lower_bound))
    return count


def main():
    rng=Random(20261103)
    cases=0
    for n in [3,4,5,6,7,8,9,10,11,12,15,17,20,25,30,41,50,75,100]:
        for k in range(2,n):
            choices={((n+k-1)//k),min(n-1, ((n+k-1)//k)+1),n//2,n-1}
            for t in choices:
                if not ((n+k-1)//k <= t < n and k*t>n):continue
                for _ in range(8):
                    S=sample_cover(n,k,t,rng)
                    T=sample_cover(n,k,t,rng)
                    optimal_route(n,k,S,T)
                    cases+=1
    print('CONSTRUCTIVE_GEODESIC_PASS', 'instances=',cases)

if __name__=='__main__':
    main()
