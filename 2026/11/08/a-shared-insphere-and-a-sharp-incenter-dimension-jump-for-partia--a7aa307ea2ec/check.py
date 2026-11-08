"""Independent finite-dimensional checks for partial alternating-sign-matrix inspheres.

Dependency: scipy>=1.9, numpy>=1.21; invoked with python check.py.
The all-dimensions proof is in RESULT.md, not in this script.
"""
from math import sqrt, isclose
import numpy as np
from scipy.optimize import linprog


def pasm_constraints(m, n):
    """Return A,b: A @ flattened(x) <= b (all row/column prefix constraints)."""
    A, b = [], []
    for i in range(m):
        for j in range(n):
            row = np.zeros((m, n)); row[:i + 1, j] = 1
            for s in (-1, 1):
                A.append(s * row.flatten()); b.append(int(s == 1))
            row = np.zeros((m, n)); row[i, :j + 1] = 1
            for s in (-1, 1):
                A.append(s * row.flatten()); b.append(int(s == 1))
    return np.array(A), np.array(b)


def pperm_constraints(m,n):
    A,b = [],[]
    for i in range(m):
        for j in range(n):
            z = np.zeros((m,n)); z[i,j]=-1
            A.append(z.flatten()); b.append(0)
    for i in range(m):
        z=np.zeros((m,n)); z[i,:]=1
        A.append(z.flatten()); b.append(1)
    for j in range(n):
        z=np.zeros((m,n)); z[:,j]=1
        A.append(z.flatten()); b.append(1)
    return np.array(A), np.array(b)


def solve(m,n,typ):
    A,b=(pasm_constraints if typ=='pasm' else pperm_constraints)(m,n)
    vals=np.linalg.norm(A,axis=1)
    aub=np.column_stack([A,vals]); obj=np.zeros(m*n+1); obj[-1]=-1
    ans=linprog(obj,A_ub=aub,b_ub=b,bounds=[(None,None)]*(m*n)+[(0,None)],method='highs')
    assert ans.success, (m,n,typ,ans.message)
    r=1/(max(m,n)+sqrt(max(m,n)))
    assert abs(ans.x[-1]-r)<3e-9, (m,n,typ,ans.x[-1],r)
    uniform=np.full(m*n,r)
    assert np.max(A@uniform+vals*r-b)<1e-9, (m,n,typ)
    return A,b,r


def witness(m,n):
    r=1/(max(m,n)+sqrt(max(m,n)))
    x=np.full((m,n),r)
    eps=r/(100*m*n)
    if m<n:
        x[1:,0]=r+eps
        x[1:,1:]=r-2*eps/(n-1)
    elif m>n:
        x[0,1:]=r+eps
        x[1:,1:]=r-2*eps/(m-1)
    elif m>1:
        x[1:,1:]=r-eps
    return x


def forced_and_rank(m,n):
    A,b=pasm_constraints(m,n)
    r=1/(max(m,n)+sqrt(max(m,n)))
    x=witness(m,n).flatten()
    norm=np.linalg.norm(A,axis=1)
    gap=b-A@x-r*norm
    assert np.min(gap)>-1e-9, (m,n,np.min(gap))
    active=abs(gap)<1e-9
    rank=np.linalg.matrix_rank(A[active],tol=1e-8)
    expected_codim=max(m,n) if m!=n else 2*n-1
    assert rank==expected_codim, (m,n,rank,expected_codim)
    assert np.min(gap[~active])>1e-9 if np.any(~active) else True
    return rank,int(np.sum(active))


def main():
    trials=0
    for m in range(1,9):
        for n in range(1,9):
            solve(m,n,'pasm');solve(m,n,'pperm')
            rank,act=forced_and_rank(m,n)
            trials+=1
    # Distinguish unique versus nonunique via two different feasible centers.
    for m,n in ((2,2),(2,5),(5,2),(3,3),(6,6)):
        r=1/(max(m,n)+sqrt(max(m,n)))
        x=witness(m,n)
        A,b=pasm_constraints(m,n)
        assert np.linalg.norm(x-r)>1e-7
        assert max(A@x.flatten()+r*np.linalg.norm(A,axis=1)-b)<1e-9
    # Exact small-case hand identity: PASM(2,2) center segment
    r=1/(2+sqrt(2))
    lo=r*(sqrt(2)-1);hi=r
    for z in (lo,(lo+hi)/2,hi):
        A,b=pasm_constraints(2,2)
        x=np.array([r,r,r,z])
        assert np.max(A@x+r*np.linalg.norm(A,axis=1)-b)<1e-10
    assert hi>lo
    print('PASM_INBALL_CHECKS_PASSED',trials,2*trials,'linear programs, ranks and witnesses')

if __name__=='__main__': main()
