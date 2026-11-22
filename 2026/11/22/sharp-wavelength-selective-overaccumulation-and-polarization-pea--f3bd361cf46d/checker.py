"""Independent algebraic and Fourier-resolvent checks for delay-selective active response.
Run: python checker.py
Requires: numpy, scipy, sympy.
"""
import math
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.linalg import expm

a,t,K,v=sp.symbols('a t K v', positive=True, real=True)
Q=1+2*a*t+K**2*t**2
H=(1+4*a*t)/Q
P=t/Q
assert sp.simplify((H-1)-t*(2*a-K**2*t)/Q)==0
assert sp.simplify(sp.diff(P,t)-(1-K**2*t**2)/Q**2)==0
assert sp.simplify(sp.diff(H,t)-(2*a-2*K**2*t-4*a*K**2*t**2)/Q**2)==0
opt=(sp.sqrt(1+8*a*a/K**2)-1)/(4*a)
assert sp.simplify((2*a-2*K**2*opt-4*a*K**2*opt**2))==0
assert sp.simplify(H.subs(t,0)-1)==0

for alpha in (0.3,1.0,3.0):
  for v0 in (0.7,1.2):
    for k in (0.5,1.0,2.0):
      for tau in (0.15,0.4,1.0,2.5):
        eta=1.0/tau
        # Matrix-resolvent route for state-weighted memory Fourier amplitudes.
        A=np.array([[eta+alpha+1j*k*v0,-alpha],[-alpha,eta+alpha-1j*k*v0]],complex)
        source=np.array([eta/4,eta/4],complex) # cos(kx) Fourier coefficient 1/2, state mass 1/2
        b=np.linalg.solve(A,source)
        B=b.sum(); BD=b[0]-b[1]
        S=np.array([[alpha+1j*k*v0,-alpha],[-alpha,alpha-1j*k*v0]],complex)
        d=np.linalg.solve(S,-1j*k*np.array([b[0],-b[1]]))
        expected_density=-.5/v0*(1+4*alpha*tau)/(1+2*alpha*tau+(k*v0*tau)**2)
        expected_polar=1j*k*.5*tau/(1+2*alpha*tau+(k*v0*tau)**2)
        assert abs(d.sum()-expected_density)<2e-12, (d,expected_density)
        assert abs(d[0]-d[1]-expected_polar)<2e-12, (d,expected_polar)
        # Independent telegraph characteristic function integral.
        # phi solves phi''+2alpha phi'+(kv0)^2 phi=0, phi(0)=1, phi'(0)=0.
        Qgen=np.array([[0.,1.],[-(k*v0)**2,-2*alpha]])
        val=quad(lambda s: eta*math.exp(-eta*s)*expm(Qgen*s)[0,0],0,max(60.0/eta,40.0/alpha),epsabs=2e-10)[0]
        assert abs(val*0.5-B)<1e-8,(alpha,k,tau,val,B)
print('PASS: 72 parameter sets; independent Fourier resolvent and telegraph Green-function integration; symbolic thresholds and unique optimizers')
