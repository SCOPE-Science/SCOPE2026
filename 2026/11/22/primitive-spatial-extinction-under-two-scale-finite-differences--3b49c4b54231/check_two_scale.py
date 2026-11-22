"""Exhaustive finite checks for primitive-input extinction under two-scale differences.

Standard library only. The analytic proof, not these finite checks, covers all
prime characteristics and all ring lengths coprime to the characteristic.
"""
from itertools import product
from math import gcd, lcm


def divisors(n):
    return [d for d in range(1,n+1) if n%d == 0]


def mobius(n):
    factors=0
    d=2
    while d*d<=n:
        if n%d==0:
            n//=d
            factors+=1
            if n%d==0:
                return 0
        d+=1
    if n>1:
        factors+=1
    return (-1)**factors


def primitive_count(n,q):
    return sum(mobius(n//d)*q**d for d in divisors(n))


def exact_extinct(n,a,b,q):
    return sum(mobius(n//d)*q**(gcd(d,a)+gcd(d,b)-gcd(d,a,b)) for d in divisors(n))


def period(x):
    n=len(x)
    for d in divisors(n):
        if all(x[i]==x[(i+d)%n] for i in range(n)):
            return d
    raise AssertionError


def output(x,a,b,q):
    n=len(x)
    return tuple((x[i]-x[(i+a)%n]-x[(i+b)%n]+x[(i+a+b)%n]) % q for i in range(n))


def main():
    checked=0
    states=0
    # The selected rings include semisimple prime powers and non-prime-powers.
    families=((2,(1,3,5,7,9,15)),(3,(1,2,4,5,7,8)),(5,(1,2,3,4,6)))
    for q, ns in families:
        for n in ns:
            if n%q==0:
                continue
            divs=divisors(n)
            # A and B below represent every stride residue class up to gcd(n,stride).
            observed={(a,b):0 for a in divs for b in divs}
            for state in product(range(q),repeat=n):
                if period(state)==n:
                    for a in divs:
                        for b in divs:
                            if all(v==0 for v in output(state,a,b,q)):
                                observed[(a,b)]+=1
                states+=1
            for (a,b),count in observed.items():
                predicted=exact_extinct(n,a,b,q)
                assert count==predicted, (q,n,a,b,count,predicted)
                exists = (count>0)
                assert exists == (lcm(gcd(n,a),gcd(n,b))==n), (q,n,a,b,exists)
                if gcd(a,b)==1 and n==a*b:
                    assert count*q==primitive_count(a,q)*primitive_count(b,q)
                checked+=1
    print('Direct configurations inspected:',states)
    print('Complete extinction counts and existence comparisons:',checked)
    print('All tests passed')

if __name__=='__main__':
    main()
