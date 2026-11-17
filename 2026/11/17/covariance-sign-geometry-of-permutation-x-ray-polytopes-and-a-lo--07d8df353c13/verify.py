"""Exact checks for covariance sign geometry of anti-diagonal permutation X-rays.

The infinite statements depend on the written proof. This script checks finite cases
independently by enumerating permutations and forming exact second moments.
"""
from fractions import Fraction
from itertools import permutations
from math import comb, factorial, log


def xrays(k):
    for pi in permutations(range(k)):
        x = [0] * (2*k-1)
        for i, j in enumerate(pi):
            x[i+j] += 1
        yield tuple(x)


def m(k, t):
    return k-abs(t-k+1)


def covariance_numerator(k,s,t):
    h=sum(0 <= s-i < k and 0 <= t-i < k for i in range(k))
    return k*k*(m(k,s) if s==t else 0)-2*k*h + m(k,s)*m(k,t)


def predicted_positive(k):
    return sum((2*k*(k-a)+(2*k-a)-1)//(2*k-a)-1 for a in range(1,k))


def test():
    checks=0
    for k in range(2,9):
        d=2*k-1; sample=list(xrays(k)); n=len(sample)
        assert n==factorial(k);checks+=1
        sums=[sum(x[s] for x in sample) for s in range(d)]
        for s in range(d):
            assert sums[s]==n*m(k,s)//k;checks+=1
        moments=[[0]*d for _ in range(d)]
        for x in sample:
            for s in range(d):
                if x[s]:
                    for t in range(d):
                        moments[s][t]+=x[s]*x[t]
        pos=zeros=0
        for s in range(d):
            for t in range(d):
                numerator=covariance_numerator(k,s,t)
                assert Fraction(moments[s][t],n)-Fraction(sums[s]*sums[t],n*n)==Fraction(numerator,k*k*(k-1));checks+=1
                if s==t:
                    assert numerator>0;checks+=1
                else:
                    if s<t:
                        if s < k-1 < t:
                            a=s+1;b=2*k-1-t
                            f=(2*k-a)*(2*k-b)-2*k*k
                            assert (numerator>0)-(numerator<0)==(f>0)-(f<0);checks+=1
                        else:
                            assert numerator<0;checks+=1
                        pos += numerator>0
                        zeros += numerator==0
        assert pos==predicted_positive(k);checks+=1
        assert sum(covariance_numerator(k,s,s) for s in range(d))==k*k*(k-1)*Fraction(3*k*k-k-1,3*k);checks+=1
        assert all(sum(covariance_numerator(k,s,t) for t in range(d))==0 for s in range(d));checks+=1
        assert all(sum(t*covariance_numerator(k,s,t) for t in range(d))==0 for s in range(d));checks+=1
        print(f'k={k}: sample_size={n}, positive_pairs={pos}, zero_pairs={zeros}, checks={checks}')
    for k in range(9,101):
        d=2*k-1; pos=zero=0
        for s in range(d):
            for t in range(s+1,d):
                numerator=covariance_numerator(k,s,t)
                if s<k-1<t:
                    a=s+1;b=2*k-1-t
                    f=(2*k-a)*(2*k-b)-2*k*k
                    assert (numerator>0)-(numerator<0)==(f>0)-(f<0);checks+=1
                else:
                    assert numerator<0;checks+=1
                pos+=numerator>0
                zero+=numerator==0
        assert pos==predicted_positive(k);checks+=1
        assert zero<=k-1;checks+=1
    for k in (200,500,1000,2500):
        density=predicted_positive(k)/((2*k-1)*(k-1))
        print(f'k={k}: positive fraction={density:.12f}; limit={1-log(2):.12f}')
    print(f'PASS: {checks} exact assertions; exhaustive permutation samples through k=8; sign counts through k=100.')


if __name__=='__main__':test()
