#!/usr/bin/env python3
"""Independent finite consistency tests for crown one-point extension orbit formulas.
Run with Python 3 standard library only.
"""
from math import gcd
from collections import Counter


def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a


def luc(n):
    return fib(n-1)+fib(n+1)


def euler_phi(n):
    return sum(gcd(k,n)==1 for k in range(1,n+1))


def shift(mask,n,k):
    return sum(1<<((i+k)%n) for i in range(n) if mask & (1<<i))


def reversal_a(mask,n,k):
    return sum(1<<((k-i)%n) for i in range(n) if mask & (1<<i))


def reversal_b(mask,n,k):
    return sum(1<<((k-i-1)%n) for i in range(n) if mask & (1<<i))


def transform(profile,n,k,reflection):
    a,b=profile
    if reflection:
        return reversal_a(a,n,k),reversal_b(b,n,k)
    return shift(a,n,k),shift(b,n,k)


def crown_ideals(n):
    return {(am,bm) for am in range(1<<n) for bm in range(1<<n)
            if all(not(bm>>j&1) or (am>>j&1 and am>>((j+1)%n)&1)
                   for j in range(n))}


def id_to_set(ide,n):
    a,b=ide
    return set(i for i in range(n) if a>>i&1) | set(n+j for j in range(n) if b>>j&1)


def compatible_profile(L,U,n):
    # No duplicated parameter and every old parameter below the new point
    # is strictly below each one above the new point.
    if L & U: return False
    return all(p < n and q >= n and (q-n==p or (q-n+1)%n==p)
               for p in L for q in U)


def encode_pair(L,U,n):
    return ((sum(1<<i for i in L if i<n),sum(1<<(i-n) for i in L if i>=n)),
            (sum(1<<i for i in U if i<n),sum(1<<(i-n) for i in U if i>=n)))


def action_on_profile(profile,n,k,reflection):
    L,U=profile
    return transform(L,n,k,reflection),transform(U,n,k,reflection)


def literal_profiles(n):
    # Tests the logic independently via the 3 choices (<, >, incomparable)
    # on every vertex, rather than using the type counting formula.
    v=2*n
    allowed=[]
    for word in range(3**v):
        z=word;L=set();U=set()
        for i in range(v):
            digit=z%3;z//=3
            if digit==1:L.add(i)
            elif digit==2:U.add(i)
        if not compatible_profile(L,U,n):continue
        # Downset: old upper points in L force both old lower neighbors in L.
        if any(n+j in L and (j not in L or (j+1)%n not in L) for j in range(n)):
            continue
        # Upset: old lower points in U force both old upper neighbors in U.
        if any(i in U and (n+i not in U or n+(i-1)%n not in U) for i in range(n)):
            continue
        allowed.append(encode_pair(L,U,n))
    return set(allowed)


def orbit_count(objects,n,action):
    # Directly groups objects by their full group orbits.
    unseen=set(objects);orbits=0
    while unseen:
        x=next(iter(unseen))
        orbit={action(x,n,k,r) for k in range(n) for r in (False,True)}
        assert orbit <= objects
        unseen.difference_update(orbit)
        orbits+=1
    return orbits


def formula_B(n):
    return (sum(euler_phi(n//d)*luc(2*d) for d in range(1,n+1) if n%d==0)
            +n*fib(n+3))//(2*n)


def run():
    assert [luc(2*n) for n in (3,4,5,6)] == [18,47,123,322]
    for n in range(3,11):
        objects=crown_ideals(n)
        assert len(objects)==luc(2*n)
        assert all(sum(transform(x,n,k,False)==x for x in objects)==luc(2*gcd(n,k)) for k in range(n))
        assert all(sum(transform(x,n,k,True)==x for x in objects)==fib(n+3) for k in range(n))
        b=orbit_count(objects,n,transform)
        assert b==formula_B(n)
        if n<=6:
            tp=literal_profiles(n)
            assert len(tp)==2*len(objects)-1+4*n
            mixed={p for p in tp if any(p[0]) and any(p[1])}
            assert len(mixed)==4*n
            assert orbit_count(mixed,n,action_on_profile)==3
            assert orbit_count(tp,n,action_on_profile)==2*b+2
        print(f'n={n} ideals={len(objects)} fixed_reflection={fib(n+3)} ideal_orbits={b} extension_orbits={2*b+2}')
    for n in range(3,201):
        d=sum(euler_phi(n//j)*luc(2*j) for j in range(1,n+1) if n%j==0)+n*fib(n+3)
        assert d%(2*n)==0
        assert d//(2*n)==formula_B(n)
    a4=crown_ideals(4)
    free={s for s in a4 if all(transform(s,4,k,r)!=s for k in range(4) for r in (False,True) if (k,r)!=(0,False))}
    assert len(free)==8
    assert not any(all(transform(s,3,k,r)!=s for k in range(3) for r in (False,True) if (k,r)!=(0,False)) for s in crown_ideals(3))
    print('verified: complete type orbits n=3..6; ideal Burnside n=3..10; integrality n=3..200; first asymmetric ideal n=4')
    print('VERIFY_OK')

if __name__=='__main__':run()
