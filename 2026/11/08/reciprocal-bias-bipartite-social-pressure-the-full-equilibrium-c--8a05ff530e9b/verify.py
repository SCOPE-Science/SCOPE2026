#!/usr/bin/env python3
"""Exact algebra and independent time integration for reciprocal-bias opinion flow.
All calculations are on the *deterministic* flow; no inference about stochastic urn trajectories.
Run: python verify.py
"""
from fractions import Fraction as Q
from random import Random
from math import exp, sqrt

def f(z,g):
    return g*z/(1+(g-1)*z)

def check_rational():
    r=Random(4481)
    n=0
    for _ in range(12000):
        g=Q(r.randint(2,14),r.randint(1,5))
        if g<=1: continue
        a=Q(r.randint(0,30),30); b=Q(r.randint(0,30),30)
        k=g-1; L=g-k*a; H=1+k*b; R=H/L
        da=f(b,g)-a
        db=f(a,1/g)-b
        assert db*L+H*da==0
        assert (-2*k*L*da)==2*(g/R-L*L)
        assert R>=1/g and R<=g
        for q in [Q(0),Q(1,3),Q(1,2),Q(1)]:
            # At exponential phase q=e^{-2t}, the mean-formula squared identity.
            L2=g/R+(L*L-g/R)*q
            assert L2>=1 and L2<=g*g
        n+=1
    return n

def exact(t, aa,bb,g):
    a0=sum(aa)/len(aa); b0=sum(bb)/len(bb)
    k=g-1; L0=g-k*a0; H0=1+k*b0; R=H0/L0
    L=sqrt(g/R+(L0*L0-g/R)*exp(-2*t))
    a=(g-L)/k; b=(R*L-1)/k
    return [a+exp(-t)*(x-a0) for x in aa]+[b+exp(-t)*(x-b0) for x in bb]

def rhs(x,na,nb,g):
    a=sum(x[:na])/na; b=sum(x[na:])/nb
    return [f(b,g)-v for v in x[:na]]+[f(a,1/g)-v for v in x[na:]]

def rk4(x,h,na,nb,g):
    k1=rhs(x,na,nb,g)
    k2=rhs([u+h*v/2 for u,v in zip(x,k1)],na,nb,g)
    k3=rhs([u+h*v/2 for u,v in zip(x,k2)],na,nb,g)
    k4=rhs([u+h*v for u,v in zip(x,k3)],na,nb,g)
    return [u+h*(v1+2*v2+2*v3+v4)/6 for u,v1,v2,v3,v4 in zip(x,k1,k2,k3,k4)]

def check_trajectories():
    rng=Random(924)
    count=0
    for na in range(1,6):
      for nb in range(1,6):
       for g in [1.1,1.5,2.,4.,12.]:
        for _ in range(2):
         aa=[rng.random() for __ in range(na)]
         bb=[rng.random() for __ in range(nb)]
         x=aa+bb
         h=.002; t=0.
         for step in range(2000):
          x=rk4(x,h,na,nb,g)
          t=(step+1)*h
          if step in (99,499,999,1999):
           ex=exact(t,aa,bb,g)
           assert max(abs(v-w) for v,w in zip(x,ex))<2e-9,(na,nb,g,step,x,ex)
           assert min(x)>0 and max(x)<1
         count+=1
    # exactly at the all-zero and all-one boundaries
    for g in [2,3.7]:
        for fixed in [0.,1.]:
            vals=exact(5.,[fixed]*3,[fixed]*2,g)
            assert max(abs(v-fixed) for v in vals)<2e-15
    return count

def check_bipartite_fixed():
    rng=Random(539)
    checks=0
    for na in range(1,7):
      for nb in range(1,7):
       for _ in range(35):
        g=Q(rng.randint(2,15),rng.randint(1,8))
        if g<=1: g=Q(9,4)
        a=Q(rng.randint(0,100),100)
        b=f(a,1/g)
        # connected bipartite graph with full positive rational edges;
        # every row normalization must respect the equilibrium.
        weights=[[Q(rng.randint(1,7)) for j in range(nb)] for i in range(na)]
        for i in range(na):
            z=sum(w*b for w in weights[i])/sum(weights[i]); assert f(z,g)==a
        for j in range(nb):
            z=sum(weights[i][j]*a for i in range(na))/sum(weights[i][j] for i in range(na))
            assert f(z,1/g)==b
        checks+=1
    return checks

if __name__=='__main__':
    x=check_rational(); y=check_trajectories(); z=check_bipartite_fixed()
    print('VERIFY_OK exact_identities=%d independent_trajectories=%d weighted_graph_equilibria=%d' %(x,y,z))
