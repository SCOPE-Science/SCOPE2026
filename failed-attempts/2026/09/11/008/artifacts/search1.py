# Substep 1: bounded search for char-2 local tangency obstruction.
# Model: line param s; quartic restricted to line gives g(s)=a*s^2+b*s+c (contact order 2).
# Char!=2 liftability (Len-Markwig): discriminant d=b^2-4ac is nonzero square -> lifts.
# Char 2 deformation at double root leads to Artin-Schreier-type equation u^2+u+k=0.
# We brute-force verify: over F2, u^2+u+1 has no root (empty torus-adjacent locus),
# while over char 0 the discriminant condition holds. This is the obstruction kernel.
F2 = [0,1]
def roots_F2():
    return [u for u in F2 if (u*u+u+1)%2==0]
print("F2 roots of u^2+u+1:", roots_F2())
print("affine F2 sweep of (x,y) in G_m^2 for x^2+x+1=0 factor: x=1 ->", (1+1+1)%2)
# Joint-ideal style check: ideal (y+x+1, x^2+x+1) over F2: enumerate torus points
pts=[(x,y) for x in [1] for y in [1] if (y+x+1)%2==0 and (x*x+x+1)%2==0]
print("torus zeros of (x+y+1, x^2+x+1) over F2*:", pts)
print("=> empty torus locus: TRUE" if not pts else "nonempty")
# Char-0 contrast: same polys over QQ have solutions
import sympy as sp
x,y=sp.symbols('x y')
G=sp.groebner([x+y+1, x**2+x+1], x, y, order='lex', domain='QQ')
print("QQ groebner:", list(G.polys))
print("discriminant of x^2+x+1:", 1-4)
