#!/usr/bin/env python3
"""Finite checks for the joint full-period Fermat quotient theorem.

Python 3 standard library only. This verifies examples, not the infinite proof.
Run: python3 verify.py
"""
from collections import Counter
from cmath import exp
from itertools import product
from math import pi


def fermat_q(u, p):
    """Fermat quotient modulo p for p-units, via modular powering."""
    u = u % (p * p)
    assert u % p != 0
    return ((pow(u, p - 1, p * p) - 1) // p) % p


def add(x, y, p):
    return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)


def convol(f, g, p):
    h = Counter()
    for x, cx in f.items():
        for y, cy in g.items():
            h[add(x, y, p)] += cx * cy
    return h


def line_info(p, h0, h1):
    out = []
    for a in range(p):
        if (a + h0) % p == 0 or (a + h1) % p == 0:
            continue
        c = (fermat_q(a + h0, p), fermat_q(a + h1, p))
        v = (-pow((a + h0) % p, -1, p) % p,
             -pow((a + h1) % p, -1, p) % p)
        out.append((a, c, v))
    return out


def line_points(c, v, m, p):
    return {((m*c[0] + t*v[0]) % p, (m*c[1] + t*v[1]) % p)
            for t in range(p)}


def check(p, h0, h1):
    assert (h0 - h1) % p
    points = [(fermat_q(n+h0, p), fermat_q(n+h1, p))
              for n in range(p*p) if (n+h0) % p and (n+h1) % p]
    R = p-2
    assert len(points) == p*R
    mu = Counter(points)
    info = line_info(p, h0, h1)
    assert len(info) == R
    directions = {(v[1]*pow(v[0],-1,p)) % p for _,c,v in info}
    assert len(directions) == R == len(set(range(p))-{0,1})
    assert directions == set(range(p))-{0,1}
    mu_lines = Counter(z for _,c,v in info for z in line_points(c,v,1,p))
    assert mu == mu_lines
    for m in [1,2,3]:
        r = mu if m==1 else convol(r,mu,p)
        if m>=2:
            expected=Counter({(x,y):p**(m-2)*(R**m-R)
                              for x in range(p) for y in range(p)})
            for _,c,v in info:
                for z in line_points(c,v,m,p):
                    expected[z] += p**(m-1)
            assert r == expected, (p,h0,h1,m)
            if p>=5:
                assert len(r)==p*p
                assert min(r.values())==p**(m-2)*(R**m-R)
        moment=sum(v*v for v in r.values())
        assert moment==p**(2*m-2)*(R**(2*m)+R*(p-1)),(p,h0,h1,m)
    for u,v in product(range(p), repeat=2):
        if u==v==0:
            continue
        if u*v*(u+v)%p==0:
            # Exact cancellation of complete t-sums (not floating point).
            assert not [a for a,c,d in info if (u*d[0]+v*d[1])%p==0]
        else:
            candidates=[(a,c) for a,c,d in info if (u*d[0]+v*d[1])%p==0]
            assert len(candidates)==1
    if p<=11:
        zeta=exp(2j*pi/p)
        for u,v in product(range(p),repeat=2):
            calc=sum(count*zeta**((u*x+v*y)%p) for (x,y),count in mu.items())
            want=(p*R if u==v==0 else
                  (0 if u*v*(u+v)%p==0 else p*zeta**(
                   (u*line_info(p,h0,h1)[next(i for i,(a,c,d) in enumerate(info)
                      if (u*d[0]+v*d[1])%p==0)][1][0]
                    +v*line_info(p,h0,h1)[next(i for i,(a,c,d) in enumerate(info)
                      if (u*d[0]+v*d[1])%p==0)][1][1])%p)))
            assert abs(calc-want)<1e-6,(p,h0,h1,u,v,calc,want)
    return len(mu)


def main():
    cases=0; image_total=0
    for p in [3,5,7,11,13,17,19]:
        for h0,h1 in [(0,1), (0,2), (-3,4), (6,-1), (1,p+2)]:
            if (h0-h1)%p==0:continue
            image_total+=check(p,h0,h1)
            cases+=1
    print('VERIFY_OK prime_cases=%d image_entries=%d m=1,2,3 exact_convolutions=PASS '
          'all_nonzero_frequency_classes=PASS complex_Fourier_small_primes=PASS '
          'two_sum_full_support_and_sharp_min=PASS' % (cases,image_total))

if __name__=='__main__': main()
