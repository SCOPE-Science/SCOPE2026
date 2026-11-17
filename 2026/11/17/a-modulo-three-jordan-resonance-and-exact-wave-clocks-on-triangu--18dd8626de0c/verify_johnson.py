"""Exact finite checks for reversible characteristic-three waves on triangular Johnson graphs.
No external dependencies other than NumPy; the argument proving all n is in RESULT.md.
"""
from itertools import combinations
from math import comb
import numpy as np

P=3

def adjacency(n):
    edges=list(combinations(range(n),2))
    A=np.zeros((len(edges),len(edges)),dtype=np.int64)
    for a,(i,j) in enumerate(edges):
        for b,(k,l) in enumerate(edges):
            if a!=b and len({i,j}&{k,l})==1:
                A[a,b]=1
    return A

def transition(A):
    m=len(A); I=np.eye(m,dtype=np.int64)
    O=np.zeros_like(A)
    return np.block([[A,(-I)%3],[I,O]])

def powmod(M,e):
    r=np.eye(len(M),dtype=np.int64)
    while e:
        if e%2:r=r@M%3
        M=M@M%3;e//=2
    return r

def rankmod(M):
    a=M.copy()%3; rows,cols=a.shape; rank=0
    for j in range(cols):
        k=next((i for i in range(rank,rows) if a[i,j]),None)
        if k is None:continue
        a[[rank,k]]=a[[k,rank]]
        if a[rank,j]==2:a[rank]=2*a[rank]%3
        for i in range(rows):
            if i!=rank and a[i,j]:a[i]=(a[i]-a[i,j]*a[rank])%3
        rank+=1
        if rank==rows:break
    return rank

def exp(n,t):
    N=comb(n,2); g=1
    while t%3==0:
        g*=3;t//=3
    if n%3==0:
        return min(4,g)+(n-2)*min(2,g)+(N-n)*min(2,g)*(t%2==0)
    if n%3==1:
        return 2*(n-1)*(t%4==0)+min(4,g)*(t%2==0)+(N-n-1)*min(2,g)*(t%2==0)
    return 2*(t%4==0)+(n-1)*min(4,g)*(t%2==0)+(N-2*n+1)*min(2,g)*(t%2==0)

def order(n):
    if n==3:return 9
    return 18 if n%3==0 else 36

if __name__=='__main__':
    for n in range(3,11):
        A=adjacency(n);T=transition(A);L=order(n);dim=2*len(A)
        assert np.array_equal(powmod(T,L),np.eye(dim,dtype=np.int64)),(n,L)
        for d in range(1,L+1):
            actual=dim-rankmod((powmod(T,d)-np.eye(dim,dtype=np.int64))%3)
            predicted=exp(n,d)
            assert actual==predicted,(n,d,actual,predicted)
        for d in range(1,L):
            if L%d==0:assert not np.array_equal(powmod(T,d),np.eye(dim,dtype=np.int64)),(n,d)
        print(f'n={n}, vertices={len(A)}, period={L}, ranks_and_nullities=all {L} verified')
    print('PASS: all integer modular checks')
