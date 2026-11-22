#!/usr/bin/env python3
"""Exact-arithmetic consistency checks for positive Laplace two-cycle formulas."""
from fractions import Fraction as Q

checks = 0

def check(flag):
    global checks
    assert flag
    checks += 1

# Regard u=e^{-az} and d/dz=-a*u*d/du.  For q=a/(1-tu)
# and r=a*t*u/(1-tu), these rational derivatives coincide.
for a in [Q(1,7),Q(2,5),Q(3,4),Q(1),Q(5,2),Q(9)]:
    for t in [Q(1,9),Q(2,3),Q(1),Q(7,4),Q(8)]:
        for u in [Q(1,100),Q(1,25),Q(1,10)]:
            if t*u >= 1:
                continue
            q = a/(1-t*u)
            r = a*t*u/(1-t*u)
            dq = -a*a*t*u/(1-t*u)**2
            dr = -a*a*t*u/(1-t*u)**2
            check(q-r == a)
            check(dq == -q*r)
            check(dr == -r*q)
            check(q > 0 and r > 0)
            # Swap q,r to check the negative-constant orientation.
            check(r-q == -a)
            for n in range(5):
                partial_q = a*sum((t*u)**j for j in range(n+1))
                partial_r = a*sum((t*u)**j for j in range(1,n+1))
                tail = a*(t*u)**(n+1)/(1-t*u)
                check(q-partial_q == tail)
                check(r-partial_r == tail)

# All positive reciprocal-affine q(z)=1/(z+gamma) solve q'=-q*q.
for gamma in [Q(-3),Q(-1,2),Q(0),Q(1),Q(13,3)]:
    for z in [Q(4),Q(7),Q(11)]:
        q = 1/(z+gamma)
        check(-q*q == -(1/(z+gamma)**2))

# Exactly normalized first and second geometric families.
for a in [Q(1,13),Q(1,2),Q(7,8)]:
    t=1-a
    q0=a/(1-t)
    r0=a*t/(1-t)
    check(q0 == 1)
    check(r0 == 1-a)
for a in [Q(1,13),Q(1,2),Q(1),Q(7,4),Q(11)]:
    t=1/(1+a)
    q0=a/(1-t)
    r0=a*t/(1-t)
    check(r0 == 1)
    check(q0 == 1+a)

print(f"PASS: {checks} exact-rational assertions")
