#!/usr/bin/env python3
"""Exact standard-library five-point Walsh determinant distribution verifier.
No third-party code, external data, or approximate arithmetic is needed.
"""
from itertools import combinations, permutations
from collections import Counter
from math import comb

ROW_DEP=(0,1,2,4,7)
ROW_IND=(0,1,2,4,8)


def matrix(rows, cols):
    return [[1-2*((r & c).bit_count() & 1) for c in cols] for r in rows]


def bareiss(M):
    a=[row[:] for row in M]
    n=len(a); sgn=1; prev=1
    for k in range(n-1):
        if a[k][k] == 0:
            ix=next((i for i in range(k+1,n) if a[i][k]), None)
            if ix is None: return 0
            a[k],a[ix]=a[ix],a[k];sgn=-sgn
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                val=a[i][j]*pivot-a[i][k]*a[k][j]
                assert val%prev==0
                a[i][j]=val//prev
            a[i][k]=0
        prev=pivot
    return sgn*a[-1][-1]


def permutation_det(a):
    out=0
    for perm in permutations(range(5)):
        inv=sum(perm[i]>perm[j] for i in range(5) for j in range(i+1,5))
        term=1 if inv%2==0 else -1
        for i,j in enumerate(perm): term*=a[i][j]
        out+=term
    return out


def normalized_zero_column_distribution(rows, r):
    """Independent reduction: det(5x5 Walsh) = (+/-)16 det(4x4 bit incidence).

    The five-row representative includes zero; column translation puts zero
    among the five column indices without changing determinant magnitude.
    """
    assert rows[0] == 0
    out=Counter()
    for cs in combinations(range(1,1<<r),4):
        B=[[( (row & col).bit_count() & 1) for col in cs] for row in rows[1:]]
        out[abs(bareiss(B))]+=1
    return out


def local_distribution(rows, r):
    counts=Counter()
    optimal=[]
    for cols in combinations(range(1<<r),5):
        M=matrix(rows,cols)
        det=bareiss(M)
        assert det==permutation_det(M), (rows,cols)
        counts[abs(det)]+=1
        if abs(det)==48: optimal.append(cols)
    assert sum(counts.values())==comb(1<<r,5)
    return counts,optimal


def main():
    dep, odep=local_distribution(ROW_DEP,3)
    ind, oind=local_distribution(ROW_IND,4)
    assert dep=={0:24,32:32},dep
    assert ind=={0:1360,16:2672,32:320,48:16},ind
    prototype={0,3,5,9,14}
    assert set(oind)=={tuple(sorted(c^t for c in prototype)) for t in range(16)}
    assert len(oind)==16
    # Alternative exact 4x4 binary-incidence counts, with one column at zero.
    # Each translation orbit is counted five times by anchoring each column.
    zd=normalized_zero_column_distribution(ROW_DEP,3)
    zi=normalized_zero_column_distribution(ROW_IND,4)
    assert zd=={0:15,2:20},zd
    assert zi=={0:425,1:835,2:100,3:5},zi
    for k,v in zd.items(): assert dep[16*k]*5 == v*8
    for k,v in zi.items(): assert ind[16*k]*5 == v*16
    for d in range(4,10):
        q=1<<d
        r4=q*(q-1)*(q-2)*(q-4)*(q-8)//120
        r3=comb(q,5)-r4
        c16=2672*r4*(q//16)**5
        c32=320*r4*(q//16)**5+32*r3*(q//8)**5
        c48=16*r4*(q//16)**5
        c0=comb(q,5)**2-c16-c32-c48
        assert all(t>=0 for t in [c0,c16,c32,c48])
        # Independent Cauchy--Binet consequence of Walsh orthogonality:
        assert 16**2*c16+32**2*c32+48**2*c48==comb(q,5)*q**5
        print('dimension=',d,'counts=',(c0,c16,c32,c48))
    print('WALSH_FIVE_DETERMINANT_HISTOGRAM_PASS')

if __name__=='__main__':
    main()
