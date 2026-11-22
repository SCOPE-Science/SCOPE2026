#!/usr/bin/env python3
"""Finite cross-check of gap-run pairing in affine binary semigroups.
Standard library only; finite tests do not replace the infinite proof.
"""
from collections import Counter
from heapq import heappop, heappush


def greedy_cost(r):
    k = r.bit_length()
    c = 0
    while r:
        while (1 << k) - 1 > r:
            k -= 1
        b = (1 << k) - 1
        q, r = divmod(r, b)
        c += q
    return c


def apery_dijkstra(a):
    gens = [a] + [(a+1)*(1 << i) - 1 for i in range(1, a.bit_length()+1)]
    d = [None] * a
    d[0] = 0
    heap = [(0,0)]
    while heap:
        w, r = heappop(heap)
        if w != d[r]:
            continue
        for g in gens[1:]:
            r2 = (r + g) % a
            if d[r2] is None or d[r2] > w + g:
                d[r2] = w + g
                heappush(heap,(w+g,r2))
    return d


def check(a):
    c = [greedy_cost(r) for r in range(a)]
    pred = [r + a*(r + c[r]) for r in range(a)]
    d = apery_dijkstra(a)
    assert d == pred, ('apery',a)
    assert all(c[r] - c[r-1] in (-1,1) for r in range(1,a))
    F = max(d)-a
    # Directly construct the full finite membership word up to F.
    inS = [False]*(F+1)
    for t in range(F+1):
        r=t%a
        inS[t]=t>=d[r]
    runs = Counter()
    length=0
    for v in inS+[True]:
        if not v:
            length+=1
        elif length:
            runs[length]+=1
            length=0
    expect = Counter({a-r:2 for r in range(1,a) if c[r] == c[r-1]+1})
    assert runs==expect,(a,runs,expect)
    assert sum(runs.values())==a-1+c[a-1]
    return (sum(runs.values()),len(runs),F)


def main():
    for a in range(3,320):
        check(a)
    ncases=0
    for s in range(1,6):
        for n in range(1,6):
            a=(2**s+1)*2**n-1
            runs, lengths, _=check(a)
            assert runs==a+1 and lengths==(a+1)//2
            one=2 if n==1 else 0
            assert (greedy_cost(a-1)-greedy_cost(a-2)+1)==one
            ncases+=1
    print('PASS: full Apéry and maximal gap-run histograms at each a=3..319')
    print('PASS:',ncases,'binary-weight-two parameter cases, s,n=1..5; singleton boundary')
    print('A sample a=79:',check(79))
    print('The unbounded statement rests on the independent mathematical proof.')


if __name__ == '__main__':
    main()
