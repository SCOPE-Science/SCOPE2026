"""Reproducibility checks for correlated Brownian searcher weak-restart phase boundary.
Run: python checker.py  (requires sympy).  Exact algebra, not a substitute for the analytic first-passage tail proof.
"""
import sympy as sp
x, y, D, c, rate = sp.symbols('x y D c rate', positive=True)
rho = -c
L = lambda f: D * (sp.diff(f, x, 2) + sp.diff(f, y, 2) + 2 * rho * sp.diff(f, x, y))
mu1 = x*y/(2*D*c)
mu2 = x*y*(x*x+y*y+3*c*x*y)/(12*D**2*c*(2*c**2-1))
U = x/y+y/x
mu3 = x*y*(3*(x*x+y*y)**2 + 15*c*x*y*(x*x+y*y) + (20*c*c-1)*x*x*y*y) / (120*D**3*c*(2*c*c-1)*(4*c*c-3))
checks = 0

def eq(a,b):
    global checks
    residual = sp.factor(sp.together(a-b))
    assert residual == 0, residual
    checks += 1

eq(L(mu1), -1)
eq(L(mu2), -2*mu1)
eq(L(mu3), -3*mu2)
for m in (mu1,mu2,mu3):
    eq(m.subs(x,0),0)
    eq(m.subs(y,0),0)
    eq(m - m.subs({x:y, y:x}, simultaneous=True),0)

corr = (U+sp.sqrt(U**2+216))/18
f = sp.factor(mu2-2*mu1**2)
eq(f, x*y*(c*(x*x+y*y) + (6-9*c*c)*x*y)/(12*D**2*c*c*(2*c*c-1)))
reset_slope = sp.factor(mu1**2 - mu2/2)
eq(reset_slope, -f/2)
# At the zero-slope curve U=(9c^2-6)/c, the second coefficient is strictly positive.
mu1U = x*y/(2*D*c)
mu2U = (x*y)**2*(U+3*c)/(12*D**2*c*(2*c*c-1))
mu3U = mu3
second = sp.factor(mu3U/6 - mu1U*mu2U + mu1U**3)
second_critical = (x*y)**3/D**3*(162-161*c*c)/(720*c**3*(4*c*c-3))
second_by_U = (x*y)**3/D**3*((3*U**2+15*c*U+20*c*c-1)/(720*c*(2*c*c-1)*(4*c*c-3))-(U+3*c)/(24*c*c*(2*c*c-1))+1/(8*c**3))
eq(second, second_by_U)
eq(second_by_U.subs(U,(9*c*c-6)/c),second_critical)
# Formula for perfect anticorrelation reduces to Brownian exit from (-y,x).
# Exact Laplace transform at rho=-1, power-series coefficients checked independently.
k=sp.symbols('k',real=True)
L0 = x+y; delta=x-y
phi = sp.cosh(k*delta/2)/sp.cosh(k*L0/2)
# k^2 = rate/D; mean with restart = (1/phi-1)/rate.
ser = sp.series((1/phi-1)/k**2,k,0,8).removeO()
for order, term in enumerate([mu1.subs(c,1), (mu1**2-mu2/2).subs(c,1), (mu3/6-mu1*mu2+mu1**3).subs(c,1)]):
    # Convert k^(2order) coefficient to rate^order, with k^2=rate/D.
    target = sp.factor(term * D**(order+1))
    eq(sp.expand(ser).coeff(k,2*order),target)
# Rational examples on both sides of the threshold and different starting-distance ratios.
for X,Y,C,sign in [(1,1,sp.Rational(4,5),-1),(1,1,sp.Rational(19,20),1),
                   (1,2,sp.Rational(19,20),-1),(1,3,sp.Rational(99,100),-1),
                   (1,1,sp.Rational(99,100),1),(2,2,sp.Rational(9,10),-1)]:
    val=sp.sign(reset_slope.subs({x:X,y:Y,c:C,D:1}))
    assert val == sign, (X,Y,C,val)
    checks += 1
# For U=2 and U=3, the critical correlations are the stated algebraic constants.
u=sp.symbols('u',positive=True)
critical=(u+sp.sqrt(u*u+216))/18
eq(critical.subs(u,2),(1+sp.sqrt(55))/9)
eq(critical.subs(u,3),1)
print(f'PASS: {checks} exact symbolic, boundary, independent interval, and rational sign assertions')
print('equal-distance critical c =',sp.N(critical.subs(u,2),16))
