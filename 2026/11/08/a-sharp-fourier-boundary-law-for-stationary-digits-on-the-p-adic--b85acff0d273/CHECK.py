#!/usr/bin/env python3
"""Finite, supplementary checks of the stationary-digit Fourier boundary identity."""
import cmath
import itertools
import math

TWOPI = 2 * math.pi


def probs(word, pi, transition):
    val = pi[word[0]]
    for a, b in zip(word, word[1:]):
        val *= transition[a][b]
    return val


def reversed_transition(pi, transition):
    p = len(pi)
    return [[pi[b] * transition[b][a] / pi[a] for b in range(p)] for a in range(p)]


def direct_pair(p, pi, P, n, k):
    R = reversed_transition(pi, P)
    fwd, rev, mass_a, mass_b = 0j, 0j, 0.0, 0.0
    for w in itertools.product(range(p), repeat=n):
        a = probs(w, pi, P)
        b = probs(w, pi, R)
        x = sum(c * p**i for i,c in enumerate(w))
        y = sum(c / p**(i+1) for i,c in enumerate(w))
        fwd += a * cmath.exp(-1j * TWOPI * k * x / p**n)
        rev += b * cmath.exp(-1j * TWOPI * k * y)
        mass_a += a
        mass_b += b
    return fwd, rev, mass_a, mass_b


def reverse_prefix_fourier(p, pi, P, n, k):
    R = reversed_transition(pi,P)
    # Weighted law of the first n reverse digits, summed by a direct
    # finite-state recursion with one transition per added digit.
    z = [pi[a] * cmath.exp(-1j * TWOPI * k * a / p) for a in range(p)]
    for j in range(2,n+1):
        zz=[0j]*p
        for b in range(p):
            zz[b] = cmath.exp(-1j*TWOPI*k*b/p**j) * sum(z[a]*R[a][b] for a in range(p))
        z=zz
    return sum(z)


def test(p, pi, P, max_n, ks):
    cnt=0
    for row in P:
        assert abs(sum(row)-1)<1e-12; cnt+=1
    for j in range(p):
        assert abs(sum(pi[i]*P[i][j] for i in range(p))-pi[j])<1e-12; cnt+=1
    for n in range(1,max_n+1):
        for k in ks:
            a,b,ma,mb=direct_pair(p,pi,P,n,k)
            assert abs(ma-1)<5e-10 and abs(mb-1)<5e-10;cnt+=2
            assert abs(a-b)<5e-9;cnt+=1
            c=reverse_prefix_fourier(p,pi,P,n,k)
            assert abs(b-c)<5e-9;cnt+=1
            M=max(n+4,15)
            d=reverse_prefix_fourier(p,pi,P,M,k)
            assert abs(a-d) <= TWOPI*abs(k)*(p**(-n)+p**(-M))+2e-9;cnt+=1
    return cnt

if __name__ == '__main__':
    cases = [
        (2,[.75,.25],[[.75,.25],[.75,.25]],10,[-2,-1,1,2]),
        (2,[.5,.5],[[.82,.18],[.18,.82]],10,[-2,-1,1,2]),
        (3,[1/3]*3,[[.5,1/3,1/6],[1/6,.5,1/3],[1/3,1/6,.5]],7,[-2,-1,1,2]),
        (3,[1/3]*3,[[1/3]*3]*3,7,[-2,-1,1,2]),
    ]
    count = 0
    for p, pi, P, n, ks in cases:
        count += test(p, pi, P, n, ks)
    # For the deterministic stationary all-(p-1) digits measure,
    # the upper error bound has the sharp order p^(-n).
    for p in [2,3,5]:
        for n in range(3,16):
            value = cmath.exp(1j*TWOPI / p**n)
            assert abs(abs(value-1)/(TWOPI*p**(-n))-1)<.4
            count+=1
    # A non-Haar stationary law need not have vanishing boundary coefficients.
    p=2; pi=[.75,.25]; P=[[.75,.25],[.75,.25]]
    assert abs(reverse_prefix_fourier(p,pi,P,25,1)) > .3;count+=1
    # For Haar, all nontrivial characters disappear exactly.
    p=3;pi=[1/3]*3;P=[[1/3]*3 for _ in range(3)]
    for n in range(1,10):
        assert abs(reverse_prefix_fourier(p,pi,P,n,1))<1e-11;count+=1
    print(f'CHECK_OK finite_assertions={count} prime_alphabets=2,3,5')
