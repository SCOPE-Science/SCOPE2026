"""Independent finite checks of weighted two-level poset transfer stability.
Run: python transfer_checker.py  (requires NumPy)."""
from itertools import product
from fractions import Fraction
import math
import numpy as np

def predicted(nlo, nhi, edges, weights):
    W = max([sum(float(weights[j])**2 for j in range(nhi) if (i,j) in edges)
             for i in range(nlo)]+[0.])
    return math.sqrt((2+W+math.sqrt(W*W+4*W))/2), W

def blocks(nlo, nhi, edges, weights):
    neigh = [tuple(i for i in range(nlo) if (i,j) in edges) for j in range(nhi)]
    possibilities = [n if n else (None,) for n in neigh]
    for assignment in product(*possibilities):
        B = np.eye(nlo+nhi)
        for j,i in enumerate(assignment):
            if i is not None:B[nlo+j,i] = -float(weights[j])
        yield B

def transfer(x,nlo,nhi,edges,weights):
    z=x.copy()
    for j in range(nhi):
        nb=[i for i in range(nlo) if (i,j) in edges]
        if nb:z[nlo+j] -= float(weights[j])*max(x[i] for i in nb)
    return z

def inverse(y,nlo,nhi,edges,weights):
    z=y.copy()
    for j in range(nhi):
        nb=[i for i in range(nlo) if (i,j) in edges]
        if nb:z[nlo+j] += float(weights[j])*max(y[i] for i in nb)
    return z

def main():
    patterns=0; assignments=0; pairs=0; maxima=0
    rng=np.random.default_rng(111121)
    vals=[Fraction(0),Fraction(1,3),Fraction(2,3),Fraction(1)]
    for nlo,nhi in [(1,1),(2,2),(2,3),(3,2),(3,3),(3,4)]:
        for mask in range(1<<(nlo*nhi)):
            # All 4096 bipartite graphs with 3+4, plus every smaller graph.
            edges={(i,j) for i in range(nlo) for j in range(nhi) if mask>>(i*nhi+j)&1}
            weights=[vals[(mask+3*j+2*nlo) % 4] for j in range(nhi)]
            L,W=predicted(nlo,nhi,edges,weights)
            best=0.
            for B in blocks(nlo,nhi,edges,weights):
                assignments+=1
                Lb=np.linalg.svd(B,compute_uv=False)[0]
                Linv=np.linalg.svd(np.linalg.inv(B),compute_uv=False)[0]
                assert abs(Lb-Linv)<2e-12
                best=max(best,Lb)
                assert Lb < L + 2e-12,(nlo,nhi,edges,weights,Lb,L)
            assert abs(best-L)<2e-12,(nlo,nhi,edges,weights,L,best)
            patterns+=1
            # Reverse and forward maps on strictly feasible sample pairs
            for _ in range(2):
                a=rng.uniform(.03,.20,nlo)
                b=rng.uniform(.45,.80,nhi)
                x=np.r_[a,b]
                x2=np.r_[np.clip(a+rng.normal(0,.015,nlo),.01,.3),
                            np.clip(b+rng.normal(0,.015,nhi),.35,.9)]
                y=transfer(x,nlo,nhi,edges,weights)
                y2=transfer(x2,nlo,nhi,edges,weights)
                assert np.linalg.norm(y-y2) <= L*np.linalg.norm(x-x2)+1e-12
                assert np.linalg.norm(x-x2) <= L*np.linalg.norm(y-y2)+1e-12
                assert np.linalg.norm(inverse(y,nlo,nhi,edges,weights)-x)<1e-13
                assert np.linalg.norm(inverse(y2,nlo,nhi,edges,weights)-x2)<1e-13
                pairs+=1
            if W>0:
                # Construct local interior differentiable points with all upper
                # neighbours of a maximal weighted-degree lower node selecting it.
                root=max(range(nlo),key=lambda i: sum(float(weights[j])**2 for j in range(nhi) if (i,j) in edges))
                a=np.array([.06+.01*i for i in range(nlo)],float)
                a[root]=.25
                x=np.r_[a,np.full(nhi,.7)]
                B=np.eye(nlo+nhi)
                for j in range(nhi):
                    nb=[i for i in range(nlo) if (i,j) in edges]
                    if nb:B[nlo+j,max(nb,key=lambda i:x[i])]=-float(weights[j])
                U,S,VT=np.linalg.svd(B)
                direction=VT[0]
                eps=1e-6
                x2=x+eps*direction
                y=transfer(x,nlo,nhi,edges,weights)
                y2=transfer(x2,nlo,nhi,edges,weights)
                assert abs(np.linalg.norm(y2-y)/np.linalg.norm(x2-x)-L)<2e-7
                maxima+=1
    # Star singular value is the positive root of z^2-(2+W)z+1
    for m in range(1,30):
        for t in [0.,0.2,0.5,1.]:
            w=np.full(m,t)
            B=np.eye(m+1);B[1:,0]=-w
            L,W=predicted(1,m,{(0,j) for j in range(m)},[Fraction(str(t))]*m)
            assert abs(np.linalg.svd(B,compute_uv=False)[0]-L)<1e-12
    print(f'TRANSFER_STABILITY_PASS graphs={patterns} Jacobians={assignments} interior_pairs={pairs} sharp_witnesses={maxima} weighted_stars=116')

if __name__=='__main__':main()
