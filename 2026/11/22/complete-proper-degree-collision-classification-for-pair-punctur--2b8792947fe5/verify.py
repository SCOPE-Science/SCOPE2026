#!/usr/bin/env python3
"""Finite checks of pair-punctured triple-system extension spectra.
Uses only the Python standard library. The infinite-size inversion is proved separately.
"""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
from math import comb


def fano():
    vertices = list(range(1, 8))
    triples = {tuple(sorted((a, b, a ^ b))) for a, b in combinations(vertices, 2)}
    return vertices, sorted(triples)


def affine9():
    vertices = list(product(range(3), repeat=2))
    triples = {tuple(sorted((a, b, tuple((-s-t) % 3 for s, t in zip(a, b)))))
               for a, b in combinations(vertices, 2)}
    return vertices, sorted(triples)


def cyclic13():
    vertices = list(range(13))
    triples = {tuple(sorted((b+i) % 13 for b in starter))
               for starter in [(0,1,4),(0,2,7)] for i in vertices}
    return vertices, sorted(triples)


def validate_sts(vertices, triples):
    occurrences = defaultdict(int)
    for block in triples:
        assert len(set(block)) == 3
        for pair in combinations(block, 2):
            occurrences[frozenset(pair)] += 1
    assert len(occurrences) == comb(len(vertices), 2)
    assert all(count == 1 for count in occurrences.values())


def leave(vertices, triples, a, b):
    surviving = [v for v in vertices if v not in (a, b)]
    used = {frozenset(pair) for block in triples if a not in block and b not in block
            for pair in combinations(block, 2)}
    edges = [(u, v) for u, v in combinations(surviving, 2)
             if frozenset((u, v)) not in used]
    return surviving, edges


def cycle_lengths(surviving, edges):
    neighbors = {v: set() for v in surviving}
    for u, v in edges:
        neighbors[u].add(v)
        neighbors[v].add(u)
    assert sorted(len(neighbors[v]) for v in surviving) == [0]+[2]*(len(surviving)-1)
    unseen = set(surviving)
    lengths = []
    while unseen:
        start = min(unseen)
        stack = [start]
        component = set()
        while stack:
            x = stack.pop()
            if x in component:
                continue
            component.add(x)
            stack += sorted(neighbors[x] - component)
        unseen -= component
        if len(component) > 1:
            assert len(component) >= 4 and len(component)%2 == 0
            lengths.append(len(component))
    return sorted(lengths)


def convolution(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i+j] += ai*bj
    return c


def cycle_matching_polynomial(n):
    return [n*comb(n-k,k)//(n-k) for k in range(n//2+1)]


def enumerate_matchings(vertices, edges):
    """Independent edge inclusion recursion, not relying on cycles or factors."""
    @lru_cache(None)
    def go(i, occupied):
        if i == len(edges):
            return (1,)
        p = go(i+1, occupied)
        u, v = edges[i]
        uv = (1<<vertices.index(u)) | (1<<vertices.index(v))
        if uv & occupied:
            return p
        q = go(i+1, occupied|uv)
        result = list(p) + [0]*(max(len(p),len(q)+1)-len(p))
        for j, count in enumerate(q):
            result[j+1] += count
        return tuple(result)
    return list(go(0,0))


def mul_trunc(a, b, n):
    out = [Fraction(0)]*(n+1)
    for i, ai in enumerate(a[:n+1]):
        for j, bj in enumerate(b[:n+1-i]):
            out[i+j] += ai*bj
    return out


def div_trunc(a, b, n):
    assert b[0] == 1
    out = [Fraction(0)]*(n+1)
    for k in range(n+1):
        out[k] = (a[k] if k < len(a) else 0) - sum(b[j]*out[k-j] for j in range(1,min(k,len(b)-1)+1))
    return out


def log_unit(a, n):
    assert a[0] == 1
    deriv = [Fraction(k*a[k]) for k in range(1, min(len(a), n+1))]
    deriv += [Fraction(0)]*(n-len(deriv))
    quot = div_trunc(deriv, a, n-1)
    return [Fraction(0)] + [quot[k-1]/k for k in range(1,n+1)]


def inverse_cycles_from_polynomial(p):
    """Recovers 2-regular components solely from matching polynomial coefficients."""
    n = 2*(len(p)-1)
    # sqrt(1+4z) = 1 + 2 sum_{k>=1} (-1)^{k-1} Catalan_{k-1} z^k
    plus = [Fraction(1)] + [Fraction((-1)**(k-1)*comb(2*k-2,k-1),k) for k in range(1,n+1)]
    minus = [Fraction(1)-plus[0]] + [-plus[k] for k in range(1,n+1)]
    q = div_trunc(minus,plus,n)
    series = [Fraction(0)]*(n+1)
    lp = log_unit(p,n)
    lplus = log_unit(plus,n)
    for k in range(n+1):
        series[k] = lp[k]-n*lplus[k]
    qpower = [Fraction(1)]+[Fraction(0)]*n
    counts = {}
    for m in range(1,n+1):
        qpower = mul_trunc(qpower,q,n)
        if m < 4 or m%2 == 1:
            continue
        a = [Fraction(1)]+qpower[1:]
        correction = log_unit(a,n)
        multiplicity = series[m]
        assert multiplicity.denominator == 1 and multiplicity >= 0,(m,multiplicity)
        counts[m] = int(multiplicity)
        for k in range(n+1):
            series[k] -= multiplicity*correction[k]
    assert all(x == 0 for x in series), series
    assert sum(m*c for m,c in counts.items()) == n
    return tuple(k for k in sorted(counts) for _ in range(counts[k]))


def check_case(vertices, triples, expected):
    validate_sts(vertices,triples)
    signatures = defaultdict(int)
    for a,b in combinations(vertices,2):
        survivors,edges=leave(vertices,triples,a,b)
        cycle_tuple=tuple(cycle_lengths(survivors,edges))
        signatures[cycle_tuple] += 1
        polynomial = [1]
        for m in cycle_tuple:
            polynomial = convolution(polynomial,cycle_matching_polynomial(m))
        assert polynomial == enumerate_matchings(survivors,edges)
        assert cycle_tuple == inverse_cycles_from_polynomial(polynomial)
    assert dict(signatures)==expected, (signatures,expected)
    print('order',len(vertices),'pairs',sum(signatures.values()),'profiles',dict(signatures))


def steiner15():
    vertices = list(range(1,16))
    blocks = [(1,2,3),(1,4,5),(1,6,12),(1,7,15),(1,8,9),(1,10,11),
              (1,13,14),(2,4,6),(2,5,7),(2,8,12),(2,9,11),(2,10,14),
              (2,13,15),(3,4,7),(3,5,13),(3,6,14),(3,8,10),(3,9,12),
              (3,11,15),(4,8,11),(4,9,13),(4,10,15),(4,12,14),
              (5,6,8),(5,9,10),(5,11,14),(5,12,15),(6,7,10),
              (6,9,15),(6,11,13),(7,8,13),(7,9,14),(7,11,12),
              (8,14,15),(10,12,13)]
    return vertices,blocks


def even_partitions(n, least=4):
    if n == 0:
        yield ()
    for k in range(least,n+1,2):
        for remainder in even_partitions(n-k,k):
            yield (k,)+remainder


def polynomial_for_parts(parts):
    out=[1]
    for m in parts:
        out=convolution(out,cycle_matching_polynomial(m))
    return out


def check_near_collisions():
    for N in range(4,33,2):
        parts=list(even_partitions(N))
        buckets=defaultdict(list)
        for item in parts:
            p=polynomial_for_parts(item)
            buckets[tuple(p[:-1])].append((item,p[-1]))
        near=[v for v in buckets.values() if len(set(x[1] for x in v))>1]
        expected=[]
        if N%4==0 and N>=8:
            expected=[[((N,),2),((N//2,N//2),4)]]
        assert [set(v) for v in near]==[set(v) for v in expected],('nearcollision',N,near,expected)
    print('verified complete near-collision classification for even N=4..32')


def main():
    check_case(*fano(), {(4,):21})
    check_case(*affine9(), {(6,):36})
    check_case(*cyclic13(), {(4,6):39,(10,):39})
    vertices,triples=steiner15()
    validate_sts(vertices,triples)
    profiles=defaultdict(int)
    for a,b in combinations(vertices,2):
        surviving,edges=leave(vertices,triples,a,b)
        profile=tuple(cycle_lengths(surviving,edges))
        profiles[profile]+=1
        from_cycles=polynomial_for_parts(profile)
        assert from_cycles==enumerate_matchings(surviving,edges)
        assert inverse_cycles_from_polynomial(from_cycles)==profile
    print('order 15 pairs',sum(profiles.values()),'profiles',dict(profiles))
    for a,b,expected in [(1,2,(12,)),(3,13,(6,6))]:
        surviving,edges=leave(vertices,triples,a,b)
        assert tuple(cycle_lengths(surviving,edges))==expected
        print('puncture pair',a,b,'cycles',expected,'extension spectrum',enumerate_matchings(surviving,edges))
    p12=polynomial_for_parts((12,))
    p66=polynomial_for_parts((6,6))
    assert p12==[1,12,54,112,105,36,2]
    assert p66==[1,12,54,112,105,36,4]
    assert p12[:-1]==p66[:-1] and p66[-1]-p12[-1]==2
    check_near_collisions()
    print('VERIFY_OK')

if __name__=='__main__':
    main()
