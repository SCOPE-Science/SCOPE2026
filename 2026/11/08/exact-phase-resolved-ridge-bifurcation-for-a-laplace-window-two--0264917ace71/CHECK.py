"""Reproducible checks for the Laplace-window two-tone spectrogram ridge law.
All infinite/continuous assertions require the proof; these checks corroborate algebra and numerical cases.
Run: python CHECK.py (requires numpy, scipy, sympy)."""
import math
import numpy as np
import sympy as sp
from scipy.integrate import quad

passed=0
def ck(test,why):
    global passed
    if not test: raise AssertionError(why)
    passed+=1

t,q,c=sp.symbols('t q c',real=True)
U=t+q+1
D=sp.expand(U**2-4*q*t)
N=sp.expand((1+c)*U**2+4*(1-c)*q*t)
H=sp.expand(sp.diff(N,t)*D-2*N*sp.diff(D,t))
H_expected=( -2*(1+c)*t**3 +6*((c-3)*q-(c+1))*t**2
 -2*(3*c*q**2-2*c*q+3*c-5*q**2+6*q+3)*t
 +2*(1+q)**2*((5+c)*q-(1+c)) )
ck(sp.expand(H-H_expected)==0,'derivative polynomial')
ck(sp.factor(H.subs(t,0))==2*(q+1)**2*(c*q-c+5*q-1),'constant polynomial')
qcrit=(1+c)/(5+c)
B=3*c*q**2-2*c*q+3*c-5*q**2+6*q+3
ck(sp.simplify(B.subs(q,qcrit)-4*(c+1)*(c*c+6*c+25)/(c+5)**2)==0,'critical slope')
sc=sp.factor((1+qcrit)**2*(5+c)/B.subs(q,qcrit))
ck(sp.simplify(sc-(c+3)**2*(c+5)/((c+1)*(c*c+6*c+25)))==0,'onset coefficient')

# Independently derive the profile from its two Cauchy/Lorentzian factors.
y,b=sp.symbols('y b',real=True)
Lm=1/(1+(y-b)**2)
Lp=1/(1+(y+b)**2)
profile=sp.factor(Lm**2+Lp**2+2*c*Lm*Lp)
model=2*N/D**2
ck(sp.simplify(profile-model.subs({q:b*b,t:y*y}))==0,'rational intensity identity')

# Direct quadrature of the STFT as defined, independently of the rational simplification.
rng=np.random.default_rng(10641)
for k in range(24):
    a=rng.uniform(.5,2.)
    w=rng.uniform(.2,2.)
    x=rng.uniform(-1.5,1.5)
    xi=rng.uniform(-2.5,2.5)
    def integrand(v):
        return 2*math.cos(w*v)*math.exp(-a*abs(v-x))*np.exp(-1j*xi*v)
    # integrate on both sides of the window cusp.
    re=quad(lambda v:integrand(v).real,-np.inf,x,epsabs=1e-10)[0]+quad(lambda v:integrand(v).real,x,np.inf,epsabs=1e-10)[0]
    im=quad(lambda v:integrand(v).imag,-np.inf,x,epsabs=1e-10)[0]+quad(lambda v:integrand(v).imag,x,np.inf,epsabs=1e-10)[0]
    numerical=abs(re+1j*im)**2
    formula=abs(2*a*(np.exp(1j*w*x)/(a*a+(xi-w)**2)+np.exp(-1j*w*x)/(a*a+(xi+w)**2)))**2
    ck(abs(numerical-formula)<3e-8*(1+abs(formula)),'STFT quadrature '+str(k))

# Coefficients and real positive roots: a non-exhaustive independent test of the global ridge classification.
fnfast=sp.lambdify((t,q,c),2*N/D**2,'numpy')
poly=sp.Poly(H,t)
coefffunc=sp.lambdify((q,c),poly.all_coeffs(),'numpy')
for k in range(3000):
    qq=10**rng.uniform(-3,2)
    cc=rng.uniform(-1,1)
    co=np.asarray(coefffunc(qq,cc),dtype=float)
    rr=np.roots(co)
    pos=sorted([r.real for r in rr if abs(r.imag)<1e-7*max(1,abs(r.real)) and r.real>1e-8])
    expected= 1 if qq>(1+cc)/(5+cc) else 0
    ck(len(pos)==expected,'critical root count '+str(k))
    if len(pos):
        u=pos[0]
        # finite difference derivative sign across positive root
        fn=lambda s:float(fnfast(s,qq,cc))
        d=min(u*.01,.002)
        ck(fn(u)>fn(u-d) and fn(u)>fn(u+d),'positive maximum '+str(k))
    else:
        fn=lambda s:float(fnfast(s,qq,cc))
        ck(fn(0)>fn(.01),'central maximum '+str(k))

# Two explicit endpoint phases.
for qq in [0.01,0.2,0.33,0.4,1.,3.,10.]:
    coeff=np.asarray(coefffunc(qq,-1.),dtype=float)
    roots=np.roots(coeff)
    root=max(r.real for r in roots if abs(r.imag)<1e-8 and r.real>0)
    exact=(qq-1+2*math.sqrt(qq*qq+qq+1))/3
    ck(abs(root-exact)<1e-8,'anti-phase peak')
    if qq>1./3:
        coeff=np.asarray(coefffunc(qq,1.),dtype=float)
        roots=np.roots(coeff)
        root=max(r.real for r in roots if abs(r.imag)<1e-7 and r.real>0)
        exact=2*math.sqrt(qq*(1+qq))-(1+qq)
        ck(abs(root-exact)<1e-8,'in-phase peak')

# Phase occupancy law in one beat period.
for qq in [.001,.01,.08,.2,.3,1/3,.6,2.]:
    analytic=1-math.acos((5*qq-1)/(1-qq))/math.pi if qq<1/3 else 1.0
    thetas=np.linspace(0,2*math.pi,30001,endpoint=False)
    observed=np.mean(qq>(1+np.cos(thetas))/(5+np.cos(thetas)))
    ck(abs(analytic-observed)<8e-5,'beat-phase measure '+str(qq))

# Leading small-gap bubble duty cycle.
for bb in [0.003,0.005,0.01]:
    qq=bb*bb
    duty=1-math.acos((5*qq-1)/(1-qq))/math.pi
    ck(abs(duty/bb-2*math.sqrt(2)/math.pi)<2e-4,'bubble asymptotic')
print('LAPLACE_STFT_CHECKS_PASSED',passed)
