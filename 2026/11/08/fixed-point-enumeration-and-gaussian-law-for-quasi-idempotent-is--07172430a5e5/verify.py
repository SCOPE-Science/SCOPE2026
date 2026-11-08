#!/usr/bin/env python3
"""Standalone finite checks for bounded-height isotone maps of finite chains.
Python 3 standard library only; deterministic, no data dependencies.
"""
from itertools import combinations_with_replacement
from math import comb

def basin_one_side(L):
    return 1 if L == 0 else 1 << (L - 1)

def basin_count(m):
    assert m >= 1
    return sum(basin_one_side(L) * basin_one_side(m - 1 - L) for L in range(m))

def full_h(n, k):
    if n == k == 0: return 1
    if not (1 <= k <= n): return 0
    h = n-k
    return sum((-1)**i * comb(2*k, i) * 2**(h-i) * comb(2*k+h-i-1,h-i)
               for i in range(min(h,2*k)+1))

def idem_h(n,k):
    if n == k == 0: return 1
    if not (1 <= k <= n): return 0
    return comb(n+k-1,n-k)

def brute(n):
    fct = [0]*(n+1); ect=[0]*(n+1)
    for f in combinations_with_replacement(range(n),n):
        f2 = tuple(f[f[i]] for i in range(n))
        f3 = tuple(f[f2[i]] for i in range(n))
        f4 = tuple(f[f3[i]] for i in range(n))
        assert (f2 == f4) == (f2 == f3), (n, f)
        k = sum(f[i] == i for i in range(n))
        if f2 == f3: fct[k] += 1
        if f2 == f: ect[k] += 1
    return fct,ect

def test():
    b = [0]+[basin_count(m) for m in range(1,18)]
    assert b[1:10] == [1,2,5,12,28,64,144,320,704], b
    for n in range(1,11):
        full,idem=brute(n)
        for k in range(n+1):
            assert full[k] == full_h(n,k),(n,k,full[k],full_h(n,k))
            assert idem[k] == idem_h(n,k),(n,k,idem[k],idem_h(n,k))
        assert sum(full) <= comb(2*n-1,n)
        assert sum(idem) <= sum(full)
    totals=[]; quasis=[]
    for n in range(1,17):
        h=sum(full_h(n,k) for k in range(n+1))
        e=sum(idem_h(n,k) for k in range(n+1))
        totals.append(h);quasis.append(h-e)
        if n>=4: assert h==5*totals[-2]-6*totals[-3]+totals[-4]
    assert totals[:10] == [1,3,10,33,108,352,1145,3721,12087,39254]
    assert quasis[:10] == [0,0,2,12,53,208,768,2734,9503,32489]
    print('VERIFY_OK exhaustive n<=10, fixed-point refinement, rational recurrence, independent basin counts')
if __name__=='__main__': test()
