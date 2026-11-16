#!/usr/bin/env python3
"""Exact standalone tests for triangular-book Walsh spanning-tree formulas.
Scientific conventions: binary edge ordering is [spine, u0,v0,u1,v1,...].
No external packages or data are required.
"""
from math import comb
from itertools import product
import random

def support(n):
    # Each leaf is attached by exactly one of its two incident edges if
    # the spine is in the tree; without the spine exactly one leaf has both.
    r=[]
    for bits in product((0,1),repeat=n):
        t=1
        for j,b in enumerate(bits):
            t |= 1<<(1+2*j+b)
        r.append(t)
        for j in range(n):
            if bits[j]!=0:continue  # Both chosen: avoid duplicate encoding.
            t=0
            for k,b in enumerate(bits):
                t |= 1<<(1+2*k+b)
                if k==j:t |= 1<<(1+2*k+(1-b))
            r.append(t)
    assert len(r)==len(set(r))==(n+2)*(1<<(n-1))
    return r

def fast_walsh(a):
    a=list(a); N=len(a);h=1
    while h<N:
        for base in range(0,N,2*h):
            for j in range(base,base+h):
                x=a[j];y=a[j+h]
                a[j]=x+y;a[j+h]=x-y
        h*=2
    return a

def predicted(n,f):
    c=1 if f&1==0 else -1
    vs=[];discord=0
    for i in range(n):
        x=1 if f&(1<<(2*i+1))==0 else -1
        y=1 if f&(1<<(2*i+2))==0 else -1
        if x!=y:discord+=1
        else:vs.append(x)
    if discord>=2:return 0
    if discord==1:
        # Sole discordant pair contributes product x*y=-1.
        z=1
        for v in vs:z*=v
        return -(1<<(n-1))*z
    z=1
    for v in vs:z*=v
    return (1<<(n-1))*z*(2*c+sum(vs))

def rank_formula(n):
    return (1<<(n+1))*(n+1)-(2*comb(n,n//2-1) if n%2==0 else 0)

def l1_numerator_formula(n):
    # Exact rational sharp norm of the frequency projection.
    # The main expression is rational with denominator 2^n.
    e=2*n+1
    numer= n*(1<<(n-1)) + n*comb(n-1,(n-1)//2)+comb(n,n//2)
    # \Lambda=n/2+n*binom/2^n+central/2^n
    return (n*(1<<(n-1)) + n*comb(n-1,(n-1)//2)+comb(n,n//2)), 1<<n



def integer_det(A):
    """Independent exact integer determinant by fraction-free elimination."""
    M=[list(row) for row in A];n=len(M)
    if n==0:return 1
    scale=1;prev=1
    for k in range(n-1):
        if M[k][k]==0:
            p=next((i for i in range(k+1,n) if M[i][k]),None)
            if p is None:return 0
            M[k],M[p]=M[p],M[k];scale=-scale
        pivot=M[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                q=pivot*M[i][j]-M[i][k]*M[k][j]
                assert q%prev==0
                M[i][j]=q//prev
        for i in range(k+1,n):M[i][k]=0
        prev=pivot
    return scale*M[-1][-1]

def signed_tree_determinant(n,frequency):
    s=1 if frequency&1==0 else -1
    # Ground hub u. Remaining vertices v,w0,...,w(n-1).
    L=[[0]*(n+1) for _ in range(n+1)]
    L[0][0]+=s
    for j in range(n):
        x=1 if frequency&(1<<(2*j+1))==0 else -1
        y=1 if frequency&(1<<(2*j+2))==0 else -1
        L[0][0]+=y
        L[j+1][j+1]+=x+y
        L[0][j+1]-=y
        L[j+1][0]-=y
    return integer_det(L)

def main():
    for n in range(1,9):
        dim=2*n+1;N=1<<dim
        a=[0]*N
        s=support(n)
        for t in s:a[t]=1
        trans=fast_walsh(a)
        assert all(v==predicted(n,f) for f,v in enumerate(trans)),n
        assert sum(v!=0 for v in trans)==rank_formula(n),(n,'rank')
        vals=[abs(v) for v in trans if v]
        assert min(vals)==1<<(n-1),(n,'min')
        assert max(vals)==(n+2)*(1<<(n-1)),(n,'max')
        a_num,a_den=l1_numerator_formula(n)
        assert sum(map(abs,trans))*a_den==a_num*N,(n,'norm')
        print('n',n,'freq',N,'trees',len(s),'rank',len(vals),
              'min',min(vals),'max',max(vals),'norm',str(a_num)+'/'+str(a_den))
    rand=random.Random(20261109)
    for n in range(1,16):
        for _ in range(75):
            f=rand.randrange(1<<(2*n+1))
            assert signed_tree_determinant(n,f)==predicted(n,f),(n,f)
    for n in range(1,101):
        # Independent exact binomial identity E max(|S|,2)-E|S|.
        counts=[comb(n,k) for k in range(n+1)]
        correction=sum(c*(max(abs(n-2*k),2)-abs(n-2*k)) for k,c in enumerate(counts))
        assert correction==2*comb(n,n//2)
    print('BOOK_WALSH_EXACT_TESTS_PASS')

if __name__=='__main__':main()
