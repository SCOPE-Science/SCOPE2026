"""Reproduce finite instances of the length-five exact two-symbol-burst theorem.

Uses only the Python standard library. The all-alphabet upper bound and the
existence theorem for directed triple systems are mathematical inputs, not
conclusions of the finite checks.
"""
from itertools import product

DTS = {
    3: [(0,1,2),(2,1,0)],
    4: [(0,1,2),(1,0,3),(2,3,1),(3,2,0)],
    7: [(0,3,5),(0,4,1),(0,6,2),(1,5,3),(1,6,0),
        (2,1,4),(2,5,0),(3,2,6),(3,4,0),(4,2,3),
        (4,5,6),(5,1,2),(6,3,1),(6,5,4)],
    9: [(0,2,8),(0,5,3),(0,6,7),(1,4,2),(1,6,3),
        (1,7,8),(2,3,6),(2,5,4),(3,2,0),(3,8,5),
        (4,1,5),(4,3,7),(4,8,0),(5,1,0),(5,7,6),
        (6,0,4),(6,2,1),(6,5,8),(7,0,1),(7,3,4),
        (7,5,2),(8,2,7),(8,3,1),(8,4,6)]
}
# The standard cyclic six-point directed triple system, with point 5=infinity.
DTS[6] = [tuple((v+t)%5 if v!=5 else 5 for v in base)
          for t in range(5) for base in ((0,5,4),(0,1,3))]

def burst_outputs(word):
    return {word[:i] + word[i+2:] for i in range(4)}

def check_dts(q, triples):
    arcs = set()
    assert len(triples) == q*(q-1)//3
    for a,b,c in triples:
        assert len({a,b,c}) == 3 and all(0 <= x < q for x in (a,b,c))
        for edge in ((a,b),(a,c),(b,c)):
            assert edge not in arcs
            arcs.add(edge)
    assert arcs == {(a,c) for a in range(q) for c in range(q) if a != c}

def code(q, triples):
    result = [(a,b,a,b,a) for a in range(q) for b in range(q)]
    result += [(a,m,b,m,c) for m in range(q) for a,b,c in triples]
    return result

def check_code(q, triples):
    check_dts(q, triples)
    words = code(q, triples)
    assert len(words) == q*q*(q+2)//3
    seen = set()
    for w in words:
        ball = burst_outputs(w)
        assert seen.isdisjoint(ball)
        seen.update(ball)
    assert seen == set(product(range(q), repeat=3))
    print('DTS_AND_PERFECT_COVER_OK', q, len(words), len(seen))

def check_weight(q):
    # Multiply the weight of each output by three to avoid fractions.
    for w in product(range(q), repeat=5):
        ball=burst_outputs(w)
        weight3=sum(3 if z[0]==z[2] else 1 for z in ball)
        assert weight3 >= 3, (q,w,ball)
    print('UNIVERSAL_DUAL_OK',q,q**5)

for q, triples in sorted(DTS.items()):
    check_code(q, triples)
for q in range(2,7):
    check_weight(q)
print('VERIFY_OK')
