"""indep.py: rigorous rank>=2 certificate via E(Q)/2E(Q) Kummer images.
delta(P) = (sqf(x), sqf(x-9d)) in Q*/Q*2 x Q*/Q*2. If <delta(P),delta(Q),torsions>
has 16 distinct elements => dim E(Q)/2 >= 4 => rank >= 2 (full 2-torsion => dim = r+2).
Torsion images: O=(1,1); T1=(0,0)->(-9d,-729d); T2=(9d,0)->(9d,-720d); T3=(729d,0)->(729d,720d).
All products componentwise mod squares (sqf kernel). Exact integer arithmetic.
"""
import sys, math
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-310/output/artifacts')
from fractions import Fraction
import sympy as sp
from ecarith import add_pts, y2_of

def sqf(n):
    # squarefree kernel of Fraction n (mod Q*2), as (sign, int); sound: n1*n2^-1 square <=> same key
    if n == 0:
        return None
    f = Fraction(n)
    num, den = abs(f.numerator), abs(f.denominator)
    k = num*den
    fa = sp.factorint(k)
    ker = 1
    for p, e in fa.items():
        if e % 2 == 1:
            ker *= p
    return (-1 if f < 0 else 1, ker)

def sqfmul(a, b):
    if a is None or b is None:
        return None
    s = a[0]*b[0]
    g = a[1]*b[1]
    # reduce mod squares
    fa = sp.factorint(g)
    k = 1
    for p, e in fa.items():
        if e % 2 == 1:
            k *= p
    return (s, k)

def delta(d, P):
    x = P[0]
    return (sqf(x), sqf(x - 9*d))

def tors_images(d):
    # b-map (Cassels replacement): delta(O)=(1,1); delta((0,0))=(1,-9d)... verify: use limit rule
    # (0,0)->(e2*e3 mod sq, e1-e2)=(1*? ) — safer: images of T1,T2,T3 generate the 4-elem torsion subgroup;
    # derive T2=(9d,0)->(9d, 9d-729d=-720d); T3=(729d,0)->(729d,729d-9d=720d); T1=(0,0)->(1,-9d) is the
    # standard limit (x->0 with x(x-9d)(x-729d) square => class (1,-9d)); check T1*T2=T3 in the quotient.
    t1 = ((1, 1), sqf(-9*d))
    t2 = (sqf(9*d), sqf(-720*d))
    t3 = (sqf(729*d), sqf(720*d))
    return [(((1, 1)), ((1, 1))), t1, t2, t3]

def cert_rank2(d, P, Q):
    # returns (ok, detail)
    assert P[1]*P[1] == y2_of(d, P[0]) and Q[1]*Q[1] == y2_of(d, Q[0])
    t = tors_images(d)
    dp, dq = delta(d, P), delta(d, Q)
    seen = set()
    for i in (0, 1):
        for j in (0, 1):
            for tk in t:
                e1 = sqfmul(sqfmul(dp[0] if i else ((1,1)), dq[0] if j else ((1,1))), tk[0])
                e2 = sqfmul(sqfmul(dp[1] if i else ((1,1)), dq[1] if j else ((1,1))), tk[1])
                seen.add((e1[0], e1[1], e2[0], e2[1]))
    return (len(seen) == 16, {'dp': str(dp), 'dq': str(dq), 'n': len(seen)})
