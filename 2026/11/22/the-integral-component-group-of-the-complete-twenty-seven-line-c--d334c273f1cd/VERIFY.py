"""Exact standard-library verification for the 27-line divisor of a smooth cubic surface.

Line classes are in the lattice Z H + Z E_1 + ... + Z E_6,
encoded as d H - sum(m_i E_i). An actual exceptional curve E_i
has m_i=-1. Run with Python 3.8 or later: python VERIFY.py.
"""
from itertools import combinations
from collections import Counter
from math import prod


def classes():
    out=[]
    for i in range(6):
        m=[0]*6; m[i]=-1
        out.append((0,tuple(m)))
    for i,j in combinations(range(6),2):
        out.append((1,tuple(int(k in (i,j)) for k in range(6))))
    for i in range(6):
        out.append((2,tuple(int(k!=i) for k in range(6))))
    return out


def intersect(x,y):
    return x[0]*y[0]-sum(a*b for a,b in zip(x[1],y[1]))


def build():
    curves=classes()
    assert len(curves)==27
    assert [sum(c[0] for c in curves)]+[sum(c[1][k] for c in curves) for k in range(6)]==[27]+[9]*6
    A=[[0 if i==j else intersect(x,y) for j,y in enumerate(curves)] for i,x in enumerate(curves)]
    assert all(x in (0,1) for row in A for x in row)
    assert all(sum(row)==10 for row in A)
    assert sum(map(sum,A))==270
    # The graph has parameters srg(27,10,1,5), checked at every entry.
    assert all(sum(A[i][k]*A[k][j] for k in range(27)) == (10 if i==j else (1 if A[i][j] else 5)) for i in range(27) for j in range(27))
    return [[10*(i==j)-A[i][j] for j in range(27)] for i in range(27)]


def minor(M,deleted):
    return [[v for j,v in enumerate(row) if j!=deleted] for i,row in enumerate(M) if i!=deleted]


def bareiss_det(M):
    A=[row[:] for row in M]; n=len(A)
    if n==0:return 1
    sign=1;den=1
    for k in range(n-1):
        if A[k][k]==0:
            i=next(i for i in range(k+1,n) if A[i][k])
            A[k],A[i]=A[i],A[k];sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=A[i][j]*pivot-A[i][k]*A[k][j]
                assert num%den==0
                A[i][j]=num//den
        for i in range(k+1,n):A[i][k]=0
        den=pivot
    return sign*A[n-1][n-1]


def local_smith_exponents(matrix,p,N=5):
    """Exact Smith valuations over Z / p^N via invertible row/column operations."""
    mod=p**N
    X=[[entry%mod for entry in row] for row in matrix]
    n=len(X); exponents=[]
    def val(z):
        v=0
        if z%mod==0:return N
        while z%p==0:z//=p;v+=1
        return v
    for k in range(n):
        v,i,j=min((val(X[i][j]),i,j) for i in range(k,n) for j in range(k,n))
        if v==N:raise AssertionError('precision too small')
        X[k],X[i]=X[i],X[k]
        for row in X:row[k],row[j]=row[j],row[k]
        pv=X[k][k]
        assert val(pv)==v
        # The pivot's unit factor is invertible modulo p^(N-v).
        inv=pow(pv//(p**v),-1,p**(N-v))
        for i in range(k+1,n):
            z=X[i][k];assert z%(p**v)==0
            multiplier=(z//(p**v)*inv)%(p**(N-v))
            for j in range(k,n):
                X[i][j]=(X[i][j]-multiplier*X[k][j])%mod
            assert X[i][k]==0
        for j in range(k+1,n):
            z=X[k][j];assert z%(p**v)==0
            multiplier=(z//(p**v)*inv)%(p**(N-v))
            for i in range(k,n):
                X[i][j]=(X[i][j]-multiplier*X[i][k])%mod
            assert X[k][j]==0
        exponents.append(v)
    return Counter(exponents)


def main():
    L=build()
    # From SRG relation A^2=5I-4A+5J: eigenvalues 10,1^20,-5^6.
    # Thus L has 0,9^20,15^6, and the matrix-tree determinant is
    # 9^20 * 15^6 / 27 = 3^43 * 5^6.
    tree=3**43*5**6
    assert tree==5129015115539641837921875
    for deleted in (0,18,26):
        B=minor(L,deleted)
        assert bareiss_det(B)==tree
        a=local_smith_exponents(B,3)
        b=local_smith_exponents(B,5)
        assert a==Counter({0:7,2:14,3:5}),a
        assert b==Counter({0:20,1:6}),b
        factors=[1]*7+[9]*13+[45]+[135]*5
        assert len(factors)==26
        assert all(factors[i+1]%factors[i]==0 for i in range(25))
        assert prod(factors)==tree
        assert [sum(x%3==0 for x in factors) for _ in range(1)]==[19]
        print('sink',deleted,'tree',tree,'3-primary',dict(a),'5-primary',dict(b),'invariant factors',factors)
    print('SCHLAEFLI_27_LINE_BOUNDARY_INTEGRAL_COMPONENT_GROUP_OK')

if __name__=='__main__':main()
