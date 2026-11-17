#!/usr/bin/env python3
"""Reproducible exact and finite checks for stationary inertial telegraph oscillator kurtosis."""
import sympy as sp
import numpy as np

q,z=sp.symbols('q z',positive=True)
B=26*z**3+224*z**2+476*z+264
H=3*z**5+48*z**4+288*z**3+816*z**2+1104*z+576
P=(9*z-24)*q**2-B*q-H
V=(z+2)/(2*q*(z*z+2*z+q))
N=q*z**4+3*z**4+11*q*z**3+42*z**3+9*q*q*z*z+53*q*z*z+204*z*z+45*q*q*z+136*q*z+408*z+12*q*q+132*q+288
E4=3*N/(4*q*q*(q+3)*(z*z+2*z+q)*(z*z+6*z+9*q)*(z*z+6*z+q+8))
K=3*q*P/((z+2)**2*(q+3)*(z*z+6*z+9*q)*(z*z+6*z+q+8))

def indices(even=False):
    result=[]
    for degree in range(5):
        if even and degree%2:continue
        for i in range(degree+1):
            for j in range(degree-i+1):
                h=degree-i-j
                if h in (0,1):result.append((i,j,h))
    return result

def generator(even=False):
    states=indices(even)
    I={state:a for a,state in enumerate(states)}
    A=sp.zeros(len(states)); rhs=sp.zeros(len(states),1)
    for row,(i,j,h) in enumerate(states):
        if i==j==h==0:
            A[row,row]=1; rhs[row]=1;continue
        if i:A[row,I[i-1,j+1,h]]+=i
        if j:
            A[row,I[i,j,h]]+=-2*j
            A[row,I[i+1,j-1,h]]+=-q*j
            A[row,I[i,j-1,1-h]]+=j
        if h:A[row,I[i,j,h]]+=-z
    return states,A,rhs

states,A,rhs=generator(True)
assert len(states)==15
sol=A.inv()*rhs
ix={x:i for i,x in enumerate(states)}
assert sp.cancel(sol[ix[(2,0,0)]]-V)==0
assert sp.cancel(sol[ix[(4,0,0)]]-E4)==0
assert sp.cancel((E4-3*V**2)/V**2-K)==0
assert sp.factor(sp.together(E4-3*V**2).as_numer_denom()[0]).has(P) or sp.cancel((E4-3*V**2)/V**2-K)==0
assert sp.factor(P.subs({q:1000,z:4}))==4532160
assert sp.cancel(K.subs({q:1000,z:4})-sp.Rational(590125,14847409))==0
assert P.subs({q:1000,z:1})<0
assert P.subs({q:1000,z:100})<0
# Independent full generator matrix, including odd parities, compared to closed formulas.
all_states,full_A,full_rhs=generator(False)
assert len(all_states)==25
ix_all={x:i for i,x in enumerate(all_states)}
rng=np.random.default_rng(246813579)
for attempt in range(160):
    qv=float(np.exp(rng.uniform(-2.0,6.5)))
    zv=float(np.exp(rng.uniform(-3.0,4.5)))
    full_num=np.array(full_A.subs({q:qv,z:zv}),dtype=float)
    rhs_num=np.array(full_rhs,dtype=float).ravel()
    numerical=np.linalg.solve(full_num,rhs_num)
    actual_v=numerical[ix_all[(2,0,0)]]
    actual_4=numerical[ix_all[(4,0,0)]]
    v_pred=float(V.subs({q:qv,z:zv}))
    k_pred=float(K.subs({q:qv,z:zv}))
    actual_k=actual_4/actual_v**2-3
    assert abs(actual_v-v_pred) <2e-10*max(1,abs(v_pred))
    assert abs(actual_k-k_pred) <3e-7
    # Full generator satisfies all stationary polynomial identities.
    assert np.linalg.norm(full_num@numerical-rhs_num,np.inf)<1e-8
# Exact check of positivity threshold at representative rational parameters.
for zv in [sp.Rational(1,3),sp.Rational(8,3),sp.Integer(3),sp.Integer(4),sp.Integer(6)]:
    for qv in [sp.Rational(1,10),sp.Integer(1),sp.Integer(10),sp.Integer(1000)]:
        pv=sp.factor(P.subs({q:qv,z:zv}))
        kv=sp.factor(K.subs({q:qv,z:zv}))
        assert sp.sign(pv)==sp.sign(kv)
print('PASS: exact symbolic stationary moment identities, 160 full-generator cross-checks, 20 exact-rational sign checks')
