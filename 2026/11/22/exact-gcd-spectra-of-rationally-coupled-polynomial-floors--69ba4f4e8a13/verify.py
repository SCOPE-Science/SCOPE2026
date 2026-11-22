"""Exact finite diagnostics for a rationally coupled floor-gcd limit law.

The infinite natural-density theorem requires polynomial equidistribution
and the published large-prime estimate, neither certified by finite tests.
"""
from fractions import Fraction
from math import gcd, isqrt, pi as PI
from collections import Counter


def prime_divisors(n):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.append(n)
    return out


def A(n):
    out = Fraction(1)
    for p in prime_divisors(n):
        out *= Fraction(p*p-1,p*p)
    return out


def H(c,d):
    return A(c//d)/d**2 if c % d == 0 else Fraction(0)


def pi(b,d,zeta2_inv):
    return zeta2_inv/Fraction(b*d*d) + Fraction(2,b*b) * sum(
        (b-r)*H(r,d) for r in range(1,b)
    )


def mu(n):
    out = 1
    for p in prime_divisors(n):
        if n % (p*p) == 0:
            return 0
        out = -out
    return out


def pi_mobius(b,d,zeta2_inv):
    if b <= d:
        return zeta2_inv/Fraction(b*d*d)
    t = Fraction(b,d)
    terms = [ell for ell in range(1,b) if ell*d < b]
    s1 = sum((Fraction(mu(ell),d**3 * ell**3) for ell in terms),Fraction(0))
    s2 = (zeta2_inv - sum((Fraction(mu(ell),ell*ell) for ell in terms),Fraction(0))) / (b*d*d)
    s3 = Fraction(0)
    for ell in terms:
        x = Fraction(b,d*ell)
        k = (b-1) // (d*ell)
        theta = x-k
        s3 += Fraction(mu(ell),b*b*d*ell)*theta*(1-theta)
    return s1+s2+s3


def diagnostics():
    local = 0
    for c in range(1,32):
        counts=Counter(gcd(c,gcd(x,y)) for x in range(c) for y in range(c))
        for d in range(1,c+1):
            assert Fraction(counts[d],c*c) == H(c,d), (c,d)
            local+=1
        assert sum(H(c,d) for d in range(1,c+1)) == 1

    symbolic = 0
    for b in range(1,51):
        for d in range(1,36):
            # Check exact Möbius transformation for a symbolic variable
            # zeta2_inv, by checking coefficients at two rational values.
            for v in (Fraction(0),Fraction(1)):
                assert pi(b,d,v)==pi_mobius(b,d,v),(b,d,v)
                symbolic+=1

    # Sample actual polynomial with completely exact integer-square-root
    # floors; this only tests arithmetic implementation, not asymptotics.
    empirical=[]
    N=60000
    for b in (1,2,3,5,10):
        count=0
        for n in range(1,N+1):
            t=isqrt(2*n**4)
            u=(isqrt(2*b*b*n**4)+n)//b
            assert t*t <= 2*n**4 < (t+1)*(t+1)
            count += gcd(n,gcd(t,u))==1
        predicted=float(pi(b,1,Fraction(0))) + (6/(PI*PI))/(b)
        observed=count/N
        assert abs(observed-predicted)<0.025, (b, observed, predicted)
        empirical.append((b,round(observed,5),round(predicted,5)))
    print('DEPENDENT_FLOOR_GCD_CHECK_OK', 'local_exact',local,'mobius_equalities',symbolic,'empirical_coprime',empirical)

if __name__=='__main__':
    diagnostics()
