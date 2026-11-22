#!/usr/bin/env python3
"""Exact integral graph-lattice certificate for two order-six Latin group nets.

No external packages required. Prime-power operations are elementary unimodular
row/column operations over Z/(p**e); a high enough e resolves all exponents.
"""
from collections import Counter
from math import prod

N = 6

def mul_cyclic(a, b):
    return (a + b) % N

def mul_dihedral(a, b):
    r, e = divmod(a, 2)
    s, f = divmod(b, 2)
    return 2 * ((r + (-1 if e else 1) * s) % 3) + ((e+f) % 2)

def incidence(mul):
    B = [[0] * 36 for _ in range(18)]
    for a in range(6):
        for b in range(6):
            k = 6*a+b
            for i in (a, 6+b, 12+mul(a,b)):
                B[i][k] = 1
    assert all(sum(r)==6 for r in B)
    assert all(sum(B[i][j] for i in range(18))==3 for j in range(36))
    # The net/Latin property gives a 3x3 Gram matrix: 6I diagonally,
    # all-ones matrices off diagonal; verify this independently of table.
    for i in range(18):
        for j in range(18):
            dot = sum(B[i][k]*B[j][k] for k in range(36))
            assert dot == (6 if i==j else 0 if i//6==j//6 else 1)
    return B

def laplacian(B):
    L = [[0]*54 for _ in range(54)]
    for i in range(18):
        L[i][i]=6
        for j in range(36):
            if B[i][j]:
                L[i][18+j] = L[18+j][i] = -1
    for j in range(36):
        L[18+j][18+j]=3
    assert sum(sum(row) for row in L)==0
    assert all(sum(row)==0 for row in L)
    assert sum(1 for i in range(54) for j in range(i+1,54) if L[i][j]==-1)==108
    return L

def rank_mod_p(mat, p):
    a=[[x%p for x in row] for row in mat]
    rows=len(a)
    cols=len(a[0])
    r=0
    for c in range(cols):
        k=next((k for k in range(r,rows) if a[k][c]),None)
        if k is None: continue
        a[k],a[r]=a[r],a[k]
        inv=pow(a[r][c],-1,p)
        for j in range(c,cols):a[r][j]=a[r][j]*inv%p
        for i in range(r+1,rows):
            if a[i][c]:
                v=a[i][c]
                for j in range(c,cols):a[i][j]=(a[i][j]-v*a[r][j])%p
        r+=1
        if r==rows:break
    return r

def valuation(a,p,e):
    if a==0:return e
    v=0
    while a%p==0:
        a//=p;v+=1
        if v==e:return e
    return v

def local_smith_exponents(mat,p,e):
    """p-adic Smith exponents modulo p^e via invertible row/col operations."""
    modulus=p**e
    A=[[int(z)%modulus for z in row] for row in mat]
    n=len(A)
    assert all(len(r)==n for r in A)
    out=[]
    for k in range(n):
        best=(e,None,None)
        for i in range(k,n):
            for j in range(k,n):
                v=valuation(A[i][j],p,e)
                if v<best[0]:best=(v,i,j)
        v,i,j=best
        if v==e:
            out.extend([e]*(n-k))
            break
        A[i],A[k]=A[k],A[i]
        for row in A: row[j],row[k]=row[k],row[j]
        pp=p**v
        assert A[k][k]%pp==0
        inv=pow(A[k][k]//pp,-1,modulus//pp)
        for i in range(k+1,n):
            assert A[i][k]%pp==0
            mult=(A[i][k]//pp*inv)%(modulus//pp)
            if mult:
                for j in range(k,n):
                    A[i][j]=(A[i][j]-mult*A[k][j])%modulus
        for j in range(k+1,n):
            assert A[k][j]%pp==0
            mult=(A[k][j]//pp*inv)%(modulus//pp)
            if mult:
                for i in range(k,n):
                    A[i][j]=(A[i][j]-mult*A[i][k])%modulus
        assert all(A[i][k]==0 for i in range(k+1,n))
        assert all(A[k][j]==0 for j in range(k+1,n))
        out.append(v)
    assert len(out)==n
    return sorted(out)

def main():
    expected={
        'C6': {2:{0:38,1:1,2:12,3:2},3:{0:30,1:11,2:11,3:1}},
        'S3': {2:{0:38,1:1,2:12,3:2},3:{0:32,1:7,2:13,3:1}},
    }
    for name,mul in [('C6',mul_cyclic),('S3',mul_dihedral)]:
        B=incidence(mul)
        L=laplacian(B)
        expected_rank={'C6':15,'S3':16}[name]
        assert rank_mod_p(B,3)==expected_rank
        for root in (0,53):
            M=[[L[i][j] for j in range(54) if j!=root]
               for i in range(54) if i!=root]
            E2=local_smith_exponents(M,2,36)
            E3=local_smith_exponents(M,3,40)
            assert dict(Counter(E2))==expected[name][2],(name,root,2,Counter(E2))
            assert dict(Counter(E3))==expected[name][3],(name,root,3,Counter(E3))
            assert sum(E2)==31 and sum(E3)==36
            invariant_factors=[(2**a)*(3**b) for a,b in zip(E2,E3)]
            assert all(d2%d1==0 for d1,d2 in zip(invariant_factors,invariant_factors[1:]))
            assert prod(invariant_factors)==2**31*3**36
            nontrivial=dict(Counter(d for d in invariant_factors if d!=1))
            if name=='C6':assert nontrivial=={3:8,6:1,12:2,36:10,72:1,216:1},nontrivial
            else:assert nontrivial=={3:6,6:1,36:12,72:1,216:1},nontrivial
            print(name,'root',root,'rank B mod3',expected_rank,
                  '2-adic',dict(Counter(E2)), '3-adic',dict(Counter(E3)),
                  'nontrivial invariant factors',nontrivial)
    print('NET6_CYCLIC_DIHEDRAL_NERON_GROUPS_OK')
if __name__=='__main__':main()
