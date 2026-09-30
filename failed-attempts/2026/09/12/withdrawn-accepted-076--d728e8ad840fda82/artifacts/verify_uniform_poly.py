"""Exact verification of the uniform H^2 character polynomial for F_n(C minus r points).

Model: H^*(F_n(C_r)) = Orlik-Solomon algebra of arrangement
  H_{ij}={z_i=z_j}, H_{i,p}={z_i=p} in C^n (fiber-type, exponents r..r+n-1).
Degree 1 basis: e_{ij} (i<j), f_{i,p}. S_n acts geometrically (no signs):
  e_{ij} -> e_{s(i)s(j)} (reordered), f_{i,p} -> f_{s(i),p}.
Degree 2: V = wedge^2(H^1)/span(R) with relation vectors:
  R_I:   eij^ejk - eij^eik + ejk^eik            (Arnold triples)
  R_II:  eij^fip - eij^fjp + fip^fjp            (mixed)
  R_III: fip^fiq = 0                            (disjoint fibers)
Caps wedge signs are normalized via ordered generator indices.
The script checks:
  (a) rank(R) = C(n,3)+r*C(n,2)+n*C(r,2) and dim quotient = Poincare e2;
  (b) S_n-invariance of span(R) (residual of N R = R M is 0);
  (c) quotient character == P(X1..X4;r) on tested permutations.
Run: python3 verify_uniform_poly.py  (numpy required)
"""
import itertools
import numpy as np


def Pval(X1, X2, X3, X4, r):
    return (X1**4/8 + X1**3*r/2 - 5*X1**3/12 + X1**2*X2/2
            + X1**2*r**2/2 - X1**2*r + 3*X1**2/8 + X1*X2*r - X1*X2/2
            - X1*r**2/2 + X1*r/2 - X1/12 - X2**2/2 + X2/2 - X3 - X4)


def build(n, r):
    gens = []
    idx = {}
    for i in range(n):
        for j in range(i + 1, n):
            idx[('c', i, j)] = len(gens)
            gens.append(('c', i, j))
    for i in range(n):
        for p in range(r):
            idx[('p', i, p)] = len(gens)
            gens.append(('p', i, p))
    d = len(gens)
    wbasis = [(a, b) for a in range(d) for b in range(a + 1, d)]
    widx = {w: k for k, w in enumerate(wbasis)}
    D = len(wbasis)

    def gimg(g, sg):
        if g[0] == 'c':
            _, i, j = g
            si, sj = sg[i], sg[j]
            return idx[('c', si, sj)] if si < sj else idx[('c', sj, si)]
        _, i, p = g
        return idx[('p', sg[i], p)]

    def mat(sg):
        M = np.zeros((D, D))
        for k, (a, b) in enumerate(wbasis):
            ia, ib = gimg(gens[a], sg), gimg(gens[b], sg)
            if ia == ib:
                continue
            if ia < ib:
                M[widx[(ia, ib)], k] = 1
            else:
                M[widx[(ib, ia)], k] = -1
        return M

    def wv(g1, g2):
        a, b = idx[g1], idx[g2]
        v = np.zeros(D)
        if a == b:
            return v
        if a < b:
            v[widx[(a, b)]] = 1
        else:
            v[widx[(b, a)]] = -1
        return v

    rels = []
    for i, j, k in itertools.combinations(range(n), 3):
        rels.append(wv(('c', i, j), ('c', j, k)) - wv(('c', i, j), ('c', i, k))
                    + wv(('c', j, k), ('c', i, k)))
    for i, j in itertools.combinations(range(n), 2):
        for p in range(r):
            rels.append(wv(('c', i, j), ('p', i, p)) - wv(('c', i, j), ('p', j, p))
                        + wv(('p', i, p), ('p', j, p)))
    for i in range(n):
        for p, q in itertools.combinations(range(r), 2):
            rels.append(wv(('p', i, p), ('p', i, q)))
    R = np.array(rels) if rels else np.zeros((0, D))
    return mat, R


def cyc(sg):
    n = len(sg)
    vis = [0] * n
    c = {}
    for i in range(n):
        if not vis[i]:
            j, ln = i, 0
            while not vis[j]:
                vis[j] = 1
                j = sg[j]
                ln += 1
            c[ln] = c.get(ln, 0) + 1
    return c


def check(n, r, perms):
    from math import comb
    mat, R = build(n, r)
    m = R.shape[0]
    nrel = (comb(n, 3) if n >= 3 else 0) + r * (comb(n, 2) if n >= 2 else 0) \
        + n * (comb(r, 2) if r >= 2 else 0)
    rank = 0 if min(R.shape) == 0 else int(np.linalg.matrix_rank(R))
    assert rank == nrel, (n, r, rank, nrel)
    worst = 0.0
    for sg in perms:
        M = mat(sg)
        if m:
            RM = R.dot(M)
            G = R.dot(R.T)
            N = RM.dot(R.T).dot(np.linalg.inv(G))
            res = float(np.max(np.abs(N.dot(R) - RM)))
            q = float(np.trace(M) - np.trace(N))
        else:
            res, q = 0.0, float(np.trace(M))
        cy = cyc(sg)
        pv = Pval(cy.get(1, 0), cy.get(2, 0), cy.get(3, 0), cy.get(4, 0), r)
        worst = max(worst, res)
        assert res < 1e-6, (n, r, sg, res)
        assert abs(q - pv) < 1e-4, (n, r, sg, q, pv)
    return worst


def main():
    cases = [(1, 1), (1, 3), (2, 1), (2, 2), (2, 5), (3, 1), (3, 2),
             (3, 3), (4, 1), (4, 2), (4, 3), (5, 1), (5, 2)]
    for n, r in cases:
        w = check(n, r, list(itertools.permutations(range(n))))
        print(f"n={n} r={r}: exhaustive OK (resid {w:.1e})")
    rng = np.random.default_rng(1)
    for n, r in [(6, 3), (6, 5), (7, 2)]:
        w = check(n, r, [list(rng.permutation(n)) for _ in range(6)])
        print(f"n={n} r={r}: 6 random perms OK (resid {w:.1e})")
    print("ALL CHECKS PASSED")


if __name__ == '__main__':
    main()
