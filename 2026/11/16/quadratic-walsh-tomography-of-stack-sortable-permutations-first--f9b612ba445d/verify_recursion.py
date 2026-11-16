"""Exact finite certificates for quadratic moments on 231-avoiding permutations.
Run: python verify_recursion.py (from the same directory as kernel6.json).
Requires only Python's standard library.
"""
import json
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path

@lru_cache(None)
def avoiding(n):
    if n == 0:
        return ((),)
    return tuple(left + (n,) + tuple(k + x for x in right)
                 for k in range(n)
                 for left in avoiding(k)
                 for right in avoiding(n-k-1))

def features(p):
    ans = {('constant',)}
    for i, a in enumerate(p):
        ans.add(('single', i, a))
    for i, j in combinations(range(len(p)), 2):
        ans.add(('pair', i, p[i], j, p[j]))
    return ans

def bit_rank(rows):
    pivots = {}
    for v in rows:
        while v:
            k = v.bit_length()-1
            if k not in pivots:
                pivots[k] = v
                break
            v ^= pivots[k]
    return len(pivots)

def feature_rank(perms):
    universe = sorted(set().union(*(features(p) for p in perms)))
    index = {v:i for i,v in enumerate(universe)}
    vectors = [sum(1 << index[f] for f in features(p)) for p in perms]
    return bit_rank(vectors),len(universe)

def perfect_pairings(t):
    if not t:
        yield ()
        return
    for k in range(1,len(t)):
        for other in perfect_pairings(t[1:k]+t[k+1:]):
            yield ((t[0],t[k]),)+other

def all_swap_cubes(perms):
    valid = set(perms)
    unique = set()
    for pairs in perfect_pairings(tuple(range(6))):
        for p in perms:
            orbit = []
            for choices in product((0,1),repeat=3):
                q = list(p)
                for k,(a,b) in enumerate(pairs):
                    if choices[k]: q[a],q[b] = q[b],q[a]
                orbit.append(tuple(q))
            if set(orbit).issubset(valid):
                unique.add(frozenset(orbit))
    return unique

def check():
    for n, expected in [(1,1),(2,2),(3,5),(4,14),(5,42),(6,112)]:
        perms = avoiding(n)
        r,c = feature_rank(perms)
        assert r == expected, (n,r,expected)
        if n<=5:
            assert r == len(perms)
        print('length',n,'permutations',len(perms),'features',c,'rank_mod_2',r)
    perms = avoiding(6)
    index = {''.join(map(str,p)): i for i,p in enumerate(perms)}
    cert = json.loads(Path(__file__).with_name('kernel6.json').read_text('utf-8'))
    assert len(cert)==20
    vbits=[]
    for relation in cert:
        terms = {}
        for name, coefficient in relation:
            assert name in index and coefficient in (-1,1) and name not in terms
            terms[name] = coefficient
        vbits.append(sum(1 << index[name] for name in terms))
        total = {}
        for name, coefficient in terms.items():
            for f in features(tuple(map(int,name))):
                total[f] = total.get(f,0)+coefficient
        assert all(x==0 for x in total.values())
    assert bit_rank(vbits)==20
    cubes = all_swap_cubes(perms)
    cbits = [sum(1 << index[''.join(map(str,p))] for p in cube) for cube in cubes]
    assert len(cubes)==12 and bit_rank(cbits)==12
    for cube in cubes:
        assert len(cube)==8
    print('kernel_certificates',len(cert),'independent_mod_2',bit_rank(vbits))
    print('disjoint_swap_cubes',len(cubes),'cube_span_rank_mod_2',bit_rank(cbits))
    print('PASS: exact integer annihilation and complementary rank bounds')

if __name__ == '__main__':
    check()
