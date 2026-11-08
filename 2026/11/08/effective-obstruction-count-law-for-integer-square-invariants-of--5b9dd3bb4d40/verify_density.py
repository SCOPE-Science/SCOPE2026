#!/usr/bin/env python3
"""Independent exact checks and rigorous Euler-product truncation bounds.

No external packages, networking, or persisted data are required.
"""
from collections import Counter
from decimal import Decimal, getcontext
from fractions import Fraction
from math import gcd


def primes_upto(n):
    flag = bytearray(b'\x01') * (n + 1)
    flag[0:2] = b'\x00\x00'
    for d in range(2, int(n**0.5) + 1):
        if flag[d]:
            flag[d*d:n+1:d] = b'\x00' * ((n-d*d)//d + 1)
    return [p for p in range(2, n+1) if flag[p]]


def factor(n, primes):
    result = []
    for p in primes:
        if p*p > n:
            break
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            result.append((p, e))
    if n > 1:
        result.append((n, 1))
    return result


def bad_primes(k, primes):
    bad = []
    for p,e in factor(k, primes):
        if e % 2 or e == 0:
            continue
        u = k // (p**e)
        if p == 2:
            if e >= 4 and u % 4 == 3:
                bad.append(p)
        elif pow(-u % p, (p-1)//2, p) == 1:
            bad.append(p)
    return bad


def check_local_factors():
    checked = 0
    for p in (3,5,7,11):
        L = 2
        m = p**(2*L+1)
        count = 0
        for k in range(m):
            if k == 0:
                continue
            e, u = 0, k
            while u % p == 0:
                u //= p
                e += 1
            if e >= 2 and e % 2 == 0 and pow(-u % p,(p-1)//2,p) == 1:
                count += 1
        expected = sum(Fraction(p-1,2*p**(2*j+1)) for j in range(1,L+1))
        assert Fraction(count,m) == expected, (p,count,m,expected)
        checked += m
    m = 256
    count = 0
    for k in range(1,m):
        e,u=0,k
        while u%2==0:
            e,u=e+1,u//2
        if e>=4 and e%2==0 and u%4==3:
            count+=1
    expected = sum(Fraction(1, 4**(j+1)) for j in (2,3))
    assert Fraction(count,m)==expected,(count,m,expected)
    checked += m
    return checked


def verify_dynamics(primes):
    # Published integer-square criterion at the first nontrivial iterate:
    # x_2 = k*x_0/(x_0*x_0+k), with common divisor g.
    good_tests=0
    bad_witnesses=0
    for k in range(1,1001):
        bad=bad_primes(k,primes)
        if not bad:
            for A in range(1,15):
                for B in range(1,15):
                    if gcd(A,B)!=1:continue
                    g=gcd(k*A*B, A*A+k*B*B)
                    assert (A*A-k*B*B)%g==0,(k,A,B)
                    good_tests+=1
        else:
            for p in bad:
                e=next(e for q,e in factor(k,primes) if q==p)
                if p==2:
                    x0=2**(e//2)
                else:
                    u=k//p**e
                    roots=[w for w in range(1,p) if (w*w+u)%p==0]
                    assert roots
                    x0=p**(e//2)*roots[0]
                g=gcd(k*x0,x0*x0+k)
                assert (x0*x0-k)%g!=0,(k,p,x0)
                bad_witnesses+=1
    return good_tests,bad_witnesses


def verify_counts(primes):
    out={}
    for cap in (1000,10000,100000):
        counts=Counter(len(bad_primes(n,primes)) for n in range(1,cap+1))
        out[cap]=dict(sorted(counts.items()))
    assert out[1000]=={0:902,1:98}
    assert out[10000]=={0:9026,1:947,2:27}
    assert out[100000]=={0:90140,1:9516,2:343,3:1}
    return out


def probability_bounds(primes, P):
    getcontext().prec=45
    probs=[Decimal(1),Decimal(0),Decimal(0),Decimal(0)]
    s=Decimal(0)
    s2=Decimal(0)
    for p in primes:
        if p>P: break
        q=(Decimal(1)/Decimal(48) if p==2 else Decimal(1)/(2*Decimal(p)*(p+1)))
        s+=q
        s2+=q*(1-q)
        for r in range(3,0,-1):
            probs[r]=probs[r]*(1-q)+probs[r-1]*q
        probs[0]*=1-q
    tail=Decimal(1)/(2*Decimal(P+1))
    # For every r, the full probability differs by at most tail
    # from the product truncated to primes <= P.
    return probs,s,s2,tail


def main():
    P=1000000
    primes=primes_upto(P)
    local=check_local_factors()
    good,bad=verify_dynamics(primes)
    counts=verify_counts(primes)
    probs,mean,var,tail=probability_bounds(primes,P)
    print('VERIFY_OK local_residues=%d good_pair_tests=%d constructed_bad_witnesses=%d exact_counts=yes arithmetic=exact' % (local,good,bad))
    for n,dist in counts.items():
        print('COUNT n=%d defects=%s' % (n,str(dist)))
    print('LIMIT p0=%s p1=%s p2=%s p3=%s' % tuple(format(x,'.12f') for x in probs))
    print('RIGOROUS_TRUNCATION_ABS_ERROR_PER_PROBABILITY <= %s' % format(tail,'.12f'))
    print('LIMIT_MEAN_TRUNC=%s LIMIT_VARIANCE_TRUNC=%s' % (format(mean,'.12f'),format(var,'.12f')))

if __name__=='__main__':main()
