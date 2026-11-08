#!/usr/bin/env python3
"""Direct finite-field checks of square-zero fibers in a symplectic centralizer.

Only ordinary Python is required. The computations use the displayed matrices,
not the geometric orbit-counting proof.
"""
from itertools import product
from collections import Counter

N=4
upper=[(i,j) for i in range(N) for j in range(i,N)]
skew=[(i,j) for i in range(N) for j in range(i+1,N)]

def mm(A,B,q):
    h=len(A); t=len(B[0]); l=len(B)
    return [[sum(A[i][k]*B[k][j] for k in range(l))%q for j in range(t)] for i in range(h)]

def trans(A): return [list(row) for row in zip(*A)]

def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]

def rank(A,q):
    a=[[x%q for x in row] for row in A]; m=len(a); n=len(a[0]); r=0
    for j in range(n):
        p=next((i for i in range(r,m) if a[i][j]),None)
        if p is None: continue
        a[p],a[r]=a[r],a[p]
        z=pow(a[r][j],-1,q)
        a[r]=[(x*z)%q for x in a[r]]
        for i in range(m):
            if i!=r and a[i][j]:
                x=a[i][j]
                a[i]=[(a[i][k]-x*a[r][k])%q for k in range(n)]
        r+=1
        if r==m:break
    return r

def sym(c):
    M=[[0]*N for _ in range(N)]
    for (i,j),x in zip(upper,c): M[i][j]=M[j][i]=x
    return M

def skew_A(c, Sdiag, q):
    C=[[0]*N for _ in range(N)]
    for (i,j),x in zip(skew,c): C[i][j]=x;C[j][i]=-x
    return [[C[i][j]*pow(Sdiag[j],-1,q)%q for j in range(N)] for i in range(N)]

def linear_kernel_basis(A, q):
    # The map B -> AB - BA^T on the 10-dimensional symmetric coefficient space.
    AT=trans(A)
    cols=[]
    for j in range(len(upper)):
        c=[0]*len(upper);c[j]=1; B=sym(c)
        X=mm(A,B,q);Y=mm(B,AT,q)
        cols.append([(X[i][k]-Y[i][k])%q for i in range(4) for k in range(4)])
    mat=[[cols[j][i] for j in range(10)] for i in range(16)]
    rows=[row[:] for row in mat]; piv=[]; r=0
    for j in range(10):
        p=next((i for i in range(r,16) if rows[i][j]),None)
        if p is None:continue
        rows[p],rows[r]=rows[r],rows[p]
        v=pow(rows[r][j],-1,q)
        rows[r]=[(v*x)%q for x in rows[r]]
        for i in range(16):
            if i!=r and rows[i][j]:
                u=rows[i][j]
                rows[i]=[(rows[i][k]-u*rows[r][k])%q for k in range(10)]
        piv.append(j);r+=1
        if r==16:break
    free=[j for j in range(10) if j not in piv]
    basis=[]
    for j in free:
        v=[0]*10;v[j]=1
        for row,p in enumerate(piv):v[p]=(-rows[row][j])%q
        basis.append(v)
    return basis

def full_X(A,B,q):
    AT=trans(A)
    return [A[i]+B[i] for i in range(4)]+[[0]*4+[(-x)%q for x in AT[i]] for i in range(4)]

def polynomial(q,split):
    a=[1,q**4-1,q*q*(q-1)*(q*q+1)*(q*q+q+1),
       q*q*(q-1)**2*(q+1)*(q*q+1)*(q*q+q+1),
       q**6*(q-1)**2*(q*q+q+1)]
    if split: a[4]+=2*(q*q-1)*q**6
    return a

for q,non_square in [(3,2),(5,2),(7,3)]:
    full_split_hist=Counter()
    for typ in ('split','nonsplit'):
        sd=[1,1,1,1 if typ=='split' else non_square]
        count=0; first=None
        for c in product(range(q),repeat=6):
            A=skew_A(c,sd,q)
            if any(any(row) for row in mm(A,A,q)):continue
            if any(c):
                count+=1
                assert rank(A,q)==2
                assert len(linear_kernel_basis(A,q))==6
                if first is None:first=A
                if q==3:
                    basis=linear_kernel_basis(A,q)
                    for coeff in product(range(q),repeat=6):
                        v=[sum(coeff[t]*basis[t][j] for t in range(6))%q for j in range(10)]
                        B=sym(v);X=full_X(A,B,q)
                        assert not any(any(row) for row in mm(X,X,q))
                        assert rank(X,q)==4
                        if typ=='split':full_split_hist[4]+=1
        expected=2*(q*q-1) if typ=='split' else 0
        assert count==expected,(q,typ,count,expected)
        if first is not None:
            B_basis=linear_kernel_basis(first,q)
            # Every vector in the B-kernel yields rank exactly four; all for q=3.
            choices=product(range(q),repeat=6) if q==3 else ((i,j,0,1,2,0) for i in range(q) for j in range(q))
            for coeff in choices:
                v=[sum(coeff[t]*B_basis[t][j] for t in range(6))%q for j in range(10)]
                B=sym(v)
                X=full_X(first,B,q)
                assert not any(any(row) for row in mm(X,X,q))
                assert rank(X,q)==4
        print('SKEW_AND_RANK_CHECK',q,typ,count,'PASS')
    if q==3:
        assert full_split_hist[4]==2*(q*q-1)*q**6
        print('FULL_NONZERO_A_PAIR_COUNT',q,full_split_hist[4],'PASS')

q=3
hist=Counter()
for v in product(range(q), repeat=10):
    hist[rank(sym(v),q)]+=1
assert [hist[i] for i in range(5)]==polynomial(q,False)
print('FULL_SYMMETRIC_RANK_HISTOGRAM',q,[hist[i] for i in range(5)],'PASS')

for q in (3,5,7,9):
    for split in (False,True):
        p=polynomial(q,split)
        assert sum(p)==q**10+(2*q**6*(q*q-1) if split else 0)
        assert len(p)==5 and all(c>0 for c in p)
        print('POLYNOMIAL_TOTAL',q,'split' if split else 'nonsplit',sum(p),'PASS')
print('ALL_SYMPLECTIC_SQUARE_ZERO_FIBER_CHECKS_PASS')
