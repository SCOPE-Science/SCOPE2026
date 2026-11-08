#!/usr/bin/env python3
"""Independent numerical verification of three-boson complete-network loss identities."""
import itertools, math
import numpy as np
from scipy.linalg import null_space

def run(n):
    states=[a for a in itertools.combinations_with_replacement(range(n),3)]
    dim=len(states)
    occupations=[]
    for t in states:
        occ=[0]*n
        for x in t:occ[x]+=1
        occupations.append(tuple(occ))
    index={x:i for i,x in enumerate(occupations)}
    H=np.zeros((dim,dim));
    for j,occ in enumerate(occupations):
        for src in range(n):
            if occ[src]==0:continue
            for dst in range(n):
                if src==dst:continue
                w=list(occ); w[src]-=1;w[dst]+=1
                H[index[tuple(w)],j]+=np.sqrt(occ[src]*(occ[dst]+1))
    assert np.max(np.abs(H-H.T))<1e-12
    vals,vecs=np.linalg.eigh(H)
    diagidx=[index[tuple(3 if i==v else 0 for i in range(n))] for v in range(n)]
    dark=np.zeros((dim,dim)); rs=[]
    for r in range(4):
        E=3*(n-1)-n*r
        cols=vecs[:,np.abs(vals-E)<1e-7]
        assert cols.shape[1]==math.comb(n+r-2,r), (r,cols.shape)
        C=cols[diagidx,:]
        z=null_space(C, rcond=1e-9)
        Q=cols@z
        dark+=Q@Q.T
        rs.append((cols.shape[1],np.linalg.matrix_rank(C,tol=1e-8)))
    d=dim-3*n
    if n<=6:
        # Site-dependent positive rates: exactly d spectral poles are undamped.
        rates=np.array([0.5+0.23*v for v in range(n)])
        Gamma=np.zeros(dim)
        Gamma[diagidx]=rates
        spectra=np.linalg.eigvals(H-0.5j*np.diag(Gamma))
        assert np.sum(np.abs(np.imag(spectra))<1e-8)==d,(n,spectra)
    assert abs(np.trace(dark)-d)<1e-7,(n,np.trace(dark),d)
    assert np.max(np.abs(dark@dark-dark))<1e-8
    patterns=[('same',(0,0,0),1),('double',(0,0,1),(n*n-2*n+2)/((n-1)*(n*n-3*n+3))),('distinct',(0,1,2),6*(n-2)/((n-1)*(n*n-3*n+3)))]
    for typ,t,expected in patterns:
        actual=1-dark[index[tuple([t.count(v) for v in range(n)])],index[tuple([t.count(v) for v in range(n)])]]
        assert abs(actual-expected)<1e-8,(n,typ,actual,expected)
        print(n,typ, 'eta=',round(actual,12),'exact=',round(expected,12))
    print('n',n,'dark',d,'sector dims, ranks',rs)
    return True
for n in range(3,9):run(n)
print('ALL TESTS PASS')
