#!/usr/bin/env python3
"""Exact independent coefficient checks for the two residue families.

Uses reciprocal of (1-X^a)(1-X^b), not the two-rectangle support proof.
Run: python3 CHECK.py
"""
from collections import Counter
from math import gcd


def exact_coefficients(a, b):
    # The polynomial (1-X)(1-X^(ab))/((1-X^a)(1-X^b))
    # has degree (a-1)(b-1), strictly smaller than ab.
    d = (a-1)*(b-1)
    ways = [0]*(d+1)
    for n in range(d+1):
        ways[n] = ((n == 0)
                   + (ways[n-a] if n >= a else 0)
                   + (ways[n-b] if n >= b else 0)
                   - (ways[n-a-b] if n >= a+b else 0))
    return [ways[n]-(ways[n-1] if n else 0) for n in range(d+1)]


def predicted(a, s, sign):
    h = (a-1)//2
    if sign == 1:
        return Counter({1:2*h*h*s+2*h, **{2*j:2*s for j in range(1,h+1)}})
    return Counter({1:2*h*h*s+2*h*(h-1),
                    **{2*j:2*s+2 for j in range(1,h)}, 2*h:2*s})


def support_rows(a, b):
    coeffs = exact_coefficients(a,b)
    rows = {}
    for n,c in enumerate(coeffs):
        if c:
            rows.setdefault(n//a, []).append(n%a)
    return rows, coeffs


def expected_rows(a, s, sign):
    h=(a-1)//2
    rows={}
    if sign == 1:
        for j in range(h+1):
            for t in range(j*s,(j+h)*s+1):
                rows.setdefault(t,[]).append(2*j)
        for j in range(h):
            for t in range(j*s,(j+h+1)*s+1):
                rows.setdefault(t,[]).append(2*j+1)
    else:
        u=s+1
        for t in range((h+1)*u-1):
            rows.setdefault(t,[]).append(0)
        for t in range(h*u-1):
            rows.setdefault(t,[]).append(1)
        for j in range(1,h):
            for t in range(j*u-1,(j+h+1)*u-2):
                rows.setdefault(t,[]).append(a-2*j)
        for j in range(1,h+1):
            for t in range(j*u-1,(j+h)*u-2):
                rows.setdefault(t,[]).append(a+1-2*j)
    return {t:sorted(v) for t,v in rows.items()}


def run():
    trials=0; coeff_entries=0; row_entries=0
    examples=[]
    for a in range(5,58,2):
        for s in range(1,16):
            for sign in (+1,-1):
                b=s*a+2 if sign==1 else (s+1)*a-2
                assert b>a and gcd(a,b)==1
                rows,coeffs = support_rows(a,b)
                assert set(coeffs)<= {-1,0,1}
                predicted_rows = expected_rows(a,s,sign)
                assert rows==predicted_rows,(a,b,'row mismatch')
                nonzeros=[i for i,c in enumerate(coeffs) if c]
                hist=Counter(y-x for x,y in zip(nonzeros,nonzeros[1:]))
                expect=predicted(a,s,sign)
                assert hist==expect,(a,b,hist,expect)
                assert nonzeros[0]==0 and nonzeros[-1]==len(coeffs)-1
                assert sum(g*c for g,c in hist.items())==(a-1)*(b-1)
                trials+=1; coeff_entries+=len(coeffs);row_entries+=len(nonzeros)
                if (a,s,sign) in [(5,1,1),(5,2,-1),(7,3,1),(7,2,-1),(11,7,1),(11,2,-1)]:
                    examples.append((a,b,dict(sorted(hist.items()))))
    print('PASS: cases=%d coefficient_positions=%d support_positions=%d' %(trials,coeff_entries,row_entries))
    print('Representative histograms:',examples)

if __name__=='__main__':run()
