#!/usr/bin/env python3
"""Independent finite checks for maximum-cut degeneracy of two-token friendship graphs."""
from itertools import product
from math import comb, factorial

H = list(product((0, 1), repeat=2))

def local(h):
    return sum(not (h[0] == h[1] == v) for v in (0, 1))

def pair(h, g):
    count = 0
    for x in product((0, 1), repeat=4):
        ok = all(not (h[r] == x[2*r] == x[2*r+1]) for r in (0, 1))
        ok &= all(not (g[c] == x[c] == x[2+c]) for c in (0, 1))
        count += int(ok)
    return count

M = [[pair(h,g) for g in H] for h in H]
assert M == [[7,5,5,2], [5,6,6,5], [5,6,6,5], [2,5,5,7]]
assert [local(h) for h in H] == [1,2,2,1]
print('INDEPENDENT_LOCAL_AND_PAIR_MATRIX_PASS')

def direct_hub(q):
    z = 0
    for hh in product(range(4), repeat=q):
        val = 1
        for v in hh:
            val *= local(H[v])
        for i in range(q):
            for j in range(i+1,q):
                val *= M[hh[i]][hh[j]]
        z += val
    return z

def closed(q):
    z = 0
    for a in range(q+1):
        for b in range(q-a+1):
            c = q-a-b
            z += (factorial(q)//(factorial(a)*factorial(b)*factorial(c))
                *4**c *7**(comb(a,2)+comb(b,2)) *2**(a*b)
                *5**((a+b)*c) *6**comb(c,2))
    return z//2
expected=[0, 3, 97, 17239, 17108945, 96059118421, 3084812337312399]
for q in range(1,7):
    assert direct_hub(q) == 2 * closed(q)
    assert closed(q)==expected[q]
print('FULL_HUB_STATE_VS_THREE_TYPE_FORMULA_PASS q=1..6')
for q in (10,15,20,30,40):
    rat=closed(q)/7**comb(q,2)
    print(f'ASYMPTOTIC_SAMPLE q={q} ratio={rat:.12g}')
assert closed(30)>7**comb(30,2)
print('FORMULA_VERIFICATION_OK')
