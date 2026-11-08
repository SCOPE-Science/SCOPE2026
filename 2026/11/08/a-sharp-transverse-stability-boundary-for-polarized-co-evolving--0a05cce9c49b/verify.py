#!/usr/bin/env python3
"""Reproduce equilibrium identities, invariant modes, and asymptotic examples.

Requires sympy, numpy, scipy. Checks support, rather than replace, the analytic proof.
"""
import random
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

A,B,k,a,u,y=sp.symbols('A B k a u y',positive=True)
y_star=A/(A+B*k*k)
u_star=A*a/(A+B*k**3)
q=sp.factor(k+(1-k)*y_star)
eta=sp.factor((A+B*k*k)*u_star*u_star)
F=-(k+(1-k)*y)*u+a*y
G=u*u*(A*(1-y)-B*k*k*y)
assert sp.simplify(F.subs({u:u_star,y:y_star}))==0
assert sp.simplify(G.subs({u:u_star,y:y_star}))==0
J=sp.Matrix([F,G]).jacobian([u,y]).subs({u:u_star,y:y_star})
assert sp.simplify(J[0,0]+q)==0
assert sp.simplify(J[0,1]-a*k/q)==0
assert sp.simplify(J[1,0])==0
assert sp.simplify(J[1,1]+eta)==0
assert sp.simplify(q.subs({A:2,B:2,k:1})-1)==0
assert sp.simplify(eta.subs({A:2,B:2,k:1,a:1})-1)==0
assert sp.simplify(y_star-u_star/a)==sp.simplify(A*B*k*k*(k-1)/((A+B*k*k)*(A+B*k**3)))

random.seed(62917)
count=0
for _ in range(120):
    n1=random.randint(1,5);n2=random.randint(1,5)
    n=n1+n2;kp=random.uniform(.05,1.95);p=kp/2
    W=np.zeros((n,n))
    for i in range(n):
        own=np.arange(n1) if i<n1 else np.arange(n1,n)
        opp=np.arange(n1,n) if i<n1 else np.arange(n1)
        weights_own=np.array([random.uniform(.3,2) for j in own]);weights_own/=sum(weights_own)
        weights_opp=np.array([random.uniform(.3,2) for j in opp]);weights_opp/=sum(weights_opp)
        W[i,own]=(1-p)*weights_own;W[i,opp]=p*weights_opp
    v=np.array([1.]*n1+[-1.]*n2)
    assert np.max(np.abs(W @ v-(1-kp)*v))<1.e-12
    alpha=random.uniform(.3,9.);beta=random.uniform(.3,9.);aa=random.uniform(.1,1.);y0=random.uniform(0,1)
    us=float(u_star.subs({A:alpha,B:beta,k:kp,a:aa}))
    ys=float(y_star.subs({A:alpha,B:beta,k:kp}))
    def scalar(t,z):
        uu,yy=z
        return [-((kp+(1-kp)*yy)*uu)+aa*yy,uu**2*(alpha*(1-yy)-beta*kp**2*yy)]
    def original(t,z):
        xx=z[:n];yy=z[n:];dif=xx-W@xx
        return np.r_[-(1-yy)*dif-yy*(xx-aa*v),alpha*(1-yy)*xx**2-beta*yy*dif**2]
    T=2
    ss=solve_ivp(scalar,(0,T),[aa,y0],rtol=1.e-10,atol=1.e-11, t_eval=np.linspace(0,T,30))
    oo=solve_ivp(original,(0,T),np.r_[aa*v,np.full(n,y0)],rtol=1.e-10,atol=1.e-11,t_eval=ss.t)
    assert ss.success and oo.success
    assert np.max(np.abs(oo.y[:n,:]-v[:,None]*ss.y[0,:]))<1.e-7
    assert np.max(np.abs(oo.y[n:,:]-ss.y[1,:]))<1.e-7
    assert 0<us<=aa and 0<ys<1
    count+=1

# Distinct leadership-slow and exact-resonance regimes; verify negative opinion tail.
for alpha,beta in [(1.,1.),(2.,2.)]:
    kp=1.;aa=1.;y0=0.
    def fun(t,z):
        uu,yy=z
        return [-uu+yy,uu*uu*(alpha-(alpha+beta)*yy)]
    sol=solve_ivp(fun,(0,30),[aa,y0],rtol=1.e-12,atol=1.e-13,t_eval=np.linspace(0,30,601))
    assert sol.success
    target=alpha/(alpha+beta)
    assert min(sol.y[0])<target-1.e-4
    assert abs(sol.y[0,-1]-target)<1.e-4
# Exact full two-person Jacobian split into symmetric and antisymmetric sectors.
x1,x2,y1,y2=sp.symbols('x1 x2 y1 y2',real=True)
p=k/2
F1=-(1-y1)*p*(x1-x2)-y1*(x1-a)
F2=-(1-y2)*p*(x2-x1)-y2*(x2+a)
G1=A*(1-y1)*x1**2-B*y1*(p*(x1-x2))**2
G2=A*(1-y2)*x2**2-B*y2*(p*(x2-x1))**2
full=sp.Matrix([F1,F2,G1,G2]).jacobian([x1,x2,y1,y2])
full=full.subs({x1:u_star,x2:-u_star,y1:y_star,y2:y_star})
# Coordinates (polarization, mean opinion, mean leadership, leadership difference).
T=sp.Matrix([[1,1,0,0],[-1,1,0,0],[0,0,1,1],[0,0,1,-1]])
block=sp.simplify(T.inv()*full*T)
assert all(sp.simplify(block[i,j])==0 for i in (0,2) for j in (1,3))
assert all(sp.simplify(block[i,j])==0 for i in (1,3) for j in (0,2))
long=block.extract([0,2],[0,2])
trans=block.extract([1,3],[1,3])
assert sp.simplify(long-J)==sp.zeros(2)
assert sp.simplify(trans.trace()+y_star+eta)==0
assert sp.simplify(trans.det()-a*a*A*A*(A-2*B*k**3)/(A+B*k**3)**2)==0
for vals in [{A:1,B:1,k:1,a:1},{A:4,B:1,k:1,a:1},{A:2,B:2,k:1,a:1}]:
    L=np.array(full.subs(vals)).astype(float)
    eig=np.linalg.eigvals(L)
    print('spectrum',vals, np.sort(eig))
print('PASS: symbolic stationarity, four-mode Jacobian, exact threshold and resonance; 120 random eigenmode networks; two rebound examples')
