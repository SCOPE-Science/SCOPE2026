#!/usr/bin/env python3
"""Exact integer checks for small-gap four-point sumsets; finite tests only."""
from math import gcd

def tri(k):
    k=max(0,k)
    return k*(k+1)//2

def expected_two(a,h):
    r=2*h-a-1
    return (3*h*h+h)//2 -tri(r)+tri(h-a)+h+1-max(0,r//2+1)

def predicted_genus(a,d):
    if d==2:
        return (a+1)//2
    if a%3==0:
        return a+1
    if a%3==1:
        return a+2
    return (2*a+2)//3

def semigroup_gaps(a,d):
    b=a+d
    # beyond bound all representable; chosen bound safely exceeds Frobenius
    bound=4*b*b
    can=bytearray(bound+1)
    can[0]=1
    for s in range(1,bound+1):
        can[s]=int(any(s>=v and can[s-v] for v in (d,b-1,b)))
    gaps={s for s in range(bound+1) if not can[s]}
    assert not any(not can[s] for s in range(2*b,bound+1)), (a,d)
    return gaps

def direct_bitset(a,d,max_h):
    A=(0,1,a,a+d)
    cur=1
    for h in range(1,max_h+1):
        cur=cur | (cur<<1) | (cur<<a) | (cur<<(a+d))
        yield h,cur

def test():
    formulas=0;stable=0; genus=0; sharp=0; cases=0
    for a in range(4,151):
        for d in (2,3):
            b=a+d
            H=2 if (a,d)==(4,3) else a-1
            gapset=semigroup_gaps(a,d)
            assert len(gapset)==predicted_genus(a,d), (a,d,len(gapset))
            genus+=1
            probes={H,H+1,2*H+3}
            for h,mask in direct_bitset(a,d,max(probes)):
                if d==2 and h<=a+9:
                    assert mask.bit_count()==expected_two(a,h), (a,d,h,mask.bit_count(),expected_two(a,h))
                    formulas+=1
                if h in probes:
                    misses={b*h-n for n in range(b*h+1) if not ((mask>>n)&1)}
                    assert misses==gapset, (a,d,h,misses^gapset)
                    assert mask.bit_count()==b*h+1-predicted_genus(a,d)
                    stable+=1
                if h==H-1:
                    misses={b*h-n for n in range(b*h+1) if not ((mask>>n)&1)}
                    assert misses!=gapset,(a,d,h)
                    sharp+=1
            cases+=1
    # independent membership (set-based, not shifts) at representative crossings
    independent=0
    for a in range(4,36):
        for d in (2,3):
            A=(0,1,a,a+d)
            x={0}
            for h in range(1,a+6):
                x={u+v for u in x for v in A}
                if d==2:
                    assert len(x)==expected_two(a,h)
                if h>=a-1:
                    gaps=semigroup_gaps(a,d) if h==a-1 else known_gaps
                    known_gaps=gaps
                    assert {h*(a+d)-n for n in range(h*(a+d)+1) if n not in x}==gaps
                independent+=1
    print('TWO_GAP_ALL_H_FORMULA_OK',formulas)
    print('STABLE_HOLE_SET_OK',stable)
    print('SHARP_THRESHOLD_PREDECESSORS_OK',sharp)
    print('GENUS_EXACT_SEMIGROUP_OK',genus)
    print('INDEPENDENT_SET_SUM_CROSSCHECK_OK',independent)
    print('VERIFY_OK cases',cases,'a_min',4,'a_max',150,'d_values',[2,3], 'infinite_proof_separate',True,'independent_audit',False)

if __name__=='__main__':
    test()
