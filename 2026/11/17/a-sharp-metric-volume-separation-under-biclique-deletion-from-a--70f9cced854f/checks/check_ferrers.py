#!/usr/bin/env python3
"""Reproduce exact projection, face-volume and volume-loss formulas.

No external data are required.  Python dependencies: numpy, scipy, sympy.
"""
import itertools, math
from fractions import Fraction
import numpy as np
from scipy.optimize import minimize
import sympy as sp


def ideal_projection(a,b,s,t,i=0,j=0):
    u,v=a-s,b-t
    den=2*u*v+u+v
    theta=Fraction(v*(u+1),den)
    x=[Fraction(0) for _ in range(a)]
    y=[Fraction(0) for _ in range(b)]
    x[i]=theta
    y[j]=1-theta
    for h in range(s,a): x[h]=(1-theta)/u
    for h in range(t,b): y[h]=theta/v
    return x+y, Fraction((u+1)*(v+1),den)


def root_vertices(a,b,s,t):
    return [np.r_[np.eye(a)[i],np.eye(b)[j]]
        for i in range(a) for j in range(b) if i>=s or j>=t]


def finite_shuffle_probability(a,b,s,t):
    v=b-t
    n=a+b-2
    total=math.comb(n,a-1)
    return Fraction(sum(1 for pa in itertools.combinations(range(n),a-1)
        if sorted(pa)[s-1]>sorted(set(range(n))-set(pa))[v-1]), total)


def hypergeom_formula(a,b,s,t):
    v=b-t; N=a+b-2; K=s+v-1
    n=sum(math.comb(K,j)*math.comb(N-K,a-1-j) for j in range(s)
        if 0<=a-1-j<=N-K)
    return Fraction(n, math.comb(N,a-1))


def gram_det(u,v):
    a,b=u+1,v+1; s=t=1
    roots=root_vertices(a,b,s,t)
    # Face: (e_0,f_j) for all j>=1; (e_i,f_0) for all i>=1.
    # Convenient order in explicit ambient coordinates
    A=np.r_[np.eye(a)[0],np.eye(b)[1]]
    edges=[np.r_[np.eye(a)[0],np.eye(b)[j]]-A for j in range(2,b)]
    edges += [np.r_[np.eye(a)[i],np.eye(b)[0]]-A for i in range(1,a)]
    D=sp.Matrix(np.array(edges,dtype=int)).T
    return int((D.T*D).det())


def numerical_projection(a,b,s,t,i,j):
    vs=np.asarray(root_vertices(a,b,s,t))
    point=np.r_[np.eye(a)[i],np.eye(b)[j]]
    # Independently minimize over all convex coefficients of surviving vertices.
    N=len(vs)
    target=point
    def loss(w):
        residual=w@vs-target
        return 0.5*residual@residual
    def jac(w):
        return vs@(w@vs-target)
    res=minimize(loss,np.ones(N)/N,jac=jac,method='SLSQP',
        bounds=[(0,1)]*N,
        constraints=[{'type':'eq','fun':lambda w: w.sum()-1,
                      'jac':lambda w: np.ones_like(w)}],
        options={'ftol':1e-12,'maxiter':2000})
    assert res.success,(a,b,s,t,i,j,res.message)
    return res.x@vs,2*res.fun


def run():
    configurations=exact=qp=0
    maxerr=0.
    for a in range(2,8):
      for b in range(2,8):
        for s in range(1,a):
          for t in range(1,b):
            configurations+=1
            u,v=a-s,b-t
            # independent interleaving count and binomial-sum expression
            assert finite_shuffle_probability(a,b,s,t)==hypergeom_formula(a,b,s,t)
            assert gram_det(u,v)==2*u*v+u+v
            for i in range(s):
              for j in range(t):
                z,d2=ideal_projection(a,b,s,t,i,j)
                target=[Fraction(int(h==i)) for h in range(a)]+[Fraction(int(h==j)) for h in range(b)]
                assert sum((xx-zz)**2 for xx,zz in zip(target,z))==d2
                # Check all valid vertices have no larger projection-normal dot than projection.
                normal=[xx-zz for xx,zz in zip(target,z)]
                max_dot=max(sum(normal[k]*Fraction(int(k==h)) for k in range(a))+
                    sum(normal[a+k]*Fraction(int(k==l)) for k in range(b))
                    for h in range(a) for l in range(b) if h>=s or l>=t)
                z_dot=sum(xx*zz for xx,zz in zip(normal,z))
                assert max_dot==z_dot
                exact+=1
                if a<=5 and b<=5 and i==0 and j==0:
                    zopt,vopt=numerical_projection(a,b,s,t,i,j)
                    err=max(np.linalg.norm(zopt-np.array(z,dtype=float)),abs(vopt-float(d2)))
                    maxerr=max(maxerr,err)
                    assert err<1e-6,(a,b,s,t,err)
                    qp+=1
    print(f'FERRERS_DELETION_PASS configurations={configurations} exact_missing_vertices={exact} independent_QP={qp} max_gap={maxerr:.2e} exact_hypergeom_and_gram={configurations}')
if __name__=='__main__': run()
