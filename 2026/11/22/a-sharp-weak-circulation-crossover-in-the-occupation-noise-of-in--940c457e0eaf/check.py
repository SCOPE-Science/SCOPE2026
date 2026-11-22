"""Independent matrix and asymptotic checks for cyclic interacting-urn noise."""
import numpy as np
from scipy.linalg import solve_continuous_lyapunov, expm

def formula(m,g,delta,t=0.0):
    k=np.arange(1,m)
    theta=2*np.pi*k/m
    lam=(m+g)/(2*m)*(1-np.cos(theta))
    w=delta/2*np.sin(theta)
    c=np.sum(np.exp(-lam*t)*np.cos(w*t))/(m*(m+g))
    a=2*np.sum(lam/(lam**2+w**2))/(m*(m+g))
    return float(c),float(a)

def matrices(m,g,delta):
    p=(1+delta)/2;q=(1-delta)/2
    h=np.zeros((m,m));Q=np.zeros_like(h)
    a=p/2+g/(4*m);b=q/2+g/(4*m)
    for i in range(m):
        h[i,i]-=a+b
        h[i,(i-1)%m]+=a
        h[i,(i+1)%m]+=b
        Q[i,i]+=1/m
        Q[i,(i-1)%m]-=1/(2*m)
        Q[i,(i+1)%m]-=1/(2*m)
    return h,Q

def matrix_prediction(m,g,delta,t):
    h,Q=matrices(m,g,delta)
    P=np.eye(m)-np.ones((m,m))/m
    # Work on the m-1 dimensional sum-zero range by shifting null mode.
    H=h-np.ones((m,m))/m
    C=solve_continuous_lyapunov(H,-Q)
    tc=expm(H*t)@C
    A=-2*np.linalg.solve(H,C)
    return tc[0,0],A[0,0],C,P

cnt=0
for m in [3,4,5,6,7,8,13,24]:
 for g in [0.0, 0.5,2.0,11.0]:
  for d in [-.88,-.35,0,.47,.9]:
   for t in [0.0,.31,2.1]:
    c,a=formula(m,g,d,t)
    cc,aa,C,P=matrix_prediction(m,g,d,t)
    assert np.isclose(c,cc,rtol=1e-9,atol=1e-11),(m,g,d,t,c,cc)
    assert np.isclose(a,aa,rtol=1e-9,atol=1e-11),(m,g,d,t,a,aa)
    assert np.allclose(C,P/(m+g),atol=1e-10)
    cnt+=3
for m in [3,4,5,9,31,101]:
 for g in [0,3,10]:
  ans=formula(m,g,0)[1]
  expected=2*(m*m-1)/(3*(m+g)**2)
  assert np.isclose(ans,expected,rtol=3e-13,atol=1e-13)
  cnt+=1
for M in [500,1000,2000,4000]:
 for kappa in [0,.5,2]:
  g=M*kappa
  for zeta in [0,.3,2,6]:
   d=zeta/M
   u=zeta/(1+kappa)
   ref=2/(3*(1+kappa)**2) if not zeta else 2/(1+kappa)**2*(u/np.tanh(u)-1)/u**2
   actual=formula(M,g,d)[1]
   # 1/M finite-size correction, rapidly improves
   assert abs(actual-ref)<0.015,(M,kappa,zeta,actual,ref)
   cnt+=1
print('PASS',cnt,'assertions')
print('Example m=6 g=3 delta 0 and 0.75',formula(6,3,0),formula(6,3,.75))

# An independent finite-difference reconstruction of the nonlinear flux drift.
def drift_from_rates(x,g,d):
    m=len(x);p=(1+d)/2;q=(1-d)/2
    def t(a,b):
        return 1/(1+np.exp(g*(b-a)))
    j=np.array([p*x[i]*t(x[i],x[(i+1)%m])-q*x[(i+1)%m]*t(x[(i+1)%m],x[i]) for i in range(m)])
    return np.roll(j,1)-j
for m in [3,4,6,9]:
 for g in [0,1,4]:
  for d in [-0.7,0,0.58]:
   x=np.full(m,1/m)
   jac=np.zeros((m,m));step=1e-6
   for k in range(m):
    e=np.eye(m)[k]
    jac[:,k]=(drift_from_rates(x+step*e,g,d)-drift_from_rates(x-step*e,g,d))/(2*step)
   h,q=matrices(m,g,d)
   assert np.allclose(jac,h,atol=1e-9,rtol=1e-9),(m,g,d)
   cnt+=1
for m in [300,700,1500]:
 for gmult in [0,1.4]:
  for delta in [0.2,.7]:
   observed=formula(m,m*gmult,delta)[1]
   pred=2/(delta*m*(1+gmult))
   assert abs(observed/pred-1)<0.05,(m,gmult,delta,observed,pred)
   cnt+=1
print('PASS',cnt,'total assertions including nonlinear drift and strong-bias asymptotics')
