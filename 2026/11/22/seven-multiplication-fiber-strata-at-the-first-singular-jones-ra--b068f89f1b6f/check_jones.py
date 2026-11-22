#!/usr/bin/env python3
"""Independent planar-diagram gluing check for the rank-(n-2) Jones product law.

Uses only Python's standard library. All positions are zero-based in code.
"""
from collections import Counter, defaultdict
from functools import lru_cache


def high(n, i, j):
    top = [a for a in range(n) if a not in (i, i + 1)]
    bottom = [a for a in range(n) if a not in (j, j + 1)]
    return tuple(sorted(tuple(sorted(x)) for x in
        [(i, i + 1), (n+j, n+j+1)] +
        [(a, n+b) for a, b in zip(top, bottom)]))


def product(a, b, n):
    # True connectivity gluing, not an implementation of the claimed formulas.
    parent = list(range(3 * n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x, y):
        x, y = find(x), find(y)
        if x != y:
            parent[x] = y
    for x, y in a:
        union(x, y)
    for x, y in b:
        union(n+x if x<n else n+x, n+y if y<n else n+y)
    # The b diagram's top x maps to middle n+x and bottom n+t maps to bottom 2n+t.
    # This is simply an n-position shift for both its top and bottom vertices.
    groups = defaultdict(list)
    for x in list(range(n)) + list(range(2*n, 3*n)):
        groups[find(x)].append(x if x < n else x-n)
    assert all(len(v) == 2 for v in groups.values())
    return tuple(sorted(tuple(sorted(v)) for v in groups.values()))


def rank(diagram, n):
    return sum((a < n) != (b < n) for a, b in diagram)


def half_type(diagram, n, which):
    pairs = sorted((a,b) for a,b in diagram if a<n and b<n) if which=='top' \
        else sorted((a-n,b-n) for a,b in diagram if a>=n and b>=n)
    assert len(pairs) == 2, pairs
    (a,b),(c,d) = pairs
    if a < c and d < b:
        assert (b,c,d)==(a+3,a+1,a+2)
        return ('N',a)
    assert b == a+1 and d == c+1 and c>=a+2, pairs
    return ('D',a,c)


def delta(a,b): return int(a==b)


def formula(U,V):
    if U[0]=='N' and V[0]=='N':
        return 1+delta(U[1],V[1])
    if U[0]=='N' and V[0]=='D':
        a=U[1]; c,d=V[1:]
        return 2+delta(a,c)+delta(a+2,d)
    if U[0]=='D' and V[0]=='N':
        a,b=U[1:]; c=V[1]
        return 2+delta(a,c)+delta(b,c+2)
    a,b=U[1:]; c,d=V[1:]
    return 4+delta(a,c)+delta(b,d)+delta(b,c+2)+delta(d,a+2)


def histogram_formula(n):
    m=n-3
    return {1:m*(m-1),
            2:m*(m*m-m+1),
            3:2*m*(m-1),
            4:m*(m+1)*(m*m-3*m+6)//4,
            5:m*(m-1)*(m-2),
            6:5*m*(m-1)//2,
            8:m}

@lru_cache(None)
def noncrossing(pairs):
    # Recursive full Catalan pairing enumeration on 2*pairs circle positions.
    if pairs == 0:
        return ((),)
    ans=[]
    for j in range(1,2*pairs,2):
        for inner in noncrossing(j//2):
            for outer in noncrossing(pairs-1-j//2):
                ans.append(tuple(sorted([ (0,j) ] +
                    [(a+1,b+1) for a,b in inner] +
                    [(a+j+1,b+j+1) for a,b in outer])))
    return tuple(ans)


def convert_circle_to_diagram(p,n):
    def conv(x): return x if x<n else n+(2*n-1-x)
    return tuple(sorted(tuple(sorted((conv(a),conv(b)))) for a,b in p))


def run():
    for n in range(3, 11):
        factors=[high(n,i,j) for i in range(n-1) for j in range(n-1)]
        assert len(set(factors)) == (n-1)**2
        if n <= 8:
            all_diagrams={convert_circle_to_diagram(p,n) for p in noncrossing(n)}
            assert set(factors) == {p for p in all_diagrams if rank(p,n)==n-2}
        freq=Counter()
        rank_fib=Counter()
        for a in factors:
            for b in factors:
                p=product(a,b,n)
                freq[p]+=1
                assert rank(p,n) in (n-2,n-4)
        if n==3:
            assert len(freq)==4 and set(freq.values())=={4}
        else:
            for p,v in freq.items():
                if rank(p,n)==n-2:
                    assert v==3*n-5
                else:
                    u=half_type(p,n,'top');w=half_type(p,n,'bottom')
                    assert v==formula(u,w),(n,u,w,v,formula(u,w))
            hist=Counter(v for p,v in freq.items() if rank(p,n)==n-4)
            assert {x:hist[x] for x in [1,2,3,4,5,6,8]}==histogram_formula(n)
            m=n-3; halves=m*(m+3)//2
            assert sum(hist.values())==halves**2
        assert sum(freq.values())==(n-1)**4
        print('n=%s: high=%s, image=%s, counts=%s: PASS'%(n,len(factors),len(freq),dict(sorted(Counter(freq.values()).items()))))
    print('ALL_CHECKS_PASS')

if __name__=='__main__': run()
