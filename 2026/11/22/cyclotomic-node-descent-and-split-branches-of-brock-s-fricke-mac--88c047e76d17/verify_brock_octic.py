#!/usr/bin/env python3
"""Exact algebraic certificate for the singular-node and Frobenius statements.

Requires Python 3.10+ and sympy. All algebraic identities use exact integer
and rational coefficients. Brute-force finite-field checks are auxiliary only.
"""
import sympy as s

x, y, t, r, z = s.symbols('x y t r z')
P = 1 + 7*t + 21*t**2 + 35*t**3 + 28*t**4
G = 4*t**2 + 3*t + 1
A = t**2 - 2*t - 1
H = 64*t**4 + 71*t**3 + 35*t**2 + 9*t + 1
Q = 49*t**4 + 48*t**3 + 26*t**2 + 8*t + 1
assert s.expand(7*P - 2*t*s.diff(P,t) + 7*A*G) == 0
assert s.expand(196*t**5 - s.diff(P,t)**2 + 49*G*H) == 0
assert s.resultant(A,H,t) == 392
assert s.discriminant(G,t) == -7
assert s.discriminant(Q,t) == 2**12 * 7**2
assert s.expand(P**2 - 16*t**7 - G**2*Q) == 0
assert s.rem(t*s.diff(P,t,2) - 6*s.diff(P,t), G, t) == 0
assert s.rem(s.diff(P,t) + t*s.diff(P,t,2) - s.Rational(49,4)*(1-t), G, t) == 0

F = 1 + 7*x*y + 21*x**2*y**2 + 35*x**3*y**3 + 28*x**4*y**4 + 2*x**7 + 2*y**7
R = 2*r*r + r + 1
for f in (F, s.diff(F,x), s.diff(F,y), s.diff(F,x,2), s.diff(F,y,2)):
    assert s.rem(s.expand(f.subs({x:r,y:r})), R, r) == 0
assert s.rem(s.expand(s.diff(F,x,y).subs({x:r,y:r}) - s.Rational(49,4)*(1-r*r)),R,r) == 0
assert s.rem(s.expand(r**7 - (7*r+5)/64),R,r) == 0
assert s.rem(s.expand((r*r) + (r+1)/2),R,r) == 0

gauss = z + z**2 + z**4 - z**3 - z**5 - z**6
assert s.rem(s.expand(gauss**2 + 7), sum(z**j for j in range(7)),z) == 0

node_x = 128*x**14 - 13*x**7 + 1
f2 = 2*x**2 + x + 1
f6a = 8*x**6 - 16*x**5 + 18*x**4 - 15*x**3 + 9*x**2 - 4*x + 1
f6b = 8*x**6 + 12*x**5 + 4*x**4 - x**3 + 2*x**2 + 3*x + 1
assert s.expand(f2*f6a*f6b - node_x) == 0
assert all(s.Poly(z,x).is_irreducible for z in (f2,f6a,f6b))

expected = {1:[1]*14, 2:[1,1,3,3,3,3], 3:[2,6,6],
            4:[1,1,3,3,3,3], 5:[2,6,6], 6:[2]*7}
for a in range(1,7):
    quadratic_residue = pow(a,3,7) == 1
    def step(z):
        sign,j=z
        return (sign if quadratic_residue else 1-sign, (a*j)%7)
    unseen = {(sign,j) for sign in range(2) for j in range(7)}
    cycles=[]
    while unseen:
        start=min(unseen);cur=start;size=0
        while cur in unseen:
            unseen.remove(cur);size+=1;cur=step(cur)
        assert cur==start
        cycles.append(size)
    assert sorted(cycles)==expected[a],(a,cycles)

for p in (3,5,11,13,17,19,23,29,31,37,41,43):
    count=0
    for a in range(p):
        for b in range(p):
            v=a*b%p
            fp=(1+7*v+21*v*v+35*v**3+28*v**4+2*pow(a,7,p)+2*pow(b,7,p))%p
            dp=(7+42*v+105*v*v+112*v**3)%p
            if fp == (b*dp+14*pow(a,6,p))%p == (a*dp+14*pow(b,6,p))%p == 0:
                count+=1
    assert count == (14 if p%7==1 else 2 if p%7 in (2,4) else 0), (p,count)

print('BROCK_OCTIC_NODE_GALOIS_AND_BRANCH_CERTIFICATE_OK')
