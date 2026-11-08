#!/usr/bin/env python3
"""Exact enumeration checks for envy-free budgeted unit chores.

Reproduces the finite tests with no external dependencies:
    python3 verify.py
"""
from itertools import product
from math import factorial



def direct_ef(labels, caps):
    n=len(caps)
    counts=[labels.count(i) for i in range(n+1)]
    if any(counts[i]>caps[i] for i in range(n)):
        return False
    for i in range(n+1):
        for j in range(n):
            if min(counts[i],caps[j])>counts[j]:
                return False
    return True


def candidate_loads(m,caps):
    n=len(caps)
    total=sum(caps)
    if m>=total:
        yield tuple(caps)+(m-total,)
    for level in range(max(caps)):
        loads=tuple(min(b,level) for b in caps)
        h=m-sum(loads)
        if 0<=h<=level:
            yield loads+(h,)


def exact_count(m,caps):
    return sum(factorial(m)//_denom(loads) for loads in candidate_loads(m,caps))


def _denom(loads):
    p=1
    for a in loads:
        p*=factorial(a)
    return p


def brute_count(m,caps):
    return sum(direct_ef(a,caps) for a in product(range(len(caps)+1),repeat=m))


def equal_feasible(m,n,B):
    return m>=n*B or any(n*l<=m<=(n+1)*l for l in range(B))


def main():
    instances=0
    assignments=0
    for n in (2,3):
        for caps in product(range(1,5),repeat=n):
            for m in range(0,9):
                observed=brute_count(m,caps)
                expected=exact_count(m,caps)
                assert observed==expected,(n,caps,m,observed,expected)
                instances+=1
                assignments+=(n+1)**m
    for n in (4,):
        for caps in product(range(1,4),repeat=n):
            for m in range(0,6):
                observed=brute_count(m,caps)
                expected=exact_count(m,caps)
                assert observed==expected,(n,caps,m,observed,expected)
                instances+=1
                assignments+=(n+1)**m
    for n in range(2,15):
        for B in range(1,15):
            threshold=n*min(B,n-1)
            assert threshold>=1
            assert not equal_feasible(threshold-1,n,B),(n,B,'sharp')
            for m in range(threshold,threshold+n*B+9):
                assert equal_feasible(m,n,B),(n,B,m,'eventual')
            for m in range(0,n*B+1):
                assert equal_feasible(m,n,B)==(exact_count(m,(B,)*n)>0),(n,B,m)
    heterogeneous_checks=0
    for n in range(2,7):
        for caps in product(range(1,6), repeat=n):
            last_gap=max(t for t in range(1,max(caps)+1)
                         if sum(b>=t for b in caps)>=t+1)
            T=sum(min(b,last_gap) for b in caps)
            assert exact_count(T-1,caps)==0,(caps,last_gap,T,'sharp')
            for m in range(T,T+10):
                assert exact_count(m,caps)>0,(caps,last_gap,T,m,'eventual')
            heterogeneous_checks+=1
    print('PASS: exact counts for',instances,'instances;',assignments,'complete labeled assignments')
    print('PASS: sharp equal-capacity stabilization for',13*14,'(n,B) settings')
    print('PASS: sharp heterogeneous-capacity stabilization for',heterogeneous_checks,'vectors')
    for n,B,m in [(3,3,5),(3,3,6),(4,5,11),(4,5,12),(2,2,3),(3,3,7)]:
        print('n,B,m:',n,B,m,'allocations:',exact_count(m,(B,)*n),'feasible:',equal_feasible(m,n,B))

if __name__=='__main__':main()
