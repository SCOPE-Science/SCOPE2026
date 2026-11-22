#!/usr/bin/env python3
"""Exact checks for finite-parameter ultrametric extension-type spectra."""
from itertools import product
from collections import defaultdict
from math import comb, factorial
from fractions import Fraction

def partitions(n):
    def extend(i, blocks):
        if i == n:
            yield tuple(tuple(b) for b in blocks)
            return
        for b in blocks:
            b.append(i)
            yield from extend(i + 1, blocks)
            b.pop()
        blocks.append([i])
        yield from extend(i + 1, blocks)
        blocks.pop()
    yield from extend(0, [])

def census():
    for n in range(1, 6):
        profiles = defaultdict(set)
        total = 0
        for lower in partitions(n):
            for upper in partitions(len(lower)):
                # The canonical isometry code is the multiset, over top blocks,
                # of multisets of bottom-block sizes.
                code = tuple(sorted(tuple(sorted(len(lower[i]) for i in block))
                                    for block in upper))
                sizes = (tuple(sorted(len(b) for b in lower)),
                         tuple(sorted(sum(len(lower[i]) for i in block)
                                      for block in upper)))
                profiles[sizes].add(code)
                total += 1
        types = sum(len(v) for v in profiles.values())
        pairs = sum(len(v) * (len(v)-1)//2 for v in profiles.values())
        expected = [(1,1,0),(3,3,0),(12,6,0),(60,14,0),(358,27,1)][n-1]
        assert (total, types, pairs) == expected, (n,total,types,pairs)
        print(f'old_n={n}: labeled_nested={total} isometry_types={types} profile_collision_pairs={pairs}')

def base(upper):
    bottom = [(0,1),(2,),(3,),(4,)]
    def same(p,i,j): return any(i in b and j in b for b in p)
    return {(i,j): (1 if same(bottom,i,j) else 2 if same(upper,i,j) else 3)
            for i in range(5) for j in range(i)}

def ultra3(x,y,z):
    a,b,c = sorted((x,y,z))
    return b==c

def slots(old):
    return [v for v in product((1,2,3),repeat=5)
            if all(ultra3(v[i],v[j],old[i,j])
                   for i in range(5) for j in range(i))]

def brute(old,k):
    profiles = slots(old)
    count=0
    for new_profiles in product(profiles,repeat=k):
        for dnew in product((1,2,3), repeat=k*(k-1)//2):
            d={(i,j):dnew[i*(i-1)//2+j] for i in range(k) for j in range(i)}
            if not all(ultra3(new_profiles[i][a],new_profiles[j][a],d[i,j])
                       for i in range(k) for j in range(i) for a in range(5)):
                continue
            if not all(ultra3(d[i,j],d[i,h],d[j,h])
                       for i in range(k) for j in range(i) for h in range(j)):
                continue
            count+=1
    return len(profiles),count

def spectrum(c,upto=6):
    h=len(c); nmax=upto
    # u_0(0)=u_0(1)=1; u_{j+1}=exp(u_j-1)
    u=[[0]*(nmax+1) for _ in range(h+1)]
    u[0][0]=u[0][1]=1
    for lev in range(1,h+1):
        u[lev][0]=1
        for m in range(1,nmax+1):
            u[lev][m]=sum(comb(m-1,i-1)*u[lev-1][i]*u[lev][m-i]
                          for i in range(1,m+1))
    def multiply(a,b):
        return [sum(comb(m,i)*a[i]*b[m-i] for i in range(m+1))
                for m in range(nmax+1)]
    t=[1]+[0]*nmax
    for lev,nslots in enumerate(c,1):
        for _ in range(nslots):t=multiply(t,u[lev])
    return t,u

def det(a):
    a=[[Fraction(x) for x in row] for row in a]
    n=len(a);d=Fraction(1)
    for k in range(n):
        q=next((j for j in range(k,n) if a[j][k]),None)
        if q is None:return 0
        if q!=k:a[k],a[q]=a[q],a[k];d=-d
        pivot=a[k][k];d*=pivot
        for j in range(k+1,n):
            f=a[j][k]/pivot
            for t in range(k,n):a[j][t]-=f*a[k][t]
    return int(d)

def main():
    census()
    A=base(((0,1,2),(3,4)))
    B=base(((0,1),(2,3,4)))
    assert sorted(A.values())!=sorted(B.values()) or A!=B
    counts,u=spectrum((4,2,1))
    for k in range(1,5):
        s1,ta=brute(A,k)
        s2,tb=brute(B,k)
        assert (s1,s2,ta,tb)==(7,7,counts[k],counts[k])
        print(f'new_arity={k}: independent_counts=({ta},{tb}); EGF={counts[k]}')
    print('EGF arities 0..6:',counts)
    for h in range(2,8):
        _,u=spectrum([1]*h,upto=h)
        m=[[u[j-1][k] for j in range(1,h)] for k in range(1,h)]
        d=det(m)
        assert d!=0
        print(f'height={h}: inversion_matrix_determinant={d}')
    print('ALL_CHECKS_PASS')

if __name__=='__main__':main()
