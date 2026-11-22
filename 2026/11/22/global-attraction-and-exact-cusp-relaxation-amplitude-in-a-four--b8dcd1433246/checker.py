#!/usr/bin/env python3
"""Exact symbolic checks and supplementary integrations for a four-compartment cusp."""
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp

c = sp.symbols('c', real=True)
g = 1/(1+128*c**3)
h = c*g
F = sp.Rational(9,2)*h + sp.Rational(3,2)*c-sp.Rational(3,4)
c0 = sp.Rational(1,4)
assert sp.simplify(F - 3*(4*c-1)**3*(4*c+1)/(4*(1+128*c**3))) == 0
assert sp.simplify(sp.diff(F,c) - 6*(1-64*c**3)**2/(1+128*c**3)**2) == 0
assert [sp.simplify(sp.diff(h,c,j).subs(c,c0)) for j in range(4)] == [sp.Rational(1,12),-sp.Rational(1,3),0,sp.Rational(128,3)]
assert sp.diff(F,c,3).subs(c,c0)==192
s,C,b,t=sp.symbols('s C b t',real=True)
gC=g.subs(c,C);hC=h.subs(c,C);hprime=sp.diff(h,c).subs(c,C);FC=F.subs(c,C)
G=sp.Matrix([-sp.Rational(15,4)*s+sp.Rational(3,4)*(1-C-b-t),s-hC,s-gC*b,s-t])
X=sp.Matrix([s,C,b,t]);X0=sp.Matrix([sp.Rational(1,12),sp.Rational(1,4),sp.Rational(1,4),sp.Rational(1,12)])
J=G.jacobian(X).subs(dict(zip(X,X0)))
L=sp.symbols('L')
assert sp.factor(J.charpoly(L).as_expr())==L*(3*L+1)*(12*L**2+53*L+53)/36
q=sp.Matrix([-sp.Rational(1,3),1,1,-sp.Rational(1,3)])
assert J*q==sp.zeros(4,1)
v=s-hC;y=t-hC;z=b-C
vp=-(sp.Rational(15,4)+hprime)*v-FC-sp.Rational(3,4)*(z+y)
yp=(1-hprime)*v-y
zp=-gC*z
assert sp.simplify(G[1]-v)==0
assert sp.simplify(sum(sp.diff(v,x)*gx for x,gx in zip(X,G))-vp)==0
assert sp.simplify(sum(sp.diff(y,x)*gx for x,gx in zip(X,G))-yp)==0
assert sp.simplify(sum(sp.diff(z,x)*gx for x,gx in zip(X,G))-zp)==0
# The critical center equation is u'=a u^3+..., y=b u^3+...
a,beta=sp.symbols('a beta')
d0=sp.Rational(41,12)
sol=sp.solve([d0*a+32+sp.Rational(3,4)*beta,beta-sp.Rational(4,3)*a],(a,beta))
assert sol[a]==-sp.Rational(384,53)
assert sp.simplify(1/(-2*sol[a])-sp.Rational(53,768))==0
# Strict Lyapunov derivative, using U'(c)=F(c):
Vdot=FC*v+v*vp+sp.Rational(3,4)*y*yp+64*z*zp
expected=-(sp.Rational(15,4)+hprime)*v**2-sp.Rational(3,4)*y**2-64*gC*z**2-sp.Rational(3,4)*hprime*v*y-sp.Rational(3,4)*v*z
assert sp.simplify(Vdot-expected)==0

# Supplementary numerical tail convergence: not a proof.
def rhs(time, state):
 S,cc,B,T=state
 gg=1/(1+128*cc**3)
 return [-3.75*S+0.75*(1-cc-B-T),S-gg*cc,S-gg*B,S-T]
limit=float(sp.sqrt(sp.Rational(53,768)))
for initial, sign in [([.15,.30,.30,.10],1),([.15,.20,.20,.10],-1)]:
 ans=solve_ivp(rhs,(0,30000),initial,method='BDF',rtol=2e-10,atol=2e-12,t_eval=[1000,3000,10000,30000])
 assert ans.success
 empirical=np.sqrt(ans.t)*(ans.y[1]-.25)
 assert abs(empirical[-1]-sign*limit)<.012
 print('tail:',initial,'scaled car displacements:',[round(v,7) for v in empirical])
print('Exact symbolic identities and local critical normal form: PASS')
