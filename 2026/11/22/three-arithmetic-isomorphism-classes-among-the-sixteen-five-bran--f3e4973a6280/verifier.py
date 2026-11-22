#!/usr/bin/env python3
"""Exact finite-field and affine-orbit certificate for five-branch Humbert curves.

No external libraries or network required; all operations are finite and exact.
"""
from itertools import product
from collections import Counter

P=5
SQ5={1,4}
B=range(5)

# F25=F5[z]/(z^2-2).
def plus(x,y): return ((x[0]+y[0])%5,(x[1]+y[1])%5)
def times(x,y): return ((x[0]*y[0]+2*x[1]*y[1])%5,(x[0]*y[1]+x[1]*y[0])%5)
def power(x,n):
    r=(1,0)
    while n:
        if n&1: r=times(r,x)
        x=times(x,x);n>>=1
    return r
def div(x,y):
    if y==(0,0): raise ZeroDivisionError
    return times(x,power(y,23))
def minus(x,y): return plus(x,((-y[0])%5,(-y[1])%5))
def as_f25(a): return (a%5,0)
def square(x): return x==(0,0) or power(x,12)==(1,0)
F25=list(product(range(5),repeat=2))
assert len(set(F25))==25
assert all(times(x,power(x,23))==(1,0) for x in F25 if x!=(0,0))
assert sum(square(x) for x in F25)==13

def local_fibre(eps, j, q):
    # q=5 or 25; return rational points over the rational base point x=j.
    if q==5:
        embed=lambda a: a%5
        mult=lambda a,b:(a*b)%5
        quotient=lambda a,b: (a*pow(b,-1,5))%5
        is_sq=lambda a: a in SQ5
    else:
        embed=as_f25;mult=times;quotient=div;is_sq=square
    if j=='infty':
        return 16 if all(is_sq(embed(x)) for x in eps) else 0
    if j==0:
        ok=all(is_sq(quotient(mult(embed(eps[a-1]),embed(a)),embed(eps[0]))) for a in range(2,5))
        return 8 if ok else 0
    # x=j is a simple zero for the jth radical; the other three determine the residue field.
    ok=all(is_sq(quotient(mult(embed(eps[a-1]),embed(j-a)),embed(j))) for a in range(1,5) if a!=j)
    return 8 if ok else 0

def fibre_generic(eps,x,q):
    if q==5:
        raise AssertionError('Every finite x in F5 is branched')
    z=as_f25
    return 16 if all(square(div(times(z(eps[a-1]),minus(x,z(a))),x)) for a in range(1,5)) else 0


def eta(eps):
    # Character of quadratic twist on five genus-one quotients E_j.
    chi=lambda x: 1 if x==1 else -1
    cs=[chi(x) for x in eps]
    p=1
    for x in cs:p*=x
    return (p,)+tuple(p*cs[j-1] for j in range(1,5))

def pt_count(eps,q):
    total=local_fibre(eps,'infty',q)+sum(local_fibre(eps,j,q) for j in B)
    if q==25:
        total+=sum(fibre_generic(eps,x,q) for x in F25 if x[1]!=0)
    return total

# The elliptic quotient y^2=prod_{b != j}(x-b) has two infinity points.
def elliptic_point_count(j):
    return 2+sum(1+(0 if val==0 else 1 if val in SQ5 else -1) for x in B for val in [__import__('math').prod((x-b)%5 for b in B if b!=j)%5])

assert [elliptic_point_count(j) for j in B]==[8]*5

S=list(product((1,2),repeat=4))
all_rows=[]
for eps in S:
    sig=eta(eps)
    assert __import__('math').prod(sig)==1
    m=sig.count(-1)
    assert m in (0,2,4)
    n5=pt_count(eps,5)
    n25=pt_count(eps,25)
    assert n5==16-4*m, (eps,n5,m)
    assert n25==56, (eps,n25)
    assert n5==6-(-2*(5-2*m))
    all_rows.append((eps,m,n5,n25))
assert Counter(m for e,m,n5,n25 in all_rows)=={0:1,2:10,4:5}
assert Counter(n5 for e,m,n5,n25 in all_rows)=={16:1,8:10,0:5}

# Exact affine action on quotient-trace signatures; any affine substitution
# sends the five monic quartics f_j to other such quartics up to a fourth power.
perms=[]
for u in range(1,5):
    for v in B:
        sigma=tuple((u*j+v)%5 for j in B)
        assert len(set(sigma))==5
        perms.append(sigma)
assert len(set(perms))==20
signatures={eta(eps) for eps in S}
assert len(signatures)==16

def perm_sig(sig, sigma):
    out=[None]*5
    for j in B:out[sigma[j]]=sig[j]
    return tuple(out)

orbits=[]
remaining=set(signatures)
while remaining:
    s=min(remaining)
    orbit={perm_sig(s,sigma) for sigma in perms}
    assert orbit<=signatures
    orbits.append(orbit)
    remaining-=orbit
assert sorted(map(len,orbits))==[1,5,10]
assert {next(iter(orbit)).count(-1) for orbit in orbits}=={0,2,4}
print('HUMBERT_F5_FIVE_BRANCH_TWISTS_VERIFIED')
print('16 twists; affine group 20; orbit sizes 1,5,10; F5 point counts 16,8,0; all F25 point counts 56')
