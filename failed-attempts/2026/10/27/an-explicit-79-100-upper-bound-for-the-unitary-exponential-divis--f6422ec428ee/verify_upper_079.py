#!/usr/bin/env python3
"""Exact integer certificate: density of unitary/exponential divisor-sum dominance < 79/100.

Only Python's standard library is needed. Every threshold comparison and
all upper bounds for prime-tail moments are computed with integers.
"""
from itertools import product
from math import comb, factorial, prod
from fractions import Fraction
from bisect import bisect_right

SMALL_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19)
CAPS = (10, 6, 4, 3, 3, 2, 2, 2)
EXTRA_PRIMES = (23, 29, 31, 37, 41, 43)
# Rational upper endpoints for prefix ratios, and moments for primes >=47.
BINS = (
    (3,4,139),(4,5,139),(33,40,139),(17,20,139),
    (7,8,139),(22,25,139),(89,100,139),(9,10,139),
    (181,200,139),(91,100,139),(183,200,139),(23,25,139),
    (37,40,139),(93,100,139),(187,200,139),(47,50,139),
    (189,200,139),(19,20,139),(191,200,139),(24,25,139),
    (193,200,139),(97,100,138),(39,40,126),(49,50,111),
    (197,200,90),(99,100,59),
)
SCALE = 10**12
RISK_SCALE = 10**9


def ceildiv(x, y):
    return (x+y-1)//y


def prime_sieve(bound):
    sieve=bytearray(b'\x01')*(bound+1)
    sieve[:2]=b'\x00\x00'
    for p in range(2, int(bound**0.5)+1):
        if sieve[p]:
            for n in range(p*p,bound+1,p):
                sieve[n]=0
    return [p for p in range(2,bound+1) if sieve[p]]


def local_table(p, cap):
    ans=[]
    for a in range(cap+1):
        numerator=p**a+1 if a else 1
        denominator=sum(p**d for d in range(1,a+1) if a%d==0) if a else 1
        integer_weight=(p-1)*p**(cap-a)
        ans.append((numerator,denominator,integer_weight))
    return ans


def prefix_distribution():
    tables=[local_table(p,a) for p,a in zip(SMALL_PRIMES,CAPS)]
    D=prod(p**(a+1) for p,a in zip(SMALL_PRIMES,CAPS))
    records=[]
    for tup in product(*tables):
        num=den=weight=1
        for x,y,w in tup:
            num*=x;den*=y;weight*=w
        records.append((Fraction(num,den),weight))
    records.sort(key=lambda row:row[0])
    values=[];weights=[];running=0
    for val,weight in records:
        running+=weight
        values.append(val)
        weights.append(running)
    return D,values,weights


def extra_distribution():
    # For an extra prime p, the ratio is <=1 unless v_p(n)=1.
    # v_p(n)=1 has density (p-1)/p^2 and ratio 1+1/p.
    # The complementary event has density (p^2-p+1)/p^2.
    D=prod(p*p for p in EXTRA_PRIMES)
    states=[]
    for bits in product((0,1),repeat=len(EXTRA_PRIMES)):
        numerator=denominator=weight=1
        for p,b in zip(EXTRA_PRIMES,bits):
            if b:
                numerator*=p+1; denominator*=p; weight*=p-1
            else:
                weight*=p*p-p+1
        states.append((Fraction(numerator,denominator),weight))
    assert sum(w for _,w in states)==D
    return D,states


def prefix_bin_masses():
    d1,values,prefix=prefix_distribution()
    d2,states=extra_distribution()
    cums=[]
    for qnum,qden,_ in BINS:
        q=Fraction(qnum,qden)
        total=0
        for factor,weight in states:
            ix=bisect_right(values,q/factor)
            if ix:total+=weight*prefix[ix-1]
        cums.append(total)
    masses=[];old=0
    for c in cums:
        assert c>=old
        masses.append(c-old);old=c
    return d1*d2,masses


def upper_moment(k,later_primes):
    """Ceiling for exp(S_k) at SCALE via exact integer rounding.

    S_k=sum_{p>=47} ((1+1/p)^k-1)/p. We sum primes <=1000
    exactly with upward rounding; primes >1000 are bounded by
    sum_{j=1}^k binom(k,j)/(j*1000^j) using the integral test.
    """
    sup=0
    for p in later_primes:
        sup+=ceildiv(((p+1)**k-p**k)*SCALE,p**(k+1))
    for j in range(1,k+1):
        sup+=ceildiv(comb(k,j)*SCALE,j*1000**j)
    assert sup<9*SCALE
    assert 9**81*SCALE*82 < factorial(81)*73
    term=total=SCALE
    for j in range(1,81):
        term=ceildiv(term*sup,SCALE*j)
        total+=term
    return total+1, sup


def failure_risk_ppb(qnum,qden,k,later_primes,cache):
    if k not in cache:
        cache[k]=upper_moment(k,later_primes)
    e_upper,supper=cache[k]
    risk=ceildiv(e_upper*qnum**k*RISK_SCALE,SCALE*qden**k)
    return min(RISK_SCALE,risk),supper


def main():
    D,masses=prefix_bin_masses()
    later=[p for p in prime_sieve(1000) if p>43]
    cache={}
    lower_numerator=0
    for (a,b,k),mass in zip(BINS,masses):
        risk,supper=failure_risk_ppb(a,b,k,later,cache)
        lower_numerator+=mass*(RISK_SCALE-risk)
        print(f'endpoint={a}/{b} moment={k} '
              f'mass_numerator={mass} failure_upper_ppb={risk} '
              f'S_k_upper={supper}/{SCALE}')
    denominator=D*RISK_SCALE
    # Negative density >21/100, hence positive density <79/100.
    exact_gap=100*lower_numerator-21*denominator
    assert exact_gap>0
    print('CYLINDER_DENOMINATOR',D)
    print('NEGATIVE_DENSITY_LOWER_NUM',lower_numerator)
    print('NEGATIVE_DENSITY_LOWER_DEN',denominator)
    print('NEGATIVE_EXCESS_OVER_21_PERCENT_NUM',exact_gap)
    print('NEGATIVE_EXCESS_OVER_21_PERCENT_DEN',100*denominator)
    print('NEGATIVE_LOWER_DECIMAL',lower_numerator/denominator)
    print('POSITIVE_UPPER_DECIMAL',1-lower_numerator/denominator)
    print('VERIFY_OK')


if __name__=='__main__':
    main()
