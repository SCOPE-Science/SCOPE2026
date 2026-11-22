"""Exact local-equilibrium checks for a refuge-induced Beddington-DeAngelis predator-prey system.
Public reproducibility code: only equations and mathematical tests, no provenance claims.
"""
import sympy as s
X,q,a,alpha,beta,delta,K,mu,h=s.symbols('X q a alpha beta delta K mu h', positive=True)
y=q/beta
D=1+delta*X+q
U=(1+q*q)/(1+q)**2
g=alpha*(1-X*U/K)-a*q/(beta*D)
f=-mu+h*X/D
T=mu/(h-mu*delta)
rho=T/K
eta=a*mu/(alpha*beta*h*T)
F=1-rho+(1-eta)*q-rho*q**2
# On the predator equilibrium nullcline, X=T(1+q).
g_on=s.factor(g.subs(X,T*(1+q)))
assert s.simplify((1+q)*g_on/alpha-F)==0
# General determinant identity on the predator nullcline and at a coexistence root.
gX=s.diff(g,X); gq=s.diff(g,q)
fX=s.diff(f,X); fq=s.diff(f,q)
Jdet=X*y*beta*(gX*fq-gq*fX)
root_sub={X:T*(1+q)}
assert s.simplify(f.subs(root_sub))==0
# Verify the determinant identity by differentiating the predator nullcline.
assert s.simplify((gX*fq-gq*fX+fX*s.diff(g_on,q)).subs(root_sub))==0
assert s.simplify(g_on-alpha*F/(1+q))==0
# Exact rational parameters: h=2, mu=delta=alpha=beta=1, a=1/5, K=10/11.
vals={alpha:s.S(1),K:s.Rational(10,11),beta:s.S(1),delta:s.S(1),a:s.Rational(1,5),mu:s.S(1),h:s.S(2)}
assert s.simplify(T.subs(vals)-1)==0
assert s.simplify(rho.subs(vals)-s.Rational(11,10))==0
assert s.simplify(eta.subs(vals)-s.Rational(1,10))==0
poly=s.factor(F.subs(vals))
assert s.simplify(poly-(-1+9*q-11*q*q)/10)==0
roots=sorted(s.solve(poly,q),key=lambda r: float(r))
assert roots==[(s.S(9)-s.sqrt(37))/22,(s.S(9)+s.sqrt(37))/22]
# Strict rational isolators and derivative sign.
for j,(lo,hi) in enumerate([(s.Rational(1,10),s.Rational(1,5)),(s.Rational(3,5),s.Rational(4,5))]):
 assert (lo<roots[j]<hi)
assert s.diff(poly,q).subs(q,roots[0])>0
assert s.diff(poly,q).subs(q,roots[1])<0
# Direct linearization of the actual original ODE (not a reduced surrogate).
yvar=s.symbols('y',positive=True)
direct_q=beta*yvar
D2=1+delta*X+direct_q
ODE=s.Matrix([X*(alpha*(1-X*(1+direct_q**2)/(K*(1+direct_q)**2))-a*yvar/D2), yvar*(-mu+h*X/D2)])
Jac=ODE.jacobian((X,yvar))
for j,rt in enumerate(roots):
 JJ=s.simplify(Jac.subs(vals).subs({X:1+rt,yvar:rt}))
 det=s.simplify(JJ.det()); tr=s.simplify(s.trace(JJ))
 assert det<0 if j==0 else det>0
 if j==1:assert tr<0
 assert ODE.subs(vals).subs({X:1+rt,yvar:rt}).applyfunc(s.simplify)==s.zeros(2,1)
 print('coexistence',j,'q=',rt,'q_numeric=',float(rt),'det=',float(det),'trace=',float(tr))
BB=s.simplify(Jac.subs(vals).subs({X:s.Rational(10,11),yvar:0}))
assert s.simplify(BB.eigenvals()[s.S(-1)])==1
assert s.trace(BB)<0 and BB.det()>0
print('boundary_eigenvalues',BB.eigenvals())
print('checked: nullcline reduction, exact witnesses, vector field equilibrium, Jacobians and stability')
