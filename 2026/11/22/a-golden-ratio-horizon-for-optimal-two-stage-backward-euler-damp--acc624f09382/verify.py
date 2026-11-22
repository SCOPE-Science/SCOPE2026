"""Reproducibility checks for a two-stage backward-Euler Jordan-shear design.

Run: python verify.py  (Python 3.9+, NumPy and SymPy installed).
The theorem's global assertion is proved analytically; finite checks are supplementary.
"""
import math
import numpy as np
import sympy as sp

T, V, B = sp.symbols('T V B', positive=True, real=True)
D = 1 + T + V
# Product of two resolvents in the unit-decay normalization.
W, Z = sp.symbols('W Z', nonnegative=True, real=True)
J = sp.Matrix([[0, 1], [0, 0]])
A = sp.eye(2) - B*J
R1 = (sp.eye(2) + W*A).inv()
R2 = (sp.eye(2) + Z*A).inv()
prod = sp.simplify(R1*R2)
expected = sp.Matrix([[1/((1+W)*(1+Z)), B*(W+Z+2*W*Z)/((1+W)**2*(1+Z)**2)], [0,1/((1+W)*(1+Z))]])
assert sp.simplify(prod-expected) == sp.zeros(2)
# Endpoint crossing polynomial and the exact critical shear expression.
c = 1+T/2; d = 1+T
assert sp.simplify(c**3-d**2-T*(T**2-2*T-4)/8) == 0
bt2 = (T*T+8*T+8)**2/(8*(T+2)*(4+2*T-T*T))
n2 = (1-1/c)/(d*d-c**3)
y2 = sp.factor(n2*d**4-2*d*d+1/n2)
assert sp.simplify(y2/T**2-bt2)==0
# For the Jordan shear, the exact 2-norm of [[1/D, beta*(T+2V)/D^2],[0,1/D]]:
def formula(t, beta, v):
    dd = 1+t+v
    return (math.hypot(2*dd, beta*(t+2*v))+beta*(t+2*v))/(2*dd**2)
def raw_matrix(t,beta,v):
    disc = max(0,t*t-4*v)**0.5
    w,z=(t+disc)/2,(t-disc)/2
    a=np.array([[-1.0,beta],[0.,-1.]])
    P=np.linalg.inv(np.eye(2)-w*a) @ np.linalg.inv(np.eye(2)-z*a)
    return np.linalg.svd(P,compute_uv=False)[0]
for t in [.003,.025,.1,.5,1.,2.,3.,5.,10.]:
    for beta in [0.,.2,.999,1.,1.5,2.,5.,40.]:
        for v in np.linspace(0,t*t/4,101):
            f=formula(t,beta,float(v))
            assert abs(f-raw_matrix(t,beta,float(v)))<2e-12*max(1,f)
            assert f+2e-12 >= min(formula(t,beta,0),formula(t,beta,t*t/4))
# Sharp threshold and uniqueness: strict endpoint comparison on either side.
critical = 1+math.sqrt(5)
for t in [.01,.1,.3,.8,1.,1.9,3.,3.22]:
    threshold=(t*t+8*t+8)/math.sqrt(8*(t+2)*(4+2*t-t*t))
    f0=lambda b:formula(t,b,0)
    fe=lambda b:formula(t,b,t*t/4)
    assert abs(f0(threshold)-fe(threshold))<2e-12
    assert fe(.9*threshold)<f0(.9*threshold)
    assert f0(1.1*threshold)<fe(1.1*threshold)
for t in [critical,3.5,5.,10.,40.]:
    for beta in [0.,.25,1.,10.,100.,10000.]:
        assert formula(t,beta,t*t/4)<formula(t,beta,0)
# Stable but nonnormal shear exhibits the sparse-step optimum.
t,beta=.5,1.5
assert beta<2 and formula(t,beta,0)<formula(t,beta,t*t/4)
print('PASS: symbolic identities, 7,272 independent matrix-norm comparisons, endpoint global checks and threshold tests')
print('example t=0.5 beta=1.5:',format(formula(t,beta,0),'.12f'),format(formula(t,beta,t*t/4),'.12f'))
