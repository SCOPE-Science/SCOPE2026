"""Standalone checks for the event-indexed work-memory theorem.

Run: python verify.py
Requires Python 3, SymPy and NumPy. Analytic statements are proved in RESULT.md;
finite computations only cross-check the formulas.
"""
import math
from fractions import Fraction
import numpy as np
import sympy as sp

checks = 0

def ck(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

x = sp.symbols('x', positive=True)
a,b,Q,L,H = sp.symbols('a b Q L H', positive=True)
A = Q + L/(1-a)
B = Q + a*L/(1-a)
U4 = (6*Q*(a-b)*A+3*Q**2*(1-2*a+b)+6*L*B+H)/(1-b)
V4 = b*U4+6*Q*(a-b)*A+3*Q**2*(1-2*a+b)
G_independent = sp.factor(a*U4+Q*(1-a)*A-V4 - L*B)
G = -2*Q**2*(1-a)+a*L**2*(6*a-5*b-1)/((1-a)*(1-b))+H*(a-b)/(1-b)
ck(sp.cancel(G_independent-G)==0,'independently reconstructed fourth moments')
ck(sp.simplify((A-B)-L)==0,'stationary release variance shift')
ck(sp.simplify((1-a)*A-Q*(1-a)-L)==0,'stationary second-moment recursion')

P=128*x**5-720*x**4-6480*x**3-14094*x**2-14580*x-6561
expected = {
 1: 8/(2*x+1),
 2: (15*x**2+28*x+16)/(2*(x+1)**3*(x+2)),
 3: -8*P/((2*x+3)**3*(4*x**2+18*x+27)*(16*x**2+36*x+27)),
}
for m in range(1,9):
    am=(1+2*x/m)**(-m); bm=(1+4*x/m)**(-m)
    gm=sp.factor(G.subs({a:am,b:bm,Q:1/x,L:2,H:12*(1+sp.Rational(1,m))}))
    ck(sp.simplify(sp.limit(gm,x,0)-sp.Rational(8,m))==0,f'm={m} weak-confinement')
    if m>=3:
        ck(sp.simplify(sp.limit(x*x*gm,x,sp.oo)+2)==0,f'm={m} strong-confinement')
    if m in expected:
        ck(sp.factor(gm-expected[m])==0,f'm={m} exact rational formula')
    for val in [sp.Rational(1,3),sp.Rational(7,4),sp.Integer(5),sp.Integer(15)]:
        # An independent fourth-moment recursion and the closed form must agree.
        subs={a:am.subs(x,val),b:bm.subs(x,val),Q:1/val,L:2,H:12*(1+sp.Rational(1,m))}
        ck(sp.simplify(G_independent.subs(subs)-gm.subs(x,val))==0,f'm={m} independent moment sample')
ck(sp.sign(P.subs(x,sp.Rational(11141522,1000000)))==-1,'root lower rational bracket')
ck(sp.sign(P.subs(x,sp.Rational(11141523,1000000)))==1,'root upper rational bracket')
ck(sp.LC(sp.Poly(P,x))>0 and len(sp.Poly(P,x).all_coeffs())==6,'polynomial degree')

ed=sp.exp(-2*x)
G_det=sp.simplify(G.subs({a:ed,b:ed**2,Q:1/x,L:2,H:12}))
C_det=sp.simplify(x*x*(1-ed)*G_det/4)
ck(sp.simplify(sp.expand((C_det-2*ed*(x*x-sp.sinh(x)**2)).rewrite(sp.exp)))==0,'periodic limit exact')

# Check the Gamma/Erlang discrete cycles by generating Gaussian transitions
# with independently drawn dwell times; no moment identities enter this simulation.
try:
    from numba import njit
    @njit
    def cycle_works(on, off, normals1, normals2, k):
        n=len(on); w=np.empty(n); u=0.
        for i in range(n):
            e=math.exp(-k*on[i]); v=e*u+math.sqrt((1-e*e)/k)*normals1[i]
            w[i]=0.5*k*(u*u-v*v)
            u=v+math.sqrt(2*off[i])*normals2[i]
        return w
except ImportError:
    def cycle_works(on, off, normals1, normals2, k):
        n=len(on); w=np.empty(n); u=0.
        for i in range(n):
            e=math.exp(-k*on[i]); v=e*u+math.sqrt((1-e*e)/k)*normals1[i]
            w[i]=0.5*k*(u*u-v*v)
            u=v+math.sqrt(2*off[i])*normals2[i]
        return w

rng=np.random.default_rng(413311)
for m,k,n in [(1,1.,150000),(2,1.,150000),(3,5.,350000),(3,25.,350000),(4,5.,350000),(0,1.,150000)]:
    if m==0:
        on=off=np.ones(n)
        aa=math.exp(-2*k);bb=aa*aa;HH=12.
    else:
        on=rng.gamma(m,1/m,n);off=rng.gamma(m,1/m,n)
        aa=(1+2*k/m)**(-m);bb=(1+4*k/m)**(-m);HH=12*(1+1/m)
    w=cycle_works(on,off,rng.normal(size=n),rng.normal(size=n),k)[1000:]
    ck(abs(np.mean(w)-k)<0.10*k + .03, f'm={m} stationary cycle work mean')
    theory_g=-2*(1/k)**2*(1-aa)+aa*4*(6*aa-5*bb-1)/((1-aa)*(1-bb))+HH*(aa-bb)/(1-bb)
    theory_cov=k*k*(1-aa)*theory_g/4
    z=w-np.mean(w)
    estimates=[]
    for j in range(12):
        i0=(len(w)-1)*j//12; i1=(len(w)-1)*(j+1)//12
        estimates.append(np.mean(z[i0:i1]*z[i0+1:i1+1]))
    stderr=np.std(estimates,ddof=1)/math.sqrt(12)
    ck(abs(np.mean(estimates)-theory_cov)<6*stderr+0.03, f'm={m},k={k} lag-one covariance')
print('PASS',checks,'assertions; exact expressions and independent cycle-transition simulation')
