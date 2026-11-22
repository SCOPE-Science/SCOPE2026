"""Exact-rational, exhaustive literal-string greedy SCS enumeration."""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import product

WORDS = tuple(''.join(p) for p in product('01', repeat=3))
EXPECTED = {10: Fraction(1136203,4365900), 11: Fraction(18241309,52390800),
            12: Fraction(683551,1905120), 13: Fraction(5,224),
            14: Fraction(41,3920)}

def ov(u,v):
    # Only proper prefix/suffix overlap: noncontainment is asserted below.
    for k in range(min(len(u),len(v))-1,0,-1):
        if u[-k:] == v[:k]:
            return k
    return 0

@lru_cache(None)
def law(state):
    assert len(state) == len(set(state))
    for i,u in enumerate(state):
        for j,v in enumerate(state):
            if i != j:
                assert u not in v and v not in u
                assert ov(u,v) <= 2
    if len(state) == 1:
        return {len(state[0]): Fraction(1)}
    pairs = [(i,j,ov(u,v)) for i,u in enumerate(state)
             for j,v in enumerate(state) if i != j]
    best = max(k for _,_,k in pairs)
    options = [(i,j) for i,j,k in pairs if k == best]
    out = defaultdict(Fraction)
    for i,j in options:
        merged = state[i]+state[j][best:]
        child = tuple(sorted([s for k,s in enumerate(state) if k not in (i,j)] + [merged]))
        for result,p in law(child).items():
            out[result] += p / len(options)
    return dict(out)

def main():
    witness = '0001011100'
    assert {witness[i:i+3] for i in range(len(witness)-2)} == set(WORDS)
    assert len(witness) == len(WORDS)+2
    dist = law(tuple(sorted(WORDS)))
    assert dist == EXPECTED
    assert sum(dist.values()) == 1
    assert sum(n*p for n,p in dist.items()) == Fraction(167269939,14968800)
    print('LITERAL_EXHAUSTIVE_OK')
    print('states',law.cache_info().currsize)
    print('distribution',sorted(dist.items()))
    print('mean',sum(n*p for n,p in dist.items()))
    print('optimal',len(witness),'max_greedy_length',max(dist))

if __name__ == '__main__':
    main()
