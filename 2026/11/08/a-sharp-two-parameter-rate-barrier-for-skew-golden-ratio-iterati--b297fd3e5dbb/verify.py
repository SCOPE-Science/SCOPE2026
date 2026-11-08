"""Exact identities and supplementary finite tests for skew GRAAL rate tuning.

Run: python verify.py. Requires sympy; numpy is used for independent numerical diagnostics.
The universal theorem follows from the analytic argument in RESULT.md, not from a finite grid.
"""
from fractions import Fraction
import math
import sympy as s
import numpy as np

q,u=s.symbols('q u', positive=True, real=True)
F=s.expand((1-u/q)**2+(u/q**2)*(1-q)**2-s.Rational(1,2)*(1-u)**2)
G=u*(1+u)*(1/q-2/(1+u))**2+(1-u)**3/(2*(1+u))
assert s.simplify(F-G)==0
assert s.simplify(F.subs({q:1,u:1}))==0

# Check the polynomial coefficients and exact double root.
z=s.symbols('z')
i=s.I
P=z**2-(1-i)*z-i/s.Integer(2)
r=(1-i)/2
assert s.expand(P-(z-r)**2)==0

# Exact initialization and recurrence on the rotation mode.
w0=s.Integer(1)
w1=1-i
vals=[w0,w1]
for k in range(1,30):
    vals.append(s.expand((1-i)*vals[-1]+i*vals[-2]/2))
for k,val in enumerate(vals):
    assert s.simplify(val-(k+1)*r**k)==0

# Strictly positive certificates for a representative rational grid away from equality.
checks=0
for cnum in range(11,60):
    c=s.Rational(cnum,10)
    qv=s.Rational(2,1)/c
    for tnum in range(1,32):
        tau=s.Rational(tnum,20)
        uv=s.factor((qv*tau)**2)
        if uv<=1:
            ff=s.factor(F.subs({q:qv,u:uv}))
            assert ff>=0
            assert ff>0 or (c==2 and tau==1)
            checks+=1

# Spectral check across a two-parameter grid, independent of the certificate.
num=0
for c in np.linspace(1.01,5.0,96):
    for tau in np.linspace(0.012,3.0,95):
        eig=np.roots([1, -1+1j*tau, -1j*tau/c])
        assert np.max(np.abs(eig)) >= 1/math.sqrt(2)-5e-13
        num+=1

# Rotation-isometry identity for a nontrivial block direct sum in dimension 6.
J2=np.array([[0.,-1.],[1.,0.]])
J=np.kron(np.eye(3),J2)
init=np.array([1.,-.75,2.,3.,-.4,.25]); prev=init.copy(); x=(np.eye(6)-J)@init
for k in range(1,21):
    theta=k*math.pi/4
    rhs=(k+1)*(2**(-k/2))*(math.cos(theta)*np.eye(6)-math.sin(theta)*J)@init
    assert np.allclose(x,rhs,atol=1e-10)
    nxt=(np.eye(6)-J)@x+0.5*J@prev
    x,prev=nxt,x
assert max([(k+1)*2**(-k/2) for k in range(40)])==1.5
print('PASS: exact sympy identities, %d rational certificates, %d independent spectral-grid cases, 20 block-isometry steps.'%(checks,num))
