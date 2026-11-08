#!/usr/bin/env python3
"""Exact finite-field checks for a local-derivation classification.
No third-party packages needed. Run: python3 verify.py
"""
from itertools import combinations, product
import random


def wedge(u, v, pairs, p):
    return [(u[i]*v[j]-u[j]*v[i]) % p for i, j in pairs]


def rho(A, n, p):
    pairs=list(combinations(range(n),2))
    out=[[0]*len(pairs) for _ in pairs]
    for c,(i,j) in enumerate(pairs):
        for a in range(n):
            # A(e_i) wedge e_j + e_i wedge A(e_j)
            ei=[0]*n; ei[a]=1
            ej=[0]*n; ej[j]=1
            v=wedge(ei,ej,pairs,p)
            for r in range(len(pairs)):
                out[r][c]=(out[r][c]+A[a][i]*v[r])%p
            ei=[0]*n; ei[i]=1
            ej=[0]*n; ej[a]=1
            v=wedge(ei,ej,pairs,p)
            for r in range(len(pairs)):
                out[r][c]=(out[r][c]+A[a][j]*v[r])%p
    return out


def matvec(A, v, p):
    return [sum(a*b for a,b in zip(row,v))%p for row in A]


def add_vec(basis, row, p):
    x=[v%p for v in row]
    for j,b in sorted(basis.items()):
        if x[j]:
            c=x[j]
            x=[(a-c*y)%p for a,y in zip(x,b)]
    pivot=next((i for i,v in enumerate(x) if v),None)
    if pivot is None:
        return False
    fac=pow(x[pivot],-1,p)
    basis[pivot]=[(fac*v)%p for v in x]
    return True


def nullspace_from_columns(cols, ambient, p):
    # Solve column vectors dot w = 0: RREF rows = cols.
    B={}
    for col in cols:
        add_vec(B,col,p)
    free=[i for i in range(ambient) if i not in B]
    ans=[]
    for k in free:
        x=[0]*ambient; x[k]=1
        for pivot,b in sorted(B.items(),reverse=True):
            x[pivot]=(-sum(b[t]*x[t] for t in range(pivot+1,ambient)))%p
        assert all(sum(a*b for a,b in zip(col,x))%p==0 for col in cols)
        ans.append(x)
    return ans


def tangent_codimension(n,p,exhaustive=False,seed=5,number=1700):
    pairs=list(combinations(range(n),2)); m=len(pairs)
    # The action on central part of a free 2-step Lie algebra.
    rho_basis=[]
    for a in range(n):
        for b in range(n):
            A=[[0]*n for _ in range(n)];A[a][b]=1
            rho_basis.append(rho(A,n,p))
    eqs={}
    rng=random.Random(seed)
    if exhaustive:
        zs=product(range(p),repeat=m)
    else:
        # Test an independently generated collection of decomposable bivectors.
        def z_stream():
            for t in range(number):
                u=[rng.randrange(p) for _ in range(n)]
                v=[rng.randrange(p) for _ in range(n)]
                yield tuple(wedge(u,v,pairs,p))
        zs=z_stream()
    examined=0
    for z in zs:
        examined+=1
        cols=[matvec(M,z,p) for M in rho_basis]
        left=nullspace_from_columns(cols,m,p)
        for ell in left:
            row=[ell[j]*z[i]%p for j in range(m) for i in range(m)]
            add_vec(eqs,row,p)
        if len(eqs)==m*m-n*n and not exhaustive:
            break
    return examined,len(eqs),m*m-len(eqs),n*n


def witnesses(n,p,seed=33,checks=150):
    rng=random.Random(seed+n*97+p);m=n*(n-1)//2
    R=[]
    for t in range(checks):
        A=[[rng.randrange(p) for _ in range(n)] for _ in range(n)]
        B=[[rng.randrange(p) for _ in range(n)] for _ in range(n)]
        f=[[rng.randrange(p) for _ in range(n)] for _ in range(m)]
        u=[rng.randrange(p) for _ in range(n)]
        if t%13==0:u=[0]*n
        z=[rng.randrange(p) for _ in range(m)]
        target_w=matvec(A,u,p)
        target_z=[(v+w)%p for v,w in zip(matvec(f,u,p),matvec(rho(B,n,p),z,p))]
        if any(u):
            k=next(i for i,v in enumerate(u) if v)
            A0=[[0]*n for _ in range(n)]
            for i in range(n): A0[i][k]=target_w[i]*pow(u[k],-1,p)%p
            rem=[(target_z[i]-v)%p for i,v in enumerate(matvec(rho(A0,n,p),z,p))]
            f0=[[0]*n for _ in range(m)]
            for i in range(m):f0[i][k]=rem[i]*pow(u[k],-1,p)%p
        else:
            A0=B; f0=[[0]*n for _ in range(m)]
        assert matvec(A0,u,p)==target_w
        assert [(a+b)%p for a,b in zip(matvec(f0,u,p),matvec(rho(A0,n,p),z,p))]==target_z
    return checks


def main():
    rc=[]
    for n,p,ex,number in [(3,3,True,0),(4,3,True,0),(5,3,False,3000),(4,5,False,1000)]:
        examined,rank,dim,expected=tangent_codimension(n,p,exhaustive=ex,number=number)
        assert dim==expected, (n,p,examined,rank,dim,expected)
        rc.append((n,p,examined,rank,dim))
    tests=sum(witnesses(n,p) for n in range(2,7) for p in (3,5,7))
    print('VERIFY_OK tangent_tests='+str(rc)+' constructive_pointwise_derivation_tests='+str(tests)+' fields=3,5,7')

if __name__=='__main__':main()
