#!/usr/bin/env python3
"""Independent discrete lattice killed-generator check of continuum moments."""
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import splu

def lattice_moments(N,L,v,lam):
    h=L/N; z=4*(N-1)
    A=lil_matrix((z,z),dtype=float)
    vel=(0,2*v,-2*v,0)
    flips=((1,2),(0,3),(0,3),(1,2))
    for j in range(1,N):
        for s in range(4):
            row=4*(j-1)+s
            A[row,row]=2*lam+abs(vel[s])/h
            for fs in flips[s]:A[row,4*(j-1)+fs]=-lam
            if vel[s]>0 and j<N-1:A[row,4*j+s]=-vel[s]/h
            if vel[s]<0 and j>1:A[row,4*(j-2)+s]=vel[s]/h
    solve=splu(A.tocsc()).solve
    m=solve(np.ones(z)); second=solve(2*m)
    return m.reshape(N-1,4), second.reshape(N-1,4)

def exact(L,v,lam):
    r=lam*L/v
    mean=(r*r+6*r+3)/(12*r)*L/v
    m2=(r**4+10*r**3+30*r*r+30*r+15)/(60*r*r)*(L/v)**2
    return mean,m2

if __name__=='__main__':
    assert exact(1,1,1)[0] == 10/12
    for L,v,lam in [(1,1,.5),(2,3,4),(1,2,10),(5,1,.03)]:
        old=None
        for N in [60,120,240]:
            a,b=lattice_moments(N,L,v,lam)
            check=np.array([a.mean(),b.mean()])
            expected=np.array(exact(L,v,lam))
            err=np.max(np.abs(check-expected))
            print(L,v,lam,N,'mean_and_E2',*check,'target',*expected,'err',err)
            if old is not None: assert err<.60*old
            old=err
    print('Separate finite-volume calculations completed; 12 parameter/mesh pairs and two moments per pair')
