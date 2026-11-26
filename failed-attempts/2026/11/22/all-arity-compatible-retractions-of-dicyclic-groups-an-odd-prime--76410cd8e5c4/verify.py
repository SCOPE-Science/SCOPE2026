"""Finite exhaustive checks for the dicyclic retraction compatibility theorem.

Run: python3 verify.py
All computations use exact integer arithmetic and the given group presentation.
"""
from collections import Counter, deque
from math import prod
from itertools import product


def odd_prime_powers(m):
    n = m
    out = []
    p = 2
    while p*p <= n:
        if n % p == 0:
            z = 1
            while n % p == 0:
                n //= p
                z *= p
            if p != 2:
                out.append(z)
        p += 1
    if n > 1 and n != 2:
        out.append(n)
    return out


def verify(m, check_triples=False, check_graph=False):
    n = 2*m
    elems = [(i, j) for j in (0, 1) for i in range(n)]
    identity = (0, 0)

    def mul(x, y):
        return ((x[0] + (-1 if x[1] else 1)*y[0] + m*x[1]*y[1]) % n, (x[1]+y[1]) % 2)

    def power(x, k):
        y = identity
        for _ in range(k):
            y = mul(y, x)
        return y

    powers = {a:[power(a, j) for j in range(n)] for a in elems}
    inverse = {a:power(a,4*m-1) for a in elems}
    endos = []
    for A in elems:
        for B in elems:
            if mul(B,B) != powers[A][m]:
                continue
            if mul(mul(B,A),inverse[B]) != inverse[A]:
                continue
            endos.append((A,B))

    def evaluate(f, x):
        y = powers[f[0]][x[0]]
        return mul(y,f[1]) if x[1] else y

    retractions = [f for f in endos if evaluate(f,f[0]) == f[0] and evaluate(f,f[1]) == f[1]]
    r = odd_prime_powers(m)
    m0 = m // prod(r)
    predicted = {(identity,identity)}
    rank_freq = Counter({1:1})
    for mask in product((0,1), repeat=len(r)):
        d = m0 * prod(v for bit,v in zip(mask,r) if bit)
        t = m//d
        c = next(c for c in range(n) if c % (2*d) == 1 and c % t == 0)
        for s in range(t):
            v = 2*d*s
            predicted.add(((c,0),(v,1)))
            rank_freq[4*d] += 1
    assert set(retractions) == predicted, (m, 'normal forms',set(retractions)^predicted)
    counts = Counter(len({evaluate(f,x) for x in elems}) for f in retractions)
    assert counts == rank_freq, (m,'ranks',counts,rank_freq)
    assert len(retractions) == 1 + prod(1+v for v in r)

    def commute(f,g):
        return evaluate(f,g[0])==evaluate(g,f[0]) and evaluate(f,g[1])==evaluate(g,f[1])

    pairs = sum(commute(f,g) for f in retractions for g in retractions)
    assert pairs == 1 + 2*prod(1+v for v in r) + prod(1+3*v for v in r), (m,'pairs',pairs)

    if check_triples:
        triples = sum(commute(f,g) and commute(f,h) and commute(g,h)
                      for f in retractions for g in retractions for h in retractions)
        expected = sum((1, 3, 3, 1)[j] * prod(1+v*(2**j-1) for v in r) for j in range(4))
        assert triples == expected, (m,'triples',triples,expected)

    if check_graph and len(r)>=1:
        zero=(identity,identity)
        one=((1,0),(0,1))
        vertices=[f for f in retractions if f!=zero and f!=one]
        adjacency={f:{g for g in vertices if g!=f and commute(f,g)} for f in vertices}
        if len(r)==1:
            assert all(not nbr for nbr in adjacency.values())
        else:
            distances={}
            for v in vertices:
                seen={v:0}
                todo=deque([v])
                while todo:
                    x=todo.popleft()
                    for y in adjacency[x]:
                        if y not in seen:
                            seen[y]=seen[x]+1
                            todo.append(y)
                assert len(seen)==len(vertices), (m,'disconnected')
                distances[v]=max(seen.values())
            assert max(distances.values())==3, (m,'diameter')

    print(f'm={m}: endomorphisms={len(endos)}, retractions={len(retractions)}, commuting_pairs={pairs}, images={dict(sorted(counts.items()))} VERIFIED')


if __name__ == '__main__':
    for m in [2,3,4,5,6,7,8,9,10,12,14,15,18,20,21,30]:
        verify(m, check_triples=(m in [3,6,15,21]), check_graph=(m in [3,6,15,21,30]))
    print('DICYCLIC_RETRACTION_COMPATIBILITY_VERIFIED')
