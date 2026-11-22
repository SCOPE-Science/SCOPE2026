"""Exact finite checks of the odd extremizer classification; Python 3 standard library.

The unrestricted proof is in RESULT.md. Finite tests are corroboration only.
"""
from itertools import permutations


def F(a):
    n = len(a)
    b = [v + (v == n) for v in a]
    b.insert(len(b) - 1, n + 2)
    b.append(n)
    return tuple(b)


def even_ladder(n):
    assert n >= 4 and n % 2 == 0
    a = (3, 4, 1, 2)
    while len(a) < n:
        a = F(a)
    return a


def insert(a, p, v):
    b = [x + (x >= v) for x in a]
    b.insert(p, v)
    return tuple(b)


def degree_added(a, p, v):
    return sum(x >= v for x in a[:p]) + sum(x < v for x in a[p:])


def two_connected(a):
    n = len(a)
    if n < 3: return False
    edges = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                edges[i] |= 1 << j
                edges[j] |= 1 << i
    for excluded in range(n):
        reach = 1 << (0 if excluded else 1)
        while True:
            nxt = reach
            for i in range(n):
                if reach & (1 << i): nxt |= edges[i]
            nxt &= ~(1 << excluded)
            if nxt == reach: break
            reach = nxt
        if reach.bit_count() != n - 1: return False
    return True


def inversions(a):
    return sum(a[i] > a[j] for i in range(len(a)) for j in range(i+1,len(a)))


def triangles(a):
    return sum(a[i] > a[j] > a[k] for i in range(len(a)) for j in range(i+1,len(a)) for k in range(j+1,len(a)))


def table(n):
    if n == 4:
        return {(0,3),(1,2),(1,4),(2,1),(2,5),(3,2),(3,4),(4,3)}
    m = n // 2
    s = {(0,3),(1,2),(1,4),(2,1),(n-2,n+1),(n-1,n-2),(n-1,n),(n,n-1)}
    for j in range(1,m-1):
        s |= {(2*j+1,2*j),(2*j+1,2*j+2),(2*j+1,2*j+4)}
    return s


def cell_family(n):
    a=even_ladder(n)
    cells={(p,v) for p in range(n+1) for v in range(1,n+2) if degree_added(a,p,v)==2}
    assert cells == table(n), (n, cells ^ table(n))
    family={insert(a,p,v) for p,v in cells}
    assert len(cells) == 3*(n//2)+2
    assert len(family) == 3*(n//2)-2
    assert sum(triangles(x)==1 for x in family) == n//2
    assert all(triangles(x) <= 1 and two_connected(x) and inversions(x)==3*(n//2) for x in family)
    return family


def main():
    assert F((3,2,1)) == insert(even_ladder(4),1,2)
    for n in range(4,52,2):
        a=even_ladder(n); ext=even_ladder(n+2)
        assert F(a)==ext
        fam=cell_family(n)
        for p,v in table(n):
            if p<n and v<=n:
                assert F(insert(a,p,v))==insert(ext,p,v),(n,p,v)
            elif (p,v)==(n-2,n+1):
                assert F(insert(a,p,v))==insert(ext,n-3,n)
            elif (p,v)==(n,n-1):
                assert F(insert(a,p,v))==insert(ext,n-1,n-2)
            else:
                raise AssertionError((n,p,v))
        if n>=6:
            assert not any(abs(a[i+1]-a[i])==1 for i in range(n-1))
        print('CELL_AND_COMMUTATION',n,'count',len(fam),'PASS')
    print('ALL_SIZE_RECURSIONS n=4..50 PASS')
    for n in (3,5,7,9):
        m=(n-1)//2
        expected = {(3,2,1)} if n==3 else cell_family(n-1)
        actual=set()
        for p in permutations(range(1,n+1)):
            inv = inversions(p)
            if inv > 3*m: continue
            if two_connected(p):
                assert inv >= 3*m, (n,p,inv)
                actual.add(p)
        assert actual == expected,(n,len(actual),len(expected),actual^expected)
        print('EXHAUSTIVE',n,'minimum-layer',len(actual),'triangles',sum(triangles(p)==1 for p in actual),'PASS')
    for n in (4,6,8):
        candidates=[]
        for p in permutations(range(1,n+1)):
            if inversions(p)==3*n//2-2 and two_connected(p):candidates.append(p)
        assert candidates==[even_ladder(n)],(n,len(candidates))
        print('EVEN_UNIQUENESS',n,'PASS')
    print('VERIFY_OK')

if __name__=='__main__':main()
