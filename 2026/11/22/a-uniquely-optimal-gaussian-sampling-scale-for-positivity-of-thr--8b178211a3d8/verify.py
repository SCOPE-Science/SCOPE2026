"""Reproduce the three-node Gaussian quadrature positivity formula and checks.

Requires Python 3, NumPy, SciPy, and mpmath. The finite checks illustrate,
but do not replace, the analytic probability and log-concavity proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import ndtr
import mpmath as mp

SQRT_2PI=math.sqrt(2*math.pi)
count=0

def check(condition,message):
    global count
    if not condition:
        raise AssertionError(message)
    count+=1

def phi(u):
    return math.exp(-u*u/2)/SQRT_2PI

def probability(q):
    assert q>0
    v,err=quad(lambda u:12*phi(u)*(ndtr(q/u)-0.5)*(1-ndtr(q/u)),0,18,
               epsabs=2e-13,epsrel=2e-13,limit=250)
    return v

def derivative(q):
    assert q>0
    v,err=quad(lambda u:12*phi(u)*phi(q/u)*(1.5-2*ndtr(q/u))/u,0,18,
               epsabs=2e-13,epsrel=2e-13,limit=250)
    return v

def polynomial_weights(x,q):
    a,b,c=sorted(x)
    return np.array([(q+b*c)/((a-b)*(a-c)),
                     (q+a*c)/((b-a)*(b-c)),
                     (q+a*b)/((c-a)*(c-b))])

rng=np.random.default_rng(231109)
for q in (0.05,0.2,0.3930943625905366,1.0,2.0):
    x=rng.standard_normal((320000,3))
    xs=np.sort(x,axis=1)
    a,b,c=xs.T
    w0=(q+b*c)/((a-b)*(a-c))
    w1=(q+a*c)/((b-a)*(b-c))
    w2=(q+a*b)/((c-a)*(c-b))
    positivity=(w0>0)&(w1>0)&(w2>0)
    sign_condition=(q+a*c<0)&(q+a*b>0)&(q+b*c>0)
    check(np.array_equal(positivity,sign_condition),'exact weight-sign region')
    p=probability(q)
    phat=positivity.mean()
    stderr=math.sqrt(max(p*(1-p),1e-10)/len(x))
    check(abs(phat-p)<5*stderr+0.001,'probability against seeded Monte Carlo')

for _ in range(10000):
    x=sorted(rng.normal(size=3))
    q=float(rng.uniform(0.03,4))
    ww=polynomial_weights(x,q)
    check(abs(sum(ww)-1)<1e-8,'constant moment')
    check(abs(np.dot(ww,x))<1e-8,'linear moment')
    check(abs(np.dot(ww,np.square(x))-q)<1e-8,'quadratic moment')

root=brentq(derivative,0.2,0.7,xtol=1e-14)
check(0.39309436258<root<0.39309436260,'unique root numerical bracket')
check(0.24697058764<probability(root)<0.24697058767,'peak value')
check(abs(probability(1)-0.178147324601194)<2e-13,'matched variance')
check(derivative(0.2)>0 and derivative(0.5)<0,'derivative signs')
for q in np.geomspace(0.02,20,100):
    p=probability(q)
    check(p<=probability(root)+1e-10,'grid peak bound')

# High-precision check of the known flat-kernel-to-polynomial limit.
mp.mp.dps=55
for x0 in ((-1.2,0.5,1.1),(-2.1,-0.5,0.7),(-0.8,0.15,2.4),(0.3,1.2,2.3)):
    x=list(map(mp.mpf, x0))
    q=mp.mpf('0.7')
    a,b,c=x
    poly=mp.matrix([(q+b*c)/((a-b)*(a-c)),
                    (q+a*c)/((b-a)*(b-c)),
                    (q+a*b)/((c-a)*(c-b))])
    discrepancies=[]
    for h in map(mp.mpf,('0.1','0.01','0.001')):
        K=mp.matrix(3)
        for i in range(3):
            for j in range(3):
                K[i,j]=mp.exp(-h*(x[i]-x[j])**2)
        v=mp.matrix([mp.exp(-h*xi*xi/(1+2*h*q))/mp.sqrt(1+2*h*q) for xi in x])
        w=mp.lu_solve(K,v)
        discrepancies.append(float(max(abs(w[i]-poly[i]) for i in range(3))))
    check(discrepancies[2]<discrepancies[1]<discrepancies[0], 'flat-limit convergence trend')
    check(discrepancies[-1]<0.1,'flat-limit absolute error at h=0.001')

print('checks passed:',count)
print('unique maximizing variance ratio q* approximately:',format(root,'.15f'))
print('optimal probability approximately:',format(probability(root),'.15f'))
print('matched variance probability P(1):',format(probability(1),'.15f'))
