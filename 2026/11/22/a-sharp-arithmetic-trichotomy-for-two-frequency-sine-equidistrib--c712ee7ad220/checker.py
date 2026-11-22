#!/usr/bin/env python3
"""Supplementary finite checks for a two-frequency sine extremal theorem.
All global claims rest on the supplied analytic proof, not this finite test.
"""
import math
from math import pi, sin, cos, gcd

def constant(m,n):
    d=gcd(m,n); r,s=m//d,n//d; S=r+s
    if S%2: return cos(pi/(2*S))
    if S%4==0: return cos(pi/S)
    return 1.

def stationary(m,n):
    S=m+n; D=n-m
    positions=[(2*j+1)*pi/S for j in range(S)]
    positions += [(2*j+1)*pi/D for j in range(D)]
    F=lambda t:n*sin(m*t)+m*sin(n*t)
    return max(F(t) for t in positions)

def contacts(m,n):
    S=m+n;c=constant(m,n)
    return [((2*j+1)*pi/S)%(2*pi) for j in range(S)
            if abs(sin(m*(2*j+1)*pi/S)-c)<1e-8
            and abs(sin(n*(2*j+1)*pi/S)-c)<1e-8]

count=0
for m in range(1,33):
    for n in range(m+1,35):
        if gcd(m,n)!=1: continue
        c=constant(m,n); S=m+n
        v=stationary(m,n)
        assert abs(v-S*c)<5e-11,(m,n,v,S*c)
        T=contacts(m,n)
        expected=2 if S%4==0 else 1
        assert len(T)==expected,(m,n,T)
        for t in T:
            assert abs(sin(m*t)-c)<1e-10
            assert abs(sin(n*t)-c)<1e-10
            assert abs(cos(m*t)+cos(n*t))<1e-9,(m,n,t)
        a=n/(S*c);b=m/(S*c)
        assert abs(a+b-1/c)<1e-12
        assert abs(v/(S*c)-1)<1e-11
        # Independent dense grid check of the globally quantified candidate.
        for j in range(257):
            t=2*pi*j/257
            assert a*sin(m*t)+b*sin(n*t)<1+2e-12
        count+=1
print('PASS:',count,'coprime frequency pairs; exact critical-point enumeration, arithmetic contacts, candidate feasibility and mesh corroboration')
