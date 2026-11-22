#!/usr/bin/env python3
"""Exhaustive checks of left Leibniz Nijenhuis operators with scalar rank-one deviation."""
from itertools import product

def mult(A,x,p):
    return tuple(sum(A[i][j]*x[j] for j in range(len(x)))%p for i in range(len(x)))

def rank(M,p):
    a=[list(row) for row in M]
    if not a:return 0
    R=len(a);C=len(a[0]); k=0
    for j in range(C):
        h=next((i for i in range(k,R) if a[i][j]%p),None)
        if h is None:continue
        a[k],a[h]=a[h],a[k]
        b=pow(a[k][j],-1,p)
        a[k]=[(v*b)%p for v in a[k]]
        for i in range(R):
            if i==k:continue
            b=a[i][j]
            if b:a[i]=[(a[i][z]-b*a[k][z])%p for z in range(C)]
        k+=1
        if k==R:break
    return k

def lhs_rhs_ok(N,T,p):
    d=len(T);n=d+1
    def br(x,y):
        return (0,)+tuple((x[0]*z)%p for z in mult(T,y[1:],p))
    e=[tuple(int(i==j) for i in range(n)) for j in range(n)]
    for x in e:
        for y in e:
            nx=mult(N,x,p);ny=mult(N,y,p)
            bxy=br(x,y);nbxy=mult(N,bxy,p)
            a=br(nx,y);b=br(x,ny)
            rhs=mult(N,tuple((a[i]+b[i]-nbxy[i])%p for i in range(n)),p)
            if br(nx,ny)!=rhs:return False
    return True

def outer(u,f,p):return tuple(tuple((ui*fj)%p for fj in f) for ui in u)
def all_e_rank1(d,p):
    seen=set();z=(0,)*d
    for u in product(range(p),repeat=d):
        if u==z:continue
        for phi in product(range(p),repeat=d):
            if phi==z:continue
            E=outer(u,phi,p)
            if E not in seen:
                seen.add(E);yield E,u,phi

def check_matrix(T,p):
    d=len(T)
    assert all(len(row)==d for row in T)
    assert rank(T,p)==d
    elements=list(product(range(p),repeat=d))
    H=0
    for f in elements:
        if not any(f):continue
        ft=tuple(sum(f[i]*T[i][j] for i in range(d))%p for j in range(d))
        if any(all(ft[j]==lam*f[j]%p for j in range(d)) for lam in range(1,p)):
            H+=1
    L=(p**d-1)//(p-1)
    K=L*(p**(d-2)-1)+p**(d-2)*H
    expect={0:1,1:p**d-1+p*K+H*p**(d-1),2:K*(p**(d-1)-p)+H*p**(d-1)*(p**(d-1)-1),d:H*p**(2*d-2),d+1:(p-1)*(p**d+p**(d-1)*K)+(p-2)*H*p**(2*d-2)}
    # Add overlapping coefficients for d=2
    expect={r:sum(v for k,v in [(0,1),(1,p**d-1+p*K+H*p**(d-1)),(2,K*(p**(d-1)-p)+H*p**(d-1)*(p**(d-1)-1)),(d,H*p**(2*d-2)),(d+1,(p-1)*(p**d+p**(d-1)*K)+(p-2)*H*p**(2*d-2))] if k==r) for r in range(d+2)}
    got={r:0 for r in range(d+2)}
    nilpotent_count=0
    E_list=[tuple(tuple(0 for _ in range(d)) for _ in range(d))]+[E for E,_,_ in all_e_rank1(d,p)]
    for E in E_list:
        for a in range(p):
            for c in elements:
                D=tuple(tuple((E[i][j]+(a if i==j else 0))%p for j in range(d)) for i in range(d))
                N=tuple([tuple([a]+[0]*d)]+[tuple([c[i]]+list(D[i])) for i in range(d)])
                actual=lhs_rhs_ok(N,T,p)
                # Independent predicted conditions using matrix products
                TE=tuple(tuple(sum(T[i][k]*E[k][j] for k in range(d))%p for j in range(d)) for i in range(d))
                ET=tuple(tuple(sum(E[i][k]*T[k][j] for k in range(d))%p for j in range(d)) for i in range(d))
                Ecomm=tuple(tuple(sum(E[i][k]*(TE[k][j]-ET[k][j]) for k in range(d))%p for j in range(d)) for i in range(d))
                predicted=all(not any(row) for row in Ecomm) and not any(mult(E,mult(T,c,p),p))
                assert actual==predicted,(T,p,a,c,E)
                if actual:
                    got[rank(N,p)]+=1
                    if E!=E_list[0]:
                        # shift M has M^3=0 exactly when E^2=0; M^2 may be nonzero
                        EE=tuple(tuple(sum(E[i][k]*E[k][j] for k in range(d))%p for j in range(d)) for i in range(d))
                        if not any(any(row) for row in EE) and any(mult(E,c,p)):
                            nilpotent_count+=1
    assert got==expect,(p,T,H,K,got,expect)
    # Only noneigenline square-zero deviations can have shifted nilpotence index three.
    assert nilpotent_count==p*(K-(H//(p-1))*(p**(d-1)-1))*(p**(d-1)-p**(d-2)),(nilpotent_count,p*(K-(H//(p-1))*(p**(d-1)-1))*(p**(d-1)-p**(d-2)))
    print('q',p,'d',d,'H',H,'K',K,'rank_spectrum',got,'index3',nilpotent_count,'OK')

if __name__=='__main__':
    check_matrix(((0,1),(1,1)),2)
    check_matrix(((0,2),(1,0)),3)
    check_matrix(((1,0),(0,2)),3)
    check_matrix(((1,1),(0,1)),3)
    check_matrix(((1,0),(0,1)),3)
    check_matrix(((0,0,1),(1,0,1),(0,1,0)),2)
    check_matrix(((1,0,0),(0,0,1),(0,1,1)),2)
    check_matrix(((1,0,0),(0,1,0),(0,0,1)),2)
    check_matrix(((0,0,0,1),(1,0,0,1),(0,1,0,0),(0,0,1,0)),2)
    print('LEIBNIZ_GENERAL_RANK_ONE_SCALAR_DEVIATION_VERIFIED')
