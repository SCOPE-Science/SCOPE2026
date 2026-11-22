#!/usr/bin/env python3
"""Independent finite-field and exact integral-polynomial checks for a quadratic permutation's 3-cycles.

Python 3 standard library only. The infinite prime-density conclusion uses Chebotarev's
 theorem and is proved mathematically, not certified by finite computation.
"""

def norm(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def add(a,b):
    z=[0]*max(len(a),len(b))
    for i,v in enumerate(a):z[i]+=v
    for i,v in enumerate(b):z[i]+=v
    return norm(z)

def neg(a):return [-v for v in a]

def sub(a,b):return add(a,neg(b))

def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):z[i+j]+=v*w
    return norm(z)

def scale(a,n):return norm([n*v for v in a])

def powpoly(a,n):
    z=[1]
    while n:
        if n&1:z=mul(z,a)
        a=mul(a,a);n//=2
    return z

U=[0,1];one=[1]
N=add(sub(neg(powpoly(U,4)),neg(powpoly(U,2))),scale(U,2)) # -u^4+u^2+2u
D=scale(sub(one,powpoly(U,2)),2)
f=[6,0,-3,0,0,0,1]
expected=mul(powpoly(U,2),f)
A=sub(add(powpoly(N,2),mul(add(powpoly(U,2),U),powpoly(D,2))),mul(N,D))
B=add(powpoly(sub(N,mul(powpoly(U,2),D)),2),mul(sub(N,mul(U,D)),D))
assert A==expected and B==expected
assert f==add(powpoly(sub(powpoly(U,3),scale(U,3)),2),scale(powpoly(sub(one,powpoly(U,2)),2),6))
print('PASS: exact integer-polynomial elimination identities and sextic decomposition')

# Finite field polynomial arithmetic, constant coefficient first.
def canon(a,p):return norm([int(v)%p for v in a])
def divrem(a,b,p):
    a=canon(a,p);b=canon(b,p)
    if b==[0]:raise ZeroDivisionError
    inv=pow(b[-1],-1,p)
    while a!=[0] and len(a)>=len(b):
        v=a[-1]*inv%p;shift=len(a)-len(b)
        for i,c in enumerate(b):a[shift+i]=(a[shift+i]-v*c)%p
        a=norm(a)
    return a

def gcd(a,b,p):
    a=canon(a,p);b=canon(b,p)
    while b!=[0]:a,b=b,divrem(a,b,p)
    return canon([(c*pow(a[-1],-1,p))%p for c in a],p)

def mulmod(a,b,f,p):
    return divrem(mul(a,b),f,p)

def powmod(a,e,f,p):
    z=[1]
    while e:
        if e&1:z=mulmod(z,a,f,p)
        a=mulmod(a,a,f,p);e//=2
    return z

def number_roots_in_extension(p,m):
    fm=canon(f,p)
    xp=powmod(U,p**m,fm,p)
    h=gcd(fm,sub(xp,U),p)
    return len(h)-1

def primes(limit):
    return [p for p in range(2,limit+1) if all(p%d for d in range(2,int(p**0.5)+1))]

counts={1:0,2:0,3:0}; pairs_checked=0
for p in primes(139):
    if p==2:continue
    rr={m:number_roots_in_extension(p,m) for m in range(1,7)}
    if p==3:
        assert all(r==1 for r in rr.values()),(p,rr) # f mod 3 = u^6, only zero root
        expected_points=1
    else:
        assert all(r in (0,6) for r in rr.values()),(p,rr)
        if rr[1]==6:order=1
        elif rr[2]==6:order=2
        else:
            assert rr[3]==6,(p,rr)
            order=3
        assert all(rr[m]==(6 if m%order==0 else 0) for m in range(1,7)),(p,rr)
        counts[order]+=1
        expected_points=1+rr[1]
    # Directly count solutions to the third-iterate equation on all p^2 states.
    cnt=0;fixed=0
    for u in range(p):
        for v in range(p):
            a,b=u,v
            for _ in range(3):a,b=(a*a+b)%p,a
            if (a,b)==(u,v):cnt+=1
            if (u*u+v)%p==u and u==v:fixed+=1
            pairs_checked+=1
    assert cnt==expected_points,(p,cnt,expected_points)
    assert fixed==1,(p,fixed)
    if p<=19:
        for x in range(p):
            for y in range(p):
                X,Y=((x+y)**2+x)%p,((x+y)**2-y)%p
                actual=(2*(X+Y)%p,2*(X-Y)%p)
                u,v=2*(x+y)%p,2*(x-y)%p
                assert actual==((u*u+v)%p,u)
    print('p=%3d: degrees 1..6 root counts %s; primitive 3-cycles %d'%(p,[rr[m] for m in range(1,7)],(cnt-1)//3))
print('PASS:',pairs_checked,'full prime-field states; Frobenius 1/2/3 degree pattern',counts)
print('All tests passed; asymptotic density and Galois identification require the written proof.')
