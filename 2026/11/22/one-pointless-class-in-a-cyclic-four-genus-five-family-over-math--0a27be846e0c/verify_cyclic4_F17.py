#!/usr/bin/env python3
"""Exact exhaustive classification of pointless cyclic-four genus-five pullbacks over F17.

All loops range over the full 17-element field, with a finite-field discriminant test.
"""
p=17
sq={x*x%p for x in range(p)}
non=set(range(1,p))-sq
H={pow(x,4,p) for x in range(1,p)}
assert sq=={0,1,2,4,8,9,13,15,16}
assert H=={1,4,13,16}

def smooth(a,b,c):
    # Discriminant of a*T^3+b*T+c, up to a nonzero factor.
    return (-4*a*b**3-27*a*a*c*c)%p!=0

def pointless(a,b,c):
    return a in non and c in non and all((a*t**3+b*t+c)%p not in sq for t in H)

triple=[(a,b,c) for a in range(1,p) for b in range(p) for c in range(1,p)]
sm=[q for q in triple if smooth(*q)]
pts=[q for q in sm if pointless(*q)]
assert len(triple)==4352 and len(sm)==4096 and len(pts)==32
normalized=[(a,b) for a in range(1,p) for b in range(p) if smooth(a,b,3) and pointless(a,b,3)]
assert normalized==[(3,5),(5,3),(12,14),(14,12)]
for a in sorted(non):
    admissible=[b for b in range(p) if all((a*t**3+b*t+3)%p not in sq for t in H)]
    assert admissible==({3:[5],5:[3],12:[14],14:[12]}.get(a,[]))
    assert all(smooth(a,b,3) for b in admissible)
# All four normalized presentations are one orbit under x->u*x, u != 0.
a,b=5,3
orbit={(a*pow(u,12,p)%p,b*pow(u,4,p)%p) for u in range(1,p)}
assert orbit==set(normalized)
# Every non-square constant c has exactly four pointless (a,b) pairs.
from collections import Counter
assert Counter(c for a,b,c in pts)=={c:4 for c in non}
# The field contains a primitive fourth root of unity (4^2=-1).
assert pow(4,4,p)==1 and pow(4,2,p)==p-1
print('CYCLIC4_POINTLESS_F17_VERIFIED smooth=4096 pointless=32 normalized=4 diagonal_orbits=1')
