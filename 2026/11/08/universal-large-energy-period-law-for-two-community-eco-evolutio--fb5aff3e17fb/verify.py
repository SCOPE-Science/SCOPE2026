"""Symbolic arithmetic and numerical replay of the stated 3D eco-evolutionary reduction.
This script tests exact transformed-field identities and provides finite numerical diagnostics;
the asymptotic period theorem is proved analytically in RESULT.md.
"""
import math
import sympy as s
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from scipy.special import expit
import numpy as np

a,b,theta,z=s.symbols('a b theta z',positive=True)
w=(b+a*z)/(1+z)
q=(theta*z-1)/(1+z)
Fp=(theta*z-1)/(b+a*z)
assert s.simplify(Fp*w-q)==0
assert s.simplify(z*s.diff(Fp,z)-z*(a+theta*b)/(b+a*z)**2)==0
assert s.simplify(s.limit(Fp,z,0)+1/b)==0
assert s.simplify(s.limit(Fp,z,s.oo)-theta/a)==0

# Check that the payoff difference from the reversal-symmetric 2x2 game is
# exactly w(x)(1-2e) for every mixture e of within/across environments.
x,e=s.symbols('x e',real=True)
T,R,P,S=s.symbols('T R P S',real=True)
A0=s.Matrix([[T,P],[R,S]])
A1=s.Matrix([[R,S],[T,P]])
A=(1-e)*A0+e*A1
p=A*s.Matrix([x,1-x])
expected=(1-2*e)*((P-S)+(T-R-P+S)*x)
assert s.simplify(p[0]-p[1]-expected)==0

A_,B_,th,de,c=2.,1.,2.,1./3.,math.log(3.)
softplus=lambda u: np.logaddexp(0.,u)
w_num=lambda u:B_+(A_-B_)*expit(u)
q_num=lambda u:(1+th)*expit(u)-1.
M=lambda v:(1-de)*expit(v)+de*expit(v-c)
F=lambda u:-u/B_+(th/A_+1/B_)*np.logaddexp(math.log(B_),math.log(A_)+u)
G=lambda v:2*(1-de)*softplus(v)+2*de*softplus(v-c)-v
u0=-math.log(th)
v0=brentq(lambda v:M(v)-.5,-15.,15.)
H0=F(u0)+G(v0)
assert abs(q_num(u0))<1e-14
assert abs(2*M(v0)-1)<1e-12

computed=[]
for E in [5.,20.,80.,160.]:
    uprime=brentq(lambda u:F(u)-F(u0)-E,u0,u0+E*A_/th+20)
    def rhs(t,y):
        u,v=y
        return [w_num(u)*(1-2*M(v)),q_num(u)]
    def event(t,y): return y[1]-v0
    event.direction=1
    event.terminal=False
    # Starting at right-hand turning point, the first UPward crossing of v=v0
    # after a complete revolution is the period.
    sol=solve_ivp(rhs,(0,2*(1+1/th)*E+100.),[uprime,v0],rtol=3e-11,
        atol=1e-11,events=event,max_step=.2)
    valid_events=[float(t) for t in sol.t_events[0] if t>1e-6]
    assert sol.success and valid_events
    T=valid_events[0]
    assert T>1
    drift=float(np.max(np.abs(F(sol.y[0])+G(sol.y[1])-H0-E)))
    assert drift<1e-7, (E,drift)
    computed.append((E,T,T/E,drift))
assert abs(computed[-1][2]-3.)<.07
for E,T,ratio,drift in computed:
    print(f'E={E:.0f} T={T:.9f} T/E={ratio:.9f} conservation_error={drift:.2e}')
print('VERIFY_OK')
