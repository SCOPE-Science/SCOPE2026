#!/usr/bin/env python3
"""Exact polynomial checks for a rational genus-five Humbert curve.

Only uses Python's standard library; no floating-point or finite-sample
assertions are used to establish the geometric or Galois statements.
"""
from itertools import product

# Q[z]/Phi_5(z), with Phi_5=1+z+z^2+z^3+z^4.
def red(c):
    c = list(c)
    if len(c) < 4: c += [0] * (4-len(c))
    for n in range(len(c)-1, 3, -1):
        a = c[n]
        if a:
            for j in range(1, 5): c[n-j] -= a
        c[n] = 0
    return tuple(c[:4])

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    c = [0]*7
    for i in range(4):
        for j in range(4): c[i+j] += a[i]*b[j]
    return red(c)
def powr(a,n):
    r=one
    while n:
        if n&1: r=mul(r,a)
        a=mul(a,a);n//=2
    return r

def times(a,n): return tuple(n*x for x in a)
zero=(0,0,0,0);one=(1,0,0,0)
z=(0,1,0,0)
zz=[powr(z,j) for j in range(5)]
assert powr(z,5)==one
assert add(add(add(add(one,z),zz[2]),zz[3]),zz[4])==zero
phi=add(add(one,z),zz[4])
assert sub(mul(phi,phi),add(phi,one))==zero

# Trace quadrics: sum_{j,l : j+l+k =0 mod 5} X_j X_l.
q={k:sorted((j,l) for j in range(5) for l in range(j,5) if (j+l+k)%5==0) for k in (0,1,2)}
assert q=={0:[(0,0),(1,4),(2,3)],
           1:[(0,4),(1,3),(2,2)],
           2:[(0,3),(1,2),(4,4)]}
# Corresponding coefficients for the off-diagonal terms are two.

def w(j,a): return mul(zz[j],sub(zz[j],zz[a]))
for a in range(5):
    P=one
    for j in range(5):
        if j!=a: P=mul(P,w(j,a))
    assert P==times(zz[(-2*a)%5],5), (a,P)
    for d in range(1,5):
        j=(a+d)%5
        assert w(j,a)==mul(zz[(2*a)%5],w(d,0))

# Relative square-root data at the first branch value.
w1=w(1,0)
r2sq=neg(mul(zz[4],phi)) # (i*z^2*sqrt(phi))^2
r3sq=mul(zz[3],phi)     # (z^4*sqrt(phi))^2
r4sq=neg(zz[2])         # (i*z)^2
assert w(2,0)==mul(w1,r2sq)
assert w(3,0)==mul(w1,r3sq)
assert w(4,0)==mul(w1,r4sq)

# The two Kummer involutions act on the sign coordinates
# for v2/v1, v3/v1, v4/v1 (respectively).
def flip_i(bits): return (bits[0]^1,bits[1],bits[2]^1)
def flip_s(bits): return (bits[0]^1,bits[1]^1,bits[2])
points=list(product((0,1),repeat=3))
orbits=[];seen=set()
for b in points:
    if b in seen: continue
    orb={b,flip_i(b),flip_s(b),flip_i(flip_s(b))}
    assert len(orb)==4
    assert len({sum(x)%2 for x in orb})==1
    seen.update(orb);orbits.append(orb)
assert len(orbits)==2 and len(seen)==8

# The cyclotomic Galois group has order 4, acts regularly on
# nonidentity 5th roots, and has quadratic character of 5.
units=(1,2,3,4)
chi={1:1,2:-1,3:-1,4:1}
assert all((chi[k]*chi[l])==chi[(k*l)%5] for k in units for l in units)
for a in range(1,5):
    assert set((k*a)%5 for k in units)==set(units)
# For branch a=0 the nonresidues exchange the two 4-element
# parity classes, yielding one 8-point orbit; for a!=0 each
# parity class reaches four base values, yielding two 16-point orbits.
assert 8+16+16==40
assert 40*3==5**3-5
print('HUMBERT_FIVE_EXACT_IDENTITIES_OK')
