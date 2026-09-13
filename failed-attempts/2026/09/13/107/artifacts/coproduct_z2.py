"""Exact coproduct of z=x12 and z^2 in T(V)#kG (free algebra level).
Symbols: noncommuting x1,x2; abelian group gens g1,g2 with g_i x_j = qij x_j g_i.
Scope relation: q12*q21 = q^-1 where q=q11. Implement normal order: g's to middle.
Compute D(z) and D(z^2) - z^2 otimes 1 - g12^2 otimes z^2, print exact coefficients.
Uses generic symbols via substitution q21 = 1/(q*q12) to enforce scope constraint.
"""
import sympy as sp

q, q12 = sp.symbols('q q12')
q21 = 1/(q*q12)  # scope constraint q12*q21 = q^-1
q22 = sp.Integer(-1)

# Monomials represented as (coeff, xword tuple, g1exp, g2exp) tensored pairs.
# Represent tensor A otimes B with A,B each (xword, gexp).
from collections import defaultdict

def add(d, key, val):
    d[key] = sp.simplify(d.get(key, 0) + val)

def Dx1():
    # x1 ot 1 + g1 ot x1
    return {(('x1',), (0,0), (), (0,0)): 1,
            ((), (1,0), ('x1',), (0,0)): 1}

def Dx2():
    return {(('x2',), (0,0), (), (0,0)): 1,
            ((), (0,1), ('x2',), (0,0)): 1}

def mulT(A, B):
    """Multiply two tensor-distributions (dicts) in (T#kG) ot (T#kG).
    Rule: (a ot b)(c ot d): move group part of b past x-part of c picking braiding scalar.
    Each factor leg is (xword, gexp). Product leg: concat xwords with scalar from gexp acting.
    gexp (e1,e2) acts on xword: each x1 -> q11^e1 * q21^e2 ; each x2 -> q12^e1 * q22^e2."""
    def act(gexp, xw):
        s = 1
        for x in xw:
            if x == 'x1':
                s *= q**gexp[0] * q21**gexp[1]
            else:
                s *= q12**gexp[0] * q22**gexp[1]
        return sp.simplify(s)
    out = {}
    for ka, va in A.items():
        for kb, vb in B.items():
            la, ga, ra, ha = ka  # left leg (xword,gexp), right leg
            lb, gb, rb, hb = kb
            # (la ga ot ra ha)(lb gb ot rb hb)
            #   = la (ga.lb) ga gb ot ra (ha.rb) ha hb
            s = act(ga, lb) * act(ha, rb)
            key = (la + lb, (ga[0]+gb[0], ga[1]+gb[1]),
                   ra + rb, (ha[0]+hb[0], ha[1]+hb[1]))
            add(out, key, sp.simplify(va*vb*s))
    return out

def show(d, title):
    print(f"--- {title} ---")
    for k in sorted(d, key=str):
        print(f"  {sp.simplify(d[k])}  *  L={k[0]}g{k[1]}  |  R={k[2]}g{k[3]}")

x1 = {(('x1',), (0,0), (), (0,0)): 1}
x2 = {(('x2',), (0,0), (), (0,0)): 1}
g1 = {((), (1,0), (), (0,0)): 1}
g2 = {((), (0,1), (), (0,0)): 1}
one = {((), (0,0), (), (0,0)): 1}

Dx1d = Dx1(); Dx2d = Dx2()
# z = x1x2 - q12 x2x1 ; tensor versions
Z = {}
add(Z, (('x1','x2'), (0,0), (), (0,0)), 1)
add(Z, (('x2','x1'), (0,0), (), (0,0)), -q12)
Dz = {}
for k, v in mulT(Dx1d, Dx2d).items():
    add(Dz, k, v)
for k, v in mulT(Dx2d, Dx1d).items():
    add(Dz, k, sp.simplify(-q12*v))
show(Dz, "Delta(z)")
Dz2 = mulT(Dz, Dz)
show(Dz2, "Delta(z^2) raw")
# subtract z^2 ot 1 and g12^2 ot z^2
Z2 = mulT(Z, Z)
G122 = {((), (2,2), (), (0,0)): 1}
sub1 = mulT(Z2, one)
sub2 = mulT(G122, Z2)
R = dict(Dz2)
for k, v in sub1.items():
    add(R, k, -v)
for k, v in sub2.items():
    add(R, k, -v)
R = {k: sp.simplify(v) for k, v in R.items() if sp.simplify(v) != 0}
show(R, "Delta(z^2) - z^2 ot 1 - g12^2 ot z^2  [intermediate + correction terms]")
import json
with open("coproduct_z2.json", "w") as f:
    json.dump({str(k): str(sp.simplify(v)) for k, v in R.items()}, f, indent=2)
print("wrote coproduct_z2.json")
