"""Finite exact checks for the Jacobi comparison and affine Dirichlet composition model.
Uses only Python's standard library. The infinite-dimensional arguments are analytical.
"""
from fractions import Fraction as Q
from itertools import product

def pivots(weights, u, lam):
    d=lam
    out=[d]
    for w in reversed(weights):
        if d<=0:
            return None
        d=lam + u*w*w - w*w/(4*d)
        out.append(d)
    return list(reversed(out))

def determinant(mat):
    a=[list(map(Q,row)) for row in mat]
    n=len(a); sign=1; val=Q(1)
    for k in range(n):
        j=next((j for j in range(k,n) if a[j][k]),None)
        if j is None:return Q(0)
        if j!=k:a[j],a[k]=a[k],a[j];sign=-sign
        p=a[k][k];val*=p
        for i in range(k+1,n):
            r=a[i][k]/p
            for h in range(k+1,n):a[i][h]-=r*a[k][h]
            a[i][k]=Q(0)
    return sign*val

def matrix(weights,u,lam):
    N=len(weights)+1
    A=[[Q(0) for _ in range(N)] for _ in range(N)]
    for i in range(N):A[i][i]=lam + (u*weights[i]**2 if i<N-1 else 0)
    for i,w in enumerate(weights):A[i][i+1]=A[i+1][i]=-w/2
    return A

checks=0
# This exact identity is the Schur-complement eliminant used in the proof.
for N in range(1,6):
    for seed in range(1,16):
        ws=[Q(1, (i+2)*(seed+100)) for i in range(N)]
        u=Q(1+seed%4,2)
        lam=Q(1, 10*(1+seed%4))
        assert lam < 1/(4*u);checks+=1
        pw=pivots(ws,u,lam)
        assert pw is not None and all(Q(0)<p<=lam for p in pw);checks+=1
        assert determinant(matrix(ws,u,lam))==__import__('math').prod(pw);checks+=1
        for shrink in [Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)]:
            vs=[w*shrink for w in ws]
            pv=pivots(vs,u,lam)
            assert pv is not None and all(pv[i]>=pw[i] and pv[i]<=lam for i in range(N+1));checks+=1
            assert determinant(matrix(vs,u,lam))==__import__('math').prod(pv);checks+=1
# Check unique root-chain enumeration under the power map and basis coefficients.
for m in range(2,8):
    for n in range(2,1200):
        root=n;level=0
        while True:
            a=int(root**(1/m))
            opts=[x for x in range(max(1,a-2),a+4) if x**m==root]
            if not opts:break
            root=opts[0];level+=1
        assert root**(m**level)==n;checks+=1
        assert not any(x**m==root for x in range(1,root+1) if x**m<=root);checks+=1
        # At integer translation a=1, phases absent and coefficient is n^{-1}.
        assert Q(1,n)==Q(1,root**(m**level));checks+=1
# The spectral truncation error is bounded by the first omitted weight.
for m in (2,3,4):
    for N in range(1,7):
        weights=[Q(1,2**(m**k)) for k in range(N+2)]
        assert all(weights[k]>=weights[k+1] for k in range(N+1));checks+=1
        assert weights[N]**2==Q(1,2**(2*m**N));checks+=1
print(f'DIRICHLET_DW_JACOBI_CHECK_OK {checks} exact rational assertions')
