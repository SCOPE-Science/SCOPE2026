"""Exact barycenter of anticanonical polytope of Bl_1 P^2.

Triangle T = conv{(-1,-1),(-1,2),(2,-1)} (P^2, anticanonical),
S = conv{(-1,-1),(-1,0),(0,-1)} (excised corner),
Q = T \\ S (quadrilateral, Bl_1 P^2).
Uses exact Fraction arithmetic and the triangle-centroid rule.
"""
from fractions import Fraction as F

def tri_area(p1, p2, p3):
    (x1, y1), (x2, y2), (x3, y3) = p1, p2, p3
    return abs(F(x1)*(F(y2) - F(y3)) + F(x2)*(F(y3) - F(y1)) + F(x3)*(F(y1) - F(y2))) / F(2)

def tri_centroid(p1, p2, p3):
    return (F(p1[0] + p2[0] + p3[0]) / F(3), F(p1[1] + p2[1] + p3[1]) / F(3))

T = [(-1, -1), (-1, 2), (2, -1)]
S = [(-1, -1), (-1, 0), (0, -1)]
AT = tri_area(*T)
AS = tri_area(*S)
AQ = AT - AS
cT = tri_centroid(*T)
cS = tri_centroid(*S)
# centroid(Q) = (AT*cT - AS*cS)/AQ
cx = (AT * cT[0] - AS * cS[0]) / AQ
cy = (AT * cT[1] - AS * cS[1]) / AQ
print("Area T:", AT, "centroid T:", cT)
print("Area S:", AS, "centroid S:", cS)
print("Area Q:", AQ, "centroid Q:", (cx, cy))
assert AT == F(9, 2) and AS == F(1, 2) and AQ == F(4, 1)
assert (cx, cy) == (F(1, 12), F(1, 12))
print("OK: barycenter(Q) = (1/12, 1/12) != (0,0)")
