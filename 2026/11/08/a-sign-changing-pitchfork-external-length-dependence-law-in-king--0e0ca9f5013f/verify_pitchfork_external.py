#!/usr/bin/env python3
"""Exact checks for pitchfork/external-length dependence in Kingman's coalescent.
No third-party dependencies. Times are integrated analytically."""
from fractions import Fraction as Q
from collections import defaultdict
from itertools import combinations
from functools import lru_cache

TESTS = 0

def assert_eq(a,b):
    global TESTS
    assert a == b, (a,b)
    TESTS += 1

def expected_stage(n,k):
    if n < 5: raise ValueError('stage formula is for n>=5')
    return Q(k*(k-1)*(n-k)*(n-k-1)*(2*k-n), 6*(n-1)*(n-2)*(n-3)*(n-4))

def transitions(k,s,d):
    other=k-s-d
    denom=k*(k-1)//2
    cases=[(s-2,d+1,0,s*(s-1)//2),
           (s-1,d-1,1,s*d),
           (s-1,d,0,s*other),
           (s,d-2,0,d*(d-1)//2),
           (s,d-1,0,d*other),
           (s,d,0,other*(other-1)//2)]
    assert sum(c for _,_,_,c in cases)==denom
    return [(a,b,p,Q(c,denom)) for a,b,p,c in cases if c]

@lru_cache(None)
def future(k,s,d):
    if k==1: return Q(0)
    return sum(prob*(dp+future(k-1,a,b)) for a,b,dp,prob in transitions(k,s,d))

def dynamic(n):
    # Each state stores (state probability, unnormalized mean pitchforks-so-far).
    states={(n,0):(Q(1),Q(0))}
    states_by_k={}
    for k in range(n,1,-1):
        states_by_k[k]=states
        nexts=defaultdict(lambda:(Q(0),Q(0)))
        for (s,d),(prob,weight) in states.items():
            for ns,nd,add,p in transitions(k,s,d):
                a,b=nexts[(ns,nd)]
                nexts[(ns,nd)]=(a+prob*p,b+(weight+prob*add)*p)
        states=nexts
    ep=sum(weight for prob,weight in states.values())
    covs={}
    total=Q(0)
    for k,di in states_by_k.items():
        es=sum(s*prob for (s,d),(prob,weight) in di.items())
        esp=sum(s*(weight+prob*future(k,s,d)) for (s,d),(prob,weight) in di.items())
        covs[k]=esp-es*ep
        total+=Q(2,k*(k-1))*covs[k]
    return total,covs,ep

def exhaustive(n):
    """Enumerate every sequence of unordered labeled coalescence events; equal weight."""
    cluster=tuple((i,) for i in range(n))
    sums_s=[0]*(n+1)
    sums_ps=[0]*(n+1)
    sums_p=0
    totalpaths=0
    def walk(clusters,p,seen):
        nonlocal sums_p,totalpaths
        k=len(clusters)
        if k==1:
            totalpaths+=1
            sums_p+=p
            for j,number in seen.items():
                sums_s[j]+=number
                sums_ps[j]+=p*number
            return
        s=sum(len(c)==1 for c in clusters)
        for i,j in combinations(range(k),2):
            a,b=clusters[i],clusters[j]
            dp=int(sorted((len(a),len(b)))==[1,2])
            rem=[clusters[h] for h in range(k) if h not in (i,j)]
            rem.append(tuple(sorted(a+b)))
            walk(tuple(sorted(rem)),p+dp,{**seen,k:s})
    walk(cluster,0,{})
    covs={}
    total=Q(0)
    for k in range(2,n+1):
        covs[k]=Q(sums_ps[k],totalpaths)-Q(sums_p*sums_s[k],totalpaths*totalpaths)
        total+=Q(2,k*(k-1))*covs[k]
    return total,covs,Q(sums_p,totalpaths)

def main():
    for n in range(2,31):
        total,stage,mean=dynamic(n)
        expected=Q(0) if n in (2,3) else (Q(2,9) if n==4 else Q(-1,18))
        assert_eq(total,expected)
        assert_eq(mean, Q(0) if n==2 else (Q(1) if n==3 else (Q(2,3) if n==4 else Q(n,6))))
        for k in range(2,n+1):
            if n>=5:
                assert_eq(stage[k],expected_stage(n,k))
        if n<=7:
            et,estage,emean=exhaustive(n)
            assert_eq(et,total)
            assert_eq(emean,mean)
            for k in range(2,n+1): assert_eq(estage[k],stage[k])
    print(f'PASS: {TESTS} exact assertions; exhaustive event histories through n=7, Markov model through n=30')

if __name__=='__main__':main()
