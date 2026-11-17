"""Standalone diagnostic checks for a deterministic adaptive-oscillator passage law."""
import math
import sympy as s
import numpy as np
from scipy.integrate import solve_ivp
v,k,eps=s.symbols('v k eps', positive=True)
vprime=k*v*(2-v)
kprime=eps*(v-k)
H=s.exp(-2*k/eps)/v
rhs=s.simplify(s.diff(H,v)*vprime+s.diff(H,k)*kprime)
assert s.simplify(rhs+(2-k)*s.exp(-2*k/eps))==0
# Elementary logarithmic integrals and squared-coupling balance
logit=s.log(v/(2-v))
assert s.simplify(s.diff(logit,v)*vprime-2*k)==0
S=k*k/(2*eps)
assert s.simplify(s.diff(S,k)*kprime-(v*k-k*k))==0
print('symbolic identities: PASS')

def passage(epsilon, k0, v0, target):
    def f(t,y):
        v,k=y
        return (k*v*(2-v), epsilon*(v-k))
    def event(t,y): return y[0]-target
    event.terminal=True; event.direction=1
    leading=math.exp(-2*k0/epsilon)/(2*v0)
    cap=10*max(leading,1)+1000
    sol=solve_ivp(f,(0,cap),(v0,k0),events=event,rtol=2e-11,atol=2e-13,method='DOP853',max_step=2.0)
    assert sol.success and len(sol.t_events[0])==1, 'passage event was not reached'
    T=float(sol.t_events[0][0]); kt=float(sol.y_events[0][0,1])
    universal=(.25+1/epsilon)*math.log(1/v0)
    return (T,leading,universal, T-leading-universal, kt)

for epsilon,k0,target in [(1.0,0.0,.5),(.8,.4,.4),(2.0,-.5,.75)]:
    print('params',epsilon,k0,target)
    vals=[]
    for v0 in [1/80,1/160,1/320,1/640,1/1280]:
        T,L,G,R,kt=passage(epsilon,k0,v0,target)
        vals.append(R)
        print(' ',f'v0={v0:.8f} T={T:.8f} leading={L:.8f} log={G:.8f} residual={R:.7f} k_at_exit={kt:.5f}')
    assert abs(vals[-1]-vals[-2])<.15
print('finite numerical diagnostics: PASS')
