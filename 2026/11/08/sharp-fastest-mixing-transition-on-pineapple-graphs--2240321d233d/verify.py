#!/usr/bin/env python3
"""Reproducible supplementary exact and numerical checks of pineapple FMMC formulas."""
from fractions import Fraction as F
from math import sqrt
import random
import numpy as np

def optimum(a,r):
    assert a>=2 and r>=2
    if r<=a:
        h=4*a*r+a+r
        return F(2*r+1,h),F(2*a+1,h),F(4*a*r-1,h)
    u=F(1,a+r)
    return u,u,1-u

def make_matrix(a,r,p,q,s):
    n=1+a+r
    P=np.zeros((n,n),float)
    for i in range(1,a+1):
        P[0,i]=P[i,0]=float(p)
    for i in range(a+1,n):
        P[0,i]=P[i,0]=float(q)
    for i in range(1,a+1):
        for j in range(i+1,a+1):
            P[i,j]=P[j,i]=float(s)
    for i in range(n):P[i,i]=1-P[i,:].sum()
    assert np.min(P)>-1.e-11
    return P

def score(P):
    vals=np.linalg.eigvalsh(P)
    return max(abs(vals[:-1]))

def check():
    from sympy import symbols, factor, diff
    a,r,t,q=symbols('a r t q',positive=True)
    n=a+r+1; h=4*a*r+a+r
    G=-n*r*q*q+(n+(r-a)*t)*q-(a+1)*t+a*t*t
    checks=0
    assert factor(G.subs(t,n/h)+n*r*(q-(2*a+1)/h)**2)==0;checks+=1
    u=1/(a+r)
    assert factor(G.subs({q:u,t:u}))==0;checks+=1
    assert factor(diff(G,q).subs({q:u,t:u})-(a-r))==0;checks+=1
    assert factor((n/h-u)-(a-r)**2/((a+r)*h))==0;checks+=1
    assert factor(a*(2*r+1)/h+r*(2*a+1)/h-1)==0;checks+=1
    rnd=random.Random(20261106)
    cases=0;comparisons=0
    for aa in range(2,13):
      for rr in range(2,13):
        p,qp,mu=optimum(aa,rr)
        s=(1-p)/aa
        P=make_matrix(aa,rr,p,qp,s)
        assert abs(score(P)-float(mu))<4e-12, (aa,rr,score(P),mu)
        # all nontrivial eigenvalues from quotient and transverse decomposition
        z=(aa+1)*p+(rr+1)*qp
        disc=z*z-4*(aa+rr+1)*p*qp
        alpha_minus=(float(z)-sqrt(float(disc)))/2
        alpha_plus=(float(z)+sqrt(float(disc)))/2
        expected=sorted([1.0,1-alpha_minus,1-alpha_plus]+[1-float(qp)]*(rr-1)+[1-float(p+aa*s)]*(aa-1))
        actual=sorted(np.linalg.eigvalsh(P))
        assert max(abs(x-y) for x,y in zip(actual,expected))<4e-12
        cases+=1
        if aa+rr<=12:
          for _ in range(60):
            # Build a random symmetric feasible transition matrix, not invariant.
            k=aa+rr+1
            B=np.zeros((k,k))
            edges=[(0,j) for j in range(1,k)]+[(i,j) for i in range(1,aa+1) for j in range(i+1,aa+1)]
            weights=[rnd.uniform(.01,1) for _ in edges]
            norm=max(sum(w for (i,j),w in zip(edges,weights) if i==v or j==v) for v in range(k))
            weights=[w/(norm*rnd.uniform(1,1.25)) for w in weights]
            for (i,j),w in zip(edges,weights):B[i,j]=B[j,i]=w
            for i in range(k):B[i,i]=1-B[i,:].sum()
            assert score(B)+2e-10>=float(mu), (aa,rr,score(B),mu)
            comparisons+=1
    return checks,cases,comparisons

if __name__=='__main__':
    a,b,c=check()
    print('VERIFY_OK symbolic_identities=%d exact_parameter_cases=%d noninvariant_competitors=%d'%(a,b,c))
