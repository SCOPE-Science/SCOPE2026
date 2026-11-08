#!/usr/bin/env python3
"""Independent exact-integer checks of a normalized two-block odd-partition distribution identity."""
from fractions import Fraction
from math import isqrt
from collections import Counter


def lambda_and_sigma(limit):
    # Separate divisor convolution: lambda(n)=sum_{d|n} chi_4(d).
    sigma = [0]*(limit+1)
    lambd = [0]*(limit+1)
    for d in range(1,limit+1):
        chi = 0 if d%2==0 else (1 if d%4==1 else -1)
        for n in range(d,limit+1,d):
            sigma[n] += d
            lambd[n] += chi
    return lambd,sigma


def partition_coefficients(limit):
    # Independently expand [z^2] product_{j>=1}(1+z*q^j/(1+q^{2j})).
    a1=[0]*(limit+1)
    a2=[0]*(limit+1)
    for j in range(1,limit+1):
        for v in range(j,limit+1,2*j):
            sign = -1 if ((v//j-1)//2)%2 else 1
            for s in range(limit-v+1):
                if a1[s]: a2[s+v] += sign*a1[s]
        for v in range(j,limit+1,2*j):
            sign = -1 if ((v//j-1)//2)%2 else 1
            a1[v] += sign
    return a2


def r(t):
    return Fraction(1,4) if t==0 else Fraction(2**(t+1)-3,4*(2**(t+1)-1))


def is_sum_two_squares(n):
    # Independent direct search, not a divisor formula.
    for x in range(isqrt(n)+1):
        z=n-x*x
        y=isqrt(z)
        if y*y==z:return True
    return False


def run(limit=256):
    a=partition_coefficients(limit)
    la,si=lambda_and_sigma(limit)
    ex=0
    distinct_support = {r(t) for t in range(limit.bit_length()+3)}
    count_by_t=Counter()
    for n in range(1,limit+1):
        expected=(si[n]-la[n]-2*si[n//2]*(n%2==0)+4*si[n//4]*(n%4==0))//4
        # Formula numerator divisible by four independently.
        numer=(si[n]-la[n]-2*si[n//2]*(n%2==0)+4*si[n//4]*(n%4==0))
        assert numer%4==0,(n,numer)
        assert a[n]==expected,(n,a[n],expected)
        t=(n & -n).bit_length()-1
        m=n >>t
        q=Fraction(a[n],si[n])
        assert q == r(t)-Fraction(la[m],4*(2**(t+1)-1)*si[m]),(n,q,t)
        exc=is_sum_two_squares(n)
        assert (la[n]>0)==exc,(n,la[n],exc)
        assert (q not in distinct_support)==exc,(n,q,t,exc)
        if exc:ex+=1
        else:count_by_t[t]+=1
        # Atoms at or below the cutoff are coordinatewise dominated.
        N=n
        for k,c in count_by_t.items():
            assert Fraction(c,N)<=Fraction(1,2**(k+1)),(n,k,c)
    # For N=limit, empirical on S is atomwise dominated; total variation equals ex/limit.
    assert sum(count_by_t.values())+ex==limit
    print('VERIFY_OK partition_coefficient_checks=%d direct_sums_of_two_squares=%d atom_noncoincidence_checks=%d finite_sample_TV_identity=yes exact_arithmetic=yes'%(limit,limit,limit))
    print('EXAMPLE cutoff=%d B=%d total_variation=%s'%(limit,ex,Fraction(ex,limit)))
    print('SUPPORT first=%s'%(str([str(r(k)) for k in range(6)])))

if __name__=='__main__':run()
