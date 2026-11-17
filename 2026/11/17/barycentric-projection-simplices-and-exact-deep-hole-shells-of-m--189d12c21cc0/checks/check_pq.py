#!/usr/bin/env python3
"""Independent finite checks of Euclidean metric geometry of complete-multipartite PQ polytopes.

The script constructs all permitted graph edge generators and independently minimizes
Euclidean distance over their convex coefficients. It also checks the exact dual
projection certificate and face affine rank for every missing generator.
"""
from fractions import Fraction
from itertools import product
from math import factorial, sqrt
import numpy as np
from scipy.optimize import minimize
from scipy.linalg import null_space


def run(parts):
    n=sum(parts); group=sum(([s]*p for s,p in enumerate(parts)),[])
    pairs=[(a,b) for a in range(n) for b in range(n) if a==b or group[a]!=group[b]]
    W=np.zeros((2*n,len(pairs)))
    for t,(a,b) in enumerate(pairs): W[a,t]=1; W[n+b,t]=1
    objective=lambda w, x: np.sum((W@w-x)**2)
    c=0
    for i in range(n):
      for j in range(n):
        x=np.zeros(2*n); x[i]=x[n+j]=1
        if group[i]!=group[j] or i==j: continue
        c+=1
        q=n-parts[group[i]];a=Fraction(1,2*(q+1))
        F=[(i,i),(j,j)]+[(i,h) for h in range(n) if group[h]!=group[i]]+[(h,j) for h in range(n) if group[h]!=group[i]]
        assert len(F)==2*q+2 and len(set(F))==len(F)
        xproj=np.zeros(2*n)
        for u,v in F: xproj[u]+=float(a); xproj[n+v]+=float(a)
        exact=Fraction(q+2,2*(q+1))
        assert abs(np.dot(x-xproj,x-xproj)-float(exact))<1e-11
        # Exact supporting-gradient inequalities, independent of floating point optimizer
        r=x-xproj
        scores=[r[u]+r[n+v] for u,v in pairs]
        h=max(scores)
        active={pairs[t] for t,v in enumerate(scores) if abs(v-h)<1e-10}
        assert active==set(F)
        assert np.max(np.abs([r[u]+r[n+v]-h for u,v in F]))<1e-10
        mat=np.array([W[:,pairs.index(t)] for t in F]).T
        assert np.linalg.matrix_rank(mat[:,1:]-mat[:,[0]])==2*q+1
        gram=(mat[:,1:]-mat[:,[0]]).T@(mat[:,1:]-mat[:,[0]])
        det=np.linalg.det(gram)
        assert abs(det-2*(q+1)*(q+2))<1e-6
        # Independent optimization over ALL allowed edge coefficient weights
        w0=np.full(len(pairs),1/len(pairs))
        solution=minimize(lambda w:objective(w,x),w0,method='SLSQP',
          bounds=[(0,None)]*len(pairs),
          constraints={'type':'eq','fun':lambda w:sum(w)-1},
          options={'ftol':1e-12,'maxiter':900})
        assert solution.success,(parts,i,j,solution.message)
        assert abs(solution.fun-float(exact))<1e-8,(parts,i,j,solution.fun,exact)
        assert np.linalg.norm(W@solution.x-xproj)<2e-5
    return c

def main():
  # Partitions have multiple repeated classes, asymmetries, singleton and two-class cases.
  cases=[(2,1),(3,1),(2,2),(3,2),(4,1),(3,1,1),(2,2,1),(4,2),(3,3),
         (2,2,2),(3,2,1),(4,1,1),(2,3,2),(3,3,1),(4,2,1),(3,2,2,1)]
  checks=0
  for p in cases: checks+=run(p)
  print(f'PQ_MULTIPARTITE_METRIC_PASS cases={len(cases)} missing_vertices={checks} exact_dual_and_affine_and_gram={checks} independent_QP={checks}')
if __name__=='__main__':main()
