"""Independent finite-dimensional tests for two hard-core bosons on bicliques.

Constructs the hopping adjacency matrix directly from allowed single-token
moves; checks the characteristic polynomial exactly, layer transition
probabilities numerically, and the classical exclusion expression.
"""
import itertools
from math import comb, sin, sqrt, exp, pi
import numpy as np
from scipy.linalg import expm
from sympy import Matrix, symbols, factor


def token_hamiltonian(m, n):
    vertices=list(range(m+n))
    states=list(itertools.combinations(vertices,2))
    lookup={a:i for i,a in enumerate(states)}
    A=np.zeros((len(states),len(states)),dtype=int)
    for col,(a,b) in enumerate(states):
        for old,other in [(a,b),(b,a)]:
            possible=range(m,m+n) if old<m else range(m)
            for new in possible:
                if new==other:continue
                dst=tuple(sorted((other,new)))
                A[lookup[dst],col]+=1
    assert (A==A.T).all()
    return A,states

def formula(m,n,t):
    u=sqrt(4*m*n-2*m-2*n)
    v=sqrt(n*(m-2)); w=sqrt(m*(n-2))
    return (sin(u*t)**2+(m-1)*sin(v*t)**2+(n-1)*sin(w*t)**2)/(m*n)

def check(m,n):
    A,states=token_hamiltonian(m,n)
    x=symbols('x')
    p=Matrix(A).charpoly(x).as_expr()
    z=comb(m+n,2)-2*(m+n-1)
    predicted=x**z*(x*x-(4*m*n-2*m-2*n))*(x*x-n*(m-2))**(m-1)*(x*x-m*(n-2))**(n-1)
    assert factor(p-predicted)==0, (m,n)
    for t in [0.011,0.12,0.37,0.79]:
        init=states.index((0,m))
        v=expm(-1j*t*A)[:,init]
        same=sum(abs(v[i])**2 for i,(a,b) in enumerate(states) if (a<m)==(b<m))
        assert abs(same-formula(m,n,t))<2e-11,(m,n,t,same,formula(m,n,t))
    if m==n:
        Q=np.asarray(A,dtype=float)
        degree=Q.sum(0)
        Q-=np.diag(degree)
        for t in [0.011,0.12,0.37]:
            cls=expm(t*Q)[:,states.index((0,m))]
            same=sum(cls[i] for i,(a,b) in enumerate(states) if (a<m)==(b<m))
            pred=(m-1)/(2*m-1)*(1-exp(-(4*m-2)*t))
            assert abs(same-pred)<2e-11,(m,t,same,pred)
    print('PASS m,n=',m,n,'states=',len(states),'zero_mult=',z)

for pair in [(3,3),(3,4),(4,4),(3,5),(4,5),(5,5)]:
    check(*pair)

for n in [4,8,16,32,64,128]:
    t=pi/(2*n)
    p=formula(n,n,t)
    c=(n-1)/(2*n-1)*(1-exp(-(4*n-2)*t))
    print('ASYMPTOTIC',n,'quantum',round(p,8),'n_times_quantum',round(n*p,8),'classical',round(c,8))
