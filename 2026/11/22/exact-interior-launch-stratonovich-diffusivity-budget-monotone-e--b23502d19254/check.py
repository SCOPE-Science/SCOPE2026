"""Reproduce the exact algebraic identities and numerical consistency checks.

Requires Python 3, SymPy, SciPy. Execute with python check.py.
"""
import math
import random
import sympy as sp
from scipy.optimize import minimize_scalar, brentq

z,a,b=sp.symbols('z a b', positive=True)
K=z**3+z-1
A=(z**3-1)/K
B=z/K
ratio=(2*z**3-1)**2/(z*(2*z**3+z-2)*K)
Tstar=(2*z**3-1)**2/(2*K**3)
assert sp.simplify(A+B-1)==0
assert sp.simplify(B*(z**3-1)-A*z)==0
assert sp.simplify(sp.diff(A,z)-(2*z**3+1)/K**2)==0
F=sp.factor(sp.diff(ratio,z))
expected=-(z-1)**2*(2*z**3-1)*(2*z**3+1)*(2*z**4+4*z**3+3*z**2+2*z-2)/(z**2*K**2*(2*z**3+z-2)**2)
assert sp.simplify(F-expected)==0
M=(a+b*z**2)*(a*b/z+b*b/(2*z*z))
assert sp.simplify(sp.diff(M,z)-a*b*(b*z**3-a*z-b)/z**3)==0
assert sp.simplify(M.subs({a:A,b:B})-Tstar)==0
assert sp.simplify(Tstar/((1-A**2)/2)-ratio)==0
assert sp.limit((1-ratio)/A**3,z,1,dir='+')==sp.Rational(1,3)
assert sp.limit(ratio/sp.sqrt(B),z,sp.oo)==2
assert sp.limit(z**3/(2*z**3-1),z,sp.oo)==sp.Rational(1,2)
# Independent numerical minimization and a discrete test of Jensen's reduction.
rng=random.Random(1147)
for q in [0.001,0.01,0.05,0.1,0.2,0.35,0.5,0.7,0.85,0.95,0.99]:
    a0=q; b0=1-q
    root=brentq(lambda x:b0*x**3-a0*x-b0, 1, 1/max(1e-6,b0)**2)
    c0=a0+b0*root*root
    d_in=1/c0; d_out=root*root/c0
    calculated=c0*(a0*b0/root+b0*b0/(2*root*root))
    direct=a0*b0/math.sqrt(d_in*d_out)+b0*b0/(2*d_out)
    opt=minimize_scalar(lambda v:(a0+b0*v*v)*(a0*b0/v+b0*b0/(2*v*v)),bounds=(0.5,root*3+10),method='bounded',options={'xatol':1e-13})
    assert abs(root-opt.x)<1e-4
    assert math.isclose(calculated,direct,rel_tol=1e-12)
    assert math.isclose(calculated,opt.fun,rel_tol=1e-10)
    assert calculated < (1-a0*a0)/2
    for _ in range(30):
        n=12
        v1=[math.exp(rng.uniform(-3,3)) for k in range(n)]
        v2=[math.exp(rng.uniform(-3,3)) for k in range(n)]
        scale=(a0*sum(v1)/n+b0*sum(v2)/n)
        v1=[w/scale for w in v1]
        v2=[w/scale for w in v2]
        l1=a0*sum(1/math.sqrt(w) for w in v1)/n
        l2=b0*sum(1/math.sqrt(w) for w in v2)/n
        T=l1*l2+l2*l2/2
        assert T+1e-10 >= calculated
print('PASS: exact rational identities, 11 independent numerical optimizations, 330 heterogeneous budget checks, endpoints')
