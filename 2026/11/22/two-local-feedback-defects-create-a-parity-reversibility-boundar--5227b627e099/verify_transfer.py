#!/usr/bin/env python3
"""Exact polynomial and two-by-two monodromy checks for a cyclic binary map."""
from functools import reduce

X=2

def pmul(a,b):
    r=0
    while b:
        if b&1:r^=a
        a<<=1;b>>=1
    return r

def pdiv(a,b):
    if b==0:raise ZeroDivisionError
    q=0
    while a and a.bit_length()>=b.bit_length():
        e=a.bit_length()-b.bit_length();a^=b<<e;q^=1<<e
    return q,a

def pgcd(a,b):
    while b:a,b=b,pdiv(a,b)[1]
    return a

def mmul(A,B):
    return (pmul(A[0],B[0])^pmul(A[1],B[2]),
            pmul(A[0],B[1])^pmul(A[1],B[3]),
            pmul(A[2],B[0])^pmul(A[3],B[2]),
            pmul(A[2],B[1])^pmul(A[3],B[3]))

def fib(n):
    p0,p1=0,1
    for _ in range(n):p0,p1=p1,pmul(X,p1)^p0
    return p0

def monodromy(n,d):
    M=(1,0,0,1)
    for i in range(n):
        step=(X^(i==0 or i==d),1,1,0)
        M=mmul(step,M)
    return M

def smith(n,d):
    M=monodromy(n,d)
    K=(M[0]^1,M[1],M[2],M[3]^1)
    q1=reduce(pgcd,K)
    determinant=pmul(K[0],K[3])^pmul(K[1],K[2])
    q2,rem=pdiv(determinant,q1)
    assert not rem and pdiv(q2,q1)[1]==0
    return q1,q2

def ordzero(p):return (p&-p).bit_length()-1

def kernel_dim_period(n,d,k,m):
    out=0
    for q in smith(n,d):
        e=ordzero(q);h=q>>e
        out+=min(k,e)+pgcd(h,(1<<m)|1).bit_length()-1
    return out

def check():
    total=0
    for n in range(3,65):
        for d in range(1,n//2+1):
            q1,q2=smith(n,d)
            P=pmul(X,fib(n))^pmul(fib(d),fib(n-d))
            assert pmul(q1,q2)==P,(n,d)
            assert P.bit_length()-1==n
            assert (P&1)==int(n%2==0 and d%2==1)
            assert ((q1&1)==0)+((q2&1)==0)==(0 if (n%2==0 and d%2==1) else (2 if n%2==0 else 1))
            if n in (3,7,15,31,63) and d==1 or n in (5,9,17,33) and d==2:
                assert P==1<<n and q1==1 and q2==1<<n
            total+=1
    print('TRANSFER PASS:',total,'(n,d) pairs for 3<=n<=64; exact char polynomial, Smith and parity; nilpotent families.')
    for n,d in [(7,1),(7,2),(8,1),(8,2),(9,2),(10,3),(15,1),(17,2)]:
        q1,q2=smith(n,d)
        print('example n,d',n,d,'invariants',hex(q1),hex(q2),'nilpotent length',max(ordzero(q1),ordzero(q2)))

if __name__=='__main__':check()
