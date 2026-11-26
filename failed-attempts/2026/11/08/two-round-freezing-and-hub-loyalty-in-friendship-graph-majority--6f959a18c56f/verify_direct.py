"""Exhaustive synchronous majority evolution on labelled friendship graphs.

Python 3 standard library only. Bits index the hub first and then the
individual vertices of each labelled peripheral edge.
"""
from math import comb


def theoretical(k):
    n = 2 * (4 ** k)
    fixed = 2 * sum(comb(k, u) for u in range(k // 2 + 1))
    rsum = sum(comb(k, u) * 3 ** (k-u) for u in range((k+1)//2, k+1))
    if k % 2 == 0:
        rsum -= comb(k, k//2)
    last_hub_change = 2 * rsum
    entry2 = 4 ** k - comb(2*k, k) - last_hub_change
    consensus = 2 * (3 ** k + 1)
    return dict(N=n, t0=fixed, t1=n-fixed-entry2, t2=entry2,
                reversal=last_hub_change, consensus=consensus)


def graph(k):
    total_vertices = 2*k+1
    neighbours = [0] * total_vertices
    for j in range(k):
        a, b = 2*j+1, 2*j+2
        for x, y in ((0,a),(0,b),(a,b)):
            neighbours[x] |= 1<<y
            neighbours[y] |= 1<<x
    return neighbours


def evolve(state, masks):
    ans = 0
    for v, mask in enumerate(masks):
        degree = mask.bit_count()
        ones = (mask & state).bit_count()
        if 2*ones > degree or (2*ones==degree and (state>>v)&1):
            ans |= 1<<v
    return ans


def check(k):
    masks = graph(k)
    full = 1<<(2*k+1)
    outcome = dict(N=full,t0=0,t1=0,t2=0,reversal=0,consensus=0)
    for start in range(full):
        s1 = evolve(start,masks)
        s2 = evolve(s1,masks)
        s3 = evolve(s2,masks)
        assert s3 == s2, (k,start,s2,s3)
        if s1==start: outcome['t0']+=1
        elif s2==s1: outcome['t1']+=1
        else: outcome['t2']+=1
        outcome['reversal'] += ((s2^start)&1)!=0
        outcome['consensus'] += s2 in (0,full-1)
    expected=theoretical(k)
    assert outcome==expected, (k,outcome,expected)
    print(f'k={k:2d}: {outcome}')


if __name__=='__main__':
    for k in range(1,9):
        check(k)
    print('EXHAUSTIVE_OK')
