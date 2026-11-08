#!/usr/bin/env python3
"""Small exhaustive verification of modal commutation and missing common-neighbor events.
Only standard library. The infinite-window limit requires the separate proof.
"""
from itertools import combinations
from math import comb

def relations(n, mask):
    a = [0]*n; z=0
    for i in range(n):
        for j in range(n):
            if i==j: continue
            if mask >> z & 1: a[i]|=1<<j
            z+=1
    return a

def comps(a):
    n=len(a)
    rr=[0]*n; tt=[0]*n
    for i in range(n):
        for j in range(n):
            common_out=(a[i]&a[j])!=0
            common_in=any(((a[k]>>i)&1) and ((a[k]>>j)&1) for k in range(n))
            if common_out: rr[i]|=1<<j
            if common_in: tt[i]|=1<<j
    return rr,tt

def boxes(a, bits):
    n=len(a); allones=(1<<n)-1
    return sum((1<<i) for i in range(n) if (a[i]&(~bits&allones))==0)

def transpose(a):
    n=len(a)
    return [sum(1<<j for j in range(n) if a[j]>>i&1) for i in range(n)]

def direct_boxes_commute(a):
    b=transpose(a); n=len(a)
    for bits in range(1<<n):
        if boxes(a,boxes(b,bits))!=boxes(b,boxes(a,bits)):
            return False
    return True

def run():
    for n in range(1,5):
        pairs=list(combinations(range(n),2)); tot=1<<(n*(n-1)); bad=0; nocommon=0; sumZ=0; both=0
        for mask in range(tot):
            a=relations(n,mask)
            rr,tt=comps(a)
            commute=(rr==tt)
            assert commute==direct_boxes_commute(a),(n,mask,a)
            z=0
            for i,j in pairs:
                o=not(rr[i]>>j&1); inn=not(tt[i]>>j&1)
                z+=o+inn
                both+=bool(o and inn)
            bad+=not commute
            nocommon+=z==0
            sumZ+=z
        if n>=2:
            expected_num = 2*len(pairs)*(3**(n-2))*(2**(n*(n-1)-2*(n-2)))  # p=1/2
            assert sumZ == expected_num,(n,sumZ,expected_num)
            expected_both=len(pairs)*(9**(n-2))*(2**(n*(n-1)-4*(n-2)))
            assert both == expected_both,(n,both,expected_both)
        print('n',n,'graphs',tot,'noncommuting',bad,'no_offdiagonal_gaps',nocommon,'total_gaps',sumZ,'both_absent',both)
    print('TENSE_COMMON_NEIGHBOR_EXHAUSTIVE_OK')
if __name__=='__main__': run()
