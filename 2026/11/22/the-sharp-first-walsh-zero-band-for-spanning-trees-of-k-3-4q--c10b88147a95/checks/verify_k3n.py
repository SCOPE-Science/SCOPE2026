#!/usr/bin/env python3
"""Exact low-weight Fourier checks for spanning-tree incidence vectors of K_{3,n}."""
from itertools import combinations, product
from fractions import Fraction as F
from math import comb

B = ((F(2,3), F(-1,3)), (F(-1,3), F(2,3)))

def gram_column(s):
    a,b,c=s
    d=a+b+c
    return ((F(a)-F(1,d), F(-a*b,d)), (F(-a*b,d),F(b)-F(1,d)))

def test_local_psd():
    for s in product((-1,1),repeat=3):
        r=sum(v<0 for v in s)
        A=gram_column(s)
        Q=[[A[i][j]-(1-4*r)*B[i][j] for j in range(2)] for i in range(2)]
        determinant=Q[0][0]*Q[1][1]-Q[0][1]*Q[1][0]
        assert Q[0][0]>=0 and Q[1][1]>=0 and determinant>=0, (s,Q)
        if r>=2:
            assert determinant>0
        elif r==1:
            assert determinant==0 and Q[0][0]+Q[1][1]>0
    print('LOCAL_EIGHT_SIGN_PSD_PASS')

def schur_w(n,mask):
    # Multiply the Schur-complement expression by 3 to keep integer arithmetic.
    aa=bb=tt=vv=n
    dprod=3**n
    for j in range(n):
        bits=(mask>>(3*j))&7
        if bits==0: continue
        a,b,c=[1-2*((bits>>i)&1) for i in range(3)]
        d=a+b+c
        t=3//d
        aa+=a-1; bb+=b-1; tt+=t-1; vv+=a*b*t-1
        dprod=(dprod//3)*d
    numerator=dprod*((3*aa-tt)*(3*bb-tt)-vv*vv)
    assert numerator%9==0
    return numerator//9

def brute_trees_n4():
    n=4; result=[]
    for edgeids in combinations(range(3*n), n+2):
        parent=list(range(n+3))
        def root(z):
            while parent[z]!=z:
                z=parent[z]
            return z
        fail=False
        for e in edgeids:
            j, i=divmod(e,3)
            r,s=root(i),root(j+3)
            if r==s:
                fail=True;break
            parent[r]=s
        if not fail:
            result.append(sum(1<<e for e in edgeids))
    assert len(result)==3**(n-1)*n**2==432
    for mask in range(1<<(3*n)):
        w=sum(1 if (mask&t).bit_count()%2==0 else -1 for t in result)
        assert w==schur_w(n,mask), (mask,w,schur_w(n,mask))
    print('N4_ALL_4096_FREQUENCIES_BRUTE_TREE_PASS')

def sparse_test(n):
    q=n//4
    for k in range(q+1):
        zeros=[]
        for subset in combinations(range(3*n),k):
            mask=sum(1<<e for e in subset)
            if schur_w(n,mask)==0:
                zeros.append(subset)
                assert k==q
                assert len({e%3 for e in subset})==1
                assert len({e//3 for e in subset})==q
        if k<q:
            assert len(zeros)==0
        else:
            assert len(zeros)==3*comb(n,q), (n, len(zeros))
    print(f'N{n}_LOW_WEIGHT_ZERO_CENSUS_PASS: first_degree={q} count={3*comb(n,q)}')

if __name__=='__main__':
    test_local_psd()
    brute_trees_n4()
    for n in (8,12,16): sparse_test(n)
    print('K3N_SHARP_FOURIER_THRESHOLD_VERIFIED')
