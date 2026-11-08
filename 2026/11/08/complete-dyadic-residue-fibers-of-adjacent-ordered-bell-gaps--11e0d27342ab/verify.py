#!/usr/bin/env python3
"""Exact integer checks for the dyadic value spectrum of adjacent Fubini gaps.

Finite consistency tests; not a substitute for the unbounded 2-adic proof.
"""
from math import comb, factorial


def fubini(nmax, mod=None):
    a=[1]
    pas=[1]
    for n in range(1,nmax+1):
        pas=[1]+[pas[j-1]+pas[j] for j in range(1,n)]+[1]
        if mod: pas=[x%mod for x in pas]
        a.append(sum(pas[j]*a[n-j] for j in range(1,n+1))%(mod or 10**100000))
    return a


def g_odd(e,t,k):
    m=1<<k
    return sum((1<<(j-1))*((j+1) if e==0 else -j*(j+1))*pow(j,2*t,m) for j in range(1,k+1,2))%m


def v2(n):
    assert n
    return (abs(n)&-abs(n)).bit_length()-1


def main():
    exact=fubini(130)
    st=[1]
    for n in range(1,31):
        st=[0]+[j*st[j]+st[j-1] if j<len(st) else st[j-1] for j in range(1,n+1)]
        assert exact[n]==sum(factorial(j)*st[j] for j in range(n+1))
    assert [exact[n+1]-exact[n] for n in range(6)]==[0,2,10,62,466,4142]
    blocks=0; cells=0; pairs=0; series=0
    for k in range(7,16):
        m=1<<k; p=1<<(k-6); nmax=max(160,k+3*p+4)
        a=fubini(nmax+1,m)
        gap=[(a[n+1]-a[n])%m for n in range(nmax)]
        target={z for z in range(m) if z%128 in (114,110)}
        assert all(gap[n]%128==(114 if n%2==0 else 110) for n in range(6,nmax))
        assert gap[k-2]!=gap[k-2+p]
        assert all(gap[n]==gap[n+p] for n in range(k-1,nmax-p))
        assert set(gap)==target|{x%m for x in (0,2,10,62,466,4142)}
        for start in (k-1,k,k+1,k+p,k+2*p-1):
            if start+p>nmax: continue
            chunk=gap[start:start+p]
            assert set(chunk)==target and len(chunk)==p
            blocks+=1; cells+=p
        for n in range(min(nmax,40)):
            d=(gap[n]-g_odd(n%2,n//2,k))%m
            expected=n+1
            if expected<k: assert v2(d)==expected
            else: assert d==0
            series+=1
        for e in (0,1):
            for t in range(30):
                for u in range(t+1,30):
                    exp=7+v2(u-t)
                    if exp<k:
                        assert v2((g_odd(e,u,k)-g_odd(e,t,k))%m)==exp
                        pairs+=1
    for k in (17,19,23):
        for e in (0,1):
            for t in range(70):
                assert v2((g_odd(e,t+1,k)-g_odd(e,t,k))%(1<<k))==7
    print('VERIFY_OK levels=7..15 gap_image=PASS sharp_start=PASS least_period=PASS')
    print('complete_blocks=',blocks,'residue_cells=',cells,'scaled_isometry_pairs=',pairs,'series_cases=',series)
    print('independent_stirling_rows=1..30 exact_integer_recurrence=0..130 extra_precision=17,19,23')

if __name__=='__main__': main()
