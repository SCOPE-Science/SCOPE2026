"""Exact finite corroboration of tetrahedral Frobenius-volume levels in Birkhoff polytopes.
Run with Python 3 standard library: python check.py .
The accompanying mathematical proof, not this finite test, establishes every n >= 5.
"""
from itertools import combinations, permutations
from math import comb, factorial


def overlaps(p, q):
    return sum(a == b for a, b in zip(p, q))


def gram_det_from_overlaps(n, o):
    # Six pairwise coordinate coincidences: 01,02,03,12,13,23.
    x, y, z, u, v, w = o
    a, b, c = 2*(n-x), 2*(n-y), 2*(n-z)
    d, e, f = n-x-y+u, n-x-z+v, n-y-z+w
    return a*b*c + 2*d*e*f - a*f*f - b*e*e - c*d*d


def independent_gram_det(P):
    # Independently construct the three difference matrices entry by entry.
    n = len(P[0]); vec = []
    for p in P[1:]:
        vec.append(tuple((int(p[i] == j) - int(P[0][i] == j))
                         for i in range(n) for j in range(n)))
    a, b, c = (sum(x*x for x in v) for v in vec)
    d, e, f = (sum(x*y for x, y in zip(vec[i], vec[j]))
               for i, j in ((0,1),(0,2),(1,2)))
    return a*b*c + 2*d*e*f - a*f*f - b*e*e - c*d*d


def cyclic_example(n, perturbed=False):
    assert n >= 5
    p = [tuple((i+j) % n for i in range(n)) for j in range(4)]
    if perturbed:
        p[0] = list(p[0]); p[0][0], p[0][1] = p[0][1], p[0][0]
        p[0] = tuple(p[0])
    return tuple(p)


def run():
    for n in (4, 5):
        ps = list(permutations(range(n)))
        zero = ps[0]
        count = {}
        num_unequal = 0
        for a, b, c in combinations(ps[1:],3):
            P = (zero,a,b,c)
            o = tuple(overlaps(P[i],P[j]) for i,j in combinations(range(4),2))
            det = gram_det_from_overlaps(n,o)
            assert det >= 0
            count[det] = count.get(det,0)+1
            if n == 4 and det == 184:
                assert sorted(o) == [0,0,0,0,1,1]
                # The two nonzero pair-indices must share a row index.
                pairs = list(combinations(range(4),2))
                a0,b0 = [pairs[k] for k, score in enumerate(o) if score]
                assert len(set(a0) & set(b0)) == 1
            if n == 5:
                maxdet = 4*n**3
                nextdet = 2*n*(n-1)*(2*n+1)
                if det == maxdet:
                    assert all(t == 0 for t in o)
                if det == nextdet:
                    assert o.count(1) == 1 and o.count(0) == 5
                if num_unequal < 75 and (det % 11 in (0,1)):
                    assert independent_gram_det(P) == det
                    num_unequal += 1
        levels = sorted(count, reverse=True)
        assert sum(count.values()) == comb(factorial(n)-1,3)
        if n == 4:
            assert (levels[0],levels[1],count[levels[0]],count[levels[1]]) == (256,184,4,48)
        else:
            assert (levels[0],levels[1],count[levels[0]],count[levels[1]]) == (500,440,224,2400)
        # Re-anchor by left multiplication to count *all* unoriented quadruples.
        max_count = count[levels[0]]*factorial(n)//4
        second_count = count[levels[1]]*factorial(n)//4
        if n == 5: assert (max_count,second_count) == (6720,72000)
        print('exact_full_enumeration',n,'anchored=',sum(count.values()),
              'highest_determinants=',levels[:2],'anchored_counts=',
              (count[levels[0]],count[levels[1]]),'unanchored_counts=',(max_count,second_count))
    for n in range(5, 45):
        for modified in (False, True):
            P = cyclic_example(n,modified)
            o = tuple(overlaps(P[i],P[j]) for i,j in combinations(range(4),2))
            assert (sorted(o) == [0]*6 if not modified else sorted(o) == [0]*5+[1])
            assert gram_det_from_overlaps(n,o) == (2*n*(n-1)*(2*n+1) if modified else 4*n**3)
            assert independent_gram_det(P) == gram_det_from_overlaps(n,o)
    print('BIRKHOFF_TETRA_GAP_PASS full_orders=4,5 example_orders=5..44 high_levels_n5=500,440 independent_gram=PASS')

if __name__=='__main__': run()
