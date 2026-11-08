#!/usr/bin/env python3
"""Exact independent coefficient/identity checks for genus-four Kummer family.
Only Python standard library required. This verifies finite instances; the
uniform statement follows from the proof, not from finite testing.
"""
from math import comb

def primes(bound):
    return [n for n in range(2,bound+1) if all(n%d for d in range(2,int(n**0.5)+1))]

def plus(a,b,p):
    c=[0]*max(len(a),len(b))
    for i in range(len(c)):
        c[i]=((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%p
    return strip(c)

def mul(a,b,p):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]=(c[i+j]+x*y)%p
    return strip(c)

def strip(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def power(a,n,p):
    b=[1]
    while n:
        if n&1:b=mul(b,a,p)
        a=mul(a,a,p);n//=2
    return b

def H(n,p):
    h=[0]*(n+1)
    for j in range(n//2+1):h[n-2*j]=(comb(n,2*j)*comb(2*j,j))%p
    return strip(h)

def direct_central(n,p):
    # Independently expand (z^2+t z+1)^n in z,
    # with coefficients in F_p[t] using three-term convolution.
    a=[[1]]
    for k in range(n):
        b=[[] for _ in range(len(a)+2)]
        for i,pol in enumerate(a):
            for shift,component in [(0,[1]),(1,[0,1]),(2,[1])]:
                idx=i+shift
                b[idx]=plus(b[idx],mul(pol,component,p),p) if b[idx] else mul(pol,component,p)
        a=b
    return a[n]

def quotient(a,b,p):
    a=strip(a[:]);b=strip(b[:]);out=[0]*max(1,(len(a)-len(b)+1))
    if b==[0]:raise ZeroDivisionError
    while len(a)>=len(b) and a!=[0]:
        deg=len(a)-len(b);q=a[-1]*pow(b[-1],-1,p)%p;out[deg]=q
        for j,v in enumerate(b):a[deg+j]=(a[deg+j]-q*v)%p
        strip(a)
    return strip(out),a

def gcd(a,b,p):
    while b!=[0]:
        _,r=quotient(a,b,p);a,b=b,r
    return a

def derivative(a,p):
    return strip([(i*a[i])%p for i in range(1,len(a))] or [0])

checked=[]
for p in primes(149):
    if p%6!=5:continue
    q=(p-2)//3;k=(q+1)//2
    A=H(q,p);B=H(2*q+1,p)
    assert A==direct_central(q,p)
    assert B==direct_central(2*q+1,p)
    assert B==mul(A,power([(-4)%p,0,1],k,p),p)
    assert len(A)==q+1 and A[-1]==1
    assert len(gcd(A,derivative(A,p),p))==1
    assert sum((A[i]*pow(2,i,p))%p for i in range(len(A)))%p!=0
    assert sum((A[i]*pow(p-2,i,p))%p for i in range(len(A)))%p!=0
    checked.append((p,q))
print('HASSE_POLYNOMIAL_IDENTITY_AND_SQUAREFREE_FINITE_CHECK_PASS',checked)

# Compare the direct full Cartier coefficient extraction with its claimed
# two-arrow form for characteristic 5 and 11 by reading coefficients of x.
for p in [5,11,17]:
    q=(p-2)//3
    F=[ [1],[0],[0],[0,1],[0],[0],[1] ] # x^6 + t x^3 + 1
    def exp_x(e):
        a=[[1]]
        for _ in range(e):
            b=[[0] for _ in range(len(a)+6)]
            for i,x in enumerate(a):
                for j,y in enumerate(F):
                    if y!=[0]:b[i+j]=plus(b[i+j],mul(x,y,p),p)
            a=b
        return a
    for j in [1,2]:
        jp=2 if j==1 else 1
        e=(p*jp-j)//3
        expanded=exp_x(e)
        for i in ([0] if j==1 else [0,1,2]):
            images={}
            for degree,coef in enumerate(expanded):
                k=degree+i
                if k%p==p-1 and coef!=[0]:
                    outdegree=(k-(p-1))//p
                    images[outdegree]=plus(images.get(outdegree,[0]),coef,p)
            if (j,i)==(1,0):assert images=={1:H(2*q+1,p)}
            elif (j,i)==(2,1):assert images=={0:H(q,p)}
            else:assert images=={}
    print('CARTIER_DIRECT_EXTRACTION_PASS',p)
