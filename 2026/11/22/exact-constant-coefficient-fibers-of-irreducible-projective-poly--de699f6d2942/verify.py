"""Independent finite checks for the prescribed-constant projective-polynomial theorem.

Standard-library Python 3; run: python verify.py
The cyclic-exponent tests apply to prime powers, and the polynomial tests
implement Rabin's irreducibility criterion over small prime fields.
"""
from math import gcd
from itertools import product


def distinct_prime_factors(n):
    out = []
    t = 2
    while t * t <= n:
        if n % t == 0:
            out.append(t)
            while n % t == 0:
                n //= t
        t += 1 if t == 2 else 2
    if n > 1:
        out.append(n)
    return out


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def claimed_fibers(q, d, ell):
    m = q - 1
    u = (q**d - 1)//m
    n = (q**d - 1)//ell
    common = gcd(m, n)
    numerator = u
    denominator = d
    for prime in distinct_prime_factors(n):
        if m % prime:
            numerator *= prime - 1
            denominator *= prime
    # Work rationally before asserting divisibility of the result.
    assert numerator % denominator == 0, (q, d, ell, numerator, denominator)
    v = numerator // denominator
    return [v if gcd(r, common) == 1 else 0 for r in range(m)]


def test_exponents():
    tests = 0
    for q in (2, 3, 4, 5, 7, 8, 9, 11, 13, 16):
        for d in (2, 3, 4):
            nfield = q**d - 1
            if nfield > 180_000:
                continue
            for ell in divisors(q - 1):
                n = nfield//ell
                m = q - 1
                got = [0]*m
                for e in range(nfield):
                    if gcd(e, n) == 1:
                        got[e % m] += 1
                assert all(x % d == 0 for x in got), (q, d, ell, got)
                got = [x//d for x in got]
                predicted = claimed_fibers(q, d, ell)
                assert got == predicted, (q, d, ell, got, predicted)
                assert sum(got) == ell * totient(n)//d
                tests += 1
    return tests


def totient(n):
    out = n
    for p in distinct_prime_factors(n):
        out = out//p * (p-1)
    return out


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def mul(a, b, p):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                c[i+j] = (c[i+j]+x*y)%p
    return trim(c)


def rem(a, b, p):
    r = trim(a[:])
    inv = pow(b[-1], -1, p)
    while len(r) >= len(b) and r != [0]:
        k = len(r)-len(b)
        u = r[-1]*inv%p
        for j, y in enumerate(b):
            r[k+j] = (r[k+j]-u*y)%p
        trim(r)
    return r


def pgcd(a, b, p):
    while b != [0]:
        a, b = b, rem(a,b,p)
    return a


def powmod(a, exponent, modulus, p):
    z = [1]
    while exponent:
        if exponent & 1:
            z = rem(mul(z,a,p),modulus,p)
        exponent >>= 1
        if exponent:
            a = rem(mul(a,a,p),modulus,p)
    return z


def irreducible_rabin(f, p):
    degree = len(f)-1
    if degree <= 0: return False
    x = [0,1]
    h = x
    checkpoints = {degree//pr for pr in distinct_prime_factors(degree)}
    for k in range(1, degree+1):
        h = powmod(h,p,f,p)
        if k in checkpoints:
            v = h[:]
            if len(v) < 2: v.extend([0]*(2-len(v)))
            v[1] = (v[1]-1)%p
            if len(pgcd(trim(v),f,p)) > 1: return False
    return h == x


def test_polynomials():
    tests = 0
    # Values deliberately small enough for independent polynomial arithmetic.
    for p, d in ((2,2),(2,3),(2,4),(3,2),(3,3),(5,2),(7,2)):
        for ell in divisors(p-1):
            exponents = [(p**j-1)//ell for j in range(d)]
            degree = (p**d-1)//ell
            got = {c:0 for c in range(1,p)}
            for coefficients in product(range(p),repeat=d):
                if coefficients[0]==0: continue
                f=[0]*(degree+1)
                f[-1]=1
                for idx,a in enumerate(coefficients): f[exponents[idx]]=a
                if irreducible_rabin(f,p): got[coefficients[0]] += 1
            order = [a for a in range(1,p) if all(pow(a,(p-1)//prime,p)!=1 for prime in distinct_prime_factors(p-1))]
            # Explicit brute-force discrete logarithms in the base prime field.
            gen = order[0] if order else 1
            predicted = claimed_fibers(p,d,ell)
            for c in range(1,p):
                element = ((-1)**d*c)%p
                exponent = next(r for r in range(p-1) if pow(gen,r,p)==element)
                assert got[c]==predicted[exponent], (p,d,ell,c,got,predicted)
            tests+=1
    return tests

if __name__ == '__main__':
    a = test_exponents()
    b = test_polynomials()
    print('PASS: %d complete cyclic exponent systems and %d exhaustive sparse-polynomial parameter cases'%(a,b))
