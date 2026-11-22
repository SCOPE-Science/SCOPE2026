"""Symbolic and finite checks for the adaptive quintic matrix-sign safety theorem.

Requires sympy; run: python verify.py.  Numerical grids are diagnostics,
not substitutes for the analytic proof in RESULT.md.
"""
from fractions import Fraction
import math
import sympy as sp

r, a = sp.symbols('r a')
F = sp.expand(1-(1-r)*(1+r/sp.Integer(2)+a*r*r)**2)
P = 128*a**3 + 496*a**2 - 1026*a + 27
rt = (8*a-3)/(10*a)
checks = 0

def check(condition, message):
    global checks
    assert bool(condition), message
    checks += 1

check(sp.simplify(F-r-r*(r-1)*(2*a*r+1)*(2*a*r*r+r+4)/4)==0, 'descent factor')
check(sp.simplify(sp.diff(F,r)-r*(10*a*r-8*a+3)*(2*a*r*r+r+2)/4)==0, 'critical derivative')
check(sp.simplify(F.subs(r,rt)+(8*a-3)**3*(4*a*a+22*a-1)/(25000*a**3))==0, 'exact min')
check(sp.simplify(F.subs(r,rt)+1/(2*a)+(4*a+1)**2*P/(25000*a**3))==0, 'exact threshold')
check(sp.simplify(F.subs(a,sp.Rational(3,2))+r-r/4*(4*(1-r)**4+7*r*(1-r)**3+4*r*r*(1-r)**2+8*r**4))==0, 'positive Bernstein identity')
check(P.subs(a,sp.Rational(29,20)) == -sp.Rational(6909,250), 'safe endpoint')
check(P.subs(a,sp.Rational(3,2)) == 36, 'unsafe endpoint')
check(sp.diff(P,a).subs(a,sp.Rational(29,20))>0, 'unique critical root beyond lower bracket')
check(F.subs({r:sp.Rational(3,5),a:sp.Rational(3,2)}) == -sp.Rational(1107,3125), 'rational unsafe witness')
check(F.subs({r:sp.Rational(3,5),a:sp.Rational(3,2)}) < -sp.Rational(1,3), 'unsafe crosses fixed-point barrier')

# Exact-rational spot tests on a two-dimensional parameter grid.
for ai in [sp.Rational(0), sp.Rational(3,8), sp.Rational(1), sp.Rational(29,20)]:
    for j in range(1,100):
        rr=sp.Rational(j,100)
        f=F.subs({r:rr,a:ai})
        check(abs(f)<rr, 'positive residual contraction on checked grid')
        check(f > -sp.Rational(1,3), 'one-sided invariant bound on checked grid')
        if j<=30:
            rn=-sp.Rational(j,100)
            gn=F.subs({r:rn,a:ai})
            check(abs(gn)<-rn, 'negative residual contraction on checked grid')

# A 3-mode test with arbitrary changing coefficients (diagonal sign / singular values).
coef=[0.125,1.44,0.8,1.45,0.4,1.28,0.01]
for x0 in [0.013,0.125,0.71]:
    x=x0
    for k in range(120):
        alpha=coef[k%len(coef)]
        rr=1-x*x
        x=x*(1+rr/2+alpha*rr*rr)
        check(math.isfinite(x), 'finite scalar iteration')
        check(abs(1-x*x)<=abs(rr)+1e-14, 'residual contraction (floating point tolerance)')
    check(abs(x-1)<1e-12, 'converges numerically to polar/sign value')

# A concrete unsafe unbounded orbit (fixed a=3/2), validated at finite times.
alpha=1.5
x=math.sqrt(2/5)
magnitudes=[]
for k in range(4):
    rr=1-x*x
    x=x*(1+rr/2+alpha*rr*rr)
    magnitudes.append(x)
    check(math.isfinite(x), 'finite early divergence witness')
check(all(magnitudes[i+1]>magnitudes[i] for i in range(3)), 'strict growth past unsafe barrier')

root=float(sp.nroots(P, maxsteps=100)[2])
check(1.45<root<1.5, 'root bracketing')
print('VERIFY_OK', 'assertions='+str(checks), 'critical_cap=%.14f'%root, 'a=1.5 witness='+repr(magnitudes[:3]))
