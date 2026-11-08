"""Reproduce exact algebra and numerical illustrations for a two-trait SIR model.
Requires scipy and sympy. Numerical checks illustrate, not certify, all-time statements.
"""
from fractions import Fraction as Q
import math
import sympy as sp
from scipy.integrate import solve_ivp

s, low, high, k, mu, nu = sp.symbols('s low high k mu nu', positive=True)
p = sp.symbols('p', positive=True)
L,H=sp.symbols('L H', positive=True)
i=L+H
x=H/i
SD=-k*s*(low*L+high*H)
LD=(k*low*s-mu)*L+nu*(H-L)
HD=(k*high*s-mu)*H+nu*(L-H)
xd=sp.diff(x,L)*LD+sp.diff(x,H)*HD
assert sp.simplify(xd-(k*(high-low)*s*x*(1-x)+nu*(1-2*x)))==0
assert sp.simplify(LD+HD-(k*s*(low*L+high*H)-mu*i))==0
assert sp.simplify(SD+(LD+HD)+mu*i)==0

# Exact-rational positive initial derivative and sharp root ordering.
s0=Q(9,10); x0=Q(7,10); K=Q(10); N=Q(1,10)
F0=K*s0*x0*(1-x0)+N*(1-2*x0)
assert F0==Q(37,20),F0
assert N*(1-2*x0)+Q(1,10)*x0*(1-x0)<0
# f(99/100)>0 because exp(99/20)>90, proved by six Taylor terms.
t=Q(99,20)
assert sum((t**j)/math.factorial(j) for j in range(7))>90
assert 1-Q(99,100)-Q(9,10)/90==0

def fun(t,y,k,mu,nu,low,high):
    S,L,H,R=y
    return [-k*S*(low*L+high*H),
            (k*low*S-mu)*L+nu*(H-L),
            (k*high*S-mu)*H+nu*(L-H),
            mu*(L+H)]

sol=solve_ivp(fun,(0,120),(0.9,0.03,0.07,0.0),args=(10,1,0.1,0,1),rtol=1e-11,atol=1e-13,dense_output=True,max_step=.025)
assert sol.success
T=sol.t; S,IL,IH,R=sol.y
X=IH/(IL+IH)
F=10*S*X*(1-X)+0.1*(1-2*X)
changes=[j for j in range(len(F)-1) if F[j]>0 and F[j+1]<0]
assert len(changes)==1,len(changes)
assert X[changes[0]]>0.7
assert X[-1]<0.7 and S[-1]<.01 and R[-1]>.99
assert abs((S+IL+IH+R-1)).max()<1e-9
assert abs( (10*S*X*(1-X)+.1*(1-2*X))[0]-float(F0))<1e-12
A=10*S[-1]
y=(A-0.2+math.sqrt(A*A+.04))/(2*A)
assert abs(X[-1]-y)<2e-7,(X[-1],y)
print('symbolic identities: 3 passed')
print('exact inequalities: 4 passed')
print('numerical trajectory: one stationary maximum at time in',T[changes[0]],T[changes[0]+1]); print('x_peak', X[changes[0]], 'x_final',X[-1], 's_final',S[-1], 'r_final',R[-1], 'equilibrium_root',y)
print('all checks passed')
