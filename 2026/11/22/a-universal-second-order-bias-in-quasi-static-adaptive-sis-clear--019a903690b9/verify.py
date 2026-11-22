"""Exact symbolic checks for a degenerate adaptive SIS pair-closure flow.

Requires SymPy; optional SciPy numerical integration supplies a diagnostic.
Run: python verify.py
"""
import sympy as sp

n, gam, x = sp.symbols('n gam x', real=True, positive=True)
w = gam * (n + 1) / (n - 1)
tau = 2 * gam / (n - 1)
a0, c0 = (n - 1) / (2 * n), 1 / n
c1 = (n - 1) / (2 * n)
b2, c2, b3, c3 = sp.symbols('b2 c2 b3 c3')
p = a0 + b2*x*x + b3*x**3
q = c0 + c1*x + c2*x*x + c3*x**3
X = x*(tau*n*p - gam)
F = gam*q+(tau*(n-1)-w)*p-tau*n*p**2 + tau*n*p*(1-3*p-q)*x/(1-x)
G = -gam*q+2*tau*p-tau*n*p*q+2*tau*n*p**2*x/(1-x)

# The fast block at the disease-free correlation equilibrium is Hurwitz.
P, Q = sp.symbols('P Q')
Ffast = gam*Q+(tau*(n-1)-w)*P-tau*n*P**2 + tau*n*P*(1-3*P-Q)*x/(1-x)
Gfast = -gam*Q+2*tau*P-tau*n*P*Q+2*tau*n*P**2*x/(1-x)
J = sp.simplify(sp.Matrix([Ffast, Gfast]).jacobian([P, Q]).subs({x:0,P:a0,Q:c0}))
assert J==sp.Matrix([[-gam*(n+1)/(n-1),gam],[2*gam/(n-1),-2*gam]])
assert sp.factor(sp.trace(J)) == -gam*(3*n-1)/(n-1)
assert sp.factor(J.det()) == 2*gam**2*n/(n-1)

# Center-manifold invariance equations to cubic order.
r1 = sp.series(F - sp.diff(p,x)*X, x,0,4).removeO().expand()
r2 = sp.series(G - sp.diff(q,x)*X, x,0,4).removeO().expand()
assert sp.factor(r1.coeff(x,0)) == sp.factor(r2.coeff(x,0)) == 0
assert sp.factor(r1.coeff(x,1)) == sp.factor(r2.coeff(x,1)) == 0
s2 = sp.solve([sp.factor(r1.coeff(x,2)),sp.factor(r2.coeff(x,2))], [b2,c2],dict=True)
assert len(s2)==1
B2 = sp.factor(s2[0][b2]); C2 = sp.factor(s2[0][c2])
assert sp.simplify(B2+(n-1)**2/(2*n**2))==0
assert sp.simplify(C2-(n-1)**2/(2*n**2))==0
r13 = sp.factor(r1.coeff(x,3).subs({b2:B2,c2:C2}))
r23 = sp.factor(r2.coeff(x,3).subs({b2:B2,c2:C2}))
s3 = sp.solve([r13,r23],[b3,c3],dict=True)
assert len(s3)==1
B3,C3 = [sp.factor(s3[0][z]) for z in [b3,c3]]
assert sp.simplify(B3-(n-2)*(n-1)**2/(2*n**3))==0
assert sp.simplify(C3-(n-1)**2/n**3)==0
K = sp.factor(-tau*n*B2)
E = sp.factor(tau*n*B3)
A = sp.sqrt(1/(2*K))
actual_second = sp.factor(E/(2*K**2))
assert sp.factor(K-gam*(n-1)/n)==0
assert sp.factor(E-gam*(n-1)*(n-2)/n**2)==0
assert sp.factor(actual_second-(n-2)/(2*gam*(n-1)))==0

# Independently reconstruct the quasi-static positive root via its quadratic.
P0=a0+B2*x*x+b3*x**3
AA=(n*tau)**2*(1+x)/(1-x)
BB=tau*n*(gam+w-tau*(n-1)+x*(tau-w))
CC=gam*(w-tau*(n+1)+x*(tau-w))
pol=sp.series(AA*P0**2+BB*P0+CC,x,0,4).removeO().expand()
assert all(sp.simplify(pol.coeff(x,j))==0 for j in range(3))
b3qs=sp.factor(sp.solve(sp.factor(pol.coeff(x,3)),b3)[0])
assert sp.factor(b3qs-(n-3)*(n-1)**2/(4*n**3))==0
qs_second=sp.factor((tau*n*b3qs)/(2*K**2))
assert sp.factor(qs_second-(n-3)/(4*gam*(n-1)))==0
assert sp.factor(actual_second-qs_second-1/(4*gam))==0
assert actual_second.subs({n:sp.Rational(5,2),gam:1})>0
assert qs_second.subs({n:sp.Rational(5,2),gam:1})<0
assert actual_second.subs({n:2,gam:1})==0
print('SYMBOLIC_PASS')
print('Full cubic coefficient:', K, 'full quartic coefficient:',E)
print('Full t^-1 coefficient:',actual_second)
print('Quasi-static t^-1 coefficient:',qs_second)
print('Universal second coefficient gap:',sp.factor(actual_second-qs_second))

# Finite-time integration is a diagnostic only, not a proof of the limit.
try:
    import scipy.integrate as sci
    for deg in [sp.Rational(5,2), 3]:
        z=float(deg); G0=1.0; W=(z+1)/(z-1); T=2/(z-1)
        xx=0.08; P=float((deg-1)/(2*deg)+B2.subs({n:deg,gam:1})*sp.Rational(8,100)**2+B3.subs({n:deg,gam:1})*sp.Rational(8,100)**3)
        Q=float(1/deg +c1.subs(n,deg)*sp.Rational(8,100)+C2.subs({n:deg,gam:1})*sp.Rational(8,100)**2+C3.subs({n:deg,gam:1})*sp.Rational(8,100)**3)
        def ode(t,y):
            i,p,q=y
            return (i*(T*z*p-1), q+(T*(z-1)-W)*p-T*z*p*p+T*z*p*(1-3*p-q)*i/(1-i), -q+2*T*p-T*z*p*q+2*T*z*p*p*i/(1-i))
        out=sci.solve_ivp(ode,(0,10**6),(xx,P,Q),method='LSODA',rtol=1e-10,atol=1e-12,t_eval=(10**5,10**6))
        assert out.success and all(val>0 for val in out.y[0])
        asym= float(A.subs({n:deg,gam:1}))
        lead=float((10**6)**0.5*out.y[0,-1])
        assert abs(lead-asym)<0.003
        print('NUMERICAL_DIAGNOSTIC n=',str(deg),'sqrt(t)*i at 1e6=',round(lead,8),'predicted=',round(asym,8))
except ImportError:
    print('NUMERICAL_SKIPPED: SciPy not installed')
print('VERIFY_OK')
