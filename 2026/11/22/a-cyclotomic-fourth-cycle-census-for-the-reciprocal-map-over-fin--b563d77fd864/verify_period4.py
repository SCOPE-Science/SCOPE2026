#!/usr/bin/env python3
"""Exact integer/cyclotomic-polynomial certificate and finite-field spot checks."""
from math import gcd

def trim(v):
    while len(v)>1 and v[-1]==0: v.pop()
    return v

def add(a,b):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b): c[i+j]+=u*v
    return trim(c)

def power(a,n):
    z=[1]
    for _ in range(n): z=mul(z,a)
    return z

def neg(a):return [-v for v in a]

def sub(a,b):return add(a,neg(b))

def mod(a,f):
    a=a[:]
    while len(a)>=len(f):
        c=a[-1];shift=len(a)-len(f)
        for i in range(len(f)):a[i+shift]-=c*f[i]
        trim(a)
    return a

def ringpow(x,n,m,f):
    z=[1];u=[0,1]
    for _ in range(n%m): z=mod(mul(z,u),f)
    return z

def cyclo(m,a,f):
    return mod(add(ringpow(0,7*a,m,f),ringpow(0,8*a,m,f)),f)

X=[0,1];N=X;D=[1]
for i in range(4):
    N,D=add(mul(N,N),mul(D,D)),mul(N,D)
Q=[1,0,2];A=[1,0,4,0,2];B=[1,0,8,0,14,0,7,0,1]
assert sub(N,mul(X,D))==mul(mul(Q,A),B)
PHI16=[1]+[0]*7+[1]
PHI30=[1,1,0,-1,-1,-1,0,1,1]
assert len(PHI30)==9

def a_conj(j):
    U=sub(ringpow(0,j,16,PHI16),ringpow(0,-j,16,PHI16))
    V=add(ringpow(0,2*j,16,PHI16),ringpow(0,-2*j,16,PHI16))
    return U,V
U,V=a_conj(1)
assert mod(add(add(mul([2],power(U,4)),mul([4],mul(power(U,2),power(V,2)))),power(V,4)),PHI16)==[0]
assert [j for j in range(1,16,2) if mod(sub(mul(a_conj(j)[0],V),mul(U,a_conj(j)[1])),PHI16)==[0]]==[1,7]
cs=[]
for j in range(1,30):
    if gcd(j,30)==1:
        c=cyclo(30,j,PHI30)
        assert c not in cs
        cs.append(c)
        z=[0]
        for i,co in enumerate(B):
            z=add(z,mul([co],power(c,i)))
        assert mod(z,PHI30)==[0]
assert len(cs)==8

# Direct enumeration of orbits in odd prime fields, no false cycles through zero.
def count4(p):
    seen=set(); c=0
    for x in range(1,p):
        if x in seen:continue
        path=[];y=x
        for _ in range(4):
            if y==0:break
            path.append(y);y=(y+pow(y,-1,p))%p
        if len(path)==4 and y==x and len(set(path))==4:
            c+=1;seen.update(path)
    return c

def primes(N):
    for n in range(7,N):
        if all(n%d for d in range(2,int(n**0.5)+1)):yield n

for p in primes(1600):
    expected=int(p%16 in (1,7))+2*int(p%30==1)
    assert count4(p)==expected,(p,count4(p),expected)
print('VERIFY_OK polynomial_identity=1 cyclotomic_16=1 cyclotomic_30=1 primes_checked',sum(1 for _ in primes(1600)))
