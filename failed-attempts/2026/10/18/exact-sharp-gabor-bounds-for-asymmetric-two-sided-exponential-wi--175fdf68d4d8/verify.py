import numpy as np
from math import exp,log,sqrt
from scipy.optimize import minimize_scalar

def formula(m,a,b):
    j=np.arange(m); x=j/m
    q1,q2=exp(-a),exp(-b)
    u=np.exp(-a*x)/(1+q1)
    v=np.exp(-b*(1-x))/(1+q2)
    U=float(u@u); V=float(v@v); C=float(u@v)
    t=((b-a)*C+sqrt((a-b)**2*C*C+4*a*b*U*V))/(2*b*V)
    xstar=log(t)/(a+b)
    A=float(np.sum((u*np.exp(-a*xstar)-v*np.exp(b*xstar))**2))
    uu=np.exp(-a*x)/(1-q1)
    vv=np.exp(-b*(1-x))/(1-q2)
    B=float(np.sum((uu+vv)**2))
    return A,B,xstar,U,V,C

def zak(t,w,a,b):
    q1,q2=exp(-a),exp(-b)
    e=np.exp(2j*np.pi*w)
    return exp(-a*t)/(1-q1/e)+exp(-b*(1-t))*e/(1-q2*e)

def direct(m,a,b,x,w):
    return sum(abs(zak(x+j/m,w,a,b))**2 for j in range(m))

rng=np.random.default_rng(2500)
N=0
for m in [2,3,4,6,10,25]:
  for z in range(40):
    a,b=np.exp(rng.uniform(-2.3,2.0,2))
    A,B,xstar,aa,bb,cc=formula(m,a,b)
    assert 0<xstar<1/m,(m,a,b,xstar)
    assert 0<A<B
    assert abs(direct(m,a,b,xstar,.5)-A)<1e-8*(1+A)
    assert abs(direct(m,a,b,0.,0.)-B)<1e-8*(1+B)
    assert abs(direct(m,a,b,1/m,0.)-B)<1e-8*(1+B)
    assert abs(direct(m,a,b,0.,.5)-direct(m,a,b,1/m,.5))<1e-9*(1+A)
    for v in range(20):
        x=float(rng.uniform(0,1/m)); w=float(rng.uniform(0,1))
        val=direct(m,a,b,x,w)
        if not (A-1e-8*(1+A) < val < B+1e-8*(1+B)):
            raise AssertionError(('bounds',m,a,b,x,w,A,val,B))
        N+=1
    res=minimize_scalar(lambda xx:direct(m,a,b,xx,.5),bounds=(0,1/m),method='bounded',options={'xatol':1e-12})
    assert abs(res.fun-A)<1e-8*(1+A)
print('VERIFY_OK',N,'complex-Zak direct comparisons across',6*40,'parameter triples')
print('sample',formula(4,.7,2.8))
