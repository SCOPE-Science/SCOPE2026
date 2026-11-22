#!/usr/bin/env python3
"""Independent full-matrix and factorized-spectrum checks for two hard-core excitations on a complete split network."""
from itertools import combinations
import numpy as np
import sympy as sp

def build(r,m):
    n=r+m
    adj=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if i<r or j<r: adj[i][j]=adj[j][i]=1
    pairs=list(combinations(range(n),2)); at={a:i for i,a in enumerate(pairs)}
    H=sp.zeros(len(pairs))
    for a,(x,y) in enumerate(pairs):
        for z in range(n):
            if z!=y and adj[x][z]:H[a,at[tuple(sorted((z,y)))]]=1
            if z!=x and adj[y][z]:H[a,at[tuple(sorted((x,z)))]]=1
    return H,pairs

def predicted(r,m):
    x=sp.Symbol('x');
    FA=(x-(r-4))*(x+1)-m*(r-2)
    FB=x*(x-r+1)-r*(m-2)
    F3=(x-2*r+4)*(x*(x-r+1)-2*r*(m-1))-2*m*(r-1)*x
    return sp.Poly((x+2)**(r*(r-3)//2)*(x+1)**((r-1)*(m-1))*x**(m*(m-3)//2)*FA**(r-1)*FB**(m-1)*F3,x)

def verify():
    cases=0
    for r in range(3,7):
      for m in range(3,7):
        H,pairs=build(r,m)
        # All characteristic coefficients checked as exact integers for selected small cases
        if (r,m) in [(3,3),(3,4),(4,3),(4,4),(5,3)]:
            assert H.charpoly(sp.Symbol("x")).as_poly()==predicted(r,m),(r,m)
        roots=np.linalg.eigvalsh(np.array(H,dtype=float))
        exp=[]
        for rt,mult in sp.polys.polytools.intervals(predicted(r,m),eps=sp.Rational(1,100000000)):
            mid=float((rt[0]+rt[1])/2)
            exp.extend([mid]*mult)
        assert len(roots)==len(exp)
        assert max(abs(a-b) for a,b in zip(roots,exp))<1e-7,(r,m)
        # The BB dark projector has constant diagonal and precisely the predicted dimension.
        BB=[i for i,(a,b) in enumerate(pairs) if a>=r]
        U=sp.zeros(m,len(BB))
        for k,ii in enumerate(BB):
          a,b=pairs[ii]
          U[a-r,k]=U[b-r,k]=1
        assert U.rank()==m
        P=sp.eye(len(BB))-U.T*(U*U.T).inv()*U
        assert all(P[i,i]==sp.Rational(m-3,m-1) for i in range(len(BB)))
        assert P*P==P and U*P==sp.zeros(m,len(BB))
        # Spectral evolution of localized peripheral pairs retains the dark fraction.
        if (r,m) in [(3,4),(4,5),(5,6)]:
          vv,WW=np.linalg.eigh(np.asarray(H,dtype=float))
          one=np.zeros(H.rows); one[BB[0]]=1
          dfrac=float(sp.Rational(m-3,m-1))
          for t in [0.0,0.5,1.2,3.7,9.1]:
            state=WW@((np.exp(-1j*t*vv))*(WW.T@one))
            assert sum(abs(state[k])**2 for k in BB)>=dfrac-1e-9
        d=m*(m-3)//2
        assert len(U.nullspace())==d
        # Every BB null-incidence vector is annihilated by the actual full H.
        for z in U.nullspace():
          full=sp.zeros(H.rows,1)
          for k,ii in enumerate(BB):full[ii]=z[k]
          assert H*full==sp.zeros(H.rows,1)
        # All other characteristic blocks are invertible at zero.
        assert H.nullspace().__len__()==d
        cases+=1
    print('PASS: 16 independent matrix vs factorization cases, 5 exact charpolys, full dark eigenspaces.')
if __name__=='__main__':verify()
