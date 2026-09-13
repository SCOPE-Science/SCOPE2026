"""Exact setup: multilinearized relations M(p)q=0, E=V(det M), t=sigma(O)=(a:b:c)."""
import sympy as sp
a,b,c,x,y,z = sp.symbols('a b c x y z')
M = sp.Matrix([[c*x, b*z, a*y],[a*z, c*y, b*x],[b*y, a*x, c*z]])
detM = sp.factor(M.det())
print("det M =", detM)
E = a*b*c*(x**3+y**3+z**3)-(a**3+b**3+c**3)*x*y*z
print("detM - k*E balanced:", sp.expand(detM - 0) )
# check detM equals scalar multiple of E form: collect
print("detM/E check at (1,2,3) point on (7,11,13):", detM.subs({a:7,b:11,c:13,x:1,y:2,z:3}), E.subs({a:7,b:11,c:13,x:1,y:2,z:3}))
MO = M.subs({x:1,y:-1,z:0})
print("M(O) =", MO.tolist(), " rank:", MO.rank())
print("ker M(O):", MO.nullspace())
print("O on E:", sp.expand(E.subs({x:1,y:-1,z:0})))
print("t=(a:b:c) on E:", sp.expand(E.subs({x:a,y:b,z:c})))
