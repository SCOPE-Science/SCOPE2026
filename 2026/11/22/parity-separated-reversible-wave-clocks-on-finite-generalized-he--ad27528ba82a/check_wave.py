#!/usr/bin/env python3
"""Exact GF(2) matrix checks for wave clocks and Jordan-block fixed spaces.

Tests an actual 12-cycle and faithful cyclic modules of the two
universal generalized-hexagon adjacency polynomials. Cyclic modules
are algebraic test models, not constructed generalized hexagons.
"""

def eye(n):
    return [1 << i for i in range(n)]

def add(X,Y):
    return [x^y for x,y in zip(X,Y)]

def mul(X,Y):
    n = len(X)
    out=[]
    for x in X:
        r=0
        while x:
            bit=x&-x
            r^=Y[bit.bit_length()-1]
            x-=bit
        out.append(r)
    return out

def powmat(A,k):
    B=eye(len(A))
    while k:
        if k&1:B=mul(B,A)
        A=mul(A,A)
        k//=2
    return B

def rank(A):
    b={}
    for x in A:
        while x:
            i=x.bit_length()-1
            if i not in b:
                b[i]=x
                break
            x^=b[i]
    return len(b)

def nullity(A):
    return len(A)-rank(A)

def cycle(n):
    return [(1<<((i-1)%n))|(1<<((i+1)%n)) for i in range(n)]

def companion(exponents):
    n=max(exponents)
    A=[]
    for i in range(n):
        # Matrix rows: multiplication by x modulo the polynomial
        r = (1 << (i-1)) if i>0 else 0
        if i in exponents and i != n:
            r |= (1 << (n-1))
        A.append(r)
    return A

def wave(A):
    n=len(A)
    return [row | (1<<(i+n)) for i,row in enumerate(A)] + [(1<<i) for i in range(n)]

def fixed_formula(A, k, m0, m1):
    n=len(A)
    I=eye(n)
    ker0=[0]
    ker1=[0]
    for i in range(1,max(m0,m1)+2):
        if i<=m0+1:ker0.append(nullity(powmat(A,i)))
        if i<=m1+1:ker1.append(nullity(powmat(add(A,I),i)))
    def blocks(h,j):return 2*h[j]-h[j-1]-h[j+1]
    v2=(k&-k)
    d=sum(blocks(ker0,j)*min(2*j,v2) for j in range(1,m0+1))
    if k%3==0:
        d+=2*sum(blocks(ker1,j)*min(j,v2) for j in range(1,m1+1))
    return d

def check(name,A,period,m0,m1):
    T=wave(A)
    N=len(T)
    assert powmat(T,period)==eye(N)
    for p in (2,3):
        if period%p==0:assert powmat(T,period//p)!=eye(N)
    for k in range(1,period+1):
        actual=nullity(add(powmat(T,k),eye(N)))
        formula=fixed_formula(A,k,m0,m1)
        assert actual==formula,(name,k,actual,formula)
    print(name,'dimension',len(A),'wave order',period,
          'checked fixed spaces',period,'PASS')

if __name__=='__main__':
    check('actual C12 adjacency',cycle(12),12,2,4)
    check('even-parameter cyclic algebra',companion((5,7)),48,5,2)
    check('odd-parameter cyclic algebra',companion((2,6)),12,2,4)
