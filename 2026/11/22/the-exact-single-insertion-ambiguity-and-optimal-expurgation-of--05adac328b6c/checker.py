"""Exhaustive inverse-list and confusability-census checks for doubled blocks.

Usage: python3 checker.py
Requires only Python 3 standard library.
"""
from collections import Counter, defaultdict
from itertools import product
from math import gcd


def primitive_necklaces(q, d):
    def mobius(n):
        if n == 1:
            return 1
        p = 2
        parity = 0
        while p * p <= n:
            if n % p == 0:
                n //= p
                parity += 1
                if n % p == 0:
                    return 0
            p += 1
        if n > 1:
            parity += 1
        return -1 if parity & 1 else 1
    return sum(mobius(e) * q ** (d // e) for e in range(1, d + 1) if d % e == 0) // d


def test(q, m):
    alphabet = tuple(map(str, range(q)))
    parents = defaultdict(set)
    for half in product(alphabet, repeat=m):
        h = ''.join(half)
        square = h + h
        for i in range(2*m+1):
            for ch in alphabet:
                word = square[:i]+ch+square[i:]
                parents[word].add(h)
    empirical = Counter(map(len, parents.values()))
    expected_two = q**m - q
    incidence = q**m * ((2*m+1)*q-2*m)
    expected_one = incidence-2*expected_two
    assert empirical == Counter({1: expected_one, 2: expected_two} if expected_two else {1: expected_one}), (q,m,empirical)
    graph_edges=set()
    for w, roots in parents.items():
        if len(roots)==2:
            a = w[:m]
            c = w[m]
            b = w[m+1:]
            assert c == a[0] and b == a[1:]+c, (q,m,w,roots)
            assert roots == {a,b}, (q,m,w,roots)
            graph_edges.add(frozenset(roots))
    expected_edges=set()
    rotations=set()
    alphabet_words = {''.join(t) for t in product(alphabet, repeat=m)}
    for root in alphabet_words:
        rot=root[1:]+root[0]
        if rot!=root:
            expected_edges.add(frozenset({root, rot}))
    assert graph_edges==expected_edges, (q,m,'graph differs')
    q_orbits=set()
    covered=set()
    calc_max=0
    calc_ways=1
    for root in alphabet_words:
        if root in covered:
            continue
        orbit=[]
        x=root
        while x not in orbit:
            orbit.append(x)
            x=x[1:]+x[0]
        assert x==root
        covered.update(orbit)
        d=len(orbit)
        local_edges={frozenset({u,v}) for u,v in ((x, x[1:]+x[0]) for x in orbit) if u!=v}
        assert {e for e in graph_edges if root in e or e.issubset(set(orbit))} == local_edges or d>2
        best=0;ways=0
        for mask in range(1<<d):
            subset={orbit[i] for i in range(d) if mask >> i & 1}
            if any(e.issubset(subset) for e in local_edges):
                continue
            count=len(subset)
            if count>best:
                best=count;ways=1
            elif count==best:
                ways+=1
        assert best==(1 if d==1 else d//2), (q,m,d,best)
        assert ways==(1 if d==1 else 2 if d%2==0 else d), (q,m,d,ways)
        calc_max+=best
        calc_ways*=ways
    assert covered==alphabet_words
    formula_max=q+sum(primitive_necklaces(q,d)*(d//2) for d in range(2,m+1) if m%d==0)
    formula_ways=1
    for d in range(2,m+1):
        if m%d==0:
            formula_ways *= (2 if d%2==0 else d)**primitive_necklaces(q,d)
    assert (calc_max,calc_ways)==(formula_max,formula_ways),(q,m,calc_max,formula_max)
    print(f'q={q} m={m} singleton={expected_one} doubleton={expected_two} max_subcode={formula_max} optimal_subcodes={len(str(formula_ways))} digits')


def main():
    for q,max_m in [(2,9),(3,6),(4,4)]:
        for m in range(1,max_m+1):
            test(q,m)
    print('VERIFY_OK')

if __name__=='__main__':
    main()
