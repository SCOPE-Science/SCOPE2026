#!/usr/bin/env python3
"""Exact finite-group and finite-ring checks for the quaternion group cellular-automaton normal form.
These tests support, but do not replace, the all-neighborhood classification proof.
"""
from itertools import product
from collections import Counter

# Q8 elements encoded as 2*axis + sign, axis=0,1,2,3 for 1,i,j,k.
M = [[(0,0),(0,1),(0,2),(0,3)],
     [(0,1),(1,0),(0,3),(1,2)],
     [(0,2),(1,3),(1,0),(0,1)],
     [(0,3),(0,2),(1,1),(1,0)]]
def mul(a,b):
    t,s=divmod(a,2); v,u=divmod(b,2)
    w,z=M[t][v]
    return 2*z+(s^u^w)
def inv(a):
    return a if a//2==0 else a^1
def power(a,n):
    v=0
    for _ in range(n):v=mul(v,a)
    return v
T=[[mul(a,b) for b in range(8)] for a in range(8)]
assert all(mul(mul(a,b),c)==mul(a,mul(b,c)) for a,b,c in product(range(8),repeat=3))
assert all(mul(a,inv(a))==0 for a in range(8))

# Q8=<i,j|i^4=1, i^2=j^2, j^{-1}ij=i^{-1}>.
# Unique normal form i^a j^b, a in 0..3, b in 0..1.
words = {(mul(power(2,a),power(4,b))): (a,b) for a in range(4) for b in range(2)}
assert len(words)==8

def valid_endo(A,B):
    return power(A,4)==0 and power(A,2)==power(B,2) and mul(mul(inv(B),A),B)==inv(A)
def endo(A,B):
    return tuple(mul(power(A,words[x][0]),power(B,words[x][1])) for x in range(8))
E={endo(a,b) for a,b in product(range(8),repeat=2) if valid_endo(a,b)}
assert len(E)==28
for e in E:
    assert all(e[mul(a,b)]==mul(e[a],e[b]) for a,b in product(range(8),repeat=2))
Aut=[e for e in E if len(set(e))==8]
Cent=[e for e in E if set(e).issubset({0,1})]
assert len(Aut)==24 and len(Cent)==4 and len(set(E)-set(Aut)-set(Cent))==0
assert all(e[1]==0 for e in Cent)
assert all(e[1]==1 for e in Aut)
assert all(e[e[x]]==0 for e in Cent for x in range(8))

def compatible(e,f):
    return all(mul(a,b)==mul(b,a) for a,b in product(set(e),set(f)))
assert all(compatible(e,f) for e,f in product(Cent, repeat=2))
assert all(compatible(e,f) for e in Aut for f in Cent)
assert all(not compatible(e,f) for e,f in product(Aut, repeat=2))
for r in (1,2,3):
    count=sum(all(compatible(t[i],t[j]) for i in range(r) for j in range(i+1,r)) for t in product(E,repeat=r))
    expected=4**r+24*r*4**(r-1)
    print('r=',r,'count=',count,'formula=',expected)
    assert count==expected

# Check central shears on the cyclic test ring of length 3:
# H_B(x)_i = x_i * chi(x_{i+1}) * psi(x_{i+2}).
chars=Cent

def H(x,c,d):
    n=len(x)
    return tuple(mul(x[i],mul(c[x[(i+1)%n]],d[x[(i+2)%n]])) for i in range(n))
for x in product(range(8),repeat=3):
    for c,d in product(chars,repeat=2):
        assert H(H(x,c,d),c,d)==x
# Product of the two independent offsite characters: H_c H_d=H_(c+d).
def add_char(c,d):return tuple(mul(c[x],d[x]) for x in range(8))
for x in product(range(8),repeat=3):
    for c,d in product(chars,repeat=2):
        c2,d2=chars[(chars.index(c)+1)%4],chars[(chars.index(d)+2)%4]
        assert H(H(x,c,d),c2,d2)==H(x,add_char(c,c2),add_char(d,d2))
print('PASS: 28 quaternion endomorphisms, all 3 local rule counts, central shear involutions and addition laws')

# Algebraic action of Aut(Q8) on central characters and orders of normalized
# reversible automata A_alpha H_(chi_1,chi_2).
def compose_map(a,b):return tuple(a[b[x]] for x in range(8))
def map_order(a):
    v=tuple(range(8))
    for k in range(1,25):
        v=compose_map(a,v)
        if v==tuple(range(8)):return k
    raise AssertionError

def conjugate_char_by_auto(c,a):
    ai=tuple(a.index(x) for x in range(8))
    return tuple(c[ai[x]] for x in range(8))
zeros=tuple([0]*8)
orders=Counter()
for a in Aut:
    for c,d in product(Cent,repeat=2):
        v=tuple(range(8)); w1=zeros; w2=zeros
        for t in range(1,5):
            # (a H_c)^t has offsite character sum of a^j.c, j=0..t-1.
            if t==1:
                w1,w2=c,d
            else:
                w1=add_char(w1,conjugate_char_by_auto(c,v))
                w2=add_char(w2,conjugate_char_by_auto(d,v))
            v=compose_map(v,a)
            if v==tuple(range(8)) and w1==zeros and w2==zeros:
                orders[t]+=1;break
        else: raise AssertionError('order greater than four')
print('normalized reversible map order counts on two offsite coordinates',dict(orders))
assert set(orders)=={1,2,3,4}
