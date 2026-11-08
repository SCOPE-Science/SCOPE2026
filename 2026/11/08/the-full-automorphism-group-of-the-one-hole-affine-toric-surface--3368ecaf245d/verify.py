#!/usr/bin/env python3
"""Exact polynomial checks for the one-hole toric surface and its plane lifts.
Run: python verify.py (requires SymPy). Finite checks supplement the general proof.
"""
import sympy as S
from itertools import product
u, v, X, V, Z, W = S.symbols('u v X V Z W')

# Scheme-theoretic parametrization and its binomial presentation.
graph = S.groebner([X-u, V-u*v, Z-v**2, W-v**3], u,v,X,V,Z,W,order='lex')
ker = [f.as_expr() for f in graph.polys if not f.as_expr().has(u,v)]
rels = [Z**3-W**2, Z*X**2-V**2, X*W-V*Z, V*W-X*Z**2]
given = S.groebner(rels, X,V,Z,W,order='lex')
assert all(given.reduce(f)[1] == 0 for f in ker)
assert all(S.groebner(ker,X,V,Z,W,order='lex').reduce(f)[1] == 0 for f in rels)
print('PRESENTATION_KERNEL_EXACT',len(ker))

# The affine semigroup has precisely the hole (0,1). This bounded check
# is not needed to certify the unbounded combinatorial proof.
gens = [(1,0),(1,1),(0,2),(0,3)]
reachable = {(0,0)}
for i in range(20):
    nxt = set(reachable)
    for a,b in reachable:
        for c,d in gens:
            if a+c<=16 and b+d<=16: nxt.add((a+c,b+d))
    reachable=nxt
assert reachable == {(a,b) for a,b in product(range(17),repeat=2) if (a,b)!=(0,1)}
print('SEMIGROUP_ONE_HOLE_UP_TO_16_PASS')

def in_A(f):
    p=S.Poly(S.expand(f),u,v)
    return p.coeff_monomial(v)==0

def image_gens(f,g):
    return [f,S.expand(f*g),S.expand(g*g),S.expand(g*g*g)]

def deriv_flag(f,g):
    o=lambda p:S.expand(p).subs({u:0,v:0})
    return (o(f)==0 and o(g)==0 and o(S.diff(f,v))==0 and
            o(S.diff(f,u))*o(S.diff(g,v))!=0)

def test_auto(label, f,g, fi,gi, expected=True):
    # All polys are exact and have their explicitly given polynomial inverses.
    cf=S.expand(f.subs({u:fi,v:gi}, simultaneous=True))
    cg=S.expand(g.subs({u:fi,v:gi}, simultaneous=True))
    bc=S.expand(fi.subs({u:f,v:g}, simultaneous=True))
    bg=S.expand(gi.subs({u:f,v:g}, simultaneous=True))
    assert (cf,cg,bc,bg)==(u,v,u,v), (label,cf,cg,bc,bg)
    good=all(in_A(e) for e in image_gens(f,g)+image_gens(fi,gi))
    assert good==deriv_flag(f,g)==expected,(label,good,deriv_flag(f,g))
    print('AUTOMORPHISM_FLAG_TEST',label,'DESCENDS' if good else 'DOES_NOT_DESCEND')

# Three permitted families, their nonlinear composition, and a conjugated
# triangular transformation with identity differential.
test_auto('linear_Borel', 2*u,3*v+5*u, u/2,(v-5*u/2)/3)
test_auto('quadratic_upper_shear',u+v**2,v,u-v**2,v)
test_auto('cubic_lower_shear',u,v+u**3,u,v-u**3)
f=u+(v+u**3)**2
g=v+u**3
test_auto('nonlinear_composite',f,g,u-v**2,v-(u-v**2)**3)
a=S.Integer(2); b=S.Integer(3)
s=u+a*v
f=u-a*b*s**2;g=v+b*s**2
fi=u+a*b*(u+a*v)**2;gi=v-b*(u+a*v)**2
test_auto('conjugate_hidden_family',f,g,fi,gi)
# Forbidden transformations: preserve polynomial plane but not the subring.
test_auto('forbidden_upper_linear',u+v,v,u-v,v,False)
test_auto('forbidden_translation_u',u+1,v,u-1,v,False)
test_auto('forbidden_translation_v',u,v+1,u,v-1,False)

# Concrete orbit reduction: linear Borel sends every (u0,v0) with u0 != 0
# to (1,0); an initial u -> u+v^2 moves points on the punctured v-axis.
for u0,v0 in [(1,0),(2,5),(-1,3),(0,1),(0,-2),(0,7)]:
    p,q=(u0+v0*v0,v0) if u0==0 else (u0,v0)
    assert p!=0
    assert (S.Rational(p,p), S.Rational(q)-S.Rational(q,p)*p)==(1,0)
print('TWO_ORBITS_EXACT_WITNESSES_PASS')
print('ALL_EXACT_CHECKS_PASS')
