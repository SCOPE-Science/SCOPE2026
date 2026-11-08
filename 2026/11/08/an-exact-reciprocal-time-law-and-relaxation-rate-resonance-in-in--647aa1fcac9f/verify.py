"""Symbolic and numerical reproducibility checks for a critical inhibitory SIS–activity model.
Run: python verify.py
Dependencies: Python 3, sympy, scipy, numpy.
These finite checks supplement the analytic proof; they are not an infinite proof.
"""
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp

x,y,s,k,zeta,kappa,eta,c,d=sp.symbols('x y s k zeta kappa eta c d',positive=True)
f=x*(eta*(1-x)/(1+s*y)-zeta)
g=kappa*(k*x-y)
U=(c+d*y)/x
Ud=sp.factor(sp.diff(U,x)*f+sp.diff(U,y)*g)
# Universal identity and its rigidity for c>0, s>0, k>0.
critical=sp.factor(Ud.subs(eta,zeta).subs(d,c*s))
assert sp.simplify(critical - c*(zeta*(1+s*k)+s*(zeta-kappa)*(y/x-k)))==0
assert sp.simplify(critical.subs(kappa,zeta)-c*zeta*(1+s*k))==0
assert sp.simplify(Ud.subs(y,0)-(d*kappa*k+c*eta-c*(eta-zeta)/x))==0
# At eta=zeta, the constant-in-y at x->infinity requires d=c*s.
p0=sp.simplify(sp.limit(Ud.subs(eta,zeta),x,sp.oo))
assert sp.simplify(sp.diff(p0,y)-zeta*(d-c*s)/(1+s*y)**2)==0
# Cubic slow-manifold coefficient and reciprocal logarithmic coefficient.
A=zeta*(1+s*k)
a=k*A/kappa
xp=sp.series(f.subs(eta,zeta).subs(y,k*x+a*x**2),x,0,4).removeO().expand()
B=sp.factor(xp.coeff(x,3))
assert sp.simplify(B-zeta*s*k*(1+s*k)*(1-zeta/kappa))==0
assert sp.simplify(-B/A - s*k*(zeta/kappa-1))==0
# Several exact positive rational substitutions, not just unit-rate normalizations.
for ss,kk,zz,kap in ((2,3,5,5),(sp.Rational(1,4),2,3,1),(3,sp.Rational(2,5),2,4)):
    subs={s:ss,k:kk,zeta:zz,kappa:kap,eta:zz,c:1,d:ss}
    expr=sp.factor(critical.subs({s:ss,k:kk,zeta:zz,kappa:kap,c:1}))
    want=zz*(1+ss*kk)+ss*(zz-kap)*(y/x-kk)
    assert sp.simplify(expr-want)==0

# Quantitative trajectories at 3 relative activity-relaxation rates.
def integrate(kk,tt=(5000.,20000.),x0=.6,y0=.4):
    ss=1.; zz=1.; kval=1.; M=zz*(1+ss*kval)
    def rhs(t,z):
        xx,yy=z
        return [-zz*xx*(xx+ss*yy)/(1+ss*yy),kk*(kval*xx-yy)]
    sol=solve_ivp(rhs,[0,tt[-1]], [x0,y0],method='DOP853',rtol=3e-13,atol=3e-15,dense_output=True)
    assert sol.success
    xx0,yy0=sol.sol(tt[0]); xx1,yy1=sol.sol(tt[1]);
    b=(1/xx1-1/xx0-M*(tt[1]-tt[0]))/np.log(tt[1]/tt[0])
    return float(b),float(xx1),float(yy1)

for kap, target in ((.5,1.),(1.,0.),(2.,-.5)):
    got, xx,yy=integrate(kap)
    assert abs(got-target)<0.02,(kap,got,target)
    print('rate',kap,'estimated logarithm',round(got,7),'exact',target,'x_end',xx,'y_end',yy)

for kap in (1.,):
    x0=.6; y0=.4; ss=1.; zz=1.; kval=1.; U0=(1+ss*y0)/x0
    def rhs(t,v):
        xx,yy=v
        return [-zz*xx*(xx+ss*yy)/(1+ss*yy),kap*(kval*xx-yy)]
    sol=solve_ivp(rhs,[0.,1000.],[x0,y0],method='DOP853',rtol=1e-13,atol=1e-15,dense_output=True)
    for t in (0,0.1,1,5,20,100,500,1000):
        xx, yy = sol.sol(t)
        assert abs((1+ss*yy)/xx-(U0+2*t))<2e-8,(t,xx,yy)
# Matched-rate reciprocal identity at non-unit rational parameters.
def general_rhs(t,v):
    xx, yy=v
    ss, kval, zz, kap=2.,3.,5.,5.
    return [-zz*xx*(xx+ss*yy)/(1+ss*yy),kap*(kval*xx-yy)]
sol=solve_ivp(general_rhs,[0,5],[.6,.25],method='DOP853',rtol=2e-13,atol=2e-15,dense_output=True)
for t in (0,.1,.5,1,2,5):
    xx,yy=sol.sol(t)
    assert abs((1+2*yy)/xx-(2.5+35*t))<2e-8,(t,xx,yy)
print('All symbolic and numerical checks passed.')
