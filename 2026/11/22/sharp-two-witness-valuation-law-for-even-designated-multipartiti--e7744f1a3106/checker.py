#!/usr/bin/env python3
"""Independent finite diagnostics for exact two-adic gcds of designated multipartitions.

The infinite statement follows from the separately written formal-power-series proof;
these computations test its critical low-degree identities and sample instances.
"""
from math import gcd

def mul(a,b,mod):
    n=len(a)-1
    return [sum(a[j]*b[i-j] for j in range(i+1))%mod for i in range(n+1)]

def power(a,k,mod):
    n=len(a)-1
    out=[1]+[0]*n
    a=[v%mod for v in a]
    while k:
        if k&1:out=mul(out,a,mod)
        k//=2
        if k:a=mul(a,a,mod)
    return out

def f_combinatorial(n,mod):
    x=[1]+[0]*n
    for t in range(1,n+1):
        y=x[:]
        for j in range(1,n//t+1):
            for r in range(n+1-j*t):
                y[r+j*t]=(y[r+j*t]+j*x[r])%mod
        x=y
    return x

def f_eta(n,mod):
    # Independent product f6/(f1*f2*f3), each f_delta is Euler product.
    def prod(delta):
        p=[1]+[0]*n
        for t in range(delta,n+1,delta):
            for i in range(n,t-1,-1): p[i]=(p[i]-p[i-t])%mod
        return p
    def inv(p):
        v=[1]+[0]*n
        for i in range(1,n+1):v[i]=-sum(p[j]*v[i-j] for j in range(1,i+1))%mod
        return v
    d=mul(prod(1),mul(prod(2),prod(3),mod),mod)
    return mul(prod(6),inv(d),mod)

def v2(x):
    if x==0:return 99999
    return (x&-x).bit_length()-1

def expected(k):
    if k%4==0:return v2(k)
    if k%8==6:return 2
    if k%8==2:return 3
    return v2(k+1)-1

def run():
    n=95;mod=256
    F=f_combinatorial(n,mod)
    assert F==f_eta(n,mod)
    f2=power(F,2,16)
    f16=power(F,16,16)
    assert f2[:8]==[1,2,7,0,7,0,11,8]
    assert f16[:8]==[1,0,8,0,4,0,8,0]
    assert (8*f2[5]+4*f2[3]+8*f2[1])%16==0
    checks=0
    for k in range(2,161,2):
        e=expected(k)
        B=power(F,k,mod)
        assert all(B[4*j+3]%(1<<e)==0 for j in range((n-3)//4+1)),(k,e)
        if k%16==2:
            assert B[7]%16==8,k
        elif k%4==0 or k%8==6 or k%16==10:
            assert v2(B[3])==e,k
        checks+=1
    for e in range(2,9):
        B=power(F,1<<e,1<<e)
        assert all(B[j]==0 for j in range(1,n+1,2)),e
    print('DESIGNATED_EVEN_FINITE_OK',checks,'even k,',n,'coefficients, two methods, witnesses, Frobenius')

if __name__=='__main__':run()
