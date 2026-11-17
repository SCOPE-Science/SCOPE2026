#!/usr/bin/env python3
"""Standalone finite algebraic / numerical checks for neutral equal-latency phage dynamics.
All infinite-time assertions in the accompanying theorem are proved analytically."""
import math
import sympy as sp
u=sp.symbols('u',real=True)
mu=sp.Rational(1); E=sp.Rational(1,2); alpha=sp.Rational(2)
k=[sp.Integer(1)]*2; ell=[sp.Integer(1)]*2
m=[sp.Integer(1)]*2; d=[sp.Integer(1)]*2
b=[sp.Integer(2),sp.Integer(6)]
r=[d[i]/m[i] for i in range(2)]
B0=sp.simplify(sum(k[i]*r[i] for i in range(2))*(1-E)/mu)
A=[sp.simplify(k[i]*(1-b[i]*E)+ell[i]*B0) for i in range(2)]
K=sp.simplify(sum(k[i]*d[i]*A[i]/m[i]**2 for i in range(2)))
C=sp.simplify(sum(k[i]*d[i]*A[i]**2/m[i]**3 for i in range(2)))
assert B0==1 and A==[1,-1] and K==0 and C==2
Q=[r[i]*(1-A[i]/m[i]*u+(A[i]/m[i])**2*u**2) for i in range(2)]
I=B0*u
S_rhs=sp.expand(u*(alpha-sum(k[i]*Q[i] for i in range(2))))
assert S_rhs == -2*u**3
# On the center manifold at K=0, the delayed product equals the present product up to u^2.
I_rhs=sp.expand(sum(k[i]*(1-E)*Q[i]*u for i in range(2))-mu*I)
assert sp.series(I_rhs,u,0,3).removeO()==0
for i in range(2):
    Qi_rhs=sp.expand(d[i]-m[i]*Q[i]-k[i]*Q[i]*u-ell[i]*Q[i]*I+k[i]*b[i]*E*Q[i]*u)
    assert sp.series(Qi_rhs,u,0,3).removeO()==0
# General formal calculation: the common-delay critical curvature is strictly positive.
k0,k1,d0,d1,m0,m1,a0,a1=sp.symbols('k0 k1 d0 d1 m0 m1 a0 a1',positive=True)
Q0=d0/(m0+a0*u);Q1=d1/(m1+a1*u)
F=k0*Q0+k1*Q1
F2=sp.simplify(sp.diff(F,u,2).subs(u,0)/2)
assert sp.simplify(F2-(k0*d0*a0**2/m0**3+k1*d1*a1**2/m1**3))==0
# Independent finite-time integration of positive compatible histories, first-order Euler.
# Delay interpolation uses fixed dt<tau. Initial S=0.1,Q=(1,1),I=0.1 compatible with delay integral.
dt=0.01; tau=math.log(2.0); N=int(1200/dt)
S=[0.1]; I_n=[0.1]; Q_0=[1.0]; Q_1=[1.0]
def delayed(arr,idx):
    x=idx-tau/dt
    if x<=0:return arr[0]
    lo=int(x);f=x-lo
    return arr[lo]*(1-f)+arr[lo+1]*f
for j in range(N):
    s=S[-1]; iv=I_n[-1]; q0=Q_0[-1]; q1=Q_1[-1]
    oldS=delayed(S,j); old0=delayed(Q_0,j); old1=delayed(Q_1,j)
    inf=oldS*(old0+old1)
    dS=s*(2-q0-q1)
    dI=s*(q0+q1)-iv-0.5*inf
    dQ0=1-q0-q0*s-q0*iv+1.0*oldS*old0
    dQ1=1-q1-q1*s-q1*iv+3.0*oldS*old1
    S.append(s+dt*dS);I_n.append(iv+dt*dI)
    Q_0.append(q0+dt*dQ0);Q_1.append(q1+dt*dQ1)
for t in (300,600,1200):
    j=round(t/dt)
    assert 0 < S[j] < 0.1
    print('FINITE_DDE',t,'S=',round(S[j],9),'sqrt(t)*S=',round(math.sqrt(t)*S[j],9),'target=0.5')
assert abs(math.sqrt(1200)*S[-1]-.5)<.075
print('VERIFY_OK: exact_center_coefficients=2, exact_formal_residual_orders=3, positive_DDE_times=3; FINITE_TEST_ONLY')
