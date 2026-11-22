#!/usr/bin/env python3
"""Exact rational certificate for the generic singularity basket of the Malara octic net.

Requires Python 3.10+ and SymPy 1.12+. No numerical approximations are used.
A smooth strict transform at one specialization combines with the published
geometrically integral specialization by openness over the irreducible
parameter bundle; the assertions below certify the former specialization.
"""
import sympy as S

x, y, z, u, v = S.symbols('x y z u v')
VARS = (x, y, z)
POINTS = [(1,0,0),(-1,1,0),(0,1,0),(1,1,0),(-1,-1,1),
          (1,-1,1),(-1,1,1),(1,1,1),(0,-1,1),(-1,0,1),
          (0,0,1),(1,0,1),(0,1,1)]
MULTS = [3 if i in (0,2,10) else 1 for i in range(13)]
Q = (2, 5, 1)
MONOMIALS = [x**a*y**b*z**(8-a-b) for a in range(9) for b in range(9-a)]

def multiindices(m):
    return [(a,b,c) for a in range(m) for b in range(m-a) for c in range(m-a-b)]

def vanishing_matrix():
    rows = []
    for P, mult in zip(POINTS + [Q], MULTS + [5]):
        for a,b,c in multiindices(mult):
            rows.append([S.diff(M, x,a,y,b,z,c).subs(dict(zip(VARS,P)))
                         for M in MONOMIALS])
    return S.Matrix(rows)

# Integral specialization in the three-dimensional octic linear system at Q.
F = (
 11028*x**5*y**3 + 9190*x**5*y**2*z + 91900*x**5*y*z**2 -5493750*x**5*z**3
 -230356*x**4*y**3*z + 708960*x**4*y**2*z**2 + 9066100*x**4*y*z**3
 -11028*x**3*y**5 + 206150*x**3*y**4*z + 9632*x**3*y**3*z**2
 -10635820*x**3*y**2*z**3 + 5555300*x**3*y*z**4 + 5493750*x**3*z**5
 +46444*x**2*y**5*z -934640*x**2*y**4*z**2 +6265512*x**2*y**3*z**3
 +225680*x**2*y**2*z**4 -15147700*x**2*y*z**5
 -45952*x*y**5*z**2 +517280*x*y**4*z**3 -5610880*x*y**3*z**4
 +9903200*x*y**2*z**5 +36544*y**5*z**3 -36544*y**3*z**5
)
M = vanishing_matrix()
assert M.shape == (75,45)
assert M.rank() == 42
assert S.Poly(F,x,y,z).total_degree() == 8
coeffs = S.Matrix([S.Poly(F,x,y,z).coeff_monomial(MO) for MO in MONOMIALS])
assert M*coeffs == S.zeros(75,1)

# Each prescribed singularity is ordinary: its first nonzero homogeneous
# tangent form has distinct complex projective roots.
for name, subs, m in [
    ('P1',{x:1,y:u,z:v},3), ('P3',{x:u,y:1,z:v},3),
    ('P11',{x:u,y:v,z:1},3), ('Q',{x:2+u,y:5+v,z:1},5)]:
    E=S.Poly(S.expand(F.subs(subs)),u,v)
    order=min(a+b for (a,b),val in E.terms() if val)
    assert order == m, (name,order)
    tangent=S.expand(sum(val*u**a*v**b for (a,b),val in E.terms() if a+b==m))
    assert S.degree(tangent.subs(v,1),u) == m
    discriminant=S.discriminant(tangent.subs(v,1),u)
    assert discriminant != 0, name
    print(name,'multiplicity',order,'tangent discriminant',discriminant)

# The resultant triple detects all possible affine singular x-coordinates.
f = S.expand(F.subs(z,1)); fx=S.diff(f,x); fy=S.diff(f,y)
resultants=[S.resultant(g,h,y) for g,h in [(f,fx),(f,fy),(fx,fy)]]
assert [S.degree(R,x) for R in resultants] == [38,41,37]
projected=S.Poly(S.gcd_list(resultants),x).monic().as_expr()
assert S.expand(projected-x**4*(x-2)**16)==0
for abscissa, ordinate, multiplicity in [(0,0,2),(2,5,4)]:
    gp=S.Poly(S.gcd_list([T.subs(x,abscissa) for T in (f,fx,fy)]),y).monic().as_expr()
    assert S.expand(gp-(y-ordinate)**multiplicity)==0, (abscissa,gp)
# At infinity all roots are either P1, P3 or simple intersections.
assert S.expand(F.subs(z,0)-11028*x**3*y**3*(x-y)*(x+y))==0
print('PASS: interpolation rank 42; affine singularities exactly (0,0), (2,5); infinity only P1,P3; ordinary (3,3,3,5).')
print('delta=3*3+10=19; arithmetic genus 21; geometric genus 2 for an integral generic member.')
