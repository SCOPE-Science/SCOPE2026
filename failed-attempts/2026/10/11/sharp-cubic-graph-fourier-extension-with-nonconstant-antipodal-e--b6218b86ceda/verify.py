#!/usr/bin/env python3
"""Independent finite-group checks of the cubic-graph L2-to-L4 inequality.

No external dependencies. Tests prime fields and the quadratic extension F_25.
A finite check is corroboration, not the proof for arbitrary finite fields.
"""
from __future__ import annotations
from collections import defaultdict
import cmath
import math
import random


def field(q):
    if q == 25:
        # A square root alpha of 3 is adjoined to F_5 (3 is a nonsquare).
        elements = tuple((a, b) for a in range(5) for b in range(5))
        add = lambda x,y: ((x[0]+y[0])%5, (x[1]+y[1])%5)
        mul = lambda x,y: ((x[0]*y[0]+3*x[1]*y[1])%5,
                           (x[0]*y[1]+x[1]*y[0])%5)
        neg = lambda x: ((-x[0])%5, (-x[1])%5)
        zero = (0,0)
    else:
        elements = tuple(range(q))
        add = lambda x,y: (x+y)%q
        mul = lambda x,y: (x*y)%q
        neg = lambda x: (-x)%q
        zero = 0
    cube = lambda x: mul(mul(x,x),x)
    return elements,add,mul,neg,zero,cube


def ratio_direct(elements, add, cube, f):
    conv = defaultdict(complex)
    for x in elements:
        for y in elements:
            conv[(add(x,y), add(cube(x),cube(y)))] += f[x]*f[y]
    energy = sum(abs(z)**2 for z in conv.values())
    S = sum(abs(z)**2 for z in f.values())
    return energy/S**2


def ratio_formula(elements, neg, zero, f):
    S = sum(abs(z)**2 for z in f.values())
    diag = sum(abs(z)**4 for z in f.values())
    collapsed_products = sum(f[x]*f[neg(x)] for x in elements)
    opp = sum(abs(f[x]*f[neg(x)])**2 for x in elements if x !=zero)
    return (2*S*S -diag-abs(f[zero])**4-2*opp+abs(collapsed_products)**2)/(S*S)
    # Here 'opp' visits each antipodal pair twice, and the 2*opp term equals
    # four times the sum of |f(x)f(-x)|^2 over unordered pairs.


def test(q, rng):
    elements,add,mul,neg,zero,cube = field(q)
    seen = {}
    for x in elements:
        for y in elements:
            s=add(x,y)
            if s == zero: continue
            key=(s,add(cube(x),cube(y)))
            pair=frozenset((x,y))
            assert key not in seen or seen[key] ==pair, (q,key)
            seen[key] = pair
    bound=3-6/(2*q+1)
    # The prescribed all-field extremizer, with nontrivial antipodal phases.
    f={zero:complex(math.sqrt(3),0)}
    visited={zero}
    for x in elements:
        if x in visited:continue
        y=neg(x)
        assert x!=y
        theta=rng.uniform(-math.pi,math.pi)
        f[x]=math.sqrt(2)*cmath.exp(1j*theta)
        f[y]=math.sqrt(2)*cmath.exp(-1j*theta)
        visited.update((x,y))
    direct=ratio_direct(elements,add,cube,f)
    derived=ratio_formula(elements,neg,zero,f)
    assert abs(direct-bound)<5e-12,(q,direct,bound)
    assert abs(derived-bound)<5e-12,(q,derived,bound)
    for trial in range(40):
        f={x:complex(rng.uniform(-2,2),rng.uniform(-2,2)) for x in elements}
        direct=ratio_direct(elements,add,cube,f)
        derived=ratio_formula(elements,neg,zero,f)
        assert abs(direct-derived)<5e-12,(q,trial,direct,derived)
        assert direct <=bound+5e-12,(q,trial,direct,bound)
    print(f'q={q}: unordered-pair fiber check, 40 random vectors, '
          f'sharp extremizer checked; sharp fourth-power ratio={bound:.12f}')

if __name__=='__main__':
    rng=random.Random(420052024)
    for q in (5,7,11,13,25):test(q,rng)
    print('PASS: 200 non-extremal tests and five sharpness tests.')
