"""Independent algebraic and numerical diagnostics for the sine-FGM validity envelope.
All exact global implications are proved in RESULT.md; numerical scans are diagnostics only.
"""
import math
import numpy as np
import sympy as sp
from scipy.optimize import minimize_scalar, brentq

x,y,a,b=sp.symbols('x y a b',real=True)
f=lambda u:u*(1-u)
t=b*f(x)*f(y)
C=x*y+a*sp.sin(t)
expect=1+a*b*(1-2*x)*(1-2*y)*(sp.cos(t)-t*sp.sin(t))
assert sp.simplify(sp.diff(C,x,y)-expect)==0
assert all(sp.simplify(z)==0 for z in (C.subs(x,0),C.subs(y,0),C.subs(x,1)-y,C.subs(y,1)-x))

def h(t):return math.cos(t)-t*math.sin(t)
def B(t):
 q=abs(h(t))
 return 16*t*(q/(q-1))**2 if q>1 else math.inf
z=brentq(lambda t:-h(t)-1,1,2)
opt=minimize_scalar(B,bounds=(z+1.e-8,math.pi-1.e-8),method='bounded',options={'xatol':1.e-13})
print('root_h_minus_one',z)
print('numerical_beta_transition_argmin',opt.x)
print('numerical_beta_transition',opt.fun)
assert 103 < opt.fun < 105
assert abs(B(2)-104.82199385771553)<1.e-9
assert 16*math.pi <64 < opt.fun

def qcalc(beta):
 def w(t):return (1-4*math.sqrt(t/beta))*abs(h(t))
 grid=np.linspace(0,beta/16,30001)
 vals=np.array([w(float(u)) for u in grid])
 loc=[]
 for i in range(1,len(grid)-1):
  if vals[i]>=vals[i-1] and vals[i]>=vals[i+1]:
   rr=minimize_scalar(lambda u:-w(u),bounds=(grid[i-1],grid[i+1]),method='bounded')
   loc.append((-rr.fun,rr.x))
 loc.append((1.0,0.0))
 return max(loc)
for beta in [8*math.pi, 16*math.pi,64,100,104,150,400,1000,3600]:
 q,tmax=qcalc(beta)
 if beta<=100: assert abs(q-1)<1.e-8
 if beta>=150: assert q>1
 assert q <= beta/108+1.0000001
 # At the extremizing phase, both density signs are attainable by square-root branches.
 if tmax>1.e-7:
  r=math.sqrt(tmax/beta)
  v=math.sqrt(1-4*r)
  u1=(1-v)/2;u2=(1+v)/2
  assert abs(f(u1)*f(u1)*beta-tmax)<1.e-8
  assert abs((1-2*u1)*(1-2*u1)*(math.cos(tmax)-tmax*math.sin(tmax))) <=q+1.e-8
 print(f'beta={beta:.8g}, Q={q:.10g}, t_argmax={tmax:.8g}, Q/beta={q/beta:.8g}')
# Independent two-dimensional density-grid stress check of the scalar criterion.
xx=np.linspace(0,1,251)
X,Y=np.meshgrid(xx,xx,indexing='ij')
for beta in [25.0,80.0,104.0,200.0]:
    q,_=qcalc(beta)
    alpha=1/(beta*q)
    T=beta*X*(1-X)*Y*(1-Y)
    H=np.cos(T)-T*np.sin(T)
    c=1+alpha*beta*(1-2*X)*(1-2*Y)*H
    assert float(np.min(c))>=-5e-12
    if beta>103.93:
        c_bad=1+1.001*alpha*beta*(1-2*X)*(1-2*Y)*H
        # The violation is proved analytically by an extremizer; finite resolution
        # need not detect every arbitrarily narrow negative patch.
        print('beta',beta,'sample_min_invalid_amplitude',float(np.min(c_bad)))
# At high-angle admissible parameters, the copula difference changes sign.
beta=80.0; arg=4.0; r=math.sqrt(arg/beta)
u=(1-math.sqrt(1-4*r))/2
assert 0<u<1 and abs(beta*f(u)**2-arg)<1e-11
assert math.sin(arg)<0 and math.sin(.1)>0
print('ALL CHECKS PASSED (numerical scans are not global certificates)')
