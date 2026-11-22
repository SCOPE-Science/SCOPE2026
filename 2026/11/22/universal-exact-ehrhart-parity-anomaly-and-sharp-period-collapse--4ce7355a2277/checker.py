#!/usr/bin/env python3
"""Exact finite corroboration of the odd-cycle Ehrhart parity theorem.

All enumerations are by integer dynamic programming, all interpolation and
parity comparisons use SymPy exact rationals. This is not an infinite proof.
"""
from fractions import Fraction
from itertools import product
from sympy import Symbol, interpolate, expand, Rational

def count(b,t):
    d=len(b)
    if t==0:return 1
    caps=[t*v for v in b]
    total=0
    for first in range(min(caps[0],caps[-1])+1):
        states={first:1}
        for cap in caps[:-1]:
            nxt={}
            for x,ways in states.items():
                for y in range(cap-x+1):
                    nxt[y]=nxt.get(y,0)+ways
            states=nxt
        total+=sum(ways for last,ways in states.items() if last+first<=caps[-1])
    return total

def half_corner(b):
    d=len(b)
    return tuple(Fraction(sum((-1)**j*b[(i+j)%d] for j in range(d)),2) for i in range(d))

def audit(b):
    d=len(b)
    assert d%2 and d>=3 and all(z>0 for z in b)
    h=half_corner(b)
    # Cyclic relations x_i+x_{i+1}=b_i.
    assert all(h[i]+h[(i+1)%d]==b[i] for i in range(d))
    fractional=all(z>0 for z in h) and (sum(b)%2==1)
    t=Symbol('t'); v=[count(b,j) for j in range(2*d+4)]
    e=expand(interpolate([(j,v[j]) for j in range(0,2*d+2,2)],t))
    o=expand(interpolate([(j,v[j]) for j in range(1,2*d+3,2)],t))
    gap=expand(e-o)
    wanted=Rational(1,2**d) if fractional else 0
    assert gap==wanted, (b,gap,wanted)
    assert expand(e.subs(t,2*d+2))==v[2*d+2]
    assert expand(o.subs(t,2*d+3))==v[2*d+3]
    return str(gap)

def main():
    cases=[(1,1,1),(2,1,2),(1,1,3),(3,2,3,2,3),
           (2,1,2,1,2),(4,3,4,3,4),(1,1,1,1,1),
           (3,3,3,3,3),(4,3,4,3,4,3,4)]
    for m in (1,2,3):
        d=2*m+1
        for s in (1,2,3,4):cases.append(tuple(s+int(i%2==0) for i in range(d)))
    cases=list(dict.fromkeys(cases))
    for b in cases:
        gap=audit(b)
        print('PASS d=%d b=%s parity_gap=%s'%(len(b),','.join(map(str,b)),gap))
    print('PASS cases=%d'%len(cases))
if __name__=='__main__':main()
