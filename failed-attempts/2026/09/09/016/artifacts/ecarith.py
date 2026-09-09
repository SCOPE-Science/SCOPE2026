"""ecarith.py: exact Fraction arithmetic on E_d: y^2 = x^3 + A x^2 + B x, A=-738d, B=6561 d^2.
Point doubling/addition exact over Q (x-only + full). Torsion-exclusion: Mazur groups
containing Z/2xZ/2 have exponent | 24, so 24P != O certifies infinite order (rank>=1).
"""
from fractions import Fraction

def A_of(d):
    return -738*d

def B_of(d):
    return 6561*d*d

def y2_of(d, x):
    return x*(x-9*d)*(x-729*d)

def add_pts(d, P, Q):
    # P,Q: (x,y) Fractions or None (=O)
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P; x2, y2 = Q
    if x1 == x2:
        if y1 == -y2:
            return None
        if y1 == 0 and y2 == 0:
            return None
        # doubling
        A = Fraction(A_of(d)); B = Fraction(B_of(d))
        lam = (3*x1*x1 + 2*A*x1 + B) / (2*y1)
    else:
        lam = (y2-y1)/(x2-x1)
    A = Fraction(A_of(d))
    x3 = lam*lam - A - x1 - x2
    y3 = lam*(x1-x3) - y1
    return (x3, y3)

def mul_pt(d, P, n):
    R = None
    Q = P
    m = abs(n)
    while m:
        if m & 1:
            R = add_pts(d, R, Q)
        Q = add_pts(d, Q, Q)
        m >>= 1
    return R

def cert_nontorsion(d, x, y):
    P = (Fraction(x), Fraction(y))
    # verify on curve
    assert P[1]*P[1] == y2_of(d, P[0]), 'not on curve'
    for k in (2, 3, 4, 6, 8, 24):
        R = mul_pt(d, P, k)
        if R is None:
            return {'torsion_order_divides': k, 'infinite': False, 'killed_at': k}
    return {'infinite': True, 'killed_at': None}
