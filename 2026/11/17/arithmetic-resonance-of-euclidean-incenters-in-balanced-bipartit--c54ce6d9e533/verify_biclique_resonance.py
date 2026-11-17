"""Exact finite checks for the Euclidean inball of balanced two-block metrics.

Requires Python 3.9+, NumPy and SciPy for the optional independent
halfspace-intersection experiment. The enumeration/rank tests use stdlib only.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb


def profiles(m, t):
    assert m >= 2 and m % 2 == 0 and F(1) < t < F(2)
    # These assignments are assembled directly from all possible two-level
    # coordinates on the two blocks. The geometric proof independently
    # establishes that these, together with the cross-level pair, are exhaustive.
    for strong in (0, 1):
        for k in range(1, m):
            for top in combinations(range(m), k):
                top = set(top)
                for mask in range(1 << m):
                    part_s = [t if i in top else F(0) for i in range(m)]
                    part_w = [F(1) if (mask >> i) & 1 else t - 1
                              for i in range(m)]
                    yield tuple(part_s + part_w if strong == 0 else
                                part_w + part_s)
    yield tuple([F(0)] * m + [F(1)] * m)
    yield tuple([F(1)] * m + [F(0)] * m)


def norm2(a):
    n = len(a)
    return sum(v * v for v in a) - sum(a)**2 / n


def exact_rank(rows):
    basis = {}
    for vals in rows:
        vec = list(vals)
        for pivot, b in sorted(basis.items()):
            if vec[pivot]:
                ratio = vec[pivot]
                vec = [u - ratio * v for u, v in zip(vec, b)]
        piv = next((i for i, v in enumerate(vec) if v), None)
        if piv is not None:
            factor = vec[piv]
            basis[piv] = tuple(u / factor for u in vec)
    return len(basis)


def resonance_pairs(h, t):
    return [(u, v) for u in range(1, h) for v in range(u + 1, h + 1)
            if t == F(2 * v, u + v)]


def check_exact(m, t):
    n, h = 2*m, m//2
    topvar = F(m, 4) * (t*t + (2-t)**2)
    res = resonance_pairs(h, t)
    target_contacts = 2*comb(m, h)**2 + 4*sum(
        comb(m, h+u)*comb(m, h-v) for u,v in res)
    maxvar, contact, num = F(-1), [], 0
    for a in profiles(m, t):
        num += 1
        q = norm2(a)
        if q > maxvar:
            maxvar, contact = q, [a]
        elif q == maxvar:
            contact.append(a)
    assert num == 2 * (2**m - 1)**2, (m,t,num)
    assert maxvar == topvar, (m,t,maxvar,topvar)
    assert len(contact) == target_contacts, (m,t,len(contact),target_contacts)
    # Exact Gaussian elimination checks contact-normal span, with no floats.
    centered = [tuple(z - sum(a)/n for z in a) for a in contact]
    rank = exact_rank(centered)
    assert rank == (n-1 if res else n-2), (m,t,rank,res)
    print('EXACT_ALL_FACET_POTENTIALS_PASS', 'm=',m,'t=',str(t),
          'profiles=',num,'contacts=',len(contact),'rank=',rank,
          'resonances=',res)


def check_independent_halfspace(m, t):
    import numpy as np
    from scipy.spatial import HalfspaceIntersection
    n, d = 2*m, 2*m-1
    inequalities = []
    for i in range(n):
        for j in range(i+1, n):
            metric = float(t if (i < m) == (j < m) else 1)
            row = np.zeros(d)
            if i: row[i-1] += 1
            if j: row[j-1] -= 1
            inequalities.extend([np.r_[row, -metric], np.r_[-row,-metric]])
    vertices = HalfspaceIntersection(np.asarray(inequalities),
                                     np.zeros(d)).intersections
    vertices = np.unique(np.round(vertices, 9), axis=0)
    assert len(vertices) == 2*(2**m-1)**2, (m,t,len(vertices))
    vals = np.column_stack([np.zeros(len(vertices)), vertices])
    centered = vals-vals.mean(axis=1,keepdims=True)
    sq = (centered*centered).sum(axis=1)
    topvar = float(F(m,4)*(t*t+(2-t)**2))
    assert abs(max(sq)-topvar)<1e-7
    touching = centered[np.abs(sq-topvar) < 1e-7]
    res = resonance_pairs(m//2,t)
    expected = 2*comb(m,m//2)**2+4*sum(
        comb(m,m//2+u)*comb(m,m//2-v) for u,v in res)
    assert len(touching)==expected, (m,t,len(touching),expected)
    assert np.linalg.matrix_rank(touching, tol=1e-7)==2*m-(1 if res else 2)
    print('INDEPENDENT_HALFSPACE_INTERSECTION_PASS', 'm=',m,'t=',str(t),
          'polar_vertices=',len(vertices),'contacts=',len(touching))

if __name__ == '__main__':
    for m,t in [(2,F(5,4)),(4,F(5,4)),(4,F(4,3)),(4,F(3,2)),
                (6,F(4,3)),(6,F(3,2)),(6,F(6,5)),(6,F(7,5))]:
        check_exact(m,t)
    for m,t in [(2,F(5,4)),(4,F(5,4)),(4,F(4,3)),(4,F(3,2))]:
        check_independent_halfspace(m,t)
    print('BALANCED_BICLIQUE_RESONANT_INCENTERS_ALL_CHECKS_PASS')
