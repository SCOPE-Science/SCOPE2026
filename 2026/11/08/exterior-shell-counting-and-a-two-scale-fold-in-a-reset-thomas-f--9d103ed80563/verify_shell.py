"""Independent algebraic and quadrature checks for a reset Thomas–Fermi shell law.

Run: python verify_shell.py
Requires: sympy, scipy, numpy.
Finite checks supplement, but do not replace, the analytic theorem.
"""
import math
from scipy.integrate import quad
from scipy.optimize import brentq
import sympy as sp

N = 0

def check(condition, detail=''):
    global N
    N += 1
    if not condition:
        raise AssertionError(f'check {N}: {detail}')

def close(x, y, tol=1e-8):
    check(abs(x-y) <= tol*max(1., abs(y)), f'{x} != {y}')

lam, a, b, r = sp.symbols('lam a b r', positive=True)
s = a*a+a*b+b*b
kl = 1-sp.Rational(3,2)*a/lam+sp.Rational(1,2)*a**3/lam**3
kr = sp.Rational(3,2)*(b-a)/lam-sp.Rational(1,2)*(b**3-a**3)/lam**3
check(sp.simplify(kl.subs(lam,a)) == 0, 'left boundary')
check(sp.simplify(kl.subs(lam,b)-kr.subs(lam,b)) == 0, 'joining count')
check(sp.simplify(sp.diff(kl,lam).subs(lam,b)-sp.diff(kr,lam).subs(lam,b)) == 0, 'joining slope')
check(sp.simplify(sp.diff(kl,lam)-3*a*(lam**2-a**2)/(2*lam**4)) == 0)
check(sp.simplify(sp.diff(kr,lam)-3*(b-a)*(s-lam**2)/(2*lam**4)) == 0)
check(sp.simplify(kr.subs(lam,sp.sqrt(s))-(b-a)/sp.sqrt(s)) == 0)
check(sp.simplify(sp.diff(kl,lam,2).subs(lam,a)-3/a**2) == 0)
check(sp.simplify(sp.diff(kr,lam,2).subs(lam,sp.sqrt(s))+3*(b-a)/s**sp.Rational(3,2)) == 0)
# h = -S' on (1,inf), including the boundary singularity.
S = (sp.sqrt(lam)-sp.sqrt(lam-1))**r*sp.exp(-r*sp.sqrt(lam*(lam-1)))
h = r*sp.sqrt(lam/(lam-1))*S
check(sp.refine(sp.simplify((sp.diff(S,lam)+h)/S), sp.Q.positive(lam-1))==0, 'survival density identity')


def tail(x, alpha):
    if x <= 1:
        return 1.
    return math.exp(-alpha*(math.sqrt(x*(x-1)) + math.asinh(math.sqrt(x-1))))


def density_scale(x, alpha):
    return alpha*math.sqrt(x/(x-1))*tail(x,alpha)


def kvalue(x, aa, bb):
    if x <= aa:
        return 0.
    if x <= bb:
        return (1-aa/x)**2*(1+aa/(2*x))
    return 1.5*(bb-aa)/x-.5*(bb**3-aa**3)/x**3


def kp(x, aa, bb):
    if x < bb:
        return 1.5*aa*(x*x-aa*aa)/x**4
    return 1.5*(bb-aa)*(aa*aa+aa*bb+bb*bb-x*x)/x**4


def roots_for(k, aa, bb):
    star=math.sqrt(aa*aa+aa*bb+bb*bb)
    cap=(bb-aa)/star
    if not (0 < k < cap):
        raise ValueError('k outside smooth density support')
    low=brentq(lambda x:kvalue(x,aa,bb)-k,aa,star,xtol=1e-14)
    high=brentq(lambda x:kvalue(x,aa,bb)-k,star,max(2*star, 2*(bb-aa)/k),xtol=1e-12)
    return low, high


def pdf(k, aa, bb, alpha):
    x,y=roots_for(k,aa,bb)
    return density_scale(x,alpha)/abs(kp(x,aa,bb))+density_scale(y,alpha)/abs(kp(y,aa,bb))


def survival_k(k, aa, bb, alpha):
    x,y=roots_for(k,aa,bb)
    return tail(x,alpha)-tail(y,alpha)

for aa,bb,alpha in [(1,1.6,.65),(1,3,1.4),(1.2,2,.7),(2,4,1.1),(3,6,.4),(1.01,1.1,2.3)]:
    star=math.sqrt(aa*aa+aa*bb+bb*bb)
    cap=(bb-aa)/star
    close(kvalue(aa,aa,bb),0)
    close(kvalue(bb,aa,bb),1-1.5*aa/bb+.5*(aa/bb)**3)
    close(kvalue(star,aa,bb),cap)
    check(star>bb and cap<1)
        # Numerical mass, starting at a singular endpoint of scale density.
    close(quad(lambda t:density_scale(1+t*t,alpha)*2*t,1e-8,8,epsabs=1e-9)[0],1.,tol=2e-7)
    for frac in [.015,.04,.15,.33,.57,.8,.96,.995]:
        k=frac*cap
        lo,hi=roots_for(k,aa,bb)
        close(kvalue(lo,aa,bb),k,1e-10)
        close(kvalue(hi,aa,bb),k,1e-10)
        check(aa < lo < star < hi)
        check(pdf(k,aa,bb,alpha)>0)
        # Compare counting law against direct scale integration, independent of density inverse Jacobian.
        direct=quad(lambda x:density_scale(x,alpha),lo,hi,epsabs=1e-10)[0]
        close(survival_k(k,aa,bb,alpha),direct,5e-8)
        # Independent derivative check g(k)=-d/dk survival.
        delta=min(1e-5*cap, .1*k, .1*(cap-k))
        finite=-(survival_k(k+delta,aa,bb,alpha)-survival_k(k-delta,aa,bb,alpha))/(2*delta)
        close(finite,pdf(k,aa,bb,alpha),3e-5)
    check(0 < survival_k(1e-8*cap,aa,bb,alpha) < tail(aa,alpha))
    close(survival_k((1-1e-9)*cap,aa,bb,alpha),0.,5e-4)
    # The two inverse branch weights tend to one-half near the fold.
    for eps in [1e-4,1e-5,1e-6]:
        lo,hi=roots_for(cap*(1-eps),aa,bb)
        v1=density_scale(lo,alpha)/abs(kp(lo,aa,bb))
        v2=density_scale(hi,alpha)/abs(kp(hi,aa,bb))
        check(abs(v1/(v1+v2)-.5)<10*math.sqrt(eps),'fold posterior')
    # At upper cap the density has the predicted inverse-square-root coefficient.
    foldpref=density_scale(star,alpha)*math.sqrt(2*star**3/(3*(bb-aa)))
    for eps in [1e-5,1e-6]:
        kval=cap*(1-eps)
        close(pdf(kval,aa,bb,alpha)*math.sqrt(cap-kval),foldpref,4e-4)
    # Lower edge prefactor depends sharply on whether inner radius touches initial cloud edge.
    lowpref=(aa*density_scale(aa,alpha)/math.sqrt(6)) if aa>1 else alpha*math.pow(1.5,.25)/math.sqrt(6)
    power=.5 if aa>1 else .75
    for kval in [1e-9,3e-10]:
        close(pdf(kval,aa,bb,alpha)*kval**power,lowpref,2e-2)

print(f'PASS: {N} independent symbolic and numerical assertions')
