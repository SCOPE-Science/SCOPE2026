#!/usr/bin/env python3
"""Exact binary matrix computation using row-bitset linear algebra.
Independent of the full state graph simulator. Run: python verify_algebra.py
"""
def eye(n):return [1<<i for i in range(n)]
def xor(A,B):return [a^b for a,b in zip(A,B)]
def mul(A,B):
    n=len(A); out=[]
    for a in A:
        y=0
        while a:
            low=a&-a
            y^=B[low.bit_length()-1]
            a^=low
        out.append(y)
    return out

def rank(A):
    piv={}
    for row in A:
        while row:
            col=row.bit_length()-1
            if col not in piv:
                piv[col]=row;break
            row^=piv[col]
    return len(piv)

def cube_update(d):
    n=1<<d
    return [sum(1<<(v^(1<<i)) for i in range(d)) ^ ((1<<v) if not (v&1) else 0) for v in range(n)]

def cube_A(d):
    n=1<<d
    return [sum(1<<(v^(1<<i)) for i in range(d)) for v in range(n)]

def test(d):
    n=1<<d; I=eye(n); T=cube_update(d)
    T2=mul(T,T); T3=mul(T2,T); T6=mul(T3,T3)
    assert T6==I
    if d>=2:
        P=xor(xor(T2,T),I)
        assert mul(P,P)==[0]*n
        assert rank(P)==n//2
        assert rank(xor(T2,I))==n
        assert rank(xor(T3,I))==n//2
        assert T3!=I
    else:
        assert T3==I
    A=cube_A(d); A2=mul(A,A)
    assert A2==([0]*n if d%2==0 else I)
    print(f'd={d} dimension={n} rank(T2+T+I)={rank(xor(xor(T2,T),I))} rank(T3+I)={rank(xor(T3,I))}: OK')

if __name__=='__main__':
    for d in range(1,9):test(d)
    print('ALGEBRA_FACET_CHECK_OK')
