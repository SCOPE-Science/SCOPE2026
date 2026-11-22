#!/usr/bin/env python3
"""Direct finite checks of centralizers of canonical partial shifts."""
from itertools import combinations, permutations
from collections import Counter
from math import comb

def maps_by_forms(n):
    maps = {(): ()}
    for d in range(n):
        positions = tuple(range(d + 1, n + 1))
        for size in range(1, len(positions) + 1):
            for D in combinations(positions, size):
                m = tuple((x, x - d) for x in D)
                maps[m] = m
    for c in range(2, 2*n + 1):
        candidates = tuple(x for x in range(1, n+1)
                           if 1 <= c-x <= n and c-x <= x)
        for size in range(2, len(candidates)+1):
            for D in combinations(candidates, size):
                m = tuple((x, c-x) for x in D)
                maps[m] = m
    return list(maps)

def brute_maps(n):
    result = set()
    for size in range(n+1):
        for D in combinations(range(1, n+1), size):
            for im in permutations(range(1, n+1), size):
                m = tuple(zip(D, im))
                if any(y>x for x,y in m):
                    continue
                if any(abs(x1-x2)!=abs(y1-y2)
                       for x1,y1 in m for x2,y2 in m):
                    continue
                result.add(m)
    return result

def compose(a,b):
    right = dict(b)
    return tuple((x,right[y]) for x,y in a if y in right)

def formula(n,k):
    T = Counter({0:1})
    for d in range(n):
        product = Counter({0:1})
        for j in range(1,min(k,n-d)+1):
            length = 1+(n-d-j)//k
            new = Counter(product)
            for degree,coef in product.items():
                new[degree+length]+=coef
            product = new
        product[0]-=1
        T.update(product)
    R=Counter()
    for p in range(n-k+1,n):
        for q in range(p+1,n+1):
            choices = max(0,p+min(k,p)-q)
            for j in range(q-p):
                R[2+j]+=choices*comb(q-p-1,j)
    return T,R

def verify():
    for n in range(1,7):
        assert set(maps_by_forms(n))==brute_maps(n), ('forms incomplete',n)
    case_count=0
    for n in range(2,10):
        maps=maps_by_forms(n)
        for k in range(1,n):
            shift=tuple((x,x-k) for x in range(k+1,n+1))
            commuting=[a for a in maps if compose(a,shift)==compose(shift,a)]
            direct_T=Counter(len(a) for a in commuting if not (
                len(a)>=2 and a[0][1]>a[-1][1]))
            direct_R=Counter(len(a) for a in commuting if len(a)>=2
                             and a[0][1]>a[-1][1])
            T,R=formula(n,k)
            assert direct_T==+T, ('translation rank mismatch',n,k,direct_T,T)
            assert direct_R==+R, ('reflection rank mismatch',n,k,direct_R,R)
            assert sum(T.values())==(n-k+2)*(2**k)-n-1
            if n>=2*k-1:
                closed_R=sum((k-w)**2 * 2**(w-1) for w in range(1,k))
                assert sum(R.values())==closed_R==3*2**k-k*k-2*k-3
            case_count+=1
    print('CENTRALIZER_RANK_CENSUS_OK',case_count)

if __name__=='__main__':
    verify()
