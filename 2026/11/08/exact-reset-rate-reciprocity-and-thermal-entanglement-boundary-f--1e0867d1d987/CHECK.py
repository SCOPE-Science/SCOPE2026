#!/usr/bin/env python3
"""Standalone algebraic and matrix checks of a two-qubit reset model.

Python 3 with numpy and sympy. Finite checks supplement, not replace, the proof.
"""
from fractions import Fraction as F
import math
import numpy as np
import sympy as sp

checks = 0

def assert_check(condition, message=''):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

J, r, Gamma, delta, h = sp.symbols('J r Gamma delta h', positive=True, real=True)
D = r*(r+Gamma)+4*J**2
z = r*(r+Gamma)*delta / D
y = J*r*delta / D
assert_check(sp.cancel(r*(delta-z)-4*J*y)==0, 'population stationary balance')
assert_check(sp.cancel(J*z-(r+Gamma)*y)==0, 'coherence stationary balance')
assert_check(sp.simplify(sp.diff(J*r*delta/D, r) - J*delta*(4*J**2-r**2)/D**2)==0, 'first derivative')
assert_check(sp.simplify(sp.diff(J*r*delta/D,r).subs(r,2*J))==0,'optimum rate')
assert_check(sp.simplify((J*r*delta/D).subs(r,2*J)-J*delta/(Gamma+4*J))==0,'peak height')

# The two positive boundaries, when they exist, are roots of the same quadratic.
Fabs = sp.symbols('Fabs', positive=True)
q = h*r*r+(h*Gamma-Fabs)*r+4*h*J*J
assert_check(sp.simplify(sp.discriminant(q,r)-((Fabs-h*Gamma)**2-16*h*h*J*J))==0,'root discriminant')
assert_check(sp.simplify(q.subs(r,2*J)-2*J*(h*(4*J+Gamma)-Fabs))==0,'tangency')

s, eta = sp.symbols('s eta', positive=True)
sc = ((6+eta)-sp.sqrt(eta**2+8*eta+20))/(2*(4+eta))
thermal = 1-2*s-(4+eta)*s*(1-s)
assert_check(sp.simplify(thermal.subs(s,sc))==0,'critical population')
assert_check(sp.simplify(sc.subs(eta,0)-(3-sp.sqrt(5))/4)==0,'noiseless critical population')

I=np.eye(2,dtype=complex)
Z=np.diag([1,-1])
Z1=np.kron(Z,I)
Z2=np.kron(I,Z)
sy=np.array([[0,-1j],[1j,0]],complex)
YY=np.kron(sy,sy)

def solve_generator(rate,Jval,g1,g2,probs):
    hamiltonian=np.zeros((4,4),complex)
    hamiltonian[0,3]=hamiltonian[3,0]=Jval
    target=np.diag(probs).astype(complex)
    def generator(mat):
        return (-1j*(hamiltonian@mat-mat@hamiltonian)
                +g1*(Z1@mat@Z1-mat)+g2*(Z2@mat@Z2-mat)
                +rate*(target*np.trace(mat)-mat))
    columns=[]
    for i in range(4):
        for j in range(4):
            basis=np.zeros((4,4),complex);basis[i,j]=1
            columns.append(generator(basis).flatten())
    liouvillian=np.stack(columns,axis=1)
    normalization=np.zeros(16);normalization[[0,5,10,15]]=1
    liouvillian[0]=normalization
    rhs=np.zeros(16,complex);rhs[0]=1
    state=np.linalg.solve(liouvillian,rhs).reshape(4,4)
    assert_check(np.linalg.norm(generator(state))<3e-12,'direct stationary residual')
    return state

def predicted_state(rate,Jval,g1,g2,probs):
    a,b,c,d=probs
    gam=2*(g1+g2)
    denominator=rate*(rate+gam)+4*Jval*Jval
    imbalance=(a-d)*rate*(rate+gam)/denominator
    coherence=1j*Jval*rate*(a-d)/denominator
    return np.array([[(a+d+imbalance)/2,0,0,coherence],
                     [0,b,0,0],[0,0,c,0],
                     [coherence.conjugate(),0,0,(a+d-imbalance)/2]],complex)

def wootters_concurrence(state):
    spin_flip=YY@state.conj()@YY
    vals=np.linalg.eigvals(state@spin_flip)
    assert_check(np.max(np.abs(vals.imag))<1e-10,'spin-flip spectrum nearly real')
    roots=sorted((math.sqrt(max(0,float(x.real))) for x in vals),reverse=True)
    return max(0,roots[0]-sum(roots[1:]))

parameter_sets=[
    (1.0,0.2,0.3,(.81,.09,.09,.01)),
    (1.0,0.0,0.0,(1.,0.,0.,0.)),
    (2.5,0.7,0.0,(.7,.1,.13,.07)),
    (0.4,0.0,0.9,(.0,.0,.0,1.)),
    (3.0,0.02,0.01,(.25,.25,.25,.25)),
    (1.2,0.0,0.0,(.5,0,0,.5)),
]
for Jval,g1,g2,probs in parameter_sets:
    for rate in (0.11,0.5,1.0,2*Jval,4.1,12.0):
        state=solve_generator(rate,Jval,g1,g2,probs)
        target=predicted_state(rate,Jval,g1,g2,probs)
        assert_check(np.linalg.norm(state-target)<1e-12,'explicit stationary state')
        assert_check(np.linalg.norm(state-state.conj().T)<1e-12,'Hermiticity')
        assert_check(abs(np.trace(state)-1)<1e-12,'normalization')
        assert_check(np.min(np.linalg.eigvalsh(state))>-1e-12,'positivity')
        actual=wootters_concurrence(state)
        a,b,c,d=probs
        den=rate*(rate+2*(g1+g2))+4*Jval*Jval
        formula=2*max(0,abs(a-d)*Jval*rate/den-math.sqrt(b*c))
        assert_check(abs(actual-formula)<2e-11,'independent spin-flip concurrence')

# A strict thermally mixed entanglement interval and reciprocal endpoints.
Jval=1.0; gam=1.0; thermal_s=.1
p=(.81,.09,.09,.01)
kap=Jval*abs(p[0]-p[3]);hb=math.sqrt(p[1]*p[2])
bound=math.sqrt((kap-hb*gam)**2-16*hb*hb*Jval*Jval)
left=(kap-hb*gam-bound)/(2*hb)
right=(kap-hb*gam+bound)/(2*hb)
assert_check(abs(left*right-4*Jval*Jval)<2e-12,'reciprocal rate thresholds')
assert_check(left<2*Jval<right,'optimizer interior to entangled window')
assert_check(abs(left-0.5446441598235017)<2e-13,'left threshold')
assert_check(abs(right-7.344244729065388)<2e-13,'right threshold')
assert_check(abs(2*(kap/(gam+4*Jval)-hb)-0.14)<2e-14,'peak concurrence')
for rate in (left/2, left, (left+2)/2, 2, (2+right)/2,right,right*2):
    denominator=rate*(rate+gam)+4
    C=2*max(0,kap*rate/denominator-hb)
    assert_check((C>1e-9)==(left+1e-9<rate<right-1e-9),'window sign')

print(f'PASS: {checks} assertions; symbolic balance/optimization, 16x16 direct stationary solve, Wootters spin-flip, thresholds.')
