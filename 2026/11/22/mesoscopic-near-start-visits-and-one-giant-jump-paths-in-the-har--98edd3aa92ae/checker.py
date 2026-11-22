#!/usr/bin/env python3
"""Reproducible finite checks for mesoscopic near-start harmonic descent.
Only computational corroboration; the uniform asymptotic theorem is proved in RESULT.md.
"""
from fractions import Fraction
from math import log, isclose

checks = 0

def ok(cond, msg):
    global checks
    assert cond, msg
    checks += 1

def H_fraction(j):
    return sum((Fraction(1,t) for t in range(1,j+1)),Fraction(0))

def compositions(h,k):
    if k==1:
        if h>=1: yield (h,)
    else:
        for j in range(1,h-k+2):
            for rem in compositions(h-j,k-1):
                yield (j,)+rem

def coefficients_exact(h_max):
    # b[h][k] = [z^h] (-log(1-z))^k.
    B = [[Fraction(0) for k in range(h_max+1)] for h in range(h_max+1)]
    B[0][0] = Fraction(1)
    for h in range(1,h_max+1):
        for k in range(1,h+1):
            B[h][k] = Fraction(h-1,h)*B[h-1][k]+Fraction(k,h)*B[h-1][k-1]
    return B

def near_target_exact(n,h):
    target=n-h
    H=[H_fraction(i) for i in range(n)]
    F=[Fraction(0)]*(h+1)
    F[h]=Fraction(1)
    # F[s] = hitting probability from state n-s to n-h.
    for s in range(h-1,-1,-1):
        F[s]=sum((F[s+j]/(j*H[n-s-1]) for j in range(1,h-s+1)),Fraction(0))
    return F[0]

B=coefficients_exact(13)
for h in range(1,11):
    for k in range(1,h+1):
        manual=sum((Fraction(1,1) / prod for prod in
                    ( __import__('math').prod(parts) for parts in compositions(h,k))),Fraction(0))
        ok(B[h][k]==manual,f'convolution coefficient h={h},k={k}')
for n in range(4,22):
    for h in range(1,min(n-2,9)+1):
        exact=near_target_exact(n,h)
        low=sum((B[h][k]/H_fraction(n-1)**k for k in range(1,h+1)),Fraction(0))
        high=sum((B[h][k]/H_fraction(n-h)**k for k in range(1,h+1)),Fraction(0))
        ok(low<=exact<=high,f'path sandwich n={n},h={h}')
        ok(0<exact<1,f'probability n={n},h={h}')
        # Independent direct enumeration of all exact path weights.
        brute=Fraction(0)
        for k in range(1,h+1):
            for parts in compositions(h,k):
                prob=Fraction(1); step=0
                for j in parts:
                    prob*=1/(j*H_fraction(n-step-1)); step+=j
                brute+=prob
        ok(exact==brute,f'brute-path match n={n},h={h}')

# Approximate coefficient/asymptotic checks at large artificial n via
# O(h*K) Stirling recurrence, independently from direct chain DP.
def coefficient_spectrum(h,K):
    prev=[0.0]*(K+1)
    prev[0]=1.0
    for m in range(1,h+1):
        cur=[0.0]*(K+1)
        for k in range(1,min(m,K)+1):
            cur[k]=((m-1)*prev[k]+k*prev[k-1])/m
        prev=cur
    return prev
for n,theta in [(10**6,.25),(10**6,.5),(10**8,.25),(10**8,.5), (10**10,.4)]:
    h=round(n**theta)
    B_h=coefficient_spectrum(h,90)
    alpha=1/(log(n)+0.5772156649015329)
    approx=sum(alpha**k*B_h[k] for k in range(1,91))
    expected=1/(h*log(n)*(1-theta)**2)
    ok(abs(approx/expected-1)<.12,f'logarithmic crossover n={n},theta={theta},ratio={approx/expected}')
    # Ratio of fixed-k composition weights and predicted conditional law.
    for k in range(1,8):
        if theta > 0:
            pred=k*(1-theta)**2*theta**(k-1)
            actual=alpha**k*B_h[k]/approx
            ok(abs(actual-pred)<.04,f'conditional K n={n},theta={theta},k={k}')

print('PASS',checks,'finite exact and large-scale numerical assertions')
