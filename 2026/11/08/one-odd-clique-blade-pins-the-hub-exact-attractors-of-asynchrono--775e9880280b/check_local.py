#!/usr/bin/env python3
"""Exhaustive local constraints, maximum-cut census, and stationary hub flux.
Only Python 3 standard library is required.
"""
from fractions import Fraction
from itertools import product
from math import comb


def local(r):
    # The hub spin is fixed to zero.  Each bit is one private spin.
    selected=[]
    for s in range(1<<r):
        k=r-s.bit_count()  # Private vertices agreeing with the hub.
        strictly_improving=False
        for v in range(r):
            current=(s>>v)&1
            same=sum(((s>>u)&1)==current for u in range(r))+(current==0)
            if 2*same>r+1:
                next_s=s^(1<<v)
                old_cut=sum(((s>>u)&1)!=0 for u in range(r))
                old_cut+=sum(((s>>u)&1)!=((s>>w)&1)
                             for u in range(r) for w in range(u+1,r))
                new_cut=sum(((next_s>>u)&1)!=0 for u in range(r))
                new_cut+=sum(((next_s>>u)&1)!=((next_s>>w)&1)
                             for u in range(r) for w in range(u+1,r))
                assert new_cut>=old_cut
                if new_cut>old_cut: strictly_improving=True
        expected=(k==r//2 if r%2 else k in (r//2-1,r//2))
        assert expected==(not strictly_improving),(r,s,expected,strictly_improving)
        if expected:selected.append(s)
    expected_count=comb(r,r//2) if r%2 else comb(r+1,r//2)
    assert len(selected)==expected_count
    return selected


def check_hub(rs):
    N=1+sum(rs)
    local_states=[local(r) for r in rs]
    total=1
    for group in local_states:total*=len(group)
    count_flip=0
    for states in product(*local_states):
        same_hub=1+sum(r-s.bit_count() for r,s in zip(rs,states))
        # Since the hub is adjacent to every other vertex, its closed
        # neighborhood is the entire graph.
        if 2*same_hub>N:count_flip+=1
    if any(r%2 for r in rs):
        assert count_flip==0,(rs,count_flip)
    else:
        expected_numer=1
        for r in rs:expected_numer*=comb(r,r//2)
        assert count_flip==expected_numer,(rs,count_flip,expected_numer)
        formula=Fraction(1,N)
        for r in rs:
            a=r//2;formula*=Fraction(a+1,2*a+1)
        assert Fraction(count_flip,N*total)==formula,(rs,formula)
    return total,count_flip


def main():
    cases=0
    for m in range(1,5):
        for rs in product((1,2,3,4,5,6),repeat=m):
            if sum(rs)>12:continue
            check_hub(rs);cases+=1
    print('PASS local strict-improvement classification and exact hub-flip stationary flux')
    print('clique blade sizes tested: 1..6; tuples tested:',cases)
    for rs in [(2,2,2),(2,3,2),(4,4),(4,5)]:
        print('case:',rs,'stable states per fixed hub and hub-flip count:',check_hub(rs))
    for r in (2,4,6):
        left=check_hub((2,r))[0]
        right=check_hub((2,r+1))[0]
        assert left==right
    print('PASS one-vertex parity-switch preserves recurrent-state population')

if __name__=='__main__':main()
