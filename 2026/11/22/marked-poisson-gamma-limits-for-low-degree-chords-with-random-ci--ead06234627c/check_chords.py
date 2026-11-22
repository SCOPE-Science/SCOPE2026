#!/usr/bin/env python3
"""Exact finite checks and seeded sampling for random-chord low-degree geometry."""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
import math, random

@lru_cache(None)
def matchings(s):
    if not s:
        return ((),)
    x=s[0]
    return tuple(((x,y),)+tail for p,y in enumerate(s[1:])
                 for tail in matchings(s[1:p+1]+s[p+2:]))

def crossing(e,f):
    a,b=sorted(e); c,d=sorted(f)
    return (a<c<b) != (a<d<b)

def length(e,N):
    a,b=sorted(e)
    return min(b-a-1,N-b+a-1)

def candidates(N,j):
    # At N >= 2j+4, each chord with shorter combinatorial arc j occurs once.
    return {tuple(sorted((i,(i+j+1)%N))) for i in range(N)}

def rising(a,k):
    p=1
    for i in range(k):p*=a+i
    return p

def check_exact():
    checks=0
    for n in range(2,7):
        N=2*n
        Ms=matchings(tuple(range(N)))
        M=len(Ms)
        expected_m=math.prod(range(1,N,2))
        assert M==expected_m; checks+=1
        J=list(range(min(3,n-1)))
        rawcounts=defaultdict(int)
        paircounts=defaultdict(int)
        bad=0
        for matching in Ms:
            L={j:0 for j in J}
            for p,e in enumerate(matching):
                j=length(e,N)
                deg=sum(crossing(e,f) for t,f in enumerate(matching) if t!=p)
                if j in L:
                    L[j]+=1
                if j<=2 and j!=deg:
                    bad+=1
            for j in J:
                rawcounts[j]+=L[j]
                for k in J:
                    paircounts[j,k]+=L[j]*(L[k]-(j==k))
        for j in J:
            assert len(candidates(N,j))==N
            actual=Fraction(rawcounts[j],M)
            assert actual==Fraction(N,N-1),(n,j,actual)
            checks+=1
            for k in J:
                Cj=candidates(N,j); Ck=candidates(N,k)
                disj=sum(1 for u in Cj for v in Ck if not (set(u)&set(v)))
                expected=Fraction(disj,(N-1)*(N-3))
                got=Fraction(paircounts[j,k],M)
                assert got==expected,(n,j,k,got,expected)
                checks+=1
        # The (j+1)-gap arc is Beta(j+1, N-j-1), independently of pairing.
        for j in J:
            a=j+1
            for r in (1,2,3):
                beta_moment=Fraction(n**r*rising(a,r),rising(N,r))
                gamma_moment=Fraction(rising(a,r),2**r)
                assert beta_moment>0 and beta_moment<=gamma_moment
                checks+=1
        print(f'exact n={n}, perfect_matchings={M}, low-length/degree_mismatches_total={bad}, checked_labels={J}')
    return checks

def check_sampling():
    rng=random.Random(20261121)
    n=300; N=2*n; replicates=4000; K=2
    counts=[0]*(K+1)
    mark_sum=[0.]*(K+1)
    left_half=[0]*(K+1)
    for _ in range(replicates):
        pairing=list(range(N)); rng.shuffle(pairing)
        partner=[-1]*N
        for p in range(0,N,2):
            u,v=pairing[p:p+2]; partner[u]=v; partner[v]=u
        es=[rng.expovariate(1) for _ in range(N)]
        s=sum(es)
        x=rng.random()
        starts=[]
        for e in es:
            starts.append(x)
            x=(x+e/s)%1
        for j in range(K+1):
            for i in range(N):
                if partner[i] == (i+j+1)%N:
                    counts[j]+=1
                    arc=sum(es[(i+t)%N] for t in range(j+1))/s
                    mark_sum[j]+=n*arc
                    mid=(starts[i]+arc/2)%1
                    left_half[j]+=int(mid<.5)
    checks=0
    for j in range(K+1):
        observed=counts[j]/replicates
        mean_mark=mark_sum[j]/counts[j]
        observed_left=left_half[j]/counts[j]
        assert abs(observed-1)<.12,(j,observed)
        assert abs(mean_mark-(j+1)/2)<.12,(j,mean_mark)
        assert abs(observed_left-.5)<.06,(j,observed_left)
        checks+=3
        print(f'seeded n={n}, j={j}: mean count={observed:.4f}, mean n*arc={mean_mark:.4f}, midpoints in semicircle={observed_left:.4f}')
    return checks

if __name__=='__main__':
    e=check_exact(); s=check_sampling()
    print(f'PASS: {e} exact grouped checks and {s} seeded grouped checks')
