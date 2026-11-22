#!/usr/bin/env python3
"""Exact finite-group checks of a three-point Fourier-zero classification.
Uses rational phases, no floating point tolerance. Does not substitute for proof."""
from itertools import product
from fractions import Fraction
from math import prod, gcd

def elements(moduli):
    return list(product(*(range(n) for n in moduli)))

def add(a,b,ns):
    return tuple((x+y)%n for x,y,n in zip(a,b,ns))

def sub(a,b,ns):
    return tuple((x-y)%n for x,y,n in zip(a,b,ns))

def order(a,ns):
    from math import lcm
    o=1
    for x,n in zip(a,ns):
        o=lcm(o,n//gcd(n,x))
    return o

def subgroup(a,b,ns):
    z=(0,)*len(ns)
    seen={z}; stack=[z]
    while stack:
        x=stack.pop()
        for y in (a,b):
            v=add(x,y,ns)
            if v not in seen:seen.add(v);stack.append(v)
    return seen

def phase(c,a,ns):
    return sum((Fraction(x*y,n) for x,y,n in zip(c,a,ns)),Fraction(0))%1

def run():
    cases=[(n,) for n in range(3,24)] + [(2,2),(2,4),(2,6),(2,8),(2,10),(2,12),(3,3),(3,4),(3,6),(3,9),(4,4),(4,6),(5,5),(2,2,2),(2,2,3),(2,2,4),(2,3,5),(2,3,3),(3,3,3)]
    checked=0; two_good=0; v4=0
    for ns in cases:
        G=elements(ns); z=(0,)*len(ns)
        for i,a in enumerate(G):
            if a==z:continue
            for b in G[i+1:]:
                if b==z:continue
                H=subgroup(a,b,ns);h=len(H)
                ma,mb,mc=order(a,ns),order(b,ns),order(sub(a,b,ns),ns)
                restrictions=sorted({(phase(c,a,ns),phase(c,b,ns)) for c in G})
                assert len(restrictions)==h,(ns,a,b,h)
                good=sum(ua!=0 and ub!=0 and ua!=ub for ua,ub in restrictions)
                formula=h-h//ma-h//mb-h//mc+2
                assert good==formula,(ns,a,b,good,formula)
                assert (good==0)==(h==4 and ma==mb==mc==2),(ns,a,b,h,good)
                count_pairs=sum(1 for j in range(h) for k in range(j+1,h)
                        if restrictions[j][0]!=restrictions[k][0] and restrictions[j][1]!=restrictions[k][1]
                        and (restrictions[j][0]-restrictions[j][1])%1 != (restrictions[k][0]-restrictions[k][1])%1)
                assert count_pairs==h*good//2,(ns,a,b,count_pairs,h*good//2)
                checked+=1; two_good+=count_pairs; v4+=(good==0)
    print('VERIFY_OK', 'fixed_supports=',checked,'double_zero_coefficient_lines=',two_good,'klein_four_supports=',v4)
if __name__=='__main__':run()
