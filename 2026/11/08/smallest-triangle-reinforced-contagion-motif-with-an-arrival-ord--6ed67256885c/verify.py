#!/usr/bin/env python3
"""Exact certificate for the minimal simplicial SI infection-order reversal.
Run: python verify.py. Requires Python 3 and SymPy >=1.12.
"""
from functools import lru_cache
from itertools import combinations, permutations
from fractions import Fraction
import sympy as S

q = S.Symbol('q')
WITNESS_EDGES = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 4))

def connected(n, edges):
    reached = {0}
    while True:
        nxt = reached | {v for u,v in edges if u in reached} | {u for u,v in edges if v in reached}
        if nxt == reached:
            return len(nxt) == n
        reached = nxt

def canonical(n, edges):
    return min(tuple(sorted(tuple(sorted((perm[u], perm[v]))) for u,v in edges))
               for perm in permutations(range(n)))

def triangle_list(n, edges):
    edge_set = set(edges)
    return tuple(t for t in combinations(range(n), 3)
                 if all(pair in edge_set for pair in combinations(t, 2)))

def order_probability(n, edges, seed, u, v, variable=q):
    """Independent backward recursion over ALL infected subsets."""
    adj = [set() for _ in range(n)]
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    triangles = triangle_list(n, edges)

    @lru_cache(None)
    def recurse(mask):
        if mask & (1 << u):
            return S.Integer(1)
        if mask & (1 << v):
            return S.Integer(0)
        transitions = []
        for w in range(n):
            if mask & (1 << w):
                continue
            d = sum(bool(mask & (1 << z)) for z in adj[w])
            t = sum(w in triangle and all(mask & (1 << z) for z in triangle if z != w)
                    for triangle in triangles)
            rate = d + variable * t
            if rate != 0:
                transitions.append((w,rate))
        assert transitions
        total = sum(rate for _,rate in transitions)
        return S.cancel(sum(rate*recurse(mask | (1 << w)) for w,rate in transitions)/total)

    return S.cancel(recurse(1 << seed))

def independent_forward(n, edges, seed, u, v, ratio):
    """Separate forward mass-flow algorithm, using only fractions."""
    adj = [set() for _ in range(n)]
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    triangles = triangle_list(n, edges)
    mass = {1 << seed: Fraction(1)}
    success = Fraction(0)
    for _ in range(n-1):
        next_mass = {}
        for mask, probability in mass.items():
            clocks = {}
            for x in range(n):
                if mask & (1 << x):
                    continue
                pair = sum(bool(mask & (1 << y)) for y in adj[x])
                tri = sum(x in t and all(mask & (1 << y) for y in t if y != x)
                          for t in triangles)
                clocks[x] = Fraction(pair) + ratio * tri
            total = sum(clocks.values(), Fraction(0))
            assert total > 0
            for x,rate in clocks.items():
                if not rate:
                    continue
                w = probability * rate / total
                if x == u:
                    success += w
                elif x != v:
                    nxt = mask | (1 << x)
                    next_mass[nxt] = next_mass.get(nxt, Fraction(0)) + w
        mass = next_mass
    assert not mass
    return success

def representative_classes(n, edge_cap):
    edges = tuple(combinations(range(n),2))
    reps = set()
    for mask in range(1 << len(edges)):
        e = tuple(edges[k] for k in range(len(edges)) if mask & (1 << k))
        if len(e) > edge_cap or not connected(n,e) or not triangle_list(n,e):
            continue
        reps.add(canonical(n,e))
    return sorted(reps)

def verify():
    witness = order_probability(5,WITNESS_EDGES,2,3,4)
    formula = 2*(q*q+5*q+7)/(3*(q+3)*(q+4))
    assert S.cancel(witness-formula)==0
    assert S.cancel(S.diff(witness,q)-2*(2*q*q+10*q+11)/(3*(q+3)**2*(q+4)**2))==0
    assert S.cancel(witness-S.Rational(1,2)-(q*q-q-8)/(6*(q+3)*(q+4)))==0
    assert witness.subs(q,0)==S.Rational(7,18)
    assert S.limit(witness,q,S.oo)==S.Rational(2,3)
    assert S.solve(S.together(witness-S.Rational(1,2)).as_numer_denom()[0],q) == [(1-S.sqrt(33))/2,(1+S.sqrt(33))/2]

    # Independently substitute exact rational rates and recompute the Markov chain.
    for rate in [S.Rational(0),S.Rational(1,7),S.Rational(1,2),S.Integer(1),S.Integer(2),S.Integer(3),S.Integer(4),S.Integer(10),S.Integer(100)]:
        independent = independent_forward(5,WITNESS_EDGES,2,3,4,Fraction(int(rate.p),int(rate.q)))
        exact_formula = formula.subs(q,rate)
        assert independent==Fraction(int(exact_formula.p),int(exact_formula.q))

    # Every possible connected graph of the respective small orders is
    # enumerated via every edge mask; relabelings are canonically merged.
    # No triangle => the model is q-independent, so only triangle graphs matter.
    expected = {3:1, 4:3, 5:3}
    tested = 0
    zero = 0
    for n in (3,4,5):
        reps=representative_classes(n, 6 if n<=4 else 5)
        assert len(reps)==expected[n], (n,len(reps))
        for edges in reps:
            for seed in range(n):
                targets=[u for u in range(n) if u!=seed]
                for u,v in combinations(targets,2):
                    diff=S.cancel(2*order_probability(n,edges,seed,u,v)-1)
                    numerator,denominator = S.fraction(diff)
                    assert denominator.subs(q,0)>0
                    poly=S.Poly(numerator,q)
                    coeff=poly.all_coeffs()
                    assert all(c>=0 for c in coeff) or all(c<=0 for c in coeff), (n,edges,seed,u,v,diff)
                    tested+=1
                    if poly.is_zero:zero+=1
    assert tested==129, tested
    print('PASS: independent forward mass-flow and nine exact rational rate checks')
    print('PASS: exact formula, unique positive crossing, and strict derivative')
    print('PASS: 7 complete unlabeled triangle-graph classes (1,3,3)')
    print('PASS: 129 exact infection-order comparisons, all sign-stable; symmetric ties:',zero)

if __name__=='__main__':verify()
