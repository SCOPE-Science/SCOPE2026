#!/usr/bin/env python3
"""Exact finite cross-checks for the bounded-digit Fibonacci forcing identity."""
from collections import defaultdict


def fibonacci(k):
    f=[0,1,1]
    for j in range(3,k+1): f.append(f[-1]+f[-2])
    return f


def signed_representations(k):
    f=fibonacci(k)
    d={0:1}
    for j in range(1,k+1):
        nxt=defaultdict(int)
        for s,c in d.items():
            for a in (-1,0,1): nxt[s+a*f[j]]+=c
        d=nxt
    return d


def bounded_partition_counts(N):
    f=fibonacci(40)
    d=[0]*(N+1);d[0]=1
    for j in range(1,len(f)):
        z=f[j]
        if z>N: break
        nd=d.copy()
        for s in range(0,N+1):
            if s>=z: nd[s]+=d[s-z]
            if s>=2*z: nd[s]+=d[s-2*z]
        d=nd
    return d


def direct_bad_prefix(k, n, lower_signed):
    f=fibonacci(k)
    prefixes=((1,0),(1,1),(-1,0),(-1,-1),(1,-1,1),(-1,1,-1))
    result=0
    for pr in prefixes:
        base=sum(a*f[k-i] for i,a in enumerate(pr))
        d=lower_signed[k-len(pr)]
        result+=d.get(n-base,0)
    return result


def main():
    K=23; N=180
    fib=fibonacci(K)
    signed=[{0:1}]
    for k in range(1,K+1):
        nxt=defaultdict(int)
        for s,c in signed[-1].items():
            for a in (-1,0,1): nxt[s+a*fib[k]]+=c
        signed.append(nxt)
    parts=bounded_partition_counts(N)
    published=[0,1,2,4,5,7,9,11,13,15,17,20,21,24,26,29]
    assert [0]+parts[:15]==published
    checked=0
    for k in range(19,K+1):
        for n in range(-N,N+1):
            if k >= 4:
                bad=signed[k].get(n,0)-signed[k-1].get(n,0)-signed[k-2].get(n,0)-signed[k-3].get(n,0)
                assert bad==direct_bad_prefix(k,n,signed),(k,n,bad)
                if k>=19: # F_(k-4)>180, and n in [-180,180]
                    expected=0 if n==0 else parts[abs(n)-1]
                    assert bad==expected,(k,n,bad,expected)
                checked+=1
    effective_cases=0
    for k in range(5, 22):
        bound=min(fib[k-4], N)
        for n in range(-bound,bound+1):
            observed=direct_bad_prefix(k,n,signed)
            expected=0 if n==0 else parts[abs(n)-1]
            assert observed==expected,(k,n,observed,expected)
            effective_cases+=1
    # Check rigorous counting sandwiches for a range of x and indices J.
    part10000=bounded_partition_counts(12000)
    cumulative=0; tested=0
    for X in range(1,12001):
        cumulative+=part10000[X-1]
        J=max(i for i in range(1,len(fib)) if fib[i]<=max(X-1,1))
        assert cumulative<=3**J,(X,cumulative,J)
        if J>=5 and X-1>=fib[J]: assert cumulative>=3**(J-4),(X,cumulative,J)
        tested+=1
    print('VERIFY_OK signed_prefix_and_recurrence_cases=',checked,
          'published_f_terms=',len(published),'effective_bound_cases=',effective_cases,'summatory_bounds=',tested,
          'max_weight=',max(fib[1:]),'arithmetic=exact')

if __name__=='__main__': main()
