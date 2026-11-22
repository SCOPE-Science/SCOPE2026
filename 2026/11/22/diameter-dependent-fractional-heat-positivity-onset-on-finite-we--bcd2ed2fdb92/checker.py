"""Numerical corroboration of a fractional graph-heat positivity onset theorem.

Requires NumPy and SciPy. Finite tests supplement but do not certify an infinite proof.
"""
import math
import numpy as np
from scipy.linalg import eigh
from scipy.optimize import brentq


def graph_laplacian(n, edges):
    W=np.zeros((n,n),dtype=float)
    for i,j,w in edges:
        assert 0 <= i < n and 0 <= j < n and i != j and w > 0
        W[i,j]=W[j,i]=float(w)
    return np.diag(W.sum(axis=1))-W, W


def shortest_paths(W):
    n=len(W)
    d=np.full((n,n),1000,dtype=int)
    for i in range(n):
        d[i,i]=0
        for j in range(n):
            if W[i,j]>0:
                d[i,j]=1
    for k in range(n):
        d=np.minimum(d,d[:,k,None]+d[None,k,:])
    return d


def properties(L,W):
    lam,Q=eigh(L)
    lam=np.where(lam<1e-11,0,lam)
    d=shortest_paths(W)
    bvals=np.where(lam>0,lam*np.log(np.maximum(lam,1e-100)),0)
    B=(Q*bvals)@Q.T
    out=[]
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            k=d[i,j]
            if k<2: continue
            a=np.linalg.matrix_power(W,k)[i,j]/math.factorial(k)
            b=B[i,j]
            assert a>0 and b>0,(i,j,k,a,b)
            const=(b/a)**(1/(k-1))
            out.append((i,j,k,a,b,const))
    def F(i,j,t,eps):
        weights=np.exp(-t*np.power(lam,1+eps))
        return float(np.sum(Q[i,:]*Q[j,:]*weights))
    return out,F


def cases():
    for n in [3,4,5,6,7]:
        yield f'path-{n}',graph_laplacian(n,[(i,i+1,1) for i in range(n-1)])
    yield 'weighted-path',graph_laplacian(5,[(0,1,0.6),(1,2,1.4),(2,3,0.8),(3,4,1.8)])
    yield 'C6',graph_laplacian(6,[(i,(i+1)%6,1) for i in range(6)])
    yield 'C7',graph_laplacian(7,[(i,(i+1)%7,1) for i in range(7)])
    yield 'star',graph_laplacian(6,[(0,i,1.0+0.2*i) for i in range(1,6)])
    yield 'diamond',graph_laplacian(4,[(0,1,1),(0,2,1),(1,2,1),(1,3,1),(2,3,1)])
    yield 'bipartite',graph_laplacian(6,[(i,j,1) for i in range(2) for j in range(2,6)])
    yield 'branched-tree',graph_laplacian(7,[(0,1,1),(1,2,1),(1,3,1),(3,4,1),(3,5,1),(5,6,1)])


def main():
    total_pairs=0
    checks=0
    print('P4 exact endpoint constant:',math.sqrt(1.5*math.log(2)))
    for name,(L,W) in cases():
        info,F=properties(L,W)
        assert info
        diameter=max(row[2] for row in info)
        # At small eps, compare first and last signs and local root with predicted onset.
        for eps in [0.001,0.003,0.01,0.03]:
            roots=[]
            for i,j,d,a,b,c in info:
                scale=eps**(1/(d-1))
                lo=c*scale*0.1
                hi=c*scale*3.0
                flo=F(i,j,lo,eps)
                fhi=F(i,j,hi,eps)
                # Cancellation is at most 1e-16 in spectral sums; test safely away from 0.
                assert flo<-1e-12 or (abs(flo)<1e-12 and d>=5),(name,eps,i,j,d,lo,flo)
                assert fhi>0,(name,eps,i,j,d,hi,fhi)
                root=brentq(lambda t:F(i,j,t,eps),lo,hi,xtol=1e-13)
                roots.append((d,root))
                if eps <=0.003:
                    assert abs(root/(c*scale)-1)<0.50,(name,eps,d,root/(c*scale))
                # Sample sign behavior over a geometric time grid up to large-time positive regime.
                tgrid=np.geomspace(lo,20,70)
                values=np.array([F(i,j,t,eps) for t in tgrid])
                assert np.all(values[tgrid <0.85*root]<1e-10)
                assert np.all(values[tgrid >1.15*root]>-1e-10)
                checks+=len(values)+4
            diam_roots=[r for d,r in roots if d==diameter]
            if diameter>2 and eps <=0.003:
                assert max(diam_roots)>=max(r for d,r in roots if d<diameter)
            # All edges are positive throughout the sampled time range.
            vals,Q=eigh(L)
            for i in range(len(L)):
                for j in range(i+1,len(L)):
                    if W[i,j]>0:
                        for t in [1e-4,0.01,0.1,1,5,20]:
                            g=float(np.sum(Q[i]*Q[j]*np.exp(-t*np.maximum(vals,0)**(1+eps))))
                            assert g>0,(name,eps,i,j,t,g)
                            checks+=1
        total_pairs+=len(info)
        print(name,'diameter',diameter,'nonedge pairs',len(info),'largest coefficient',round(max(row[5] for row in info if row[2]==diameter),9))
    print('PASS',len(list(cases())),'graphs',total_pairs,'nonedge pairs,',checks,'numerical assertions/evaluations')


if __name__=='__main__':main()
