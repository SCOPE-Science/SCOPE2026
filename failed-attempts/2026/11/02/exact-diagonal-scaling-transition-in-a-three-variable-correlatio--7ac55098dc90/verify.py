"""Reproducibility checks for the explicit 3x3 diagonal congruence optimum.

Only finite checks and exact identities are computationally verified;
the global minimax and asymptotic claims are proved in RESULT.md.
"""
import math
import numpy as np
import sympy as sp
from scipy.optimize import minimize

T, S, U = sp.symbols('T S U', positive=True)
A = sp.Matrix([[1,T,S], [T,1,S], [S,S,1]])
D = sp.diag(sp.sqrt(U), sp.sqrt(U), 1)
B = D*A*D
F = sp.Matrix([[sp.sqrt(2)/2, sp.sqrt(2)/2,0],
               [0,0,1],
               [sp.sqrt(2)/2,-sp.sqrt(2)/2,0]])
M = sp.simplify(F*B*F.T)
assert sp.simplify(M[0,0]-(1+T)*U)==0
assert sp.simplify(M[0,1]-sp.sqrt(2)*S*sp.sqrt(U))==0
assert sp.simplify(M[1,1]-1)==0
assert sp.simplify(M[2,2]-(1-T)*U)==0
assert all(sp.simplify(M[i,2])==0 for i in (0,1))
blk = M[:2,:2]
a = (1-T)*U
assert sp.simplify((blk-a*sp.eye(2)).det() - 2*U*(T-S**2-T*(1-T)*U))==0
uc = (T-S**2)/(T*(1-T))
u0 = 1/(1+T)
assert sp.simplify((uc-u0)*T*(1-T)*(1+T) - (2*T**2-S**2*(1+T)))==0
kw = sp.factor((1+2*T*uc)/((1-T)*uc))
assert sp.simplify(kw-T*(1+T-2*S**2)/((1-T)*(T-S**2)))==0
threshold = 2*T**2/(1+T)
kstr = sp.sqrt(2)*S/sp.sqrt(1+T)
assert sp.simplify(kw.subs(S, sp.sqrt(threshold)) - ((1+kstr)/(1-kstr)).subs(S,sp.sqrt(threshold))) == 0

# A rational example in the boundary-eigenvalue regime.
tr = sp.Rational(9,10); sr=sp.Rational(4,5)
uopt = sp.factor(uc.subs({T:tr,S:sr}))
kr=sp.factor(kw.subs({T:tr,S:sr}))
assert uopt==sp.Rational(26,9) and kr==sp.Rational(279,13)
Ae=A.subs({T:tr,S:sr})
assert sp.simplify(Ae.det())>0
Dopt=sp.diag(sp.sqrt(uopt),sp.sqrt(uopt),1)
lam=(Dopt*Ae*Dopt).eigenvals()
assert lam == {sp.Rational(13,45):2, sp.Rational(31,5):1},lam
vals=sorted([float(v) for v in lam])
assert abs(vals[-1]/vals[0]-float(kr))<1e-10

# Asymptotic ratio: along t=1-e^2, s=sqrt(1-e), the weak-regime optimum
# is (2+e-e^2)/e^2, and Jacobi's largest eigenvalue / e^2 is asymptotic.
e=sp.symbols('e', positive=True)
ua=sp.factor(uc.subs({T:1-e**2, S:sp.sqrt(1-e)}))
ka=sp.factor(kw.subs({T:1-e**2,S:sp.sqrt(1-e)}))
assert sp.simplify(ka-(2+e-e**2)/e**2)==0
jac_top = (3-e**2+sp.sqrt(9-8*e-2*e**2+e**4))/2
assert sp.limit(jac_top/(e**2*ka),e,0,dir='+')==sp.Rational(3,2)

# 160 parameter pairs: exact formula vs sampled asymmetric optimization.
rng=np.random.default_rng(350027)
passed=0
for i in range(160):
    t=float(rng.uniform(.02,.97))
    s=float(rng.uniform(.01, .99*math.sqrt((1+t)/2)))
    A0=np.array([[1,t,s],[t,1,s],[s,s,1.]],dtype=float)
    u=(t-s*s)/(t*(1-t)) if s*s<2*t*t/(1+t) else 1/(1+t)
    k=t*(1+t-2*s*s)/((1-t)*(t-s*s)) if s*s<2*t*t/(1+t) else (1+math.sqrt(2)*s/math.sqrt(1+t))/(1-math.sqrt(2)*s/math.sqrt(1+t))
    d=np.diag([math.sqrt(u),math.sqrt(u),1.])
    v=np.linalg.eigvalsh(d@A0@d)
    assert abs(v[-1]/v[0]/k-1)<1.e-9
    def score(x):
        z=np.exp(np.r_[x,0.]);m=(z[:,None]*A0)*z[None,:]
        vals=np.linalg.eigvalsh(m)
        return math.log(vals[-1]/vals[0])
    x=np.array([.5*math.log(u),.5*math.log(u)])
    for seed in ([0.,0.],[1.,-1.],[-1.,1.],list(x)):
        r=minimize(score,np.array(seed),method='Nelder-Mead',options={'maxiter':650,'xatol':3e-9,'fatol':2e-11})
        assert r.fun>=math.log(k)-1e-7, (t,s,r.fun,math.log(k))
    passed+=1
print(f'VERIFY_OK symbolic=8 exact_example=1 asymptotic=1 global_numeric_cases={passed} minimizations={passed*4}')
