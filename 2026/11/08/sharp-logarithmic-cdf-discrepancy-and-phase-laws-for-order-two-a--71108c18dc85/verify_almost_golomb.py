#!/usr/bin/env python3
"""Exact arithmetic finite checks of the almost-Golomb empirical-law claim."""
from fractions import Fraction
from bisect import bisect_right


def a(n):
    if n == 1: return 1
    if n < 4: return 2
    k=n.bit_length()-1; B=1<<k; j=n-B
    return 3*B//4+(j+1)//2 if j<=B//2 else n-B//2


def Phi(y,theta):
    """CDF of phase law, exact rational, for 1 <= theta <= 2."""
    y=Fraction(y); theta=Fraction(theta)
    assert 1<=theta<=2
    if y < Fraction(2,3): return Fraction(0)
    if y >= Fraction(3,4): return Fraction(1)
    t1=1/(4*(y-Fraction(1,2))); t2=1/(2*(1-y))
    full=t2-t1
    extra=max(Fraction(0),min(theta,Fraction(3,2))-t1)+max(Fraction(0),min(theta,t2)-Fraction(3,2))
    return (full+extra)/theta


def test():
    B=1<<15
    vals=[a(n) for n in range(B+1)]
    for n in range(2,B//2):
        assert vals[vals[n]+vals[n-1]]==n,(n,vals[n])
        if n>2: assert vals[n]>=vals[n-1]
    # Exact CDFs at a range of rational test points and phase cutoffs;
    # comparison is to the proved universal Kolmogorov error bound.
    experiments=0; max_ratio=Fraction(0)
    for K in range(4,15):
        for theta in [Fraction(1),Fraction(5,4),Fraction(3,2),Fraction(7,4)]:
            N=int((1<<K)*theta)
            if N>B: continue
            sorted_ratios=sorted(Fraction(vals[n],n) for n in range(1,N+1))
            for y in [Fraction(13,20),Fraction(2,3),Fraction(17,25),Fraction(7,10),Fraction(11,15),Fraction(3,4),Fraction(4,5)]:
                freq=Fraction(bisect_right(sorted_ratios,y),N)
                theo=Phi(y,theta)
                err=abs(freq-theo)
                assert err <= Fraction(30*(K+1),N),(N,y,err)
                max_ratio=max(max_ratio,Fraction(N, K+1)*err)
                experiments+=1
    exhaustive_threshold_checks=0
    for K in range(6,12):
        N=1<<K
        ratios=sorted(Fraction(vals[n],n) for n in range(1,N+1))
        test_ys=set(ratios)
        test_ys.update((a+b)/2 for a,b in zip(ratios,ratios[1:]))
        for y in test_ys:
            freq=Fraction(bisect_right(ratios,y),N)
            assert abs(freq-Phi(y,1)) <= Fraction(30*(K+1),N)
            exhaustive_threshold_checks+=1
    endpoint_cases=0
    for N in range(4,5001):
        K=N.bit_length()-1; J=(N-1).bit_length()-1
        actual=sum(4*vals[n]>=3*n for n in range(1,N+1))
        assert actual==K+J,(N,actual,K+J)
        endpoint_cases+=1
    assert Phi(Fraction(7,10),1)==Fraction(5,12)
    assert Phi(Fraction(7,10),Fraction(3,2))==Fraction(4,9)
    assert Phi(Fraction(7,10),2)==Fraction(5,12)
    assert Phi(Fraction(2,3),1)==0
    assert Phi(Fraction(3,4),1)==1
    print('VERIFY_OK recurrence_n=%d CDF_exact_cases=%d exhaustive_threshold_checks=%d worst_scaled_discrepancy=%s phase_CDFs_at_7over10=5/12,4/9,5/12 endpoint_count_cases=%d pure_rational=yes'%(B//2-2,experiments,exhaustive_threshold_checks,str(max_ratio),endpoint_cases))

if __name__=='__main__':test()
