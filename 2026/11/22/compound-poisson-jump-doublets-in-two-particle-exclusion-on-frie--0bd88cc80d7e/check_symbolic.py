"""Independent symbolic quotient and cumulant checks for two-excitation exclusion."""
import sympy as sp
m,z,lam=sp.symbols('m z lam',integer=True,positive=True)
y=sp.symbols('y')
T=sp.Matrix([[1,1,2*m-2],[2,0,0],[2,0,2]])
r=sp.Matrix([2*m,2,4]);L=y*T-sp.diag(*r)
P=sp.expand((lam*sp.eye(3)-L).det())
# Implicit differentiation P(lambda(z), exp(z))=0 at z=0 lambda=0
D=lambda expr: sp.simplify(expr.subs({lam:0,y:1}))
P_l=D(sp.diff(P,lam));P_y=D(sp.diff(P,y))
mu=sp.factor(-P_y/P_l)
var=sp.factor(-(D(sp.diff(P,lam,lam))*mu**2+2*D(sp.diff(P,lam,y))*mu+D(sp.diff(P,y,y))+D(sp.diff(P,y)))/P_l)
F=sp.factor(var/mu)
wantmu=6*(2*m-1)/(2*m+1)
wantF=(40*m**3-52*m**2+110*m-71)/(3*(2*m-1)*(2*m+1)**2)
assert sp.simplify(mu-wantmu)==0
assert sp.simplify(F-wantF)==0
assert sp.simplify(P.subs(y,1)-lam*(lam+2)*(lam+2*m+1))==0
assert sp.simplify(F-1-4*(m-1)*(4*m**2-12*m+17)/(3*(2*m-1)*(2*m+1)**2))==0
assert sp.simplify(F.subs(m,m+1)-F-4*(2*m-3)*(12*m**2-4*m-17)/((2*m-1)*(2*m+1)**2*(2*m+3)**2))==0
assert sp.limit(F,m,sp.oo)==sp.Rational(5,3)
# limiting principal eigenvalue via Schur-complement and asymptotic count mgf
Pscaled=sp.expand(P/(2*m))
limitpoly=sp.limit(Pscaled,m,sp.oo)
expect=(lam+2)*(lam+4-2*y-2*y**2)
assert sp.simplify(limitpoly-expect)==0
print('PASS symbolic all-m quotient determinant, first two cumulants, positive F-1, monotonicity, and limit')
print('mean=',mu,'F=',F,'limiting_SCgf=',2*(y-1)+2*(y**2-1))
