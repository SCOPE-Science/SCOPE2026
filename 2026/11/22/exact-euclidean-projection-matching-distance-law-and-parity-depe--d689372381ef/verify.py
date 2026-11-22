"""Reproducible numerical checks for the enclosed chainlink projection theorem."""
import itertools
import math
import numpy as np
from scipy.optimize import minimize

def projection(x,a,ell):
    d=np.maximum(x-np.roll(x,-1)-(a-ell),0.0)
    y=x-0.5*d+0.5*np.roll(d,1)
    return y,d

def matching(subset,s):
    S=set(subset)
    return all((i+1)%s not in S for i in S)

def check():
    rng=np.random.default_rng(10193)
    total=0
    for s in range(3,13):
      for rep in range(8):
        ell=rng.uniform(.05,1.5)
        a=2*ell+rng.uniform(0,2*ell,size=s)
        if rep==0: a[:]=2*ell
        for trial in range(12):
          x=a*rng.random(s)
          p,d=projection(x,a,ell)
          assert np.all(p>=-1e-9) and np.all(p<=a+1e-9)
          assert np.all(p-np.roll(p,-1)<=a-ell+1e-9)
          assert abs(np.linalg.norm(x-p)**2-0.5*np.sum(d*d))<1e-9
          feasible={'type':'ineq','fun':lambda y,a=a,ell=ell: a-ell-y+np.roll(y,-1),
                    'jac':lambda y:-np.eye(s)+np.roll(np.eye(s),1,axis=1)}
          initial=p+np.random.default_rng(trial+rep).normal(0,.1,s)
          sol=minimize(lambda y:0.5*np.sum((y-x)**2),initial,jac=lambda y:y-x,
              bounds=list(zip(np.zeros(s),a)),constraints=[feasible],method='SLSQP',
              options={'ftol':1e-11,'maxiter':600})
          assert sol.success, (s,rep,trial,sol.message)
          assert np.linalg.norm(sol.x-p)<2e-5,(s,rep,trial)
          total+=1
    assert total==960
    for s in range(3,11):
      a=np.linspace(2.4,4.8,s);ell=1
      maxima=[]; locus=[]
      for bits in itertools.product([0,1],repeat=s):
        x=np.array(bits)*a
        _,d=projection(x,a,ell)
        maxima.append(float(np.sum(d*d)/2))
        if abs(np.sum(d*d)/2-ell*ell*(s//2)/2)<1e-9:
          locus.append(bits)
      assert abs(max(maxima)-ell*ell*(s//2)/2)<1e-9
      if s%2==0: assert len(locus)==2
      else: assert len(locus)==2*s # each of s farthest segments has two endpoints
    rng=np.random.default_rng(2006)
    for s in [3,4,5,6,9]:
      a=np.array([3+.5*i for i in range(s)]);ell=1.
      X=rng.random((100000,s))*a
      E=np.maximum(X-np.roll(X,-1,axis=1)-(a-ell),0)
      empirical=np.mean(np.sum(E*E,axis=1)/2)
      exact=ell**4/24*sum(1/(a[i]*a[(i+1)%s]) for i in range(s))
      assert abs(empirical-exact)<max(.001,.07*exact)
    print('CHAINLINK_PROJECTION_PASS; 960 QP comparisons, 8 exact finite farthest tests, 5 Monte Carlo mean checks')
if __name__=='__main__':check()
