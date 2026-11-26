"""Independent finite checks for radius-one closed-neighborhood shattering in clique products.
Run with Python 3.10+; no third-party packages.
"""
from itertools import product, combinations
from math import prod

def expected(q):
    d = len(q)
    if d == 1:
        return 0
    if d >= 3:
        return 3
    a, b = sorted(q)
    return 1 if a == b == 2 else 3 if a >= 3 and b >= 4 else 2

def traces(q, subset):
    vertices = tuple(product(*(range(s) for s in q)))
    return {sum((sum(u != v for u, v in zip(x, vertices[j])) <= 1) << i
                for i, j in enumerate(subset))
            for x in vertices}

def main():
    examples = [(2,), (3,), (5,), (2,2), (2,3), (2,4), (2,6),
                (3,3), (3,4), (3,5), (4,4), (4,5),
                (2,2,2), (2,2,3), (2,3,3), (3,3,3),
                (2,2,2,2), (2,2,2,3), (2,2,2,2,2)]
    cases = 0
    for q in examples:
        n = prod(q)
        # Translation by coordinatewise alphabet permutations sends any vertex to zero.
        # Hence every candidate has a representative containing vertex index zero.
        max_k = min(4, n)
        observed = 0
        counts = {}
        for k in range(1, max_k + 1):
            count = 0
            for tail in combinations(range(1, n), k-1):
                subset = (0,) + tail
                cases += 1
                if len(traces(q, subset)) == 1 << k:
                    count += 1
            counts[k] = count
            if count:
                observed = k
        assert observed == expected(q), (q, observed, expected(q), counts)
        print('GRID',q,'anchored_shattered',counts,'VC',observed,'PASS',flush=True)
    # Reconstruct every explicit witness table used in the proof.
    for q in [(2,2,2), (2,3,2), (3,3,3), (2,2,2,2), (3,4), (4,3), (5,5)]:
        vv=list(product(*(range(s) for s in q)))
        if len(q)>=3:
            z=(0,)*len(q)
            e1=(1,)+(0,)*(len(q)-1)
            e2=(0,1)+(0,)*(len(q)-2)
            pts=[z,e1,e2]
        else:
            pts=[(0,0),(0,1),(1,2)] if q[0]>=3 and q[1]>=4 else [(0,0),(1,0),(2,1)]
        if len(q)==2 and len(set(pts))==3 and (q[0],q[1]) not in [(3,4),(5,5),(4,3)]:
            continue
        ids=tuple(vv.index(p) for p in pts)
        assert len(traces(q,ids))==8, (q,pts)
    print('VERIFY_OK exact_vc=PASS all_anchored_four_set_exclusions=PASS explicit_witnesses=PASS', 'tested',cases)

if __name__=='__main__':main()
