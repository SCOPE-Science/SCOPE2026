#!/usr/bin/env python3
"""Independent exact tests for finite-field square-zero incidence units.
Only standard Python; no external data or services are needed.
"""
from itertools import product
from math import prod


def rank_mod_p(a, p):
    b = [list(row) for row in a]
    n = len(b)
    if not n:
        return 0
    c = len(b[0])
    r = 0
    for j in range(c):
        pivot = next((k for k in range(r, n) if b[k][j] % p), None)
        if pivot is None:
            continue
        b[r], b[pivot] = b[pivot], b[r]
        inv = pow(b[r][j] % p, -1, p)
        b[r] = [(v*inv) % p for v in b[r]]
        for k in range(n):
            if k != r and b[k][j] % p:
                v = b[k][j]
                b[k] = [(b[k][t]-v*b[r][t]) % p for t in range(c)]
        r += 1
        if r == n:
            break
    return r


def matrix(word, n):
    return tuple(tuple(word[i*n+j] for j in range(n)) for i in range(n))


def zero_product(a, b, n, p):
    return all(sum(a[i][k]*b[k][j] for k in range(n)) % p == 0
               for i in range(n) for j in range(n))


def gaussian(n, r, q):
    # Exact product of rational Gaussian-binomial factors.
    from fractions import Fraction
    f = prod(Fraction(q**(n-i)-1, q**(r-i)-1) for i in range(r))
    assert f.denominator == 1
    return int(f)


def formula(n, p):
    out = []
    for r in range(n+1):
        exact_a = gaussian(n,r,p)*prod(p**n-p**i for i in range(r))
        out.append(p**(n*n)*exact_a*p**(n*(n-r)))
    return out


def direct(n,p):
    matrices = [matrix(w,n) for w in product(range(p),repeat=n*n)]
    count = [0]*(n+1)
    for a in matrices:
        ra = rank_mod_p(a,p)
        for b in matrices:
            if zero_product(a,b,n,p):
                count[ra] += 1
    return [v*p**(n*n) for v in count]


def gf4_mul(a,b):
    # Polynomial basis of F_2[t]/(t^2+t+1).
    aa,b0= a,b
    out=0
    while b0:
        if b0&1:
            out ^= aa
        aa <<= 1
        if aa & 4:
            aa ^= 7
        b0 >>= 1
    return out


def direct_gf4_n2():
    p=4
    matrices = [matrix(w,2) for w in product(range(4), repeat=4)]
    counts=[0,0,0]
    for a in matrices:
        det=gf4_mul(a[0][0],a[1][1]) ^ gf4_mul(a[0][1],a[1][0])
        ra=2 if det else (0 if all(v==0 for row in a for v in row) else 1)
        for b in matrices:
            if all(gf4_mul(a[i][0],b[0][j]) ^ gf4_mul(a[i][1],b[1][j])==0
                   for i in range(2) for j in range(2)):
                counts[ra]+=1
    counts=[c*4**4 for c in counts]
    assert counts==formula(2,4),(counts,formula(2,4))
    print('DIRECT_GF4_2',counts,'TOTAL',sum(counts))


def small_checks():
    for n,p in [(1,2),(1,4),(2,2),(3,2)]:
        # For n=1 over field of order 4, multiplication/zero testing works
        # because F4 is a field but integer residues do not represent F4.
        if p == 4:
            count = [p**2, p*(p-1)]
            exp = formula(n,p)
            assert count == exp, (n,p,count,exp)
            print('ORDER4_SCALAR',n,exp)
            continue
        a,b = direct(n,p),formula(n,p)
        assert a==b,(n,p,a,b)
        print('DIRECT',n,p,b,'TOTAL',sum(b))


def asymptotic_checks():
    import math
    q=2
    d_inf=math.prod(1-q**(-j) for j in range(1,150))
    for n in (8,16,32,64):
        rr=formula(n,q)
        denom=sum(rr)
        m=n//2
        off=0 if n%2==0 else 0.5
        theta=sum(q**(-(j-off)**2) for j in range(-40,41))
        rat=2**(math.log2(denom)-(2*n*n+(n*n)//4)-math.log2(theta/d_inf))
        hmid=sum(rr[r] for r in range(n+1) if abs(r-n/2)<=3)/denom
        print('ASYMPTOTIC',n,'ratio',round(rat,9),'rank_window_mass',round(hmid,9))
        assert 0.7 < rat < 1.1 and hmid > .999


if __name__=='__main__':
    small_checks()
    direct_gf4_n2()
    asymptotic_checks()
    print('VERIFY_OK')
