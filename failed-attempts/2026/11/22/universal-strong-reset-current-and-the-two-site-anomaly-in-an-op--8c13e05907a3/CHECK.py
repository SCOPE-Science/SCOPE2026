"""Reproduce finite-state checks for the strong-reset open exclusion current.

Requires Python 3, NumPy, SciPy, SymPy. This is a finite diagnostic, not
an infinite-chain or arbitrary-parameter proof.
"""
from fractions import Fraction
import numpy as np
import sympy as sp
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve


def generator(L, a, b, r):
    """Column generator on occupancy bits, site 1 = lowest bit."""
    n = 1 << L
    q = lil_matrix((n,n), dtype=float)
    for x in range(n):
        events = []
        if (x & 1) == 0:
            events.append((x | 1, a))
        if x & (1 << (L-1)):
            events.append((x ^ (1 << (L-1)), b))
        for j in range(L-1):
            if (x & (1 << j)) and not (x & (1 << (j+1))):
                events.append((x ^ (1 << j) ^ (1 << (j+1)), 1.))
        if (x & 1) == 0:
            for j in range(1,L):
                if x & (1 << j):
                    events.append((x ^ (1 << j) ^ 1, r))
        for y, rate in events:
            q[y,x] += rate
            q[x,x] -= rate
    return q.tocsc()


def stationary(L,a,b,r):
    q=generator(L,a,b,r)
    n=1<<L
    mat=q.tolil()
    mat[-1,:]=1.
    rhs=np.zeros(n);rhs[-1]=1.
    p=spsolve(mat.tocsc(),rhs)
    return p,q


def check():
    count=0
    a,b,r=sp.symbols('a b r',positive=True)
    # Independent symbolic generator for the 2-site chain.
    q=sp.zeros(4)
    events={0:[(1,a)],1:[(2,1)],2:[(0,b),(3,a),(1,r)],3:[(1,b)]}
    for x,evt in events.items():
        for y,rate in evt:
            q[y,x]+=rate; q[x,x]-=rate
    eq=q.copy();eq[3,:]=sp.ones(1,4)
    h=sp.Matrix([0,0,0,1]);p=eq.inv()*h
    current=sp.factor(b*(p[2]+p[3]))
    expected=a*b*(a+b)/(a*a*b+a*a+a*b*b+a*b*r+a*b+b*b)
    assert sp.factor(current-expected)==0; count+=1
    assert sp.limit(r*current,r,sp.oo)==a+b; count+=1
    assert all(sp.simplify(v)>=0 for v in [1,2,3]); count+=1
    for L in [2,3,4,5,6]:
        for aa,bb in [(0.25,0.5),(0.5,2.),(1.,1.),(2.,0.5),(3.,4.)]:
            js=[]
            for rr in [100.,1000.,10000.]:
                pr, gen=stationary(L,aa,bb,rr)
                assert abs(np.sum(pr)-1)<1e-9; count+=1
                assert np.min(pr)>-1e-10; count+=1
                assert np.linalg.norm(gen@pr,ord=np.inf)<1e-9; count+=1
                j_out=bb*sum(pr[x] for x in range(1<<L) if x&(1<<(L-1)))
                j_in=aa*sum(pr[x] for x in range(1<<L) if not x&1)
                assert abs(j_in-j_out)<1e-9; count+=1
                js.append(rr*j_out)
            lim=aa+bb if L==2 else aa
            assert abs(js[-1]-lim)<0.012; count+=1
            assert abs(js[-1]-lim)<0.20*abs(js[0]-lim)+0.003; count+=1
    return count

if __name__=='__main__':
    print('PASS',check(),'finite/symbolic assertions')
