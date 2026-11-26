"""Independent symbolic checks for a two-target Brownian cover-search placement crossover.
Requires Python 3, SymPy, SciPy, and mpmath. Numerical tests diagnose, not prove, the theorem.
"""
import math
import sympy as sp
from scipy.optimize import brentq

x, S = sp.symbols('x S', positive=True)
z = (x-1/x)/2
c = (x+1/x)/2
F = (x*x-1)**2 + 4*S*x*(x*x-1)-4*S*S
N = c*(z*z+2*z*S-S*S)+z*(z+S)**2
assert sp.simplify(4*x*N-F) == 0
assert sp.simplify(sp.diff(F,x) - (4*x*(x*x-1)+4*S*(3*x*x-1))) == 0
assert sp.diff(F,x).subs({x:2,S:3}) > 0
u=sp.symbols('u',positive=True)
test=sp.factor((F.subs({x:u,S:(u**3-u**(-3))/2})*u**6))
want=(u-1)**2*(u+1)**2*(u*u+1)*(u**6-u*u-1)
assert sp.simplify(test-want)==0
rho=brentq(lambda q:q**3-q-1,1,2,xtol=1e-14)
bc=1.5*math.log(rho)

def objective(a,b):
    return ((math.sinh(a)**2+math.sinh(b)**2)/
            (math.sinh(a)+math.sinh(b))+math.cosh(a)+math.cosh(b)-2)

def quartic(a,b):
    # The factors are kept in the original stable polynomial form.
    y=math.exp(a); h=math.sinh(b)
    return (y*y-1)**2+4*h*y*(y*y-1)-4*h*h

def optimal_a(b):
    return brentq(lambda a:quartic(a,b),0,b,xtol=1e-14)

for b in (.002,.02,.1,.2,bc/2,bc,2*bc,1,2,4,8,20):
    a=optimal_a(b)
    assert 0<a<b
    assert abs(quartic(a,b))/(math.sinh(b)**2+1) < 1e-10
    if b < bc-1e-7: assert a/b > 1/3
    if b > bc+1e-7: assert a/b < 1/3
    if abs(b-bc)<1e-7: assert abs(a/b-1/3)<1e-9
    # Independent central finite difference verifies the sign formula.
    h=1e-5*min(a,1)
    der=(objective(a+h,b)-objective(a-h,b))/(2*h)
    assert abs(der)/(1+abs(objective(a,b))) < 1e-6
    for k in (.5,.8,1.2,1.5):
        candidate=k*a
        if candidate<=0: continue
        assert objective(candidate,b)>objective(a,b)-1e-8*max(1,objective(a,b))

assert abs(optimal_a(0.0001)/0.0001-(math.sqrt(2)-1))<5e-5
assert abs((optimal_a(50)-(50-math.log(2))/3))<1e-6
assert optimal_a(2)/2 < .272
print('All symbolic factorization, unique-root sign, asymptotic, and numerical derivative diagnostics passed.')
print('plastic constant',rho,'crossover b',bc,'ratio at b=2',optimal_a(2)/2)
