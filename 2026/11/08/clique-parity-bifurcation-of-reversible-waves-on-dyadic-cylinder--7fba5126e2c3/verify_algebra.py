#!/usr/bin/env python3
"""Exact binary matrix verification for clique-fiber dyadic wave dynamics."""

def product(X,Y):
    out=[]
    for row in X:
        s=0
        while row:
            bit=row & -row
            s ^= Y[bit.bit_length()-1]
            row ^= bit
        out.append(s)
    return out

def eye(n): return [1<<i for i in range(n)]

def add(X,Y): return [a^b for a,b in zip(X,Y)]

def power(X,e):
    n=len(X); out=eye(n)
    while e:
        if e&1: out=product(out,X)
        X=product(X,X); e >>= 1
    return out

def rank(rows):
    piv={}
    for w in rows:
        while w:
            p=w.bit_length()-1
            if p not in piv:
                piv[p]=w;break
            w ^= piv[p]
    return len(piv)

def graph_mats(r,m):
    n=1<<r; N=n*m
    A=[0]*N
    for x in range(n):
        for j in range(m):
            i=x*m+j
            for xp in ((x-1)%n,(x+1)%n):
                A[i] ^= 1<<(xp*m+j)
            for jp in range(m):
                if jp!=j: A[i] ^= 1<<(x*m+jp)
    T=[0]*(2*N)
    for i in range(N):
        T[i] = A[i] | (1<<(N+i))
        T[N+i] = 1<<i
    return A,T

def expected_dim(r,m,t):
    L=1<<(r-1); v=0; s=t
    while s%2==0: v+=1; s//=2
    h=1<<v
    if m%2:
        return 2*min(h,2*L)+(4*(m-1)*min(h,L) if t%3==0 else 0)
    return 4*m*min(h,L) if t%3==0 else 0

def check():
    checked=0
    for r in (3,4,5):
        for m in (3,4,5):
            A,T=graph_mats(r,m); N=len(A); D=2*N; L=1<<(r-1)
            # Adjacency is annihilated by the predicted binary polynomial.
            nil=power(add(A,eye(N)),L)
            if m%2: nil=product(nil,power(A,L))
            assert nil==[0]*N,(r,m,'adjacency annihilator')
            order=(3*(1<<r)) if m%2 else (3*L)
            I=eye(D)
            assert power(T,order)==I,(r,m,'order fails')
            assert power(T,order//3)!=I,(r,m,'3 factor')
            assert power(T,order//2)!=I,(r,m,'2 factor')
            for t in range(1,order+3):
                val=D-rank(add(power(T,t),I))
                want=expected_dim(r,m,t)
                assert val==want,(r,m,t,val,want)
                checked+=1
            print('r=%d m=%d vertices=%d exact_order=%d verified_times=%d' %
                  (r,m,N,order,order+2))
    print('SUCCESS %d exact matrix fixed-space comparisons' % checked)

if __name__=='__main__':check()
