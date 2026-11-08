#!/usr/bin/env python3
"""Exact finite-field and group-theoretic checks for the descent theorem."""

def mul(a,b):
    acc=0
    for i in range(2):
        if (b >> i) & 1: acc ^= a<<i
    for i in (2,):
        if (acc >> i) & 1: acc ^= 0b111 << (i-2)
    return acc

def inv(a):
    assert a
    for b in range(1,4):
        if mul(a,b)==1:return b
    raise ValueError('no inverse')

def eadd(P,Q):
    if P is None:return Q
    if Q is None:return P
    x,y=P;u,v=Q
    if x==u and (y^v)==x:return None
    if x==u:
        assert x!=0
        lam=x ^ mul(y,inv(x)); nu=mul(x,x)
    else:
        lam=mul(y^v,inv(x^u));nu=y^mul(lam,x)
    xx=mul(lam,lam)^lam^x^u
    yy=mul(lam,xx)^nu^xx
    return xx,yy

def points(q):
    out=[None]
    for x in range(q):
        for y in range(q):
            if (mul(y,y)^mul(x,y)) == (mul(mul(x,x),x)^1):out.append((x,y))
    return out
P=(2,0) # rho
assert mul(2,2)^2^1==0
assert len(points(2))==4 and len(points(4))==8
assert all(P in points(4) for P in [P])
O=None;mults=[]
for i in range(1,9):
    O=eadd(O,P);mults.append(O)
assert mults[1]==(1,0)
assert mults[3]==(0,1)
assert mults[4]==(3,0)==(mul(2,2),0)
assert mults[7] is None
assert len(set(mults))==8
# Frobenius acts as P -> 5 P on E[8].
for j in range(8):
    Q= None if j==0 else mults[j-1]
    Q2= None if Q is None else (mul(Q[0],Q[0]),mul(Q[1],Q[1]))
    R= None if (5*j)%8==0 else mults[((5*j)%8)-1]
    assert Q2==R,(j,Q2,R)
# Every lift t of the generator P is of order 8. Frobenius acts
# on the lifts by t -> t^5 u^epsilon with epsilon in {0,1}.
# The lift w of elliptic inversion has w -> u*w, and u is fixed.
G=[(i,b,j) for i in range(8) for b in range(2) for j in range(2)]
def prod(a,c):
    i,b,j=a;k,d,l=c
    return ((i+(k if b==0 else -k))%8,(b+d)%2,(j+l)%2)
def sigma(a,eps):
    i,b,j=a
    return ((5*i)%8,b,(eps*i+b+j)%2)
for eps in (0,1):
    assert all(sigma(prod(a,c),eps)==prod(sigma(a,eps),sigma(c,eps)) for a in G for c in G)
    assert all(sigma(sigma(a,eps),eps)==a for a in G)
    fixed=[a for a in G if sigma(a,eps)==a]
    assert len(fixed)==8
    assert set(fixed)=={(i,0,j) for i in (0,2,4,6) for j in (0,1)}
    assert len({prod(a,c) for a in fixed for c in fixed})==8
print('GF4_ELLIPTIC_GROUP_OK')
print('FROBENIUS_ORDER_TWO_OK')
print('DESCENT_C4XC2_AND_MINIMAL_F4_OK')
print('CERTIFICATE_OK')
