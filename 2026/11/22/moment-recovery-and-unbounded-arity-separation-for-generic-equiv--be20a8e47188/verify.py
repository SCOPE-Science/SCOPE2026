"""Standalone exact checks for finite-base spectra of an equivalence-constrained graph."""
from collections import defaultdict
from fractions import Fraction
from math import factorial

def rgs_partitions(n):
    if n == 0:
        yield ()
        return
    def rec(a, hi):
        if len(a) == n:
            yield tuple(a)
            return
        for v in range(hi + 2):
            a.append(v)
            yield from rec(a, max(hi, v))
            a.pop()
    yield from rec([0], 0)

def profile_partitions(n, maximum=None):
    if n == 0:
        yield ()
        return
    if maximum is None:
        maximum = n
    for a in range(min(n, maximum), 0, -1):
        for p in profile_partitions(n-a, a):
            yield (a,) + p

def old_classes(profile):
    return tuple(i for i, s in enumerate(profile) for _ in range(s))

def count_direct(profile, r):
    old = old_classes(profile)
    n = len(old)
    total = 0
    for part in rgs_partitions(n+r):
        if any((part[i] == part[j]) != (old[i] == old[j])
               for i in range(n) for j in range(i+1, n)):
            continue
        free = sum(part[i] != part[j]
                   for i in range(n+r) for j in range(i+1,n+r) if j >= n)
        total += 1 << free
    return total

def count_by_new_blocks(profile, r):
    n = sum(profile)
    total = 0
    for rel in rgs_partitions(r):
        b = max(rel,default=-1)+1
        sizes = [rel.count(i) for i in range(b)]
        between = sum(sizes[i]*sizes[j] for i in range(b) for j in range(i+1,b))
        def rec(i, used, cost):
            if i == b:
                return 1 << (r*n+between-cost)
            subtotal = rec(i+1,used,cost) # this block creates a fresh equivalence class
            for c, a in enumerate(profile):
                if c not in used:
                    subtotal += rec(i+1,used | {c},cost+sizes[i]*a)
            return subtotal
        total += rec(0,set(),0)
    return total

def convolve(a,b):
    out = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j] += x*y
    return out

def collision_polynomial(k):
    p = [0,1]
    p = convolve(p,[1,-2,1])
    for j in range(1,k+1):
        p = convolve(p,[-1,2**j])
    return p

def moment(profile,j):
    return sum((Fraction(1,2**(j*a)) for a in profile),Fraction(0))

if __name__ == '__main__':
    cases=0
    for n in range(0,5):
        for profile in profile_partitions(n):
            for r in range(1,4):
                a=count_direct(profile,r)
                b=count_by_new_blocks(profile,r)
                assert a==b, (profile,r,a,b)
                cases+=1
    print('direct-Fraisse-diagram versus block-enumerator comparisons:',cases)
    for r in range(1,8):
        c=0
        for rel in rgs_partitions(r):
            b=max(rel)+1
            sizes=[rel.count(i) for i in range(b)]
            cross=sum(sizes[i]*sizes[j] for i in range(b) for j in range(i+1,b))
            c += (2**cross) * ((-1)**(b-1)) * factorial(b-1)
        assert c % 2 == 1
        print('moment coefficient',r,c)
    for k in range(1,6):
        poly=collision_polynomial(k)
        pos=tuple(a for a,c in enumerate(poly) for _ in range(max(0,c)))
        neg=tuple(a for a,c in enumerate(poly) for _ in range(max(0,-c)))
        assert pos != neg and sum(pos)==sum(neg)>0
        assert all(moment(pos,j)==moment(neg,j) for j in range(1,k+1))
        assert moment(pos,k+1)!=moment(neg,k+1)
        print('unbounded-arity witness',k,'base size',sum(pos),'moment next difference',moment(pos,k+1)-moment(neg,k+1))
    first=[]
    for n in range(1,13):
        d=defaultdict(list)
        for p in profile_partitions(n):
            d[moment(p,1)].append(p)
        collisions=[group for group in d.values() if len(group)>1]
        if n<12:
            assert not collisions
        else:
            assert len(collisions)==1 and len(collisions[0])==2
            assert set(collisions[0])=={(5,5,1,1),(4,2,2,2,2)}
            first=collisions[0]
        print('unary census',n,'partition profiles',sum(map(len,d.values())),'collision pairs',sum(len(z)*(len(z)-1)//2 for z in collisions))
    assert count_by_new_blocks(first[0],1)==count_by_new_blocks(first[1],1)==8448
    assert count_by_new_blocks(first[0],2)!=count_by_new_blocks(first[1],2)
    print('ALL_CHECKS_PASS')
