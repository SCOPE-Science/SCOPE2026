"""Standalone checks for diameter-disk intersections of equiangular pentagons.

Run: python check_side_disks.py
Requires sympy for the exact radical identities; random checks use the standard library.
"""
from math import cos, sin, pi, hypot, sqrt
import random
import sympy as sp

w = sp.sqrt(5)
q = (w-1)/4
r = -(w+1)/4
delta = (1-q)/2

# The four-constraint separator uses the horizontal closure identity.
a = [0]*5
for j, z in enumerate((1, 2, 2, 1)):
    a[j] -= z*delta
    a[(j+1)%5] += z
    a[(j+2)%5] -= z*delta
for actual, expected in zip(
    [sp.simplify(a[i]+[1,q,r,r,q][i]) for i in range(5)],
    [q,2*q,q/2,q/2,2*q]
):
    assert sp.simplify(actual-expected) == 0

# An explicit proper, strictly convex equiangular pentagon attains eight edges.
t = sp.Rational(1,100)
b = sp.simplify((t+2*q)/(1+2*q))
l = [t, sp.Integer(1), b, b, sp.Integer(1)]
assert sp.simplify(l[0]+q*(l[1]+l[4])+r*(l[2]+l[3])) == 0
H = []
for j in range(5):
    i, k, m = j, (j+2)%5, (j+1)%5
    z = sp.simplify(l[m]**2 + q*l[m]*(l[i]+l[k]) + (r-1)*l[i]*l[k]/2)
    H.append(z)
assert sp.simplify(H[1]-(-sp.Rational(17449,20000)+3*w/8)) == 0
assert H[1] == H[2]
assert H[4] == -sp.Rational(6299,10000)-3*w/25
assert H[0] == H[3]
assert H[0] > 0 and H[4] < 0
assert 45*20000**2 < 64*17449**2, 'Exact square test for H[1] < 0'
assert float(H[1]) < 0
assert [float(v)<0 for v in H] == [False,True,True,False,True]

# Exact integer example of a general convex pentagon with nine graph edges.
P = [(-997,-99),(689,-897),(227,240),(55,381),(-10,414)]
for i in range(5):
    a0, a1, a2 = P[i], P[(i+1)%5], P[(i+2)%5]
    cross = (a1[0]-a0[0])*(a2[1]-a1[1])-(a1[1]-a0[1])*(a2[0]-a1[0])
    assert cross > 0
edge_sq = []
for i in range(5):
    v, z = P[i], P[(i+1)%5]
    edge_sq.append((v[0]-z[0])**2+(v[1]-z[1])**2)

def are_disks_intersecting(i,j):
    # Centers have midpoint coordinates; multiplied-by-two center distance squared is Q.
    M_i = (P[i][0]+P[(i+1)%5][0],P[i][1]+P[(i+1)%5][1])
    M_j = (P[j][0]+P[(j+1)%5][0],P[j][1]+P[(j+1)%5][1])
    Q = (M_i[0]-M_j[0])**2+(M_i[1]-M_j[1])**2
    x, y = edge_sq[i],edge_sq[j]
    # Equivalence: sqrt(x)+sqrt(y) >= sqrt(Q).
    if Q<=x+y:return True
    return 4*x*y >= (Q-x-y)**2

extras = [(i,j) for i in range(5) for j in range(i+2,5) if (i,j)!=(0,4) and are_disks_intersecting(i,j)]
assert extras == [(0,2),(0,3),(1,4),(2,4)], extras

# Numerical stress check of the quantitative two-separated-pairs assertion.
rng = random.Random(20261114)
for z in range(5000):
    a, c = rng.uniform(-.9,.9), rng.uniform(-.9,.9)
    ell = [1+a*cos(4*pi*j/5)+c*sin(4*pi*j/5) for j in range(5)]
    if min(ell) <= 0:continue
    pts=[(0.0,0.0)]
    for j in range(4):
        pts.append((pts[-1][0]+ell[j]*cos(2*pi*j/5),pts[-1][1]+ell[j]*sin(2*pi*j/5)))
    mids=[((pts[j][0]+pts[(j+1)%5][0])/2,(pts[j][1]+pts[(j+1)%5][1])/2) for j in range(5)]
    gaps=[hypot(mids[j][0]-mids[(j+2)%5][0],mids[j][1]-mids[(j+2)%5][1])-(ell[j]+ell[(j+2)%5])/2 for j in range(5)]
    threshold=float(q)*sum(ell)/12
    assert sum(g>=threshold-1e-10 for g in gaps)>=2
print('EQUIANGULAR_PENTAGON_DISK_CHECKS_OK')
