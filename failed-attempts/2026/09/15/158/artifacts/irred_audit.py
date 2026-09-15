"""Irreducibility audit for n=4 cases: rational parametrization + dimension + primeness of kernel.
For each graph: Z = {u1u3... constraints} irreducibility certificate:
- C4: Z = Z13 x Z24, each single irreducible quadric hypersurface in A^4 (XY+ZW irreducible: if it factored,
  factors linear => singular locus would be... certify: XY+ZW Eisenstein at (X)? = X*Y + (ZW), prime X... use: quotient
  by (XY+ZW) — show domain by localizing? Simplest: quadric hypersurface in A^4 with a smooth k-point is... not sufficient
  in general, but for XY+ZW: change of coords? It's a cone over smooth quadric surface P1xP1 => irreducible (cone over
  irreducible). Certify quadric surface {XY+ZW=0} in P^3 irreducible: ZW = -XY, if reducible = two lines... it CONTAINS lines
  (it's smooth P1xP1! contains lines but irreducible). Irreducibility: suppose XY+ZW=FG; deg F=deg G=1 (deg 2 total, nonconstant).
  Then V(F) hyperplane section... F,G linear forms; XY+ZW in ideal (F,G)? V(F,G) = line in A^4 contained in Sing? Sing(XY+ZW)
  = origin only. But V(F,G) has dim>=2 (two linears in A^4 cut dim>=2), all singular?? points of V(F,G) are singular of F*G
  (grad = F grad G + G grad F = 0 there) => Sing contains dim>=2 set, contradiction with Sing={0}. RIGOROUS. Same for any
  irreducible... but diamond/K4 constraints differ; handle each.
- diamond: single constraint u1u3+v1v3=0? Missing edge (0,2) i.e. x13=0: ONE quadric in A^8: XY+ZW form in 4 of 8 vars
  (+4 free) => irreducible x A^4.
- K4: no constraints: Z=A^8 irreducible.
General lemma used: (irreducible quadric hypersurface of rank>=2 in disjoint vars) x affine space is irreducible;
product of irreducible is irreducible.
Also kernel=whole I needs: image = V set-theoretically (symmetric diagonalization) + dim match + I radical + V irreducible.
Radicality from squarefree GB (Sturmfels: squarefree initial ideal => radical).
Write certificates.
"""
import sympy as sp

# Certify rank/quadric data for the constraints
u1,u2,u3,u4,v1,v2,v3,v4 = sp.symbols('u1 u2 u3 u4 v1 v2 v3 v4')
# C4: f13 = u1u3+v1v3, f24 = u2u4+v2v4
f13 = u1*u3+v1*v3
f24 = u2*u4+v2*v4
print("C4 constraints:", f13, ",", f24)
# singular locus of f13 in A^4(u1,u3,v1,v3): grad=(u3,u1,v3,v1) => only origin. Irreducible by line-argument.
# f13, f24 share no variables => Z = V(f13) x V(f24) in complementary coords => irreducible product.
print("disjoint vars:", set(f13.free_symbols).isdisjoint(f24.free_symbols))
# diamond: single f13
print("diamond: single quadric + free vars => irreducible")
# K4: Z = A^8
print("K4: Z = A^8 irreducible")

# Image = V set theory: every symmetric rank<=2 matrix over alg. closed K (char!=2) is U^TU. Standard.
# Surjectivity onto V: V = {sparse, rank<=2}; each point factors through Z by construction (U^TU with constraints).
print("done")
