#!/usr/bin/env python3
"""Standalone numerical checks of exact two-block pinning allocation."""
import math
import random
from fractions import Fraction as Q
import numpy as np
from scipy.optimize import brentq, minimize


def target(prices_a, prices_b, t):
    p, q = len(prices_a), len(prices_b)
    aa=np.array(prices_a,dtype=float); bb=np.array(prices_b,dtype=float)
    def raw(C):
        x=np.maximum(q-t,C/np.sqrt(aa))
        A=np.sum(1/x)
        D=C*A
        y=np.maximum(p-t,D/np.sqrt(bb))
        B=np.sum(1/y)
        return A*B-1,D,x,y
    lo=1e-14;hi=1.
    while raw(hi)[0]>0:hi*=2
    C=brentq(lambda C: raw(C)[0],lo,hi,xtol=5e-15,rtol=9e-15)
    v,D,x,y=raw(C)
    u=np.maximum(0,t-q+C/np.sqrt(aa))
    w=np.maximum(0,t-p+D/np.sqrt(bb))
    cost=float(aa@u+bb@w)
    return cost,np.concatenate((u,w)),C,D,v


def matrix(p,q):
    L=np.zeros((p+q,p+q))
    L[:p,:p]=q*np.eye(p)
    L[p:,p:]=p*np.eye(q)
    L[:p,p:]=-1
    L[p:,:p]=-1
    return L


def test_many():
    rng=random.Random(81237)
    counts={'eigen':0,'opt':0,'support':0,'high':0,'two_price':0,'exact':0}
    for it in range(100):
        p,q=rng.randrange(2,7),rng.randrange(2,7)
        aa=np.array([math.exp(rng.uniform(-2,2)) for _ in range(p)])
        bb=np.array([math.exp(rng.uniform(-2,2)) for _ in range(q)])
        t=rng.uniform(0.001,8)
        cost, u, C,D,err=target(aa,bb,t)
        lam=np.linalg.eigvalsh(matrix(p,q)+np.diag(u))[0]
        assert abs(lam-t)<2e-8,(p,q,t,lam,u)
        counts['eigen']+=1
        # Separate constrained numerical optimization at fixed target
        a=np.r_[aa,bb]
        sol=minimize(lambda z:float(a@z),u+0.01,method='SLSQP',bounds=[(0,None)]*len(u),
            constraints={'type':'ineq','fun':lambda z:np.linalg.eigvalsh(matrix(p,q)+np.diag(z))[0]-t},
            options={'maxiter':300,'ftol':1e-10})
        assert sol.success and abs(float(a@sol.x)-cost)<1e-5,(p,q,t,cost,sol.message,float(a@sol.x))
        counts['opt']+=1
        for i in range(p):
          for j in range(p):
            if aa[i]<aa[j]-1e-12:
              assert u[i]>=u[j]-1e-12
              if u[j]>1e-12: assert u[i]>1e-12
              counts['support']+=1
        for i in range(q):
          for j in range(q):
            if bb[i]<bb[j]-1e-12:
              assert u[p+i]>=u[p+j]-1e-12
              if u[p+j]>1e-12: assert u[p+i]>1e-12
              counts['support']+=1
        Ta=np.sum(np.sqrt(aa));Tb=np.sum(np.sqrt(bb))
        all_t=max(0,q-Tb/math.sqrt(np.max(aa)),p-Ta/math.sqrt(np.max(bb)))
        if t>=all_t+1e-8:
          aff=(np.sum(aa)+np.sum(bb))*t-q*np.sum(aa)-p*np.sum(bb)+2*Ta*Tb
          assert abs(aff-cost)<1e-7,(aff,cost,t,all_t)
          counts['high']+=1
    for it in range(200):
      p,q=rng.randrange(2,12),rng.randrange(2,12)
      al,be=math.exp(rng.uniform(-3,2)),math.exp(rng.uniform(-3,2))
      if al==be:be*=1.05
      t=rng.uniform(.0001,10)
      cost,u,*_=target([al]*p,[be]*q,t)
      if al<be:
        tc=p*(1-math.sqrt(al/be))
        if t<=tc:
          expected=al*p*t*(p+q-t)/(p-t)
          assert np.max(abs(u[p:]))<1e-8
        else:
          expected=(al*p+be*q)*t-p*q*(math.sqrt(be)-math.sqrt(al))**2
      else:
        tc=q*(1-math.sqrt(be/al))
        if t<=tc:
          expected=be*q*t*(p+q-t)/(q-t)
          assert np.max(abs(u[:p]))<1e-8
        else:
          expected=(al*p+be*q)*t-p*q*(math.sqrt(be)-math.sqrt(al))**2
      assert abs(expected-cost)<1e-7,(cost,expected,al,be,p,q,t,tc)
      counts['two_price']+=1
    # Exact-rational two-price branch and high-target KKT identities.
    for p in range(2,9):
      for q in range(2,9):
        for t in (Q(p,4), Q(p,2), Q(p,2)+Q(1,3)):
          if t<=Q(p,2):
            a=t*(p+q-t)/(p-t)
            x=q+a-t; y=p-t
            assert Q(p,1)/x*Q(q,1)/y==1
            assert p*a==p*t*(p+q-t)/(p-t)
          else:
            a=t+q; b=t-Q(p,2)
            x=q+a-t; y=p+b-t
            assert Q(p,1)/x*Q(q,1)/y==1
            assert p*a+4*q*b==(p+4*q)*t-p*q
          counts['exact']+=1
        ka=[(j%4)+1 for j in range(p)]; kb=[(j%3)+2 for j in range(q)]
        ta=sum(ka); tb=sum(kb); t=Q(max(p,q)+1)
        xs=[Q(tb,k) for k in ka]; ys=[Q(ta,k) for k in kb]
        assert sum((Q(1)/x for x in xs),Q(0))*sum((Q(1)/y for y in ys),Q(0))==1
        assert len(set((ka[i]**2*xs[i]**2 for i in range(p))))==1
        assert len(set((kb[i]**2*ys[i]**2 for i in range(q))))==1
        counts['exact']+=1
    print('PASS',counts)

if __name__=='__main__':test_many()
