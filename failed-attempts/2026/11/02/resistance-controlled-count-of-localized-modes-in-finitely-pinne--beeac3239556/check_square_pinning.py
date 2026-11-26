"""Independent finite-grid checks for two-dimensional lattice pinning thresholds.

Requires numpy and scipy. Run: python check_square_pinning.py
All reported comparison results are finite-dimensional tests, not an infinite-lattice proof.
"""
import math
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh


def periodic_resistance(n, displacement):
    grid=2*np.pi*np.arange(n)/n
    a=2-2*np.cos(grid)
    denom=a[:,None]+a[None,:]
    phase=np.cos(displacement[0]*grid[:,None]+displacement[1]*grid[None,:])
    with np.errstate(divide='ignore',invalid='ignore'):
        t=2*(1-phase)/denom
    t[0,0]=0.
    return float(np.sum(t)/(n*n))


def defect_matrix(positions, strength, n=144):
    # Discrete resistance approximation, independently Fourier-evaluated.
    p=len(positions)
    R=np.zeros((p,p))
    for i in range(p):
        for j in range(i):
            d=tuple(positions[i][k]-positions[j][k] for k in range(2))
            R[i,j]=R[j,i]=periodic_resistance(n,d)
    # Orthonormal basis of sum-zero vectors via SVD.
    V=np.linalg.svd(np.ones((1,p)), full_matrices=True)[2].T[:,1:]
    threshold_matrix=V.T @ (-R/2-np.eye(p)/strength) @ V
    return np.linalg.eigvalsh(threshold_matrix)


def top_periodic_eigenvalues(n, positions, strength, requested=5):
    # Independent real-space sparse operator with periodic boundaries.
    ids=np.arange(n*n).reshape(n,n)
    xx,yy=np.indices((n,n))
    rows=np.repeat(ids.ravel(),5)
    cols=np.concatenate([ids.ravel(),
                         np.roll(ids,1,axis=0).ravel(), np.roll(ids,-1,axis=0).ravel(),
                         np.roll(ids,1,axis=1).ravel(), np.roll(ids,-1,axis=1).ravel()])
    # The sparse construction below groups entries in blocks rather than per row.
    rows=np.tile(ids.ravel(),5)
    vals=np.concatenate([4*np.ones(n*n),-np.ones(4*n*n)])
    H=sparse.coo_matrix((vals,(rows,cols)),shape=(n*n,n*n)).tocsr()
    if not np.allclose((H-H.T).data,0,atol=1e-12):
        raise AssertionError('not symmetric')
    diagonal=np.zeros(n*n)
    for a,b in positions:diagonal[ids[a % n,b % n]]+=strength
    H=H+sparse.diags(diagonal)
    return np.sort(eigsh(H,k=requested,which='LA',return_eigenvectors=False,tol=2e-10))


def main():
    count=0
    for n in (100,200,400,800):
        for d, target in [((1,0),0.5),((1,1),2/math.pi)]:
            result=periodic_resistance(n,d)
            assert abs(result-target)<1.5/n
            count+=1
    pos=((0,0),(1,0),(0,1))
    threshold=(math.pi,3*math.pi/(math.pi-1))
    for n in (100,200,400):
        for gamma in (2.0,3.5,5.0,6.0):
            predicted=1+sum(gamma>c for c in threshold)
            actual=1+np.count_nonzero(defect_matrix(pos,gamma,n)>1e-8)
            assert predicted==actual,(n,gamma,predicted,actual)
            count+=1
    for gamma, expected in [(2.,1),(3.5,2),(6.,3)]:
        eigenvalues=top_periodic_eigenvalues(70,pos,gamma)
        measured=int(np.count_nonzero(eigenvalues>8+1e-7))
        assert measured==expected,(gamma,eigenvalues,expected)
        print('gamma',gamma,'top five eigenvalues',eigenvalues.tolist(),'above band',measured)
        count+=1
    print('checks passed:',count)
    print('exact thresholds:',threshold)

if __name__=='__main__':main()
