#!/usr/bin/env python3
"""Standalone checker for Bernoulli approval and SJR/SSJR feasibility bounds.
No external dependencies. All computations are exact integers/Fractions.
"""
from itertools import product, combinations
from math import comb
from fractions import Fraction

def check_profile(ballots,m,k):
    n=len(ballots)
    candidates=range(m)
    supports=[set(i for i,a in enumerate(ballots) if (a>>c)&1) for c in candidates]
    cohesive={c for c in candidates if len(supports[c])*k>=n}
    private={c for c in candidates if any(a==(1<<c) for a in ballots)}
    # Every cohesive group is a subset of N_c for some cohesive c; SJR is
    # equivalent to N_c sharing an elected candidate; SSJR to N_c covered.
    sjr=False; ssjr=False; nsjr=0; nssjr=0
    for W in combinations(candidates,k):
        sjr_here=all(any(supports[c]<=supports[d] for d in W) for c in cohesive)
        ssjr_here=all(all(any(i in supports[d] for d in W) for i in supports[c]) for c in cohesive)
        # Independently verify the reduction using all cohesive voter groups.
        # This check is finite and is not itself the proof of the theorem.
        required=(n+k-1)//k
        direct_sjr=True; direct_ssjr=True
        for Gbits in range(1,1<<n):
            if Gbits.bit_count()<required: continue
            group=[i for i in range(n) if (Gbits>>i)&1]
            common=(1<<m)-1
            for i in group: common &= ballots[i]
            if not common: continue
            if not any(common&(1<<c) for c in W): direct_sjr=False
            if not all(any(ballots[i]&(1<<c) for c in W) for i in group): direct_ssjr=False
        assert direct_sjr==sjr_here and direct_ssjr==ssjr_here
        sjr |= sjr_here
        ssjr |= ssjr_here
        nsjr += int(sjr_here)
        nssjr += int(ssjr_here)
    basic=(len(cohesive)<=k)
    assert (not basic) or (sjr and ssjr)
    if len(private)==m:
        assert (sjr==basic and ssjr==basic)
        count=comb(m-len(cohesive),k-len(cohesive)) if basic else 0
        assert nsjr == nssjr == count
    assert not sjr or ssjr
    return int(basic),int(sjr),int(ssjr),len(private)==m

def exhaustive():
    results=[]
    for m,k,n in [(3,2,1),(3,2,2),(3,2,3),(3,2,4),(4,2,2),(4,2,3),(4,2,4),(4,3,3)]:
        freq=[0,0,0,0]; counts=0
        for ballots in product(range(1<<m),repeat=n):
            r=check_profile(ballots,m,k)
            freq=[v+u for v,u in zip(freq,map(int,r))]; counts+=1
        # q=1/2, each profile equally likely; compute the binomial tail baseline
        b=sum(comb(n,i) for i in range((n+k-1)//k,n+1))
        prob=Fraction(b,2**n)
        p_baseline=sum(comb(m,j)*prob**j*(1-prob)**(m-j) for j in range(k+1))
        assert p_baseline==Fraction(freq[0],counts)
        # Union bound for missing singleton approval ballots: r=1/2^m.
        delta=m*Fraction((2**m-1)**n, (2**m)**n)
        assert Fraction(freq[1]-freq[0],counts)<=delta
        assert Fraction(freq[2]-freq[0],counts)<=delta
        results.append((m,k,n,counts,tuple(freq),str(p_baseline),str(delta)))
    return results
if __name__=='__main__':
    for r in exhaustive(): print('PASS',*r)
    print('ALL_EXHAUSTIVE_CHECKS_PASS')
