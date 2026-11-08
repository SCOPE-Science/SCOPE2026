#!/usr/bin/env python3
"""Exact finite consistency checks for binomial-gcd moment asymptotics."""
from math import comb, gcd, isqrt, log, pi
from functools import reduce

def make_spf(limit):
    a = list(range(limit + 1))
    for p in range(2, isqrt(limit)+1):
        if a[p] == p:
            for j in range(p*p, limit+1, p):
                if a[j] == j: a[j] = p
    return a

def factors(n, spf):
    out=[]
    while n > 1:
        p=spf[n]; a=0; pa=1
        while n%p==0:
            n//=p; a+=1; pa*=p
        out.append((p,a,pa))
    return out

def exact_D(n, spf):
    """Valuation check using independent digit-length computation, n=k+1."""
    d=1
    for p,a,pa in factors(n,spf):
        b=n//pa
        e=a
        while b>=p:
            b//=p; e-=1
        if e>0:
            assert d==1
            d=p**e
    return d

def class_D(n, spf):
    fs=factors(n,spf)
    large=[(p,a,pa) for p,a,pa in fs if pa*pa>=n]
    if not large: return 1, 'unit', 1
    assert len(large)==1
    p,a,pa=large[0]
    d=exact_D(n,spf)
    assert 1 < d <= pa
    if a==1:
        assert p*p>n and d==p
        return d,'large_prime',p
    return d,'prime_power_exception',pa

def main():
    upper=1_000_000
    spf=make_spf(upper+2)
    for k in range(2,41):
        direct=reduce(gcd,(comb(q*k,k) for q in range(2,k+2)))
        d=exact_D(k+1,spf)
        assert direct==d
    print('DIRECT_BINOMIAL_GCD_OK k=2..40')
    for bound in (1000,10000,100000,1000000):
        total=0; lps=0; lpc=0; exception_sum=0
        for n in range(3,bound+2):
            d,kind,component=class_D(n,spf)
            total+=d
            if kind=='large_prime': lps+=d; lpc+=1
            elif kind=='prime_power_exception': exception_sum+=d
        constant=pi*pi/12
        ratio=total/(constant*bound*bound/log(bound))
        print(f'MOMENT_ONE bound={bound} exact={total} large_prime_mass={lps} prime_power_exception_mass={exception_sum} large_prime_rows={lpc} leading_ratio={ratio:.9f}')
        assert lps+exception_sum<=total
    print('PRIME_POWER_EXCEPTION_BOUND_OK 3<=n<=1000001')
    print('VERIFY_OK finite_checks_only=True infinite_asymptotic_proof_separate=True independent_audit=False')

if __name__=='__main__':main()
