"""Exhaustive finite verification of nested supports and the adaptive peeling tree.
No third-party dependencies. Execute: python check_single_peaked.py
"""
from itertools import product, combinations
from math import comb
from collections import defaultdict


def votes(n):
    out=[]
    for bits in product((0,1), repeat=max(n-1,0)):
        lo, hi=0,n-1
        worst=[]
        for b in bits:
            if b==0:
                worst.append(lo); lo+=1
            else:
                worst.append(hi); hi-=1
        worst.append(lo)
        out.append(tuple(reversed(worst)))
    return out


def signatures(n):
    queries=list(combinations(range(n),2))
    vals=[]
    for vote in votes(n):
        ranks={v:i for i,v in enumerate(vote)}
        vals.append(sum((1<<j) for j,(a,b) in enumerate(queries) if ranks[a]<ranks[b]))
    return queries,vals


def nested(pairs):
    ordered=sorted(pairs,key=lambda p:p[0])
    return all(ordered[j][0]<ordered[j+1][0] and ordered[j+1][1]<ordered[j][1] for j in range(len(ordered)-1))


def shat(vals,inds):
    found=set()
    for h in vals:
        s=sum(((h>>i)&1)<<j for j,i in enumerate(inds))
        found.add(s)
        if len(found)==(1<<len(inds)):return True
    return False


def strong(vals,inds,total_q):
    mask=sum(1<<i for i in inds)
    groups=defaultdict(set)
    for h in vals:
        p=sum(((h>>i)&1)<<j for j,i in enumerate(inds))
        groups[h&~mask].add(p)
    return any(len(s)==(1<<len(inds)) for s in groups.values())


def check():
    checked=0
    for n in range(1,9):
        qs,vs=signatures(n)
        assert len(vs)==2**max(n-1,0)
        assert len(set(vs))==len(vs)
        counts=[]
        for k in range(n//2+2):
            ok=0
            for inds in combinations(range(len(qs)),k):
                pairs=[qs[i] for i in inds]
                theoretical=nested(pairs)
                actual=shat(vs,inds)
                assert theoretical==actual,(n,pairs,'shat mismatch')
                if actual:
                    ok+=1
                    assert strong(vs,inds,len(qs)),(n,pairs,'strong mismatch')
                checked+=1
            assert ok==(comb(n,2*k) if 2*k<=n else 0),(n,k,ok)
            counts.append(ok)
        assert sum(counts)==2**max(n-1,0)
        print(f'n={n}; shattered_support_counts={counts}; concepts={len(vs)}')

    # The balanced extreme-pair decision tree has every binary outcome
    # path and identifies each vote uniquely at depth n-1.
    for n in range(1,13):
        for vote in votes(n):
            rank={a:i for i,a in enumerate(vote)}
            lo,hi=0,n-1
            outcomes=[]
            while lo<hi:
                is_left_preferred=int(rank[lo]<rank[hi])
                outcomes.append(is_left_preferred)
                if is_left_preferred: hi-=1
                else: lo+=1
            assert len(outcomes)==n-1
        seen=set()
        for vote in votes(n):
            rank={a:i for i,a in enumerate(vote)}
            lo,hi=0,n-1
            path=[]
            while lo<hi:
                left=int(rank[lo]<rank[hi])
                path.append(left)
                if left:hi-=1
                else:lo+=1
            seen.add(tuple(path))
        assert len(seen)==2**max(n-1,0),(n,len(seen))
    # For each k, construct rational sample utilities with a COMMON fixed peak
    # strictly between the two middle alternatives. Their left and right values
    # rise strictly toward the peak while freely coding all k pair outcomes.
    continuum_cases=0
    for k in range(1,12):
        for labels in product((0,1),repeat=k):
            u={}
            for i,bit in enumerate(labels,1):
                sign=1 if bit else -1
                u[i]=8*i+sign
                u[2*k+1-i]=8*i-sign
                assert (u[i]>u[2*k+1-i])==(bit==1)
            assert all(u[i]<u[i+1] for i in range(1,k))
            assert all(u[i]>u[i+1] for i in range(k+1,2*k))
            assert u[k]<8*(k+1) and u[k+1]<8*(k+1)
            continuum_cases+=1
    print('SINGLE_PEAKED_NESTED_SHATTERING_AND_ONLINE_PASS',checked,'fixed_peak_utility_cases',continuum_cases)

if __name__=='__main__':check()
