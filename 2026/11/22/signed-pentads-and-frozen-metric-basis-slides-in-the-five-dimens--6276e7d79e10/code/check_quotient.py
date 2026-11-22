#!/usr/bin/env python3
"""Independent ternary-kernel classification and folded-cube pentad verifier."""
import itertools
import json
from collections import Counter
from math import comb

D = 5
EVEN = tuple(v for v in range(32) if v.bit_count() % 2 == 0)
DELTA = tuple(v for v in itertools.product((-1, 0, 1), repeat=D) if any(v))


def resolves_by_kernel(landmarks):
    """Equivalent to absence of a nonzero {-1,0,1} vector orthogonal to all sign rows."""
    return all(any(sum(x * (1-2*((w>>i)&1)) for i, x in enumerate(vec))
                       for w in landmarks) for vec in DELTA)


def pentads():
    p = set()
    for center in EVEN:
        for i in range(D):
            family = frozenset([center] + [center ^ (1 << i) ^ (1 << j)
                                           for j in range(D) if j != i])
            assert len(family) == 5 and family <= set(EVEN)
            p.add(family)
    return sorted(p, key=lambda s: tuple(sorted(s)))


def main():
    P = pentads()
    assert len(P) == 16
    assert Counter(len(a & b) for a,b in itertools.combinations(P,2)) == {0:40,2:80}
    families = [frozenset(q) for pentad in P for q in itertools.combinations(sorted(pentad),4)]
    assert len(families) == len(set(families)) == 80
    families = set(families)
    # Check the model against ALL even-representative quadruples, not only candidates.
    for t in itertools.combinations(EVEN,4):
        assert resolves_by_kernel(t) == (frozenset(t) in families), t
    for k in (1,2,3):
        assert not any(resolves_by_kernel(t) for t in itertools.combinations(EVEN,k))
    # Every independent choice of antipodal lift gives a resolving set.
    lifted = set()
    for q in families:
        for mask in range(16):
            w = sorted(q)
            lifted.add(tuple(sorted(x ^ (31 if mask & (1 << j) else 0)
                                         for j,x in enumerate(w))))
    assert len(lifted) == 1280
    # Every projected triple lies in at most one pentad.
    triple_degree = Counter(frozenset(t) for p in P for t in itertools.combinations(p,3))
    assert max(triple_degree.values()) == 1
    # The abstract local move graph is a signed 4-of-5 system.
    abstract = set()
    for missing in range(5):
        for bits in itertools.product((0,1),repeat=4):
            abstract.add((missing,bits))
    assert len(abstract)==80
    # Direct distance counting by the exact formula.
    hist=Counter()
    for u in abstract:
        a,ua=u
        signs_u=dict(zip((i for i in range(5) if i!=a),ua))
        for v in abstract:
            b,vb=v
            signs_v=dict(zip((i for i in range(5) if i!=b),vb))
            common = [i for i in range(5) if i!=a and i!=b]
            dist=(a!=b)+sum(signs_u[i]!=signs_v[i] for i in common)
            hist[dist]+=1
    assert hist==Counter({0:80,1:960,2:2400,3:2240,4:720})
    result = {
        'even_representatives':16,
        'tested_ternary_vectors':len(DELTA),
        'tested_even_triplets':comb(16,3),
        'tested_even_quadruples':comb(16,4),
        'distinct_five_pentads':len(P),
        'four_of_five_projected_bases':len(families),
        'lifted_bases':len(lifted),
        'pentad_pair_intersection_distribution':dict(sorted(Counter(len(a & b) for a,b in itertools.combinations(P,2)).items())),
        'local_signed_states':len(abstract),
        'local_distance_profile':{k:v//80 for k,v in sorted(hist.items())},
        'local_edges':80*12//2,
        'number_components':len(P),
        'global_edges':len(P)*80*12//2,
    }
    print(json.dumps(result,sort_keys=True,indent=2))

if __name__=='__main__':main()
