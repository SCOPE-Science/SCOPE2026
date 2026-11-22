#!/usr/bin/env python3
"""Independent finite checks of the sharp global SUS theorem for weight-three words.

Uses literal factor multiplicities at small lengths and an independently derived
bounded-gap candidate search at larger lengths. Finite tests supplement the proof.
"""
from collections import Counter
from itertools import combinations
from random import Random


def literal_sus(w):
    n=len(w)
    for length in range(1,n+1):
        counts=Counter(w[i:i+length] for i in range(n-length+1))
        if any(v==1 for v in counts.values()):
            return length
    raise AssertionError('every word is a unique factor of itself')


def gap_sus(g):
    a,b,c,d=g
    candidates=[b+c+3]
    gs=sorted(g)
    if gs[3]>gs[2]:
        candidates.append(gs[3])
    # Factors containing precisely one of the three marked letters.
    left=(a,b,c); right=(b,c,d)
    for j in range(3):
        xvals={0}|{left[i]+1 for i in range(3) if i!=j and left[i]<left[j]}
        yvals={0}|{right[i]+1 for i in range(3) if i!=j and right[i]<right[j]}
        for x in xvals:
            for y in yvals:
                if all(x>left[i] or y>right[i] for i in range(3) if i!=j):
                    candidates.append(x+y+1)
    # Factors containing exactly two marked letters.
    for j, gap in enumerate((b,c)):
        l=(a,b)[j]; r=(c,d)[j]
        other=1-j; other_gap=(b,c)[other]
        if gap!=other_gap:
            candidates.append(gap+2)
        else:
            other_l=(a,b)[other]; other_r=(c,d)[other]
            if l>other_l:
                candidates.append(gap+2+other_l+1)
            if r>other_r:
                candidates.append(gap+2+other_r+1)
    return min(candidates)


def max_formula(n):
    return n-2*(n//4)


def expected_extremizers(n):
    m=n//4
    s=n-3-2*m
    return {(a,m,m,s-a) for a in range(max(0,s-m), min(m,s)+1)}


def word(g):
    a,b,c,d=g
    return '0'*a+'1'+'0'*b+'1'+'0'*c+'1'+'0'*d


def all_gaps(n):
    for positions in combinations(range(n),3):
        i,j,k=positions
        yield i,j-i-1,k-j-1,n-k-1


def main():
    tested_literal=0
    for n in range(3,22):
        attained=set()
        for g in all_gaps(n):
            ans=literal_sus(word(g)); fast=gap_sus(g)
            assert ans==fast,(n,g,ans,fast)
            tested_literal+=1
            if n>=5:
                assert ans<=max_formula(n),(n,g,ans)
                if ans==max_formula(n):attained.add(g)
        if n>=5:
            assert attained==expected_extremizers(n),(n,attained,expected_extremizers(n))
    rng=Random(20261120)
    random_cases=0
    for n in range(22,301):
        for g in expected_extremizers(n):
            assert gap_sus(g)==max_formula(n),(n,g)
        for _ in range(30):
            positions=sorted(rng.sample(range(n),3))
            i,j,k=positions
            g=(i,j-i-1,k-j-1,n-k-1)
            val=gap_sus(g)
            assert val<=max_formula(n),(n,g,val)
            assert (val==max_formula(n))==(g in expected_extremizers(n)),(n,g,val)
            random_cases+=1
    print('literal_full_words_verified:',tested_literal)
    print('exhaustive_lengths: 3..21')
    print('complete_extremizer_checks: 5..21')
    print('larger_length_extremizer_witnesses: 22..300')
    print('larger_length_seeded_gap_checks:',random_cases)
    print('status: PASS (finite consistency checks; infinite theorem uses proof)')

if __name__=='__main__':main()
