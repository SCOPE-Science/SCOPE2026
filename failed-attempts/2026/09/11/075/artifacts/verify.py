"""Replayable audit for lane-880: stacked W10 has no Whitehead-bracket support.

Reproduces (exact rational arithmetic, stdlib only):
 1. Chain-stacking W10 (16 facets, 21 missing edges, 6 hollow-triangle
    missing faces = the stacking word).
 2. Candidate (e1={3,5}, e2={4,6}, T={1,2,4}): K_{e1Ue2} is a tree,
    J*={1..6} is acyclic -> no Hochster/BBCG detecting summand.
 3. Exhaustive scan of all disjoint (e1,e2,T) triples on this W10.
 4. Bounded random-word census: no word yields an all-pairs-acyclic
    disjoint triple with J* nontrivial, and no word yields a C4
    (chordless-4-cycle) inner-bracket support.

Usage: python3 verify.py  -> prints VERIFY_OK on exact match.
"""
import itertools
import random
from fractions import Fraction


def stack(facets, face, nv):
    facets = set(facets)
    facets.remove(frozenset(face))
    a, b, c = tuple(face)
    facets.add(frozenset([nv, a, b]))
    facets.add(frozenset([nv, b, c]))
    facets.add(frozenset([nv, c, a]))
    return facets


def mat_rank(rows, ncols):
    M = [[Fraction(x) for x in r] for r in rows]
    m = len(M)
    r = c = rank = 0
    while r < m and c < ncols:
        piv = None
        for i in range(r, m):
            if M[i][c] != 0:
                piv = i
                break
        if piv is None:
            c += 1
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]
        for i in range(m):
            if i != r and M[i][c] != 0:
                f = M[i][c] / pv
                for j in range(c, ncols):
                    M[i][j] -= f * M[r][j]
        r += 1
        c += 1
        rank += 1
    return rank


def hom(facets, J):
    """Reduced Betti (b0r, b1, b2) of full subcomplex K_J over Q."""
    J = sorted(set(J))
    idx = {v: i for i, v in enumerate(J)}
    S = set(J)
    edges = [frozenset(p) for p in itertools.combinations(J, 2)
             if any(frozenset(p) <= f for f in facets)]
    tris = [f for f in facets if f <= S]
    m0, m1, m2 = len(J), len(edges), len(tris)
    eidx = {e: i for i, e in enumerate(edges)}
    if m1 == 0:
        return (0 if m0 <= 1 else m0 - 1, 0, 0)
    d1 = [[Fraction(0)] * m1 for _ in range(m0)]
    for j, e in enumerate(edges):
        u, v = sorted(e, key=lambda x: idx[x])
        d1[idx[v]][j] = Fraction(1)
        d1[idx[u]][j] = Fraction(-1)
    r1 = mat_rank(d1, m1)
    b0r = m0 - r1 - 1
    if m2 == 0:
        return (b0r, m1 - r1, 0)
    d2 = [[Fraction(0)] * m2 for _ in range(m1)]
    for j, t in enumerate(tris):
        vs = sorted(t, key=lambda x: idx[x])
        for (a, b, s) in [(vs[1], vs[2], 1), (vs[0], vs[2], -1),
                          (vs[0], vs[1], 1)]:
            d2[eidx[frozenset([a, b])]][j] = Fraction(s)
    r2 = mat_rank(d2, m2)
    return (b0r, (m1 - r1) - r2, m2 - r2)


def faces_of(facets, verts):
    edges = set()
    for f in facets:
        for p in itertools.combinations(sorted(f), 2):
            edges.add(frozenset(p))
    me = [tuple(sorted(e)) for e in itertools.combinations(verts, 2)
          if frozenset(e) not in edges]
    mt = [tuple(sorted(t)) for t in itertools.combinations(verts, 3)
          if frozenset(t) not in facets
          and all(frozenset(p) in edges
                  for p in itertools.combinations(t, 2))]
    return me, mt


def build_chain():
    F = {frozenset([1, 2, 3]), frozenset([1, 2, 4]),
         frozenset([1, 3, 4]), frozenset([2, 3, 4])}
    word = [[1, 2, 4], [1, 2, 5], [1, 2, 6],
            [1, 2, 7], [1, 2, 8], [1, 2, 9]]
    nv = 5
    for f in word:
        F = stack(F, f, nv)
        nv += 1
    return F, word


def main():
    verts = list(range(1, 11))
    F, word = build_chain()
    assert len(F) == 16, len(F)
    me, mt = faces_of(F, verts)
    assert len(me) == 21, len(me)
    assert sorted(mt) == sorted([tuple(t) for t in word]), mt
    print("W10 OK: 16 facets, 21 missing edges, 6 hollow tris = word")

    e1, e2, T = (3, 5), (4, 6), (1, 2, 4)
    h12 = hom(F, set(e1) | set(e2))
    hJ = hom(F, set(e1) | set(e2) | set(T))
    assert h12 == (0, 0, 0), h12          # K_{e1Ue2} a tree
    assert hJ == (0, 0, 0), hJ            # J* acyclic: no detector
    print("candidate OK: K_e1Ue2 tree", h12, "; J* acyclic", hJ)

    n_disj = n_12 = n_all = n_hit = 0
    for i in range(len(me)):
        for j in range(i + 1, len(me)):
            if set(me[i]) & set(me[j]):
                continue
            for Tx in mt:
                if set(Tx) & (set(me[i]) | set(me[j])):
                    continue
                n_disj += 1
                a = hom(F, set(me[i]) | set(me[j]))
                b = hom(F, set(me[i]) | set(Tx))
                c = hom(F, set(me[j]) | set(Tx))
                if a[0] == 0 and a[1] == 0:
                    n_12 += 1
                if (a[0] == 0 and a[1] == 0 and b[0] == 0 and b[1] == 0
                        and c[0] == 0 and c[1] == 0):
                    n_all += 1
                    hh = hom(F, set(me[i]) | set(me[j]) | set(Tx))
                    if hh[1] > 0 or hh[2] > 0:
                        n_hit += 1
    assert n_disj == 370 and n_hit == 0, (n_disj, n_hit)
    print(f"chain scan OK: disjoint={n_disj} e1Ue2-acyc={n_12} "
          f"all-pairs-acyc={n_all} J-nontrivial={n_hit}")

    random.seed(7)
    tot_all = tot_hit = tot_c4 = 0
    for _ in range(120):
        G = {frozenset([1, 2, 3]), frozenset([1, 2, 4]),
             frozenset([1, 3, 4]), frozenset([2, 3, 4])}
        nv = 5
        for _ in range(6):
            f = random.choice(list(G))
            G = stack(G, list(f), nv)
            nv += 1
        me2, mt2 = faces_of(G, verts)
        for i in range(len(me2)):
            for j in range(i + 1, len(me2)):
                if set(me2[i]) & set(me2[j]):
                    continue
                a = hom(G, set(me2[i]) | set(me2[j]))
                if a[0] == 0 and a[1] == 1:
                    tot_c4 += 1
                for Tx in mt2:
                    if set(Tx) & (set(me2[i]) | set(me2[j])):
                        continue
                    b = hom(G, set(me2[i]) | set(Tx))
                    c = hom(G, set(me2[j]) | set(Tx))
                    if (a[0] == 0 and a[1] == 0 and b[0] == 0
                            and b[1] == 0 and c[0] == 0 and c[1] == 0):
                        tot_all += 1
                        hh = hom(G, set(me2[i]) | set(me2[j]) | set(Tx))
                        if hh[1] > 0 or hh[2] > 0:
                            tot_hit += 1
    assert tot_all == 0 and tot_hit == 0 and tot_c4 == 0
    print(f"random census OK (120 words): all-pairs-acyc={tot_all} "
          f"J-nontrivial={tot_hit} C4-supports={tot_c4}")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
