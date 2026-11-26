#!/usr/bin/env python3
"""Exact characteristic-two bitangent and tangent-flag checks for a plane quartic.

All arithmetic uses GF(64)=GF(2)[w]/(w^6+w+1). Run with Python 3 stdlib.
"""
from collections import Counter
from itertools import combinations

MOD=0x43

def mul(a,b):
    c=0
    while b:
        if b&1: c^=a
        b>>=1
        a<<=1
        if a&64: a^=MOD
    return c

def pw(a,n):
    r=1
    while n:
        if n&1: r=mul(r,a)
        a=mul(a,a)
        n>>=1
    return r

def F(x,y,z):
    return mul(pw(x,3),y)^mul(pw(y,3),z)^mul(pw(z,3),x)

def L(t,x,y,z):
    return z^mul(pw(t,3),x)^mul(t,y)

def coord(x,y,z):
    if x:return (1,mul(y,pw(x,62)),mul(z,pw(x,62)))
    if y:return (0,1,mul(z,pw(y,62)))
    return (0,0,1)

assert len({pw(2,n) for n in range(63)})==63
T=[t for t in range(1,64) if pw(t,7)==1]
W=[w for w in range(1,64) if pw(w,2)^w^1==0]
assert len(T)==7 and len(W)==2
for t in T:
    for x in range(64):
        for y in range(64):
            z=mul(pw(t,3),x)^mul(t,y)
            q=mul(t,mul(x,x))^mul(pw(t,6),mul(x,y))^mul(pw(t,4),mul(y,y))
            assert F(x,y,z)==mul(q,q)
flags={}
for t in T:
    for w in W:
        x=mul(pw(t,5),w)
        y=1
        z=mul(t,pw(w,2))
        P=coord(x,y,z)
        assert F(*P)==0 and L(t,*P)==0
        flags[(t,w)]=P
assert len(set(flags.values()))==14

def cyc_lengths(elems,fr):
    todo=set(elems);lengths=[]
    while todo:
        a=next(iter(todo));b=a;n=0
        while b in todo:
            todo.remove(b)
            b=fr(b)
            n+=1
        assert b==a
        lengths.append(n)
    return sorted(lengths)

assert cyc_lengths(T,lambda t:pw(t,2))==[1,3,3]
assert cyc_lengths(flags,lambda q:(pw(q[0],2),pw(q[1],2)))==[2,6,6]
triples={}
for a,b in combinations(T,2):
    c=a^b
    assert c in T
    u=pw(a,2)^mul(a,b)^pw(b,2)
    v=mul(mul(a,b),c)
    P=(1,u,v)
    assert all(L(t,*P)==0 for t in (a,b,c))
    assert F(*P)!=0
    triples[P]=tuple(sorted((a,b,c)))
assert len(triples)==7
assert len(set(triples.values()))==7
assert Counter(len([t for t in T if L(t,*P)==0]) for P in triples)=={3:7}
for m in range(1,13):
    fixlines=sum(pw(t,2**m)==t for t in T)
    fixflags=sum(pw(t,2**m)==t and pw(w,2**m)==w for t,w in flags)
    assert fixlines==(7 if m%3==0 else 1)
    assert fixflags==(14 if m%6==0 else 2 if m%2==0 else 0)
print('GF64_MULTIPLICATIVE_GROUP_ORDER=63')
print('BITANGENT_PARAMETERS=7; FROBENIUS_CYCLES=(1,3,3)')
print('TANGENT_FLAGS=14; FROBENIUS_CYCLES=(2,6,6)')
print('SEVEN_OFF_CURVE_TRIPLE_INTERSECTIONS_FANO_OK')
print('QUARTIC_RESTRICTION_IS_QUADRATIC_SQUARE_ON_EACH_LINE_OK')
print('BITANGENT_AND_CONTACT_POINT_COUNTS_OVER_ALL_EXTENSIONS_OK')
print('VERIFY_OK')
