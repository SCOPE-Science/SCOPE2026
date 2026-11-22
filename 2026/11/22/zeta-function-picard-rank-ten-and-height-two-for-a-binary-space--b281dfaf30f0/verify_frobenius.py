#!/usr/bin/env python3
"""Exact integer and prime-field verification for the characteristic-two quartic."""
from math import gcd
from subprocess import check_output
from pathlib import Path

EXPECTED = [15,25,81,377,1185,4273,17473,66849,266625,1052865,
            4207361,16821377,67169793]
# Compile and run verify_points.cpp before running this script.
rows = [tuple(map(int,line.split())) for line in Path('point_counts.txt').read_text().splitlines()]
assert len(rows)==13
for n,(m,q,N) in enumerate(rows,1):
    assert m==n and q==2**n and N==EXPECTED[n-1]

# Independent direct evaluation on all normalized projective points for small fields.
# This does not use the cubic-root histogram or the log/exp representation.
PRIMITIVE = {1:0x3, 2:0x7, 3:0xb, 4:0x13, 5:0x25}
def direct_count(n):
    irr=PRIMITIVE[n];q=1<<n
    def times(a,b):
        out=0
        while b:
            if b&1:out^=a
            b>>=1;a<<=1
            if a&q:a^=irr
        return out
    def ff(x):
        def phi(i,j):
            return times(times(x[i],x[i]),x[j]) ^ times(x[i],times(x[j],x[j]))
        return (times(x[1],phi(0,1))^times(x[2],phi(1,2))^
                times(x[3],phi(2,3))^times(x[0]^x[3],phi(3,0)))
    total=0
    from itertools import product
    for j in range(3,-1,-1):
        for v in product(range(q),repeat=j):
            x=list(v)+[1]+[0]*(3-j)
            total+=ff(x)==0
    return total
for n in range(1,6):
    assert direct_count(n)==EXPECTED[n-1]

traces={n:N-1-q*q for n,q,N in rows}
# Newton identities from 22 Frobenius eigenvalues.
a=[1]
for n in range(1,12):
    z=sum(a[n-i]*traces[i] for i in range(1,n+1))
    assert z%n==0
    a.append(-z//n)
assert a==[1,-10,46,-132,248,-224,-288,1408,-1920,-2048,16384,-43008]
# Poincare duality and its nonzero middle coefficient force positive reciprocal sign.
full=a+[2**(22-2*i)*a[i] for i in range(10,-1,-1)]

def mul(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):r[i+j]+=x*y
    return r

D=[1]
for _ in range(6):D=mul(D,[1,-2])
for _ in range(2):D=mul(D,[1,0,4])
Q=[1,2,2,12,32,48,96,192,512,768,512,2048,4096]
assert mul(D,Q)==full
for n in [12,13]:
    predicted=-n*full[n]-sum(full[i]*traces[n-i] for i in range(1,n))
    assert predicted==traces[n],(n,predicted,traces[n])

# Irreducibility certificate for X^12 Q(1/X) modulo 13:
# gcd(f, X^(13^6)-X)=gcd(f, X^(13^4)-X)=1,
# and X^(13^12)=X modulo f.
p=13
f=list(reversed(Q)) # coefficients constant first, monic of degree 12

def trim(v):
    while v and v[-1]==0:v.pop()
    return v

def rem(a,b):
    a=trim([z%p for z in a]); b=trim([z%p for z in b])
    assert b
    ib=pow(b[-1],-1,p)
    while len(a)>=len(b):
        k=len(a)-len(b); c=a[-1]*ib%p
        for j,d in enumerate(b): a[j+k]=(a[j+k]-c*d)%p
        trim(a)
    return a

def modmul(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): r[i+j]=(r[i+j]+x*y)%p
    return rem(r,f)

def modpow(a,n):
    r=[1]
    while n:
        if n&1:r=modmul(r,a)
        a=modmul(a,a)
        n//=2
    return r

def poly_gcd(a,b):
    while b:a,b=b,rem(a,b)
    return [x*pow(a[-1],-1,p)%p for x in a] if a else []

x=[0,1]; power=x
for d in range(1,13):
    power=modpow(power,13)
    if d in (4,6):
        difference=[(power[i] if i<len(power) else 0)-(x[i] if i<2 else 0) for i in range(max(len(power),2))]
        assert poly_gcd(f,trim([z%p for z in difference]))==[1]
    if d==12:assert power==x

# Newton slopes of the degree-12 irreducible factor, in characteristic-polynomial order.
def v2(n):
    k=0
    while n%2==0:n//=2;k+=1
    return k
vals=[v2(c) for c in Q]
assert vals==[0,1,1,2,5,4,5,6,9,8,9,11,12]
assert all(2*v>=i for i,v in enumerate(vals) if i<=2)
assert all(v>=i-1 for i,v in enumerate(vals) if 2<=i<=10)
assert all(2*v>=3*i-12 for i,v in enumerate(vals) if i>=10)
print('PASS: point counts for degrees 1..13, Newton identities, reciprocal completion,')
print('factorization, two extra traces, mod-13 irreducibility, and Newton slopes.')
