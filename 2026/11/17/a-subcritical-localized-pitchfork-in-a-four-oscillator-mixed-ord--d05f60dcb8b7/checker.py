"""Checks for the four-node mixed-order phase model.

Run: python checker.py
Numerical checks corroborate, but do not replace, the analytical argument.
"""
import math
import numpy as np
import sympy as sp
from scipy.optimize import root

EDGES=((0,1),(1,2),(2,3))

def field(theta,k,tau):
    theta=np.asarray(theta,dtype=float)
    z1=np.mean(np.exp(1j*theta))
    z2=np.mean(np.exp(2j*theta))
    v=tau*np.imag(z2*np.conj(z1)*np.exp(-1j*theta))
    for i,j in EDGES:
        s=k*np.sin(theta[j]-theta[i]);v[i]+=s;v[j]-=s
    return v

def slow_field(a,b,k,tau):
    h=(np.sin(a)+np.sin(b))/2
    Q=(np.cos(2*a)+np.cos(2*b))/2
    return np.array([k*np.sin(b-a)-tau*h*Q*np.cos(a),
       k*(-np.sin(b-a)+np.sin(2*b))-tau*h*Q*np.cos(b)])

def jac(theta,k,tau):
    J=np.zeros((4,4))
    for i,j in EDGES:
        c=k*np.cos(theta[j]-theta[i]);
        J[i,j]+=c;J[j,i]+=c;J[i,i]-=c;J[j,j]-=c
    for i in range(4):
        for j in range(4):
            for l in range(4):
                c=tau/16*np.cos(2*theta[j]-theta[l]-theta[i])
                J[i,j]+=2*c;J[i,l]-=c;J[i,i]-=c
    return J

k,tau,a,b=sp.symbols('k tau a b',positive=True,real=True)
h=(sp.sin(a)+sp.sin(b))/2
Q=(sp.cos(2*a)+sp.cos(2*b))/2
f1=k*sp.sin(b-a)-tau*h*Q*sp.cos(a)
f2=k*(-sp.sin(b-a)+sp.sin(2*b))-tau*h*Q*sp.cos(b)
critJ=sp.Matrix([f1,f2]).jacobian([a,b]).subs({a:0,b:0})
assert sp.simplify(critJ - sp.Matrix([[-k-tau/2,k-tau/2],[k-tau/2,k-tau/2]])) == sp.zeros(2)
# At the critical parameter, a=b^3/2 on the local center manifold to order three.
cs=sp.symbols('cs',real=True)
assert sp.expand(sp.series(f1.subs({a:cs*b**3,tau:2*k}),b,0,5).removeO()).coeff(b,3)==sp.expand(k*(1-2*cs))
assert sp.expand(sp.series(f2.subs({a:cs*b**3,tau:2*k}),b,0,5).removeO()).coeff(b,3)==k/2
# Jacobian characteristic polynomial in the full 4-phase system.
S=[1,1,-1,-1]
M=sp.zeros(4)
for i,j in EDGES:
    c=k*S[i]*S[j]
    M[i,i]-=c;M[j,j]-=c;M[i,j]+=c;M[j,i]+=c
s=sp.Matrix(S)
M-=tau*s*s.T/4
z=sp.symbols('z')
assert sp.factor(M.charpoly(z).as_expr()) == z*(z+2*k)*(z*z+tau*z+k*tau-2*k*k)

rng=np.random.default_rng(20261106)
for _ in range(200):
    th=rng.uniform(-5,5,size=4)
    kk=rng.uniform(.1,4)
    tt=rng.uniform(0.1,8)
    brute=np.zeros(4)
    for i in range(4):
        for j in range(4):
            for l in range(4):
                brute[i]+=(tt/16)*np.sin(2*th[j]-th[l]-th[i])
    for i,j in EDGES:
        v=kk*np.sin(th[j]-th[i]);brute[i]+=v;brute[j]-=v
    assert np.allclose(brute,field(th,kk,tt),atol=2e-13)
    eps=1e-6
    numJ=np.array([(field(th+eps*np.eye(4)[j],kk,tt)-field(th-eps*np.eye(4)[j],kk,tt))/(2*eps) for j in range(4)]).T
    assert np.max(np.abs(numJ-jac(th,kk,tt))) < 1e-8
    aa=rng.uniform(-.8,.8);bb=rng.uniform(-.8,.8)
    actual=field([aa,bb,np.pi-bb,np.pi-aa],kk,tt)
    red=slow_field(aa,bb,kk,tt)
    assert np.allclose(actual,np.r_[red,-red[::-1]],atol=3e-14)

for mu in [.16,.08,.04,.02,.01,.005]:
    k0=1.3
    t0=k0*(2+mu)
    sol=root(lambda v:slow_field(*v,k0,t0),[mu**1.5/4,mu**.5],tol=1e-12)
    assert sol.success or np.linalg.norm(sol.fun)<1e-10
    aa,bb=sol.x
    assert bb>0 and np.linalg.norm(slow_field(aa,bb,k0,t0))<1e-10
    assert abs(bb/math.sqrt(mu)-1)<4*mu
    assert abs(aa/(mu**1.5)-.25)<2*mu
    p=[aa,bb,np.pi-bb,np.pi-aa]
    eig=np.linalg.eigvals(jac(p,k0,t0))
    assert np.count_nonzero(eig.real>1e-8)==1
    assert np.count_nonzero(eig.real<-1e-8)==2
    assert min(abs(eig)) <1e-8
print('PASS: exact Jacobian polynomial, cubic center coefficient, 200 direct full-field/derivative/symmetry tests, six nonzero saddle branches')
