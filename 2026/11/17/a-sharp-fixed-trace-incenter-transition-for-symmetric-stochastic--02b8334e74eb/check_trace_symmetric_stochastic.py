"""Standalone verification of Euclidean radii of fixed-trace symmetric stochastic polytopes.

Only finite numerical checks are performed; the accompanying proof covers all n>=4.
Requires Python 3, numpy, scipy. Does not obtain results from any network service.
"""
from itertools import combinations
from math import sqrt
import numpy as np
from scipy.optimize import linprog


def constants(n):
    d = sqrt((n - 1) * (n - 2)) / n
    o = sqrt((n - 2) * (n*n - n + 2) / (2*n*n*(n - 1)))
    tc = n * sqrt(2) / (sqrt(n*n - n + 2) + sqrt(2))
    return d, o, tc


def independent_projected_norms(n):
    # Construct Frobenius-orthogonal projection onto the row-zero, trace-zero
    # symmetric subspace without using the claimed closed norm formulas.
    edges = [(i,j) for i in range(n) for j in range(i,n)]
    basis = []
    for i,j in edges:
        E = np.zeros((n,n))
        E[i,j]=1
        if i != j:
            E[j,i]=1
            E /= sqrt(2)
        basis.append(E)
    # These basis matrices are orthonormal in Frobenius inner product.
    B=np.zeros((n+1,len(edges)))
    for k,E in enumerate(basis):
        B[:n,k] = E.sum(axis=1)
        B[n,k] = np.trace(E)
    _,s,vt=np.linalg.svd(B,full_matrices=True)
    rank=int((s>1e-9).sum())
    assert rank == n+1
    kernel=vt[rank:].T
    target = []
    for i,j in [(0,0),(0,1)]:
        F=np.zeros((n,n))
        F[i,j]=1
        if i!=j:
            F[j,i]=1
            F/=2
        coordinates=np.array([np.sum(F*E) for E in basis])
        target.append(np.linalg.norm(kernel.T@coordinates))
    return tuple(target),len(edges)-rank


def linear_program(n, t, d, o):
    pairs = [(i,j) for i in range(n) for j in range(i,n)]
    m=len(pairs)
    Aeq=np.zeros((n+1,m+1))
    for k,(i,j) in enumerate(pairs):
        Aeq[i,k]=1
        if j!=i: Aeq[j,k]=1
        else: Aeq[n,k]=1
    beq=np.r_[np.ones(n),t]
    Aub=np.zeros((m,m+1))
    for k,(i,j) in enumerate(pairs):
        Aub[k,k]=-1
        Aub[k,-1]=d if i==j else o
    objective=np.r_[np.zeros(m),-1.]
    result=linprog(objective,A_ub=Aub,b_ub=np.zeros(m),A_eq=Aeq,b_eq=beq,bounds=[(None,None)]*(m+1),method='highs')
    assert result.success,result.message
    return result.x[-1],result.x[:-1],pairs


def main():
    checks=0
    for n in range(4,11):
        d,o,tc=constants(n)
        (d2,o2),dim=independent_projected_norms(n)
        assert abs(d-d2)<1e-11 and abs(o-o2)<1e-11
        assert dim == n*(n-1)//2-1
        for t in [0.01,0.3,0.9*tc,tc,1.1*tc,(tc+n)/2,n-.03]:
            if not 0<t<n: continue
            radius=min(t/(n*d),(n-t)/(n*(n-1)*o))
            v,entries,pairs=linear_program(n,t,d,o)
            assert abs(v-radius)<5e-8,(n,t,v,radius)
            # The explicit invariant center, not the LP center, is feasible.
            a=t/n;b=(n-t)/(n*(n-1))
            assert a>=d*radius-1e-11 and b>=o*radius-1e-11
            # In the low-trace regime the optimizer family is a rescaled
            # symmetric zero-diagonal row-stochastic polytope.
            if t < tc-1e-9:
                lamb=radius*o
                beta=1-t/n-(n-1)*lamb
                assert beta>0
                X=np.full((n,n),lamb+beta/(n-1))
                np.fill_diagonal(X,t/n)
                assert np.allclose(X.sum(axis=1),1)
                assert np.isclose(np.trace(X),t)
            checks+=1
    print(f'TRACE_SYMMETRIC_STOCHASTIC_PASS dimensions=4..10 exact_projection_norms=14 independent_LPs={checks} threshold_cases=7')

if __name__=='__main__':main()
