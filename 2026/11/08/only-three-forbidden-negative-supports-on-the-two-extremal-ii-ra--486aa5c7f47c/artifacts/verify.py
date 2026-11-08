#!/usr/bin/env python3
"""Exact, self-contained chamber-support verification for affine E8 with a marked section."""
from collections import Counter
from fractions import Fraction
from math import comb

EDGES=((0,1),(0,2),(2,3),(0,4),(4,5),(5,6),(6,7),(7,8),(8,9))
DIAG=(2,)*9+(1,)
NULL=(6,3,4,2,5,4,3,2,1)


def submatrix(nodes):
    out=[[DIAG[u] if i == j else 0 for j,u2 in enumerate(nodes)] for i,u in enumerate(nodes)]
    # use explicit graph construction, no algebra library
    at={v:i for i,v in enumerate(nodes)}
    for u,v in EDGES:
        if u in at and v in at:
            out[at[u]][at[v]]=out[at[v]][at[u]]=-1
    return out


def det_bareiss(matrix):
    n=len(matrix)
    if not n:
        return 1
    a=[row[:] for row in matrix]
    sign=1
    prev=1
    for k in range(n-1):
        if a[k][k]==0:
            found=next((i for i in range(k+1,n) if a[i][k]!=0),None)
            if found is None:
                return 0
            a[k],a[found]=a[found],a[k]
            sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator%prev==0
                a[i][j]=numerator//prev
            a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]


def pd_by_bareiss(mat):
    return all(det_bareiss([row[:k] for row in mat[:k]])>0
               for k in range(1,len(mat)+1))


def pd_by_fraction_ldlt(mat):
    # Completely separate exact LDL^T test, independent of determinant routine.
    n=len(mat)
    lower=[[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
    diagonal=[]
    for k in range(n):
        d=Fraction(mat[k][k])-sum(lower[k][j]**2*diagonal[j] for j in range(k))
        if d<=0:
            return False
        diagonal.append(d)
        for i in range(k+1,n):
            lower[i][k]=(Fraction(mat[i][k])-sum(lower[i][j]*lower[k][j]*diagonal[j] for j in range(k)))/d
    return True


def main():
    affine=submatrix(list(range(9)))
    assert all(sum(affine[i][j]*NULL[j] for j in range(9))==0 for i in range(9))
    assert all(NULL[i]>0 for i in range(9))
    schur_inverse_entries=[]
    for omitted in range(9):
        fiber_nodes=[i for i in range(9) if i!=omitted]
        if omitted==8:
            schur_inverse_entries.append(Fraction(0))
            continue
        mat=submatrix(fiber_nodes)
        k=fiber_nodes.index(8)
        principal_minor=[[mat[i][j] for j in range(8) if j!=k] for i in range(8) if i!=k]
        schur_inverse_entries.append(Fraction(det_bareiss(principal_minor),det_bareiss(mat)))
    assert schur_inverse_entries==list(map(Fraction, ['5/6','8/9','7/8','1','4/5','3/4','2/3','1/2','0']))
    counts=Counter()
    excluded=[]
    for mask in range(1<<10):
        vertices=[i for i in range(10) if mask&(1<<i)]
        m=submatrix(vertices)
        p1=pd_by_bareiss(m)
        p2=pd_by_fraction_ldlt(m)
        assert p1==p2,(vertices,p1,p2)
        if p1:
            counts[len(vertices)]+=1
        else:
            excluded.append(tuple(vertices))
    expected={k:comb(10,k) for k in range(9)}
    expected[9]=8
    assert dict(sorted(counts.items()))==expected
    must_exclude=[tuple(range(9)),(0,1,2,4,5,6,7,8,9),tuple(range(10))]
    assert excluded==must_exclude,excluded
    assert sum(counts.values())==1021
    print('affine_E8_kernel='+','.join(map(str,NULL)))
    print('schur_inverse_diagonal_88='+','.join(str(v) for v in schur_inverse_entries))
    print('subsets_checked=1024')
    print('method_1=exact_Bareiss_principal_minors')
    print('method_2=exact_rational_LDLt')
    print('chambers_by_support='+','.join(f'{k}:{counts[k]}' for k in range(10)))
    print('excluded_subsets='+str(excluded))
    print('total_chambers=1021')
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':
    main()
