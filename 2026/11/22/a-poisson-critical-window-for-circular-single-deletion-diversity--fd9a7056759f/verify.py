#!/usr/bin/env python3
"""Independent finite checks for the fixed-weight cyclic deletion law.

No output of this program is an asymptotic proof; see RESULT.md.
"""
from itertools import combinations
from math import comb
from collections import Counter

def canonical(word):
    return min(word[i:]+word[:i] for i in range(len(word)))

def deletion_degree(word):
    return len({canonical(word[:i]+word[i+1:]) for i in range(len(word))})

def one_runs(word):
    n=len(word)
    return sum(word[i]=='1' and word[(i+1)%n]=='0' for i in range(n))

def adjacent_ones(word):
    n=len(word)
    return sum(word[i]=='1' and word[(i+1)%n]=='1' for i in range(n))

def unique_factors(word, ell):
    n=len(word)
    factors=[tuple(word[(i+j)%n] for j in range(ell)) for i in range(n)]
    return len(set(factors))==n

def factfall(k,r):
    ans=1
    for i in range(r): ans*=k-i
    return ans

checks=0
for n in range(3,13):
    for k in range(1,n):
        counts=Counter()
        for positions in combinations(range(n),k):
            s=['0']*n
            for i in positions: s[i]='1'
            s=''.join(s)
            runs=one_runs(s)
            z=adjacent_ones(s)
            degree=deletion_degree(s)
            assert runs+z==k
            assert degree<=2*runs
            counts[runs]+=1
            for ell in range(1,(n-2)//2+1):
                if unique_factors(s,ell):
                    assert degree==2*runs,(n,k,s,ell,degree,runs)
            checks+=1
        for r in range(1,min(k,n-k)+1):
            numerator=n*comb(k-1,r-1)*comb(n-k-1,r-1)
            assert numerator%r==0
            assert counts[r]==numerator//r,(n,k,r,counts[r],numerator//r)
        mean_z=sum((k-r)*cnt for r,cnt in counts.items())/comb(n,k)
        assert abs(mean_z-k*(k-1)/(n-1)) < 1e-9
# Graph forest structure for pairs of cyclic windows, n<40.
forest_checks=0
for n in range(4,41):
    for ell in range(1,(n-2)//2+1):
        for shift in range(1,n):
            parent=list(range(n))
            def root(t):
                while parent[t]!=t:
                    t=parent[t]
                return t
            for i in range(ell):
                a=root(i);b=root((i+shift)%n)
                assert a!=b,(n,ell,shift)
                parent[a]=b
            forest_checks+=1
print('VERIFY_OK', 'binary_sources',checks,'forest_cases',forest_checks)
