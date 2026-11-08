#!/usr/bin/env python3
"""Direct finite-field checks for two-generator exterior-algebra module counts.

Only uses Python's standard library; field tests use primes 2 and 3.
All square-zero, anti-commutation, and rank checks use the original matrices.
"""
from collections import Counter
from itertools import product
from math import prod


def qbin(n,k,q):
    if k<0 or k>n: return 0
    return prod(q**(n-i)-1 for i in range(k))//prod(q**(k-i)-1 for i in range(k))


def gl(n,q):
    return prod(q**n-q**i for i in range(n))


def surj(d,r,q):
    if r>d: return 0
    return prod(q**d-q**i for i in range(r))


def zero_kernel_pairs(ell,r,s,q):
    return sum((-1)**j * q**(j*(j-1)//2) * qbin(ell,j,q)
               *surj(ell-j,r,q)*surj(ell-j,s,q)
               for j in range(ell+1))


def annihilating_profiles(m,q):
    out=Counter()
    for r in range(m+1):
        for s in range(m+1):
            for w in range(max(r,s),min(m,r+s)+1):
                for u in range(w,m+1):
                    ell=m-u
                    if max(r,s)>ell or ell>r+s: continue
                    c=(qbin(m,w,q)*qbin(w,r,q)
                       *qbin(r,r+s-w,q)*q**((w-r)*(w-s))
                       *qbin(m-w,u-w,q)*zero_kernel_pairs(ell,r,s,q))
                    if c: out[(r,s,w,u)]+=c
    return out


def count_formula(n,t,q):
    m=n-4*t
    if m<0 or t<=0: return {}
    K=gl(n,q)//(gl(m,q)*gl(t,q)*q**(3*t*t+2*t*m))
    assert K*gl(m,q)*gl(t,q)*q**(3*t*t+2*t*m)==gl(n,q)
    return {(2*t+r,2*t+s,t,3*t+w,t+u):K*c
            for (r,s,w,u),c in annihilating_profiles(m,q).items()}


def mm(A,B,n,p):
    return tuple(sum(A[i*n+k]*B[k*n+j] for k in range(n))%p
                for i in range(n) for j in range(n))


def rank(A,n,p):
    a=[list(A[i*n:(i+1)*n]) for i in range(n)]
    r=0
    for j in range(n):
        pivot=next((i for i in range(r,n) if a[i][j]),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][j],-1,p)
        a[r]=[(z*inv)%p for z in a[r]]
        for i in range(r+1,n):
            c=a[i][j]
            if c: a[i]=[(x-c*y)%p for x,y in zip(a[i],a[r])]
        r+=1
        if r==n:break
    return r


def image_span_rank(A,B,n,p):
    # Matrix concatenated side by side: rank of [A|B].
    T=[list(A[i*n:(i+1)*n])+list(B[i*n:(i+1)*n]) for i in range(n)]
    piv=0
    for j in range(2*n):
        i=next((k for k in range(piv,n) if T[k][j]),None)
        if i is None:continue
        T[piv],T[i]=T[i],T[piv];v=pow(T[piv][j],-1,p)
        T[piv]=[(x*v)%p for x in T[piv]]
        for k in range(piv+1,n):
            if T[k][j]:
                v=T[k][j];T[k]=[(x-v*y)%p for x,y in zip(T[k],T[piv])]
        piv+=1
        if piv==n:break
    return piv


def ker_intersection(A,B,n,p):
    # Column rank of vertical stack [A;B].
    T=[list(A[i*n:(i+1)*n]) for i in range(n)] +[list(B[i*n:(i+1)*n]) for i in range(n)]
    piv=0
    for j in range(n):
        i=next((k for k in range(piv,2*n) if T[k][j]),None)
        if i is None:continue
        T[piv],T[i]=T[i],T[piv];v=pow(T[piv][j],-1,p)
        T[piv]=[(x*v)%p for x in T[piv]]
        for k in range(piv+1,2*n):
            if T[k][j]:
                v=T[k][j];T[k]=[(x-v*y)%p for x,y in zip(T[k],T[piv])]
        piv+=1
    return n-piv


def direct_annihilating(m,p):
    mats=list(product(range(p),repeat=m*m)); zero=(0,)*(m*m)
    sq=[(A,rank(A,m,p)) for A in mats if mm(A,A,m,p)==zero]
    out=Counter()
    for A,r in sq:
        for B,s in sq:
            if mm(A,B,m,p)!=zero or mm(B,A,m,p)!=zero: continue
            w=image_span_rank(A,B,m,p)
            u=ker_intersection(A,B,m,p)
            out[(r,s,w,u)]+=1
    return out


def fixed_A_product_profiles(n,p):
    # canonical rank-two square-zero A with A(e_{n-2})=e_0, A(e_{n-1})=e_1
    # basis ordering U2 | H_{n-4} | U'2
    h=n-4
    A=[0]*(n*n)
    A[0*n+n-2]=1;A[1*n+n-1]=1;A=tuple(A)
    zero=(0,)*(n*n); out=Counter()
    # all anticommuting B have block (X,Y,Z;0,C,T;0,0,-X)
    dims=4+2*h+4+h*h+2*h
    for vals in product(range(p), repeat=dims):
        k=0
        X=vals[k:k+4];k+=4
        Y=vals[k:k+2*h];k+=2*h
        Z=vals[k:k+4];k+=4
        C=vals[k:k+h*h];k+=h*h
        T=vals[k:k+2*h];k+=2*h
        B=[0]*(n*n)
        for i in range(2):
            for j in range(2):
                B[i*n+j]=X[2*i+j]
                B[i*n+(n-2+j)]=Z[2*i+j]
                B[(n-2+i)*n+(n-2+j)]=(-X[2*i+j])%p
            for j in range(h): B[i*n+(2+j)]=Y[i*h+j]
        for i in range(h):
            for j in range(h):B[(2+i)*n+(2+j)]=C[i*h+j]
            for j in range(2):B[(2+i)*n+(n-2+j)]=T[2*i+j]
        B=tuple(B)
        if mm(B,B,n,p)!=zero:continue
        AB=mm(A,B,n,p);BA=mm(B,A,n,p)
        assert all((a+b)%p==0 for a,b in zip(AB,BA))
        t=rank(AB,n,p)
        if t==0:continue
        r=rank(A,n,p);s=rank(B,n,p)
        w=image_span_rank(A,B,n,p);u=ker_intersection(A,B,n,p)
        out[(r,s,t,w,u)]+=1
    return out


def squarezero_rank2_number(n,q):
    return qbin(n,2,q)*qbin(n-2,2,q)*gl(2,q)


def direct_entire_product_distribution(n,p):
    mats=product(range(p),repeat=n*n)
    zero=(0,)*(n*n)
    sq=[M for M in mats if mm(M,M,n,p)==zero]
    out=Counter()
    for A in sq:
        for B in sq:
            AB=mm(A,B,n,p);BA=mm(B,A,n,p)
            if all((a+b)%p==0 for a,b in zip(AB,BA)):
                out[rank(AB,n,p)]+=1
    return out

if __name__=='__main__':
    for m,p in [(1,2),(2,2),(2,3),(3,2)]:
        observed=direct_annihilating(m,p)
        expected=annihilating_profiles(m,p)
        assert observed==expected,(m,p,expected,observed)
        print('annihilating',m,p,'total',sum(observed.values()),'profiles',len(observed),flush=True)
    for n,p in [(4,2),(4,3),(5,2)]:
        observed=fixed_A_product_profiles(n,p)
        predicted=count_formula(n,1,p)
        mult=squarezero_rank2_number(n,p)
        # for n=4,5, product nonzero forces rank A=2; one GL_n-orbit of A
        assert {k:v*mult for k,v in observed.items()}==predicted,(n,p,observed,predicted)
        print('exterior nonzero product',n,p,'per canonical A',sum(observed.values()),
              'labeled',sum(predicted.values()),'profiles',len(predicted),flush=True)
    for n,p in [(3,3),(4,2)]:
        observed=direct_entire_product_distribution(n,p)
        predicted_nonzero=sum(sum(count_formula(n,t,p).values())
                              for t in range(1,n//4+1))
        assert sum(v for t,v in observed.items() if t>0)==predicted_nonzero
        assert observed[0]==sum(annihilating_profiles(n,p).values())
        print('complete original equations',n,p,'product ranks',dict(observed),flush=True)
    print('EXTERIOR_PRODUCT_STRATIFICATION_DIRECT_CHECK_PASS')
