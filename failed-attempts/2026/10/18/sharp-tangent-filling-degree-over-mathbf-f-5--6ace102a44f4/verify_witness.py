#!/usr/bin/env python3
"""Pure-standard-library exact point/tangent certificate over the field with five elements."""
from itertools import product

P = [(x, y, 1) for x, y in product(range(5), repeat=2)]
P += [(x, 1, 0) for x in range(5)] + [(1, 0, 0)]

def f(p):
    x,y,z=p
    return (x**4+x**3*y+y**3*z-z**4)%5

def grad(p):
    x,y,z=p
    return ((4*x**3+3*x*x*y)%5,(x**3+3*y*y*z)%5,(y**3-4*z**3)%5)

def normalize(triple):
    assert any(triple)
    for a in reversed(triple):
        if a:
            inv=pow(a,-1,5)
            return tuple((t*inv)%5 for t in triple)

on_curve=[p for p in P if f(p)==0]
lines=sorted({normalize(grad(p)) for p in on_curve})
covered={p for p in P if any(sum(a*b for a,b in zip(line,p))%5==0 for line in lines)}
assert len(P)==31
assert len(on_curve)==11
assert len(lines)==11
assert all(any(grad(p)) for p in on_curve)
assert len(covered)==31
print('quartic points:',len(on_curve))
print('tangent lines:',len(lines))
print('normalized tangent line coefficients:',lines)
print('covered projective points:',len(covered))
print('WITNESS_VERIFIED')
