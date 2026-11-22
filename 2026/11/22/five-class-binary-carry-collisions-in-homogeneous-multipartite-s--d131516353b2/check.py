#!/usr/bin/env python3
"""Independent exact checks of the five-class type-count collision theorem.

Usage: python3 check.py [maximum_size]
No external packages are required.
"""
from collections import defaultdict
from itertools import combinations_with_replacement
from math import comb
import sys


def profiles(n, k, lower=1):
    """Construct partitions into exactly k positive parts recursively."""
    if k == 1:
        if n >= lower:
            yield (n,)
        return
    for a in range(lower, n // k + 1):
        for rest in profiles(n-a, k-1, a):
            yield (a,) + rest


def types(profile):
    n = sum(profile)
    return sum(1 << (n-a) for a in profile)


def predicted_pair(t, d):
    left = tuple(sorted((t-1-d, t, t+1, t+1, t+d)))
    right = tuple(sorted((t-d, t-d, t-1, t+1+d, t+1+d)))
    return tuple(sorted((left, right)))


def grouped_collisions(n, k):
    bins = defaultdict(list)
    for profile in profiles(n, k):
        bins[types(profile)].append(profile)
    return {num: tuple(group) for num, group in bins.items() if len(group) > 1}


def check_full_classification(max_n):
    tested = 0
    for k in (2, 3, 4):
        for n in range(k, max_n+1):
            count = sum(1 for _ in profiles(n, k))
            tested += count
            assert not grouped_collisions(n, k), (n,k)
    five_groups=0
    for n in range(5,max_n+1):
        found=grouped_collisions(n, 5)
        expected=set()
        if (n-1) % 5 == 0:
            t=(n-1)//5
            if t>=3:
                expected={predicted_pair(t,d) for d in range(1,t-1)}
        actual={tuple(sorted(group)) for group in found.values()}
        assert actual==expected,(n,actual,expected)
        assert all(len(group)==2 for group in found.values()),n
        for num,group in found.items():
            assert types(group[0])==num==types(group[1])
        tested+=sum(1 for _ in profiles(n,5))
        five_groups+=len(found)
    return tested,five_groups


def independent_small_enumeration():
    # Second method: generate all nondecreasing 5-tuples directly, no partition recurrence.
    observed=[]
    for n in range(5,17):
        bins=defaultdict(list)
        for p in combinations_with_replacement(range(1,n+1),5):
            if sum(p)==n:
                bins[sum(2**(n-a) for a in p)].append(p)
        collisions=[tuple(group) for group in bins.values() if len(group)>1]
        if n<16:
            assert collisions==[],(n,collisions)
        else:
            assert len(collisions)==1 and set(collisions[0])==set(predicted_pair(3,1))
        observed.append((n,sum(map(len,bins.values())),len(collisions)))
    return observed


def check_binary_splits(max_e=16):
    # The fixed-length, equal-first-moment binary power collisions.
    hits=0
    checked=0
    from itertools import combinations_with_replacement
    groups=defaultdict(list)
    for es in combinations_with_replacement(range(max_e+1),5):
        groups[(sum(es),sum(1<<e for e in es))].append(es)
        checked+=1
    for (s,n),v in groups.items():
        if len(v)<2:
            continue
        assert len(v)==2,(s,n,v)
        a,b=v
        bits=[e for e in range(max_e+3) if (n>>e)&1]
        assert len(bits)==3,(s,n,bits)
        C,B,A=bits
        assert A+C==2*B-1,(s,n,bits)
        expected={tuple(sorted((A,C,B-1,B-2,B-2))),
                  tuple(sorted((B,A-1,A-1,C-1,C-1)))}
        assert set(v)==expected,(s,n,v,expected)
        hits+=1
    return checked,hits


def graded_coeff(profile):
    n=sum(profile)
    coeff=[0]*(n+1)
    for a in profile:
        for j in range(n-a+1):
            coeff[j]+=comb(n-a,j)
    return tuple(coeff)


def invert_binomial_basis(coeff):
    # Unique expansion in (1+z)^e, descending leading-degree elimination.
    rem=list(coeff)
    out=[]
    for e in range(len(rem)-1,-1,-1):
        multiplicity=rem[e]
        if multiplicity:
            assert multiplicity>0
            out.extend([e]*multiplicity)
            for j in range(e+1):
                rem[j]-=multiplicity*comb(e,j)
    assert all(v==0 for v in rem)
    return tuple(sorted(out))


def direct_type_diagrams():
    # Enumerate a new vertex's class and adjacency bits to all old parameters.
    for q in (2,3,4,5):
        for n in range(q, min(q+5,11)):
            for p in profiles(n,q):
                vertices=[i for i,a in enumerate(p) for _ in range(a)]
                patterns=set()
                for i in range(q):
                    others=[j for j,jclass in enumerate(vertices) if jclass!=i]
                    for bits in range(1<<len(others)):
                        b=[0]*n
                        for bit, index in enumerate(others):
                            b[index]=(bits>>bit)&1
                        patterns.add((i,tuple(b)))
                assert len(patterns)==types(p)
                hist=[0]*(n+1)
                for i,b in patterns:
                    hist[sum(b)]+=1
                assert tuple(hist)==graded_coeff(p)
                assert invert_binomial_basis(hist)==tuple(sorted(n-a for a in p))


if __name__=='__main__':
    n=int(sys.argv[1]) if len(sys.argv)>1 else 80
    tested,groups=check_full_classification(n)
    small=independent_small_enumeration()
    combos,hits=check_binary_splits(16)
    direct_type_diagrams()
    print('PROFILE_CHECK_OK', 'max_n',n,'profiles_checked',tested,
          'five_part_collisions',groups)
    print('INDEPENDENT_MINIMAL_CENSUS',small)
    print('BINARY_SPLIT_CHECK_OK','five_term_multisets',combos,
          'binary_equal_moment_pairs',hits)
    print('DIRECT_TYPE_DIAGRAMS_OK')
    print('VERIFY_OK')
