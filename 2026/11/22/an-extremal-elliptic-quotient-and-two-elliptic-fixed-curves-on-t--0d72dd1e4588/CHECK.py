"""Independent exact symbolic checks for a quartic K3 involution quotient.
Run: python CHECK.py (requires sympy). Theoretical conclusions rely on the proof.
"""
import sympy as S

t=S.symbols('t', nonzero=True)
v,q=S.symbols('v q')
F=t*(t*t+1)
U=t+1/t
Ftau=S.factor((1/t)*((1/t)**2+1))
assert S.simplify(Ftau-F/t**4)==0
# The quartic's s-invariant affine equation F q^2+v^3+v=0.
# X=F v, Y=i F^2 q. The cubic identity reduces to zero on that surface.
X=F*v; Y=S.I*F**2*q
lhs=S.expand(Y**2-X**3-F**2*X)
assert S.simplify(lhs+F**3*(F*q*q+v**3+v))==0
# Swap sends t -> 1/t, v -> v, q -> t^2 q.
Xt=Ftau*v; Yt=S.I*Ftau**2*t*t*q
assert S.simplify(Xt-X/t**4)==0
assert S.simplify(Yt-Y/t**6)==0
# On quotient: xi=X/t^2, eta=Y/t^3, u=t+1/t.
xi=X/t**2; eta=Y/t**3
assert S.simplify(F/t**2-U)==0
assert S.simplify((eta**2-xi**3-U**2*xi)-lhs/t**6)==0
assert S.simplify(F-t*(t-S.I)*(t+S.I))==0
assert all(F.subs(t,a)!=0 for a in [1,-1])
assert S.factor(U**2-4)==(t-1)**2*(t+1)**2/t**2
# Orders of the elliptic discriminants Delta=-64 F^6 and -64 u^6.
assert S.factor(-64*F**6) == -64*t**6*(t**2+1)**6
z=S.symbols('z')
# At t=infinity, f is a section of O(4), with local representing f_inf=z^4 f(1/z).
assert S.factor(z**4*F.subs(t,1/z)) == z*(z*z+1)
# At u=infinity, u is a section of O(2), local representing u_inf=z^2(1/z)=z.
assert S.factor(z**2*(1/z))==z
# Four distinct branch points in elliptic generic fiber E[2] over C(u): xi=0, +/-i*u.
xi2,u=S.symbols('xi2 u')
assert S.simplify(xi2**3+u*u*xi2-xi2*(xi2-S.I*u)*(xi2+S.I*u))==0
print('PASS: invariant function field, involution action, base quotient, discriminant fibers, branch points, rational 2-torsion')
