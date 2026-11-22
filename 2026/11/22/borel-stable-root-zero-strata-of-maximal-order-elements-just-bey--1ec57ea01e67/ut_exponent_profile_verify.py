"""Exact finite checks for a prime-power exponent boundary in unitriangular groups.
Run: python3 ut_exponent_profile_verify.py; uses only Python standard library.
"""
from itertools import product
from collections import Counter


def matmul(A,B,q):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n))%q for j in range(n)] for i in range(n)]


def nonzero_power(A,r,q):
    B=[[int(i==j) for j in range(len(A))] for i in range(len(A))]
    for _ in range(r):
        B=matmul(B,A,q)
    return any(B[i][j] for i in range(len(A)) for j in range(i+1,len(A)))


def predicted(Z,r,q):
    Z=set(Z)
    if not Z or Z=={1} or Z=={r+1}:
        return (1,1)
    if len(Z)==1 and next(iter(Z)) in range(2,r+1):
        return (q-1,q)
    if len(Z)==2 and any(Z=={j,j+1} for j in range(1,r+1)):
        return (q-1,q)
    return (0,1)


def check(q,r):
    n=r+2
    positions=[(i,j) for i in range(n) for j in range(i+1,n)]
    hits=Counter();total=Counter()
    for v in product(range(q),repeat=len(positions)):
        A=[[0]*n for _ in range(n)]
        for (i,j),a in zip(positions,v):A[i][j]=a
        zeros=tuple(i+1 for i in range(r+1) if A[i][i+1]==0)
        total[zeros]+=1
        hits[zeros]+=nonzero_power(A,r,q)
    for Z,m in total.items():
        num,den=predicted(Z,r,q)
        assert hits[Z]*den==m*num,(q,r,Z,hits[Z],m,num,den)
    N=sum(hits.values())
    expected_num=(q-1)**r*(q*q+r*q+1)
    expected_den=q**(r+2)
    assert N*expected_den == (q**len(positions))*expected_num,(q,r,N)
    print(f'FIELD_{q}_POWER_{r}_MATRIX_{n} PASS total={sum(total.values())} maximal={N} zero_patterns={len(total)}')

if __name__=='__main__':
    # Char(q)=q for prime q. The r=2,3,4 checks include p-power cases.
    for q,r in [(2,2),(2,3),(2,4),(3,3)]:check(q,r)
    print('UT_EXPONENT_ROOT_PATTERN_VERIFIED')
