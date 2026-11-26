#!/usr/bin/env python3
"""Independent degree-subset enumeration for the cyclotomic divisor gap theorem."""
from collections import Counter


def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(n**.5)+1):
        if n % d == 0:
            return False
    return True


def totient(n):
    return sum(__import__('math').gcd(i,n)==1 for i in range(1,n+1))


def divisor_totients(n):
    return [totient(d) for d in range(1,n+1) if n%d==0]


def direct_degree_set(n):
    bits=1
    for weight in divisor_totients(n):
        bits |= bits << weight
    return {j for j in range(n+1) if (bits>>j)&1}


def closed_formula(a,b,p):
    M=2**a; n=M*p**b
    vals={u for u in range(M+1)}
    for j in range(1,b+1):
        w=(p-1)*p**(j-1)
        vals={v+w*u for v in vals for u in range(M+1)}
    if p>M+1:
        assert len(vals)==(M+1)**(b+1)
        expected=Counter({1:M*(M+1)**b})
        for j in range(1,b+1):
            expected[(p-1-M)*p**(j-1)]+=M*(M+1)**(b-j)
        assert Counter(y-x for x,y in zip(sorted(vals),sorted(vals)[1:]))==expected
        assert n+1-len(vals)==n+1-(M+1)**(b+1)
    else:
        assert len(vals)==n+1
    return vals


def run():
    checks=0
    for a in range(1,5):
        for b in range(1,4):
            for p in (3,5,7,11,13,17,19):
                if not is_prime(p):
                    continue
                n=2**a*p**b
                if n>20000: continue
                observed=direct_degree_set(n)
                predicted=closed_formula(a,b,p)
                assert observed==predicted, (a,b,p,len(observed),len(predicted))
                assert all(n-j in observed for j in observed)
                checks+=1
    print(f'VERIFY_OK: {checks} independent totient-subset enumerations; exact gap multisets and completeness regimes')

if __name__=='__main__': run()
