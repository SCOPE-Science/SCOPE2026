"""Exact rational diagnostics for a symmetric three-site anisotropic Voronoi theorem.

Run with `python3 verify.py`; Python standard library only.
Coordinates (X,Y) correspond to Euclidean point (X, sqrt(3)*Y).
Tests supplement the analytic proof and do not establish continuum topology.
"""
from fractions import Fraction as F


def costs(k, X, Y):
    t = (X, (-X + 3*Y)/2, (-X - 3*Y)/2)
    r2 = X*X + 3*Y*Y
    return tuple(r2 + k + (k-1)*u*u - 2*k*u for u in t)


def components(k, X, Y):
    if k == 1:
        return (X >= abs(Y),)
    if k < 1:
        c = 2*k/(1-k)
        return (X >= abs(Y) and -X + 3*abs(Y) <= 2*c,
                X + 3*abs(Y) <= -2*c)
    c = 2*k/(k-1)
    return (X >= abs(Y) and X + 3*abs(Y) <= 2*c,
            Y >= abs(X) and X + 3*Y >= 2*c,
            Y <= -abs(X) and X - 3*Y >= 2*c)


def actual_cell(k, X, Y):
    q = costs(k, X, Y)
    return q[0] <= q[1] and q[0] <= q[2]


def triple(k, X, Y):
    q = costs(k, X, Y)
    return q[0] == q[1] == q[2]


def check():
    n = 0
    for k in map(F, ('1/10','1/4','1/2','3/4','9/10','1','11/10','5/4','3/2','2','4','8')):
        for a in range(-42, 43):
            for b in range(-42, 43):
                X, Y = F(a, 4), F(b, 4)
                blocks = components(k, X, Y)
                assert actual_cell(k, X, Y) == any(blocks), (k,X,Y,blocks)
                n += 1
        if k != 1:
            c = 2*k/abs(k-1)
            # Origin and three rotated outer locations are triple sites.
            sgn = -1 if k < 1 else 1
            for X, Y in ((F(0),F(0)), (sgn*2*c,F(0)), (-sgn*c,sgn*c), (-sgn*c,-sgn*c)):
                assert triple(k,X,Y)
                n += 1
            if k < 1:
                assert components(k,F(0),F(0)) == (True,False)
                assert components(k,-2*c,F(0)) == (False,True)
                n += 2
            else:
                for X,Y in ((c/2,c/2),(c/2,-c/2)):
                    assert components(k,X,Y).count(True) == 2
                    n += 1
                assert components(k,2*c,F(0)) == (True,False,False)
                n += 1
                # Shoelace area in (X,Y): multiply by sqrt(3) in Euclidean coordinates.
                corners=((F(0),F(0)),(c/2,c/2),(2*c,F(0)),(c/2,-c/2))
                area2=sum(corners[i][0]*corners[(i+1)%4][1]
                         - corners[(i+1)%4][0]*corners[i][1]
                         for i in range(4))
                assert abs(area2)/2 == c*c
                n += 1
    return n

if __name__ == '__main__':
    print('EQUILATERAL_ANISOTROPIC_EXACT_CHECKS_OK', check())
