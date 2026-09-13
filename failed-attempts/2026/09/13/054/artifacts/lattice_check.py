"""Bounded lattice certificate for lane-1569 (C8 Fano NS model). Part 1 of 2.
Model: NS = Z f + Z d, Gram diag(2,-2) [f from degree-2 K3 summand, d = -delta].
Plucker g = 2f - d (q=6). Isotropic rays e = f - d (movable fiber class),
e2 = f + d (second isotropic ray). Flop-line functional from geometric inputs
g.C = 1 (Pluecker degree of pencil of lines through a point) and e.C = -1
(Mukai-flop sign flip of e'.C' = 1): with D=(x,y), D.C = x*(f.C)+y*(d.C),
solving gives (f.C, d.C) = (2, 3).
Verifies: Gram values, q(g)=6, q(e)=q(e2)=0, pairings g.e=2, g.e2=6,
e.C=-1 (NOT nef: the verified obstruction), e2.C=5 (flop wall does NOT
exclude e2: honest record of the remaining gap), primitivity classification
of isotropic vectors, and wall-ray position w0=(3,-2), q=10>0, strictly
between e and e2. No external dependencies.
"""
# Gram: (x1,y1).(x2,y2) = 2*x1*x2 - 2*y1*y2
def q(v):
    return 2*v[0]*v[0] - 2*v[1]*v[1]

def pair(v, w):
    return 2*v[0]*w[0] - 2*v[1]*w[1]

f = (1, 0)
d = (0, 1)
g = (2, -1)    # 2f - d
e = (1, -1)    # f - d
e2 = (1, 1)    # f + d
w0 = (3, -2)   # wall ray candidate

out = []
out.append("q(f)=%d (2), q(d)=%d (-2)" % (q(f), q(d)))
out.append("q(g)=%d (6)" % q(g))
out.append("q(e)=%d (0), q(e2)=%d (0)" % (q(e), q(e2)))
out.append("g.e=%d (2), g.e2=%d (6)" % (pair(g, e), pair(g, e2)))
out.append("q(w0)=%d (10, big)" % q(w0))
assert q(f) == 2 and q(d) == -2 and q(g) == 6
assert q(e) == 0 and q(e2) == 0
assert pair(g, e) == 2 and pair(g, e2) == 6 and q(w0) == 10

# Primitive isotropic classification over Q: 2x^2-2y^2=0 -> x=+-y.
bad = [(x, y) for x in range(-50, 51) for y in range(-50, 51)
       if (x, y) != (0, 0) and q((x, y)) == 0 and not (x == y or x == -y)]
out.append("non-diagonal isotropic |.|<=50: count=%d" % len(bad))
assert len(bad) == 0

# Curve functional from (f.C, d.C) = (2, 3): D.C = 2x + 3y.
def Dot(D):
    return 2*D[0] + 3*D[1]

out.append("g.C=%d (1), e.C=%d (-1: OBSTRUCTION, e not nef)" % (Dot(g), Dot(e)))
out.append("e2.C=%d (+5: flop wall does NOT exclude e2 -> GAP)" % Dot(e2))
out.append("w0.C=%d (0: wall ray)" % Dot(w0))
assert Dot(g) == 1 and Dot(e) == -1 and Dot(e2) == 5 and Dot(w0) == 0

# Position: w0 = a*e + b*e2 with a,b > 0 (strictly between) ?
# (3,-2) = a(1,-1)+b(1,1): a+b=3, -a+b=-2 -> a=5/2, b=1/2.
a = (3 + 2) / 2.0
b = (3 - 2) / 2.0
out.append("w0 = %.1f*e + %.1f*e2 (both>0: strictly between)" % (a, b))
assert a > 0 and b > 0
# g interior: g = c*e + d2*e2, c,d2>0? (2,-1)=c(1,-1)+d2(1,1): c+d2=2,-c+d2=-1 -> c=3/2,d2=1/2
c = (2 + 1) / 2.0
d2 = (2 - 1) / 2.0
out.append("g = %.1f*e + %.1f*e2 (ample interior)" % (c, d2))
assert c > 0 and d2 > 0
# det of NS
out.append("det(NS) = 2*(-2) = -4")
out.append("CERTIFICATE_OK")
print("\n".join(out))
