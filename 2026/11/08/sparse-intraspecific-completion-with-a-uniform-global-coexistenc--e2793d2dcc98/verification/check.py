"""Reproducibility checks for sparse intraspecific coexistence completion."""
from fractions import Fraction as Q
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp

x,L,h,b=sp.symbols('x L h b', real=True)
q=(L-h)*x**2-L*x**3
assert sp.expand(q.subs(x,1)+h)==0
assert sp.expand(sp.diff(q,x)-(2*(L-h)*x-3*L*x**2))==0
assert sp.factor(q+L*x**2*(x-1)+h*x**2)==0
# Uniform bounds used in the proof: 9L/64 is the negative log-diagonal contribution.
assert Q(9,64)*32==Q(9,2)
assert Q(25,8)+Q(5,4)<Q(9,2)
assert Q(9,16)*32>Q(7,4)
assert Q(25,16)*32>Q(9,4)

r=np.array([-1.,-1.]); B=np.array([[-1.,1.],[1.,-1.]])
hh=r+B.sum(axis=1)
rho=np.abs(B).sum(axis=1)
H=np.max(np.abs(hh)+rho)
LL=32*(1+H)
alpha=LL-hh

def field(t,X):
    return X*(r+B@X+alpha*X**2-LL*X**3)
assert np.max(np.abs(field(0,np.ones(2))))<1e-12
J=B+np.diag(2*alpha-3*LL)
assert np.max(np.linalg.eigvalsh(J)) < -4.5
for x0 in [[.75,.75],[1.25,.75],[.75,1.25],[1.25,1.25],[.91,1.08]]:
    sol=solve_ivp(field,(0,0.1),x0,rtol=1e-11,atol=1e-12,dense_output=False)
    assert sol.success
    assert np.all(sol.y >= .75-1e-8) and np.all(sol.y <= 1.25+1e-8)
    assert np.linalg.norm(sol.y[:,-1]-1,np.inf)<np.linalg.norm(np.array(x0)-1,np.inf)
# In one species r=b=-1 and quadratic per-capita coefficient c>0,
# any positive equilibrium has g'(x*)=sqrt(1+4c)>0.
c=sp.symbols('c',positive=True)
xstar=(1+sp.sqrt(1+4*c))/(2*c)
assert sp.simplify(-1-xstar+c*xstar**2)==0
assert sp.simplify(-1+2*c*xstar-sp.sqrt(1+4*c))==0
print('VERIFY_OK exact_completion=1 exact_uniform_constants=4 example_positive_cube=5 quadratic_order_obstruction=1')
