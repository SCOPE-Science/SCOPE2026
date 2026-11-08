#!/usr/bin/env python3
"""Exact finite enumeration and coefficient checks for the quorum-survival theorem."""
from itertools import combinations
from math import comb


def add(a, b):
    z = [0] * max(len(a), len(b))
    for i,x in enumerate(a): z[i] += x
    for i,x in enumerate(b): z[i] += x
    return z


def neg(a): return [-x for x in a]


def mul(a, b):
    z = [0] * (len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): z[i+j] += x*y
    return z


def power(a, n):
    y = [1]
    for _ in range(n): y = mul(y,a)
    return y


def norm(a):
    z=a[:]
    while len(z)>1 and z[-1]==0:z.pop()
    return z


def service(n):
    z=[0]
    for j in range(2,n+1):
        term=mul([0]*j+[comb(n,j)], power([1,-1],n-j))
        z=add(z,term)
    return norm(z)


def reliability(sizes):
    a,b,c=(service(n) for n in sizes)
    return norm(add(add(mul(a,b),mul(a,c)),add(mul(b,c),neg([2*t for t in mul(mul(a,b),c)]))))


def partitions(n,low=1,slots=3):
    if slots==1:
        if n>=low:yield (n,)
        return
    for x in range(low,n//slots+1):
        for tail in partitions(n-x,x,slots-1):yield (x,)+tail


def direct(sizes):
    n=sum(sizes)
    poly=[0]
    offsets=(0,sizes[0],sizes[0]+sizes[1],n)
    for mask in range(1<<n):
        alive=mask.bit_count()
        wins=0
        for k in range(3):
            if sum((mask>>j)&1 for j in range(offsets[k],offsets[k+1]))>=2:wins+=1
        if wins>=2:poly=add(poly,mul([0]*alive+[1],power([1,-1],n-alive)))
    return norm(poly)


def C(x):return x*(x-1)//2

def leading_difference(n):
    a=(n-1)//2;b=n-1-a
    c=n//3;d=(n+1)//3;e=(n+2)//3
    return C(a)*C(b)-C(c)*C(d)-C(c)*C(e)-C(d)*C(e)


def check():
    count=0
    for n in range(3,8):
        for sizes in partitions(n):
            assert reliability(sizes)==direct(sizes),(n,sizes)
            count+=1
    p=[0,1]; one_minus_p=[1,-1]
    A=reliability((1,3,3))
    B=reliability((2,2,3))
    Cpoly=reliability((1,2,4))
    D=reliability((1,1,5))
    assert D==[0]
    assert norm(add(A,neg(Cpoly)))==norm(mul(power(p,4),mul(one_minus_p,[3,-1])))
    assert norm(add(B,neg(A)))==norm(mul([0,0,0,0,2],mul(power(one_minus_p,2),[-1,2])))
    assert norm(add(B,neg(Cpoly)))==norm(mul(power(p,4),mul(one_minus_p,[1,5,-4])))
    X=reliability((2,2,2));Y=reliability((1,2,3))
    assert norm(add(X,neg(Y)))==norm(mul([0,0,0,0,0,2],one_minus_p))
    for n in range(7,301):
        assert leading_difference(n)>0, n
        a=(n-1)//2; c=n//3; d=(n+1)//3
        if n>=8:assert c+d-2>a-1,n
    print('PASS:',count,'independent survivor-state polynomials through seven species; all critical factor identities; 294 exact leading-coefficient and high-survival inequalities.')

if __name__=='__main__':check()
