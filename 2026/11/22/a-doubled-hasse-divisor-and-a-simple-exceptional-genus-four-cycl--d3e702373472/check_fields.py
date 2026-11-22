#!/usr/bin/env python3
"""Check the four monic irreducible polynomials used for exact point counts."""
P=31
POLYS=[[29,1],[3,21,1],[12,16,17,1],[26,25,9,5,1]] # constant-first

def trim(a):
    a=a[:]
    while a and a[-1]==0:a.pop()
    return a

def rem(a,b):
    b=trim(b)
    assert b
    a=trim(a)
    inv=pow(b[-1],-1,P)
    while len(a)>=len(b):
        c=a[-1]*inv%P; k=len(a)-len(b)
        for i,x in enumerate(b):a[k+i]=(a[k+i]-c*x)%P
        a=trim(a)
    return a

def gcd(a,b):
    while b:a,b=b,rem(a,b)
    if not a:return []
    inv=pow(a[-1],-1,P)
    return [x*inv%P for x in a]

def mul(a,b,f):
    x=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):x[i+j]=(x[i+j]+v*w)%P
    return rem(x,f)

def pw(a,k,f):
    z=[1]
    while k:
        if k&1:z=mul(z,a,f)
        a=mul(a,a,f);k>>=1
    return z

def irreducible(f):
    n=len(f)-1
    x=rem([0,1],f)
    prime_divisors=[r for r in range(2,n+1) if n%r==0 and all(r%s for s in range(2,int(r**.5)+1))]
    for r in prime_divisors:
        h=pw(x,P**(n//r),f)
        delta=[0]*max(len(h),len(x))
        for i,c in enumerate(h):delta[i]=(delta[i]+c)%P
        for i,c in enumerate(x):delta[i]=(delta[i]-c)%P
        if gcd(f,trim(delta)) != [1]:return False
    return pw(x,P**n,f)==x

if __name__=='__main__':
    for f in POLYS:
        assert irreducible(f),f
        print('irreducible degree',len(f)-1,'over F31 (constant-first):',f)
