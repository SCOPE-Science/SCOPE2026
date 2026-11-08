#!/usr/bin/env python3
"""Finite exact checks of toric semigroup formulas for weighted rational curves.

This tests finite degree truncations only. Infinite statements require the proof.
"""
from collections import defaultdict

def generators(d,e):
    return [(1,a) for a in range(1,d+1)] + [(e,a) for a in range(e)]

def enumerate_semigroup(d,e,A):
    by_degree = [set() for _ in range(A+1)]
    by_degree[0].add(0)
    for a in range(1,A+1):
        for w,b in generators(d,e):
            if a >= w:
                for alpha in by_degree[a-w]:
                    by_degree[a].add(alpha+b)
    return by_degree

def criterion(a,alpha,d,e):
    return 0<=alpha<=d*a and alpha >= (a%e)

def witness(d,e,p):
    if e==1 or (e==2 and p%2):
        return None
    if e==2: return (1,0)
    return (e-1,e-2)

def main():
    combos=0
    for d in range(1,8):
        for e in range(1,9):
            arr=enumerate_semigroup(d,e,22)
            for a in range(23):
                actual=arr[a]
                expect={x for x in range(d*a+1) if criterion(a,x,d,e)}
                assert actual==expect,(d,e,a,sorted(actual^expect))
            # Conductor: b up to e-1 realizes each congruence class.
            for a in range(1,12):
                for alpha in range(d*a+1):
                    in_conductor=all(criterion(a+b,alpha+beta,d,e)
                                     for b in range(e) for beta in range(d*b+1))
                    assert in_conductor == (alpha>=e-1),(d,e,a,alpha)
            for p in (2,3,5,7,11):
                v=witness(d,e,p)
                if v is not None:
                    a,alpha=v
                    assert not criterion(a,alpha,d,e)
                    assert criterion(p*a,p*alpha,d,e)
                else:
                    # bounded root-closed check: if pv in S then v in S
                    for a in range(1,20):
                        for alpha in range(d*a+1):
                            if criterion(p*a,p*alpha,d,e):
                                assert criterion(a,alpha,d,e),(d,e,p,a,alpha)
            combos+=1
    print('WEIGHTED_CURVE_SEMIGROUP_MEMBERSHIP_OK', combos)
    print('CONDUCTOR_AND_FROBENIUS_ROOT_TESTS_OK', combos*5)
    print('INFINITE_THEOREM_REQUIRES_WRITTEN_SEMIGROUP_PROOF')

if __name__=='__main__': main()
