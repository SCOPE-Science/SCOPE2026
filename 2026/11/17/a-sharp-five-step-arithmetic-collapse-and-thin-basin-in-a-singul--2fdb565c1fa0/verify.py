#!/usr/bin/env python3
"""Exact integer checks for a four-quadrant piecewise-affine dynamical map."""
from collections import Counter

SMALL = {(-1,-1), (1,-1), (1,1), (-1,1)}
LARGE = {(1,-3), (3,3), (-1,5), (-5,3)}
CORE = SMALL | LARGE

def T(x,y):
    return (abs(x)-y-1, x+abs(y)-1)

def R(p,q):
    x, y = p+q-1, p-q-1
    xx, yy = T(x,y)
    assert ((xx+yy+2)%2==0) and ((xx-yy)%2==0)
    return ((xx+yy+2)//2,(xx-yy)//2)

def small_initial(x,y):
    return ((x <= -2 and y in (-x-1,-x))
            or (x == -1 and y <= 1)
            or (x == 0 and y in (-2,-1,0))
            or (x == 1 and y >= -1)
            or (x >= 2 and y == x-2))

def small_transformed(p,q):
    return ((p == 0 and q in (0,1))
            or (p == 1 and q <= 1)
            or (p >= 2 and q in (1,2-p)))

# Two invariant primitive cycles; direct exact check.
for z in CORE:
    assert T(*z) in (SMALL if z in SMALL else LARGE)
for z in [(-1,-1),(1,-3)]:
    zz=z
    for j in range(1,5):
        zz=T(*zz)
        assert (zz==z)==(j==4)

# The two logically independent finite checks are corroboration of the
# symbolic all-parameter case table in RESULT.md, not a proof by sampling.
ct=0
for p in range(0,101):
    for q in range(-100,101):
        z=(p,q)
        for _ in range(4):z=R(*z)
        x,y=z[0]+z[1]-1,z[0]-z[1]-1
        assert (x,y) in CORE
        assert (x,y) in SMALL if small_transformed(p,q) else (x,y) in LARGE
        ct+=1

for N in (2,3,10,30,100):
    count=0
    for x in range(-N,N+1):
        for y in range(-N,N+1):
            z=(x,y)
            for j in range(5):z=T(*z)
            assert z in CORE
            assert (z in SMALL)==small_initial(x,y)
            count += z in SMALL
    assert count == 5*N+4,(N,count)

assert T(*T(*T(*T(*(-3,0))))) not in CORE
z=(-3,0)
for _ in range(5):z=T(*z)
assert z==(1,-3)
print('VERIFY_OK period_cycles=2 transformed_cases=20301 square_counts=5 sharpness=1')
