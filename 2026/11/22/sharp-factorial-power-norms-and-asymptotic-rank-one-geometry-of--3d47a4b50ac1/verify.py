#!/usr/bin/env python3
"""Exact coefficient checks and finite asymptotic diagnostics for a Volterra power theorem.

Uses only the Python standard library. These checks are supplementary to the proof.
"""
from fractions import Fraction
from math import comb, factorial, gcd, pi, sqrt

COUNT = 0

def check(condition, message):
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(message)

def multiply(p, q):
    r = {}
    for i, x in p.items():
        for j, y in q.items():
            r[i+j] = r.get(i+j, Fraction(0)) + x*y
    return {i:x for i,x in r.items() if x}

def power(p, n):
    result = {0:Fraction(1)}
    for _ in range(n):
        result = multiply(result,p)
    return result

def scale(p,c):
    return {i: c*x for i,x in p.items() if c*x}

def add(p,q):
    r = dict(p)
    for i,x in q.items():
        r[i]=r.get(i,Fraction(0))+x
    return {i:x for i,x in r.items() if x}

def integrate(p):
    return {i+1: x/Fraction(i+1) for i,x in p.items()}

def tg(p,g):
    derivative={j-1:Fraction(j)*a for j,a in g.items()}
    return integrate(multiply(p,derivative))

def iterate(p,g,k):
    for _ in range(k):
        p=tg(p,g)
    return p

def independent_integral(p,g,k):
    # Expand (g(z)-g(w))**(k-1) in the exact repeated-integral kernel.
    derivative={j-1:Fraction(j)*a for j,a in g.items()}
    out={}
    for ell in range(k):
        left=power(g,k-1-ell)
        inside=integrate(multiply(multiply(p,derivative),power(g,ell)))
        part=multiply(left,inside)
        out=add(out,scale(part,Fraction((-1)**ell*comb(k-1,ell),factorial(k-1))))
    return out

def boundary_constant(g):
    total=sum(g.values()); support=sorted(g)
    h=0
    for j in support[1:]:h=gcd(h,j-support[0])
    probs={j:float(v/total) for j,v in g.items()}
    mean=sum(j*p for j,p in probs.items())
    variance=sum((j-mean)**2*p for j,p in probs.items())
    return float(total), h, variance

def laplace_test(g,k):
    total,h,var=boundary_constant(g)
    norm=sqrt(sum(float(c*c) for c in power(g,k).values()))
    leading=total**k*(h*h/(4*pi*k*var))**.25
    return norm/leading

def main():
    families=(
        {1:Fraction(1),2:Fraction(1,2)},
        {1:Fraction(1),3:Fraction(1,2)},
        {1:Fraction(1),2:Fraction(2,3),4:Fraction(1,3)},
    )
    for g in families:
        total,h,var=boundary_constant(g)
        check(total>0 and h>=1 and var>0, 'symbol parameters')
        for k in range(1,8):
            check(scale(iterate({0:Fraction(1)},g,k),factorial(k))==power(g,k),'exact power on constant')
            for n in range(5):
                direct=iterate({n:Fraction(1)},g,k)
                integral=independent_integral({n:Fraction(1)},g,k)
                check(direct==integral, 'iterated integral identity')
        for k in (40,80,120):
            ratio=laplace_test(g,k)
            check(abs(ratio-1)<0.035, 'finite coefficient Laplace check')
            print('support=',sorted(g),'k=',k,'ratio=',format(ratio,'.9f'))
    # Distinct supports with the same relative spacing have identical H2 norms:
    # z + z**2/2 and z + z**3/2, for every finite integer power.
    f1,f2=families[:2]
    for k in range(1,31):
        check(sum(c*c for c in power(f1,k).values())==sum(c*c for c in power(f2,k).values()),'support rescaling')
    print('PASS:', COUNT, 'finite exact/numerical assertions')

if __name__=='__main__':
    main()
