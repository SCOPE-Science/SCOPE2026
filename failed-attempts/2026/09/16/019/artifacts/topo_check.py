"""Adjunction check for CY3 complete intersections in weighted projective stacks.
c(TX) = prod_i(1+w_i H)/prod_j(1+b_j H); int_X H^3 = prod(b)/prod(w).
Cross-checked against quintic (chi=-200)."""
from fractions import Fraction
import sympy as sp
H=sp.Symbol('H')
def invariants(weights, degs):
    prod_w=1
    for w in weights: prod_w*=w
    prod_b=1
    for b in degs: prod_b*=b
    cP=1
    for w in weights: cP*=(1+w*H)
    denom=1
    for b in degs: denom*=(1+b*H)
    s=sp.expand(sp.series(cP/denom, H, 0, 5).removeO())
    c2=s.coeff(H,2); c3=s.coeff(H,3)
    intH3=Fraction(prod_b,prod_w)
    chi=c3*prod_b/prod_w
    intc2H=c2*prod_b/prod_w
    return {"c2":int(c2),"c3":int(c3),"intH3":str(intH3),"chi":str(chi),"intc2H":str(intc2H)}
for name,w,b in [("X7",[1,1,1,1,3],[7]),("X17",[2,2,3,3,7],[17]),("quintic",[1,1,1,1,1],[5])]:
    print(name, invariants(w,b))
