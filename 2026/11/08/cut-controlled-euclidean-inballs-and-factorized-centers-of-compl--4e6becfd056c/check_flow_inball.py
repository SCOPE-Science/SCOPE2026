"""Reproducibility checks for the intrinsic inballs of complete directed flow polytopes.

Requires Python 3, NumPy and SciPy. This finite-dimensional test is not a proof.
"""
import math
from fractions import Fraction
from itertools import combinations
import numpy as np
from scipy.optimize import linprog


def edges(n):
    return list(combinations(range(n), 2))


def incidence(n):
    ed = edges(n)
    B = np.zeros((n, len(ed)))
    for j, (u, v) in enumerate(ed):
        B[u, j] = 1
        B[v, j] = -1
    return B, ed


def exact_rational_case(prefix):
    # prefix[i-1] = sum_{j<=i} b_j, for 1 <= i < n.
    n = len(prefix) + 1
    q = [k * (n-k) for k in range(1, n)]
    t = min(Fraction(prefix[k-1], q[k-1]) for k in range(1, n))
    ed = edges(n)
    x = {e: t for e in ed}
    for k in range(1, n):
        x[k-1, k] += Fraction(prefix[k-1]) - t * q[k-1]
    b = [Fraction(prefix[0])]
    b.extend(Fraction(prefix[i])-Fraction(prefix[i-1]) for i in range(1,n-1))
    b.append(-Fraction(prefix[-1]))
    calc = [Fraction(0) for _ in range(n)]
    for (i,j),val in x.items():
        calc[i] += val
        calc[j] -= val
    assert calc == b
    assert min(x.values()) == t
    crit = [k for k in range(1,n) if Fraction(prefix[k-1],q[k-1])==t]
    boundaries = [0] + crit + [n]
    dim = sum((boundaries[j+1]-boundaries[j]-1)*(boundaries[j+1]-boundaries[j]-2)//2 for j in range(len(boundaries)-1))
    return n,b,t,crit,dim,x


def run():
    checked = 0
    rng = np.random.default_rng(4815)
    for n in range(3,12):
        B, ed = incidence(n)
        # Direct orthogonal projection from a computed orthonormal row-space basis.
        U, s, Vt = np.linalg.svd(B, full_matrices=True)
        assert np.allclose(s[-1], 0, atol=1e-10)
        P = np.eye(len(ed)) - Vt[:n-1,:].T @ Vt[:n-1,:]
        norms = np.sqrt(np.diag(P))
        target = math.sqrt((n-2)/n)
        assert np.allclose(norms, target, atol=2e-12)
        for special in range(7):
            prefix = [Fraction(1) if special==0 else Fraction(int(rng.integers(1, 18)),int(rng.integers(1, 8))) for _ in range(n-1)]
            nn,b,t,crit,dim,cert=exact_rational_case(prefix)
            assert nn==n
            m=len(ed)
            Aub = np.zeros((m, m+1))
            for j in range(m):
                Aub[j,j]=-1
                Aub[j,-1]=1
            c=np.zeros(m+1);c[-1]=-1
            Aeq=np.column_stack((B,np.zeros(n)))
            result=linprog(c,A_ub=Aub,b_ub=np.zeros(m),A_eq=Aeq,b_eq=np.array([float(z) for z in b]),bounds=[(None,None)]*m+[(0,None)],method='highs')
            assert result.success, result.message
            assert abs(result.x[-1]-float(t))<1e-8
            # Independently calculate rank of the unconstrained edges inside critical blocks.
            boundaries=[0]+crit+[n]
            keep=[j for j,(i,h) in enumerate(ed) if any(boundaries[k]<=i<h<boundaries[k+1] for k in range(len(boundaries)-1))]
            dim_numeric=len(keep)-np.linalg.matrix_rank(B[:,keep],tol=1e-9)
            assert dim_numeric==dim, (n,crit,dim,dim_numeric)
            # Verify there is a relative-interior residual flow on every noncritical edge.
            new_b=np.array([float(z) for z in b])-float(t)*B@np.ones(m)
            if keep:
                C=B[:,keep]
                eps=min((float(prefix[k-1])-float(t)*k*(n-k))/(2*len(ed)) for k in range(1,n) if k not in crit)
                assert eps>0
                y=np.zeros(m)
                y[keep]=eps
                remainder=new_b -B@y
                runprefix=np.cumsum(remainder)[:-1]
                for k in range(1,n):
                    if k not in crit:
                        j=ed.index((k-1,k));y[j]+=runprefix[k-1]
                assert np.linalg.norm(B@y-new_b)<1e-8
                assert min(y[keep])>0
            checked+=1
    for n in range(3,18):
        _,b,t,crit,dim,_=exact_rational_case([1]*(n-1))
        k=n//2
        assert t==Fraction(1,n*n//4)
        assert dim==(k-1)*(k-2)
        assert crit==([k] if n%2==0 else [k,k+1])
    print('COMPLETE_FLOW_INBALL_CUT_AND_LOCUS_CHECKS_PASSED',checked)

if __name__=='__main__':
    run()
