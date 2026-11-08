#!/usr/bin/env python3
"""Exhaustive independent subspace/ideal multiplication checks for finite path algebras."""
from itertools import combinations, product
from collections import Counter
from functools import lru_cache

def rref(vectors,n,q):
    M=[list(v) for v in vectors if any(v)]
    r=0
    for c in range(n):
        j=next((j for j in range(r,len(M)) if M[j][c]%q),None)
        if j is None:continue
        M[r],M[j]=M[j],M[r]
        inv=pow(M[r][c],-1,q)
        M[r]=[(x*inv)%q for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]:
                t=M[i][c]
                M[i]=[(a-t*b)%q for a,b in zip(M[i],M[r])]
        r+=1
        if r==len(M):break
    return tuple(tuple(row) for row in M[:r])

@lru_cache(None)
def subspaces(n,q):
    ret=[]
    for d in range(n+1):
        for pivots in combinations(range(n),d):
            positions=[(i,c) for i in range(d) for c in range(pivots[i]+1,n) if c not in pivots]
            for vals in product(range(q),repeat=len(positions)):
                m=[[0]*n for _ in range(d)]
                for i,p in enumerate(pivots):m[i][p]=1
                for (i,c),v in zip(positions,vals):m[i][c]=v
                ret.append(tuple(tuple(row) for row in m))
    assert len(ret)==len(set(ret)),(n,q)
    return tuple(ret)

def rect(U,Z,a,b,q):
    vec=[]
    for u in U:
        for z in Z:
            vec.append(tuple(u[i]*z[j]%q for i in range(a) for j in range(b)))
    return rref(vec,a*b,q)

def ideals(a,b,q):
    Vs=subspaces(a,q);Ws=subspaces(b,q);Ts=subspaces(a*b,q)
    Vstd=tuple(tuple(int(i==j) for i in range(a)) for j in range(a))
    Wstd=tuple(tuple(int(i==j) for i in range(b)) for j in range(b))
    for U in Vs:
        for Z in Ws:
            forced=rect(U,Wstd,a,b,q)+rect(Vstd,Z,a,b,q)
            force_rank=len(rref(forced,a*b,q))
            for T in Ts:
                if len(rref(T+forced,a*b,q))==len(T):
                    yield U,Z,T

def gauss(n,k,q):
    if k<0 or k>n:return 0
    num=1;den=1
    for i in range(k):num*=q**(n-i)-1;den*=q**(i+1)-1
    return num//den

def G(d,q):return sum(gauss(d,i,q) for i in range(d+1))

def formula(a,b,q):
    A=[sum(gauss(b,z,q)*G((a-u)*(b-z),q) for z in range(b+1)) for u in range(a+1)]
    B=[sum(gauss(a,u,q)*G((a-u)*(b-z),q) for u in range(a+1)) for z in range(b+1)]
    N=sum(gauss(a,u,q)*A[u] for u in range(a+1))
    assert N==sum(gauss(b,z,q)*B[z] for z in range(b+1))
    z=N*(A[0]+B[0])-A[0]*B[0]
    C=N*N-2*(N-A[0])*(N-B[0])+(N-A[0]-B[0]+G(a*b,q))**2
    C+=sum(gauss(a,u,q)*gauss(b,v,q)*G((a-u)*(b-v),q)**2 for u in range(1,a+1) for v in range(1,b+1))
    return N,z,C,A,B

def verify(a,b,q):
    ideals_lst=list(ideals(a,b,q)); N=len(ideals_lst)
    predicted_N,predicted_zero,predicted_equal,A,B=formula(a,b,q)
    assert N==predicted_N,(a,b,q,N,predicted_N)
    counts=Counter();eq=0
    for I in ideals_lst:
        for J in ideals_lst:
            p=rect(I[0],J[1],a,b,q)
            counts[p]+=1
            if p==rect(J[0],I[1],a,b,q):eq+=1
    z=counts[()]
    assert z==predicted_zero,(a,b,q,z,predicted_zero)
    assert eq==predicted_equal,(a,b,q,eq,predicted_equal)
    assert len(counts)==1+sum(gauss(a,u,q)*gauss(b,v,q) for u in range(1,a+1) for v in range(1,b+1))
    for P,num in counts.items():
        if not P:continue
        possible=[(u,z,A[u]*B[z]) for u in range(1,a+1) for z in range(1,b+1) if len(P)==u*z]
        assert any(num==size for u,z,size in possible),(a,b,q,P,num,possible)
    print(f'PASS a={a} b={b} q={q}: ideals={N}; zero-product_pairs={z}; commuting_ideal_pairs={eq}; nonzero_product_targets={len(counts)-1}; weighted_mass={sum(counts.values())}')

if __name__=='__main__':
    for args in [(1,1,2),(1,1,3),(2,1,2),(1,2,3),(2,2,2),(2,2,3)]:verify(*args)
    print('ALL_THREE_LAYER_IDEAL_PRODUCT_FIBERS_PASS')
