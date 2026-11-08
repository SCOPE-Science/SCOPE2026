#!/usr/bin/env python3
"""Independent direct-neighborhood and cyclotomic checks for quartic circulants."""
from itertools import combinations
from math import comb

def degree(p):
    while p and p[-1] == 0: p.pop()
    return len(p)-1

def divide_monic(poly, divisor):
    rem = poly[:]
    quotient = [0]*max(0, len(poly)-len(divisor)+1)
    while degree(rem) >= len(divisor)-1:
        d=degree(rem)-len(divisor)+1
        a=rem[-1]
        quotient[d]=a
        for k,v in enumerate(divisor): rem[d+k]-=a*v
        degree(rem)
    return quotient,rem

def phi(k,cache={}):
    if k in cache: return cache[k]
    p=[-1]+[0]*(k-1)+[1]
    for d in range(1,k):
        if k%d == 0:
            q,r=divide_monic(p,phi(d))
            assert not r
            p=q
    cache[k]=p
    return p

def totient(n): return sum(__import__('math').gcd(i,n)==1 for i in range(1,n+1))
small=[n for n in range(1,100) if totient(n)<=6]
root_orders={}
for lam in range(-4,5):
    p=[1,0,1,-lam,1,0,1]
    roots=[]
    for d in small:
        q,r=divide_monic(p,phi(d))
        if not r: roots.append(d)
    root_orders[lam]=roots
assert root_orders=={-4:[2],-3:[],-2:[],-1:[5,6],0:[4,8],1:[3,10],2:[],3:[],4:[1]}
print('CYCLOTOMIC_CLASSIFICATION_OK',root_orders)

def prediction(n):
    out={}
    if n%2==0: out[(0,4)]=2
    if n%5==0:
        for b in range(1,5): out[(b-1,b)]=comb(5,b)
    if n%3==0:
        for b in (1,2): out[(b+1,b)]=comb(3,b)
    if n%8==0:
        for t in (1,2,3): out[(t,t)]=comb(4,t)**2
    elif n%4==0: out[(2,2)]=4
    return out

def counts(n):
    neigh=[sum(1<<((i+d)%n) for d in (-3,-1,1,3)) for i in range(n)]
    assert all(mask.bit_count()==4 for mask in neigh)
    out={}
    for setmask in range(1,(1<<n)-1):
        a=b=None
        feasible=True
        for i in range(n):
            t=(neigh[i]&setmask).bit_count()
            if setmask & (1<<i):
                if a is None: a=t
                elif t!=a: feasible=False;break
            else:
                if b is None: b=t
                elif t!=b: feasible=False;break
        if feasible:
            out[(a,b)]=out.get((a,b),0)+1
    return out
for n in range(7,19):
    actual=counts(n)
    pred=prediction(n)
    assert actual==pred, (n,actual,pred)
    print('GRAPH_ENUMERATION_OK',n,sum(actual.values()),actual)
assert sum(prediction(120).values()) == 106
assert all(sum(prediction(n).values()) <= 106 and (sum(prediction(n).values()) == 106) == (n%120==0) for n in range(7,1201))
print('UNIFORM_BOUND_SPOTCHECK_OK 7..1200')
print('VERIFY_OK')
