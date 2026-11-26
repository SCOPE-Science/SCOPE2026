"""Independent finite verification of a prime-support Lucas classification.

All bounds used by the finite searches are proved in the accompanying text.
Requires Python 3 standard library only.
"""
from itertools import product
from math import gcd


def prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def legendre(d, p):
    assert prime(p) and p % 2 and d % p
    z = pow(d, (p - 1) // 2, p)
    assert z in (1, p - 1)
    return 1 if z == 1 else -1


def korselt(n, q, r, a, b, c):
    return n == 3*q*r and all((n-a*b*c) % (p-e) == 0
                                  for p, e in ((3,a),(q,b),(r,c)))


def via_diophantine():
    out = set()
    for a,b,c in product((-1,1), repeat=3):
        for k in (1,2):
            for j in range(1, 14 if k==1 else 8):
                den = j*k - 9
                num = b*(j*k - 3*a) + k*c*(3-a)
                if den == 0:
                    assert num != 0
                    continue
                if num % den: continue
                q = num//den
                if q <= 3 or not prime(q): continue
                if (3*q-a*b) % k: continue
                r = c + (3*q-a*b)//k
                if r <= q or not prime(r): continue
                n = 3*q*r
                if korselt(n, q, r, a,b,c):
                    out.add((n,q,r,a,b,c,k,j))
    return sorted(out)


def via_independent_bounded_sieve():
    out = set()
    for q in range(5,22):
        if not prime(q):continue
        for r in range(q+1,66):
            if not prime(r):continue
            n = 3*q*r
            for a,b,c in product((-1,1),repeat=3):
                if korselt(n,q,r,a,b,c):
                    out.add((n,q,r,a,b,c))
    return sorted(out)


def prime_discriminant_witness(q,r,a,b,c):
    for d in range(5,10000,4):
        if not prime(d) or d in (3,q,r):continue
        if (legendre(d,3),legendre(d,q),legendre(d,r)) == (a,b,c):
            return d
    raise AssertionError('no small prime discriminant witness')


def main():
    rows = via_diophantine()
    finite = via_independent_bounded_sieve()
    assert [(n,q,r,a,b,c) for n,q,r,a,b,c,_,_ in rows] == finite
    expected = [
        (105,5,7,-1,1,-1,2,5),
        (195,5,13,1,1,-1,1,10),
        (255,5,17,-1,1,1,1,13),
        (399,7,19,-1,-1,-1,1,7),
        (561,11,17,1,1,1,2,5),
        (2703,17,53,-1,1,1,1,10),
    ]
    assert rows == expected
    print('VERIFY_OK')
    print('diophantine_sieve_cases=160_PASS')
    print('independent_3q r_and_8_sign_bounded_sieve=PASS')
    for n,q,r,a,b,c,k,j in rows:
        assert gcd(n,3*q*r)==n and n<10000
        d = prime_discriminant_witness(q,r,a,b,c)
        assert d%4==1 and prime(d)
        signs = tuple(legendre(d,p) for p in (3,q,r))
        assert signs==(a,b,c) and korselt(n,q,r,*signs)
        assert (3*q-a*b)==k*(r-c)
        assert (3*r-a*c)==j*(q-b)
        print(f'n={n} q={q} r={r} signs={signs} k={k} j={j} prime_D={d} PASS')
    print('finite_sieves_supplement_the_proved_bounds_and_Dirichlet_argument')

if __name__=='__main__':main()
