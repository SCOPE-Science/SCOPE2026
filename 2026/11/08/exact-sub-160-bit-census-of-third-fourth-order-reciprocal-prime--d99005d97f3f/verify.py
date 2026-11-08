#!/usr/bin/env python3
"""Exact finite census of reciprocal-order prime pairs below the 160-bit boundary.
All operations are integer arithmetic. No probabilistic primality tests are used.
"""
from math import isqrt

LIMIT = 1 << 160
EXPECTED = [(137,37),(4817,1291),(4817,17977),
            (934441,3487381),(998988257,3728274931),
            (35166746297,131244083917)]

def flip_a(a,b):
    return 4*b-a-1,b

def flip_b(a,b):
    return a,4*a-b

def all_orbit_nodes(limit):
    result={(1,1)}
    for branch in ((flip_a,flip_b),(flip_b,flip_a)):
        a=b=1
        for depth in range(5000):
            a,b=branch[depth%2](a,b)
            if max(a,b)>limit:break
            assert a>0 and b>0 and a*a+a+b*b+1==4*a*b
            assert (a*a+a+1)%b==0 and (b*b+1)%a==0
            assert (a,b) not in result
            result.add((a,b))
        else:
            raise AssertionError('step bound unexpectedly reached')
    return result

def prime_by_trial(n):
    if n<2:return False
    if n%2==0:return n==2
    t=3
    while t<=isqrt(n):
        if n%t==0:return False
        t+=2
    return True

def direct_conic_search(cap):
    out=set()
    for a in range(1,cap+1):
        z=3*a*a-a-1
        w=isqrt(z)
        if w*w==z:
            for b in (2*a-w,2*a+w):
                if 1<=b<=cap:
                    if (a*a+a+1)%b==0 and (b*b+1)%a==0:
                        out.add((a,b))
    return out

def run():
    nodes=all_orbit_nodes(LIMIT)
    assert len(nodes)==169, len(nodes)
    eligible=sorted((a,b) for a,b in nodes if min(a,b)>=5)
    assert len(eligible)==164
    parity=fermat=0
    survivors=[]
    for a,b in eligible:
        if a%2==0 or b%2==0:
            parity+=1
            continue
        # The Fermat failure is a PROOF that a coordinate is composite.
        if pow(2,a-1,a)!=1 or pow(2,b-1,b)!=1:
            fermat+=1
            continue
        survivors.append((a,b))
    assert parity==81 and fermat==77
    assert survivors==EXPECTED, (survivors,EXPECTED)
    # None of the remaining integers exceed 2^64, so trial division is cheap and exact.
    assert max(max(a,b) for a,b in survivors) < (1<<64)
    for a,b in survivors:
        assert prime_by_trial(a) and prime_by_trial(b)
        assert pow(a,3,b)==1 and a%b!=1
        assert pow(b,2,a)==a-1 and pow(b,4,a)==1
    # Cross-check the conic orbit against an independent discriminant search.
    testcap=100000
    assert all_orbit_nodes(testcap)==direct_conic_search(testcap)
    print('VERIFY_OK cutoff=2^160 orbit_nodes=169 eligible_nodes=164')
    print('CERTIFICATES even_coordinate=81 odd_fermat_base2=77')
    print('FULL_TRIAL_DIVISION_PRIMES=YES conic_discriminant_crosscheck_100000=YES')
    print('PRIME_PAIRS=' + ';'.join('%d,%d'%(a,b) for a,b in survivors))
if __name__=='__main__':
    run()
