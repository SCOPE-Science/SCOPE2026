"""Exact algebraic checks for a two-stage saturating removal example.

Dependencies: Python 3 and SymPy. Run with python verification/check_interstage.py.
The accompanying analytic proof, not these finitely many tests, certifies the
complete parameter classification.
"""
import sympy as s

x, r = s.symbols('x r')
T1 = lambda y: y - s.Rational(3, 5)*y/(1+y)
T2 = lambda y: y - s.Rational(4, 5)*y/(2+y)
poly = ((60-125*r)*x**4 + (120-300*r-125*r**2)*x**3
        + (96-130*r-425*r**2)*x**2 + (200*r-400*r**2)*x
        + (200*r-100*r**2))
den = 5*(x+1)*(x+2)*(5*r*x+5*r+5*x**2+12*x+10)*(5*r*x+10*r+5*x**2+11*x+10)
checks=0

def check(condition, info):
    global checks
    assert bool(condition), info
    checks += 1

check(s.cancel(T2(T1(x)+r)-T1(T2(x)+r)-poly/den)==0,'symbolic identity')
check(s.factor(poly.subs(r,s.Rational(2,5)))==2*(x-2)**2*(5*x**2+10*x+8),'double root')
check(s.simplify(poly.subs(x,2)+144*(5*r-2)*(5*r+8))==0,'tangency sign')
check(poly.coeff(x,3).subs(r,s.Rational(12,25))==-s.Rational(264,5),'far-root scale')
check(s.simplify(s.diff(poly,r).subs({r:s.Rational(2,5),x:2}))==-7200,'root splitting')
check(s.simplify(s.diff(poly,x,2).subs({r:s.Rational(2,5),x:2}))==192,'quadratic curvature')
check(s.factor(poly.subs(r,s.Rational(43,100)))*400 == 2500*x**4-12845*x**3-15393*x**2+4816*x+27004,'rational example')
for rv in [s.Rational(0),s.Rational(1,10),s.Rational(2,5),s.Rational(43,100),s.Rational(12,25),s.Rational(1,2),s.Rational(3,2),s.Rational(2),s.Rational(5,2)]:
    for xv in [s.Rational(1,100),s.Rational(1,2),s.Rational(1),s.Rational(2),s.Rational(3),s.Rational(10),s.Rational(100)]:
        pv=poly.subs({r:rv,x:xv})
        actual=s.cancel(T2(T1(xv)+rv)-T1(T2(xv)+rv))
        check(s.sign(actual)==s.sign(pv),f'sign match at r={rv},x={xv}')
        check(s.simplify(actual-pv/den.subs({r:rv,x:xv}))==0,'exact value')
for xv,expected in [(1,1),(2,-1),(10,1)]:
    check(s.sign(poly.subs({x:xv,r:s.Rational(43,100)}))==expected,'reentrant witness')
roots=[complex(v) for v in s.nroots(poly.subs(r,s.Rational(43,100)),maxsteps=200)]
pos=sorted(v.real for v in roots if abs(v.imag)<1e-9 and v.real>0)
check(len(pos)==2,'exactly two numerical positive roots')
check(abs(pos[0]-1.10383290344146)<1e-10,'lower root')
check(abs(pos[1]-6.05382660573888)<1e-10,'upper root')
print(f'PASS: {checks} symbolic/rational/numerical checks; r=0.43 switches at {pos[0]:.13f}, {pos[1]:.13f}')
