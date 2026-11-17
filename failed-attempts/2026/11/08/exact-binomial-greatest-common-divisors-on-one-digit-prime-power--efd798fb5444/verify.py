"""Exact arithmetic tests for a binomial-GCD prime-power formula.

All comparisons use integer arithmetic. The bounded tests supplement,
not replace, the unrestricted proof by Kummer carries and finite differences.
"""
from math import comb, gcd

def vp_factorial(n, p):
    z = 0
    while n:
        n //= p
        z += n
    return z

def vp_binomial(n, k, p):
    return vp_factorial(n, p) - vp_factorial(k, p) - vp_factorial(n-k, p)

def vp_carries(x, y, p):
    c = ans = 0
    while x or y or c:
        c = (x % p + y % p + c) // p
        ans += c
        x //= p
        y //= p
    return ans

def primes_under(z):
    return [p for p in range(2,z) if all(p%d for d in range(2,int(p**.5)+1))]

def main():
    q_checks = 0
    direct_gcd_cases = 0
    carry_checks = 0
    for p in primes_under(40):
        P = p
        for a in range(1,7):
            if P > 1100:
                break
            for m in range(1,p):
                n=m*P
                if n<3 or n>1100:
                    continue
                k=n-1
                min_v = 10**6
                for q in range(2,n+1):
                    val=vp_binomial(q*k,k,p)
                    assert val>=a, (p,a,m,q,val)
                    min_v=min(min_v,val)
                    if (q % max(1,n//10)) == 0 or q==2 or q==n:
                        assert vp_carries(k,(q-1)*k,p)==val
                        carry_checks += 1
                    q_checks += 1
                assert min_v==a, (p,a,m,min_v)
                if n<=135:
                    d=0
                    for q in range(2,n+1):
                        d=gcd(d,comb(q*k,k))
                    assert d==P, (n,p,a,m,d)
                    direct_gcd_cases+=1
            P *= p
    print('VERIFY_OK valuation_pairs=',q_checks,'carry_checks=',carry_checks,'direct_gcd_cases=',direct_gcd_cases)

if __name__ == '__main__':
    main()
