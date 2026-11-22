"""Exact elementary checks for extremal ellipsoids of a 3D trigonometric-curve hull.
Run with: python verify.py. Python standard library only.
"""
from fractions import Fraction as F
import math

s = F(3,8)            # inner transverse semiaxis squared
c2 = F(3,4)           # inner vertical semiaxis squared
S = F(3,2)            # outer transverse semiaxis squared
C2 = F(3,1)           # outer vertical semiaxis squared
assert S == 4*s and C2 == 4*c2
# E_J implies, for each coordinate, upper estimates for x*x and y*y.
# For rational z, the exact slacks must equal (z +/- 1/2)^2.
for i in range(-200,201):
    z = F(i,200)
    lhs_x = 1+z-2*s*(1-z*z/c2)
    lhs_y = 1-z-2*s*(1-z*z/c2)
    assert lhs_x == (z+F(1,2))**2
    assert lhs_y == (z-F(1,2))**2

inner_contacts=[(F(1,2), F(0), -F(1,2)),(-F(1,2),F(0),-F(1,2)),(F(0),F(1,2),F(1,2)),(F(0),-F(1,2),F(1,2))]
outer_contacts=[(F(1),F(0),F(1)),(-F(1),F(0),F(1)),(F(0),F(1),-F(1)),(F(0),-F(1),-F(1))]

def contacts(cs, axis2):
    # Avoid radicals: normalized coordinates are (x/sqrt(ax2), y/sqrt(ay2), z/sqrt(az2)).
    # Each unnormalized covariance entry divided by axis scale verifies isotropy.
    for p in cs:
        assert sum(p[i]**2/axis2[i] for i in range(3)) == 1
    assert all(sum(p[i] for p in cs)==0 for i in range(3))
    for i in range(3):
        assert F(3,4)*sum(p[i]*p[i] for p in cs)==axis2[i]
        for j in range(i):
            assert sum(p[i]*p[j] for p in cs)==0
    for i in range(4):
        for j in range(i):
            dot=sum(cs[i][k]*cs[j][k]/axis2[k] for k in range(3))
            assert dot == -F(1,3)
contacts(inner_contacts,(s,s,c2))
contacts(outer_contacts,(S,S,C2))
for x,y,z in inner_contacts:
    assert 2*x*x-1 <= z <= 1-2*y*y
for x,y,z in outer_contacts:
    assert x*x+y*y==1 and z in (F(-1),F(1))
# Also check L's global curve containment and E_J's global cylinder containment.
for i in range(10001):
    t=2*math.pi*i/10000
    x,y,z=math.cos(t),math.sin(t),math.cos(2*t)
    assert x*x/S+y*y/S+z*z/C2 < 1+1e-12
    assert 2*x*x-1 <= z+1e-12 and z<=1-2*y*y+1e-12
# The exact integral over the unit disk yields vol(K) = pi; volumes:
# vol(E_J)=pi*sqrt(3)/4 and vol(E_L)=2*pi*sqrt(3).
assert F(4,3)*s == F(1,2)
assert F(4,3)*S == F(2)
assert (S/s)*(math.sqrt(C2/c2)) == 8
print('PASS: 802 rational slack identities, two four-point isotropic certificates,')
print('      exact ellipsoid scale and volume identities, 10001 curve samples.')
print('Analytic containment and optimality follow from the documented proof, not sampling.')
