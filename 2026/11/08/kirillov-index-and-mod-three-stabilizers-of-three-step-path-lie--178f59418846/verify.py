#!/usr/bin/env python3
"""Exact finite-field verification of the path Lie-algebra Kirillov index formula.

Independently generates brackets from matrix units E_{i,i+d}, d=1,2,3,
using [E_ij,E_kl]=delta_{jk} E_il - delta_{li} E_kj.
Only entries with diagonal offset <=3 survive.
"""
from itertools import product

def basis(n):
    return [(i, i+d) for d in range(1,4) for i in range(n+1-d)]

def units_bracket(a,b):
    (i,j),(k,l)=a,b
    out={}
    if j==k and l-i<=3:
        out[(i,l)]=out.get((i,l),0)+1
    if l==i and j-k<=3:
        out[(k,j)]=out.get((k,j),0)-1
    return {k:v for k,v in out.items() if v}

def rank_mod(A,p):
    A=[[(x%p) for x in row] for row in A]
    if not A:return 0
    m=len(A);nn=len(A[0]);r=0
    for j in range(nn):
        ip=next((i for i in range(r,m) if A[i][j]),None)
        if ip is None:continue
        A[r],A[ip]=A[ip],A[r]
        inv=pow(A[r][j],-1,p)
        A[r]=[(x*inv)%p for x in A[r]]
        for i in range(m):
            if i==r or not A[i][j]:continue
            c=A[i][j]
            A[i]=[(a-c*b)%p for a,b in zip(A[i],A[r])]
        r+=1
        if r==m:break
    return r

def matrices(n,p,t=None,c=None):
    b=basis(n); N=len(b); idx={a:i for i,a in enumerate(b)}
    if t is None:t=[1]*(n-2)
    if c is None:c=[0]*(n-1)
    coeff={(i,i+3):t[i] for i in range(n-2)}
    coeff.update({(i,i+2):c[i] for i in range(n-1)})
    full=[[0]*N for _ in range(N)]
    for i,x in enumerate(b):
        for j,y in enumerate(b):
            full[i][j]=sum(coeff.get(z,0)*v for z,v in units_bracket(x,y).items())%p
    mixed=[row[n:2*n-1] for row in full[:n]]
    return full,mixed

def main():
    count=0;degenerate=0
    for p in (2,3,5,7):
        for n in range(2,19):
            c=[0]*(n-1)
            if n%3==2:c[0]=1
            B,D=matrices(n,p,c=c)
            actual=rank_mod(B,p)
            assert actual==2*(n-1),(n,p,actual)
            g=[0]*(2*n-1)
            if n%3==2:
                for j in range(0,n-1,3):g[n+j]=1
            else:
                residue=(1 if n%3==1 else 2)
                for j in range(n):
                    if (j+1)%3==residue%3:g[j]=1
            assert any(g)
            assert all(sum(a*b for a,b in zip(row,g))%p==0 for row in B),(n,p,'radical')
            dr=rank_mod(D,p)
            assert dr==(0 if n==2 else (n-2 if n%3==2 else n-1)),(n,p,dr)
            if n>=3 and dr!=n-1:degenerate+=1
            assert len(B)==3*n-3,(n,len(B))
            count+=1
    exhaustive=0
    for p, nmax in [(2,8),(3,5)]:
        for n in range(2,nmax+1):
            # All linear forms on noncentral edge and path coordinates.
            for vals in product(range(p),repeat=(n-1)+(n-2)):
                c=list(vals[:n-1]);t=list(vals[n-1:]); B,_=matrices(n,p,t,c)
                actual=rank_mod(B,p)
                assert actual<=2*(n-1) and actual%2==0
                exhaustive+=1
    print(f'VERIFY_OK full_rank_witnesses={count} modular_mixed_deficiencies={degenerate} exhaustive_forms={exhaustive} n=2..18 primes=2,3,5,7')
if __name__=='__main__':main()
