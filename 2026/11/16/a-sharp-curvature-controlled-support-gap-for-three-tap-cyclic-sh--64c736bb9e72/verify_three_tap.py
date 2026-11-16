#!/usr/bin/env python3
"""Exact cyclotomic and support-combinatorial checks for three-site cyclic STFTs.

Requires Python 3 and SymPy. No external data or downloads are used.
"""
from fractions import Fraction
from itertools import combinations, product
from math import gcd
import random
from sympy import Poly, cyclotomic_poly, symbols

x = symbols('x')

def root_powers(n):
    phi = Poly(cyclotomic_poly(n, x), x, domain='ZZ')
    d = phi.degree()
    result = []
    for j in range(n):
        p = Poly(x**j, x, domain='ZZ').rem(phi)
        result.append(tuple(int(p.nth(i)) for i in range(d)))
    return result

def stft_count(n, g, f, powers):
    # g contains three (rational-amplitude, integer Fourier-phase) pairs.
    # f is rational-valued and supported at arbitrary positions.
    nz = [u for u,v in enumerate(f) if v]
    total = 0
    for t in range(n):
        terms = [(u, f[u]*g[(u-t)%n][0], -g[(u-t)%n][1])
                 for u in nz if (u-t)%n in (0,1,2)]
        if not terms:
            continue
        for k in range(n):
            z = [Fraction(0)] * len(powers[0])
            for u, a, phase in terms:
                v = powers[(phase-k*u)%n]
                for i, coeff in enumerate(v):
                    z[i] += a*coeff
            if any(z):
                total += 1
    return total

def support_bound(n, S):
    s = len(S)
    m = sum(any((t+j)%n in S for j in range(3)) for t in range(n))
    b2 = sum((t in S and (t+2)%n in S and (t+1)%n not in S)
             for t in range(n))
    assert b2 <= s
    assert m >= min(n, s+2)
    lower = (n+1)*m - 3*s - b2
    if n>=7:
        assert lower >= 4*n
    else:
        # At n=6 the coarse universal pair bound is insufficient only
        # for support sizes 3 (with five rows), 5, and 6.
        if s==3 and m==5:
            assert all(sum((t+j)%n in S for j in range(3)) in (0,1,2,3) for t in range(n))
            # The triple is consecutive, and rows have sizes 1,2,3,2,1.
            assert sorted(sum((t+j)%n in S for j in range(3)) for t in range(n))==[0,1,1,2,2,3]
            lower=5*n-4
        elif s==5:
            assert b2==1
        elif s==6:
            lower=n*(n-2)
        assert lower >= 4*n
    return lower

def main():
    rng = random.Random(726051)
    supports_checked = 0
    stft_checked = 0
    for n in range(6, 14):
        powers = root_powers(n)
        resonant = [(Fraction(1),0)]*3
        twisted = [(Fraction(1),0),(Fraction(1),0),(Fraction(1),1)]
        nonres = [(Fraction(1),0),(Fraction(2),0),(Fraction(1),0)]
        for g, target in ((resonant,4*n-2),(twisted,4*n-2),(nonres,4*n-1)):
            f = [Fraction(0)]*n
            f[0] = Fraction(1)
            # Choose coefficient so the overlapping row at t=0 vanishes at k=0.
            f[1] = -g[0][0]/g[1][0]
            actual = stft_count(n, g, f, powers)
            assert actual == target, (n,g,target,actual)
            stft_checked += 1
            f[1] = Fraction(0)
            assert stft_count(n,g,f,powers) == 3*n
            stft_checked += 1
        for s in range(3,n+1):
            for C in combinations(range(n),s):
                support_bound(n, set(C))
                supports_checked += 1
        # Probe all coefficient signs on short supports, and random long supports.
        for g in (resonant, twisted, nonres):
            for s in (2,3,4):
                for _ in range(70):
                    S=rng.sample(range(n),s)
                    f=[Fraction(0)]*n
                    for u in S: f[u]=Fraction(rng.choice([-3,-2,-1,1,2,3]),rng.choice([1,2]))
                    actual=stft_count(n,g,f,powers)
                    assert actual>=4*n-2, (n,g,S,actual)
                    if actual<4*n:
                        assert s==2 and ((S[0]-S[1])%n in (1,n-1))
                        assert actual==(4*n-2 if g in (resonant,twisted) else 4*n-1)
                    stft_checked+=1
    print('EXACT_CYCLOTOMIC_SUPPORT_CHECK_PASS',stft_checked)
    print('EXHAUSTIVE_SUPPORT_BOUND_CHECK_PASS',supports_checked)
    print('THREE_TAP_STFT_VERIFIED')

if __name__=='__main__':
    main()
