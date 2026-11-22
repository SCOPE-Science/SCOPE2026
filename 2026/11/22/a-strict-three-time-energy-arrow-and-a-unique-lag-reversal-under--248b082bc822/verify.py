"""Exact polynomial-semigroup checks for the stationary common-reset energy triple.
Requires Python 3 and SymPy. Run: python verify.py
"""
import math
import sympy as sp

z, rho, ell, x = sp.symbols('z rho ell x', positive=True)
A = 1 + rho*(1-z)
B = 2 + rho*(1-z**2)
C = 3 + rho*(1-z**3)
Delta = sp.factor(B-A)
M1 = 1/A
M2 = 2/(A*B)
M3 = 6/(A*B*C)
V = sp.factor(M2-M1**2)
K = sp.factor(M3-3*M1*M2+2*M1**3)
H = sp.factor(2/Delta-2*M1)
T = sp.factor(H*V-K)

def iszero(expr):
    assert sp.cancel(expr) == 0, sp.factor(expr)

iszero(V-rho*(1-z)**2/(A**2*B))
iszero(K-2*rho*(1-z)**3*(rho*(1-z*z)-1)/(A**3*B*C))
iszero(H-2*rho*(1-z)**2/(A*Delta))
iszero(T-2*rho*(1-z)**3/(A*B*Delta*C))
# Test the polynomial Markov semigroup independently: L x^j = j*x^(j-1)-[j+rho(1-z^j)] x^j.
E1 = M1 + (x-M1)*sp.Symbol('u')  # u := exp(-A*s)
u, v = sp.symbols('u v', positive=True) # v := exp(-B*s)
E1 = M1 + (x-M1)*u
E2 = M2 + (2/Delta)*(x-M1)*u + (x*x-M2-(2/Delta)*(x-M1))*v
G = lambda f: sp.expand(f.diff(x)*(1-x) + rho*(f.subs(x,z*x)-f))
iszero(G(x) + A*x-1)
iszero(G(x*x) + B*x*x-2*x)
# Check semigroup initial values, and coefficients with d/ds u=-Au, d/ds v=-Bv.
iszero(E2.subs({u:1,v:1})-x*x)
iszero((-A*u*sp.diff(E2,u)-B*v*sp.diff(E2,v))-G(E2))

# Stationary expectation on all polynomials up to degree three.
def stat_avg(poly):
    poly = sp.Poly(sp.expand(poly),x)
    moments = [sp.S.One, M1, M2, M3]
    return sp.factor(sum(coef*moments[mon[0]] for mon,coef in poly.terms()))

def C_direct(uval, vval):
    # E[(U_0-mu)(U_s-mu)^2] for three distinct Brownian particles.
    return sp.factor(stat_avg((x-M1)*(E2.subs({u:uval,v:vval})-2*M1*E1.subs(u,uval)+M1*M1)))

computed = C_direct(u,v)
theorem = sp.factor(H*V*u + (K-H*V)*v)
iszero(computed-theorem)
# Remaining lag t multiplies this by e^(-A*t), by the Markov property.
for zv,rv in [(sp.S.Zero,sp.Rational(1,2)),(sp.Rational(1,4),sp.Rational(1,2)),
              (sp.Rational(1,4),sp.Integer(2)),(sp.Rational(3,4),sp.Integer(1))]:
    vals={z:zv,rho:rv}
    av,bv,cv,dv=(float(expr.subs(vals)) for expr in [A,B,C,Delta])
    vv,kv,hv,tv=(float(expr.subs(vals)) for expr in [V,K,H,T])
    for gap in [0.0,0.15,0.4,1.0,3.0]:
        cvdirect = float(computed.subs({**vals,u:sp.Float(math.exp(-av*gap)),v:sp.Float(math.exp(-bv*gap))}))
        cvclosed = math.exp(-av*gap)*(hv*vv-tv*math.exp(-dv*gap))
        assert abs(cvdirect-cvclosed)<1e-11, (vals,gap,cvdirect,cvclosed)
    if rv*(1-zv*zv)<1:
        root=math.log(float((A*A/(rho*(1-z)*C)).subs(vals)))/dv
        f=lambda s: math.exp(-av*s)*(hv*vv-tv*math.exp(-dv*s))
        assert root>0 and f(0)<0 and abs(f(root))<1e-11 and f(root+0.25)>0
    else:
        assert kv>=-1e-13
print('All polynomial moment, semigroup, three-time cumulant, and phase-boundary checks PASS.')
