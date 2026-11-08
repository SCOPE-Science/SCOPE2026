#!/usr/bin/env python3
"""Independent algebraic and exact-arithmetic checks for a two-visit occupancy-design theorem.

Run: python verify.py
Requires Python 3.10+ and SymPy 1.10+.
These checks supplement, but do not replace, the analytic proof in RESULT.md.
"""
from fractions import Fraction as Q
from math import exp, log
from random import Random
import sympy as S

checks = 0

def verify(condition, explanation):
    global checks
    if not bool(condition):
        raise AssertionError(explanation)
    checks += 1

psi,a,b,U,V = S.symbols('psi a b U V', positive=True)
p00=1-psi+psi*a*b
P=[p00,psi*(1-a)*b,psi*a*(1-b),psi*(1-a)*(1-b)]
Z=[S.diff(p,psi) for p in P]
L=[-U*a*S.diff(p,a)-V*b*S.diff(p,b) for p in P]
Izz=sum(z*z/p for z,p in zip(Z,P))
Izl=sum(z*l/p for z,l,p in zip(Z,L,P))
Ill=sum(l*l/p for l,p in zip(L,P))
Q00=1-psi+psi*a*b
F=U**2*a/(1-a)+V**2*b/(1-b)
verify(S.cancel(Izz-(1-a*b)/(psi*Q00))==0,'I psi psi')
verify(S.cancel(Izl-(U+V)*a*b/Q00)==0,'I psi lambda')
verify(S.cancel(Ill-(psi*F-psi*(1-psi)*a*b*(U+V)**2/Q00))==0,'I lambda lambda')
verify(S.cancel(Izz*Ill-Izl**2-((1-a*b)*F-a*b*(U+V)**2)/Q00)==0,'determinant identity')

rng=Random(71065)
for k in range(600):
    aa=Q(rng.randint(1,28), 31)
    bb=Q(rng.randint(1,25), 29)
    pp=Q(rng.randint(1,16), 19)
    uu=Q(rng.randint(1,35),7)
    vv=Q(rng.randint(1,35),11)
    px=[1-pp+pp*aa*bb,pp*(1-aa)*bb,pp*aa*(1-bb),pp*(1-aa)*(1-bb)]
    dz=[-1+aa*bb,(1-aa)*bb,aa*(1-bb),(1-aa)*(1-bb)]
    # Directly differentiate the four event-probability polynomials.
    dl=[-pp*(uu+vv)*aa*bb,
        pp*(uu*aa*bb-vv*(1-aa)*bb),
        pp*(-uu*aa*(1-bb)+vv*aa*bb),
        pp*(uu*aa*(1-bb)+vv*bb*(1-aa))]
    fzz=sum(x*x/p for x,p in zip(dz,px))
    fzl=sum(x*y/p for x,y,p in zip(dz,dl,px))
    fll=sum(y*y/p for y,p in zip(dl,px))
    direct=fzz*fll-fzl*fzl
    compact=((1-aa*bb)*(uu*uu*aa/(1-aa)+vv*vv*bb/(1-bb))-aa*bb*(uu+vv)**2)/(1-pp+pp*aa*bb)
    verify(direct==compact, 'rational Fisher determinant '+str(k))
    verify(direct>0,'interior positive definite '+str(k))

# With times in integer multiples of log 2, exponential probabilities are rational.
def G_log2(i,j):
    a=Q(1,2**i)
    b=Q(1,2**j)
    return ((1-a*b)*(Q(i*i)*a/(1-a)+Q(j*j)*b/(1-b))-a*b*(i+j)**2)

g_equal=G_log2(5,5)
g_asym=G_log2(3,7)
verify(g_equal==Q(775,512),'equal-budget exact value')
verify(g_asym==Q(715639,455168),'asymmetric-budget exact value')
verify(g_asym-g_equal==Q(3333,56896),'exact strict improvement')
verify(G_log2(7,3)==g_asym,'exchange symmetry')

# Additional diagnostics of the analytical large-budget limit.
lo,hi=1.,2.
for _ in range(100):
    mid=(lo+hi)/2
    if 2*(1-exp(-mid))-mid>0:
        lo=mid
    else:
        hi=mid
root=(lo+hi)/2
verify(abs(root-1.59362426004004)<1e-12,'stationary-point location')
verify(abs(root**2/(exp(root)-1)-root*(2-root))<1e-12,'stationary-point value')

def f(t):
    return t*t/__import__('math').expm1(t)
for theta in (16.,24.,40.,80.):
    # An explicit competitor with one short probe exceeds equal allocation.
    asym=f(root)+f(theta-root)
    eq=2*f(theta/2)
    verify(asym>eq,'large-budget symmetry breaking')
print(f'PASS {checks} checks; exact gain {g_asym-g_equal}; optimal finite-gap constant {root:.14f}')
