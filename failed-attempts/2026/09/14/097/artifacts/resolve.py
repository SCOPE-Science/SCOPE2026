# Minimal free resolution over S=QQ[x,y,z,w] by exact linear algebra in each degree.
# F0 = S. F1 = +S(-d) per minimal gen of degree d. Then inductively:
# F_{i+1} in degree j = ker( (F_i)_j -> (F_{i-1})_j ) / x-span of lower-degree kernel gens
# (minimality: new generators = kernel modulo maximal-ideal multiples of previous kernel).
# Represent (F_i)_j as explicit QQ-vector spaces with basis, differential matrices.
import sys; sys.path.insert(0, 'output/artifacts')
from fractions import Fraction
from apolar import mons
import sympy as sp

N = 4

class MFR:
    def __init__(self, mingens):
        # mingens: list of (deg, poly dict)
        self.mingens = mingens
        # shifts[i] = list of internal degrees of basis of F_i
        self.shifts = [[0], [d for d, p in mingens]]

def res_step(sshifts, sdiffs, maxdeg):
    pass

def minimal_resolution(mingens, maxdeg, nsteps=4):
    """Build F_0..F_nsteps degree by degree.
    Data: shifts[i] (list), and for each degree j, matrices D[i][j]: (F_i)_j -> (F_{i-1})_j.
    Basis of (F_i)_j: pairs (e, m) with e in basis(F_i), m monomial deg j - shift(e).
    D from the polynomial entries of the differential, defined inductively from syzygies."""
    shifts = [[0], [d for d, _ in mingens]]
    # F1 -> F0 differential: columns = gens
    # Represent D1[j]: rows = monomials of S of deg j (basis of (F0)_j), cols = (e,m) pairs.
    D = {}  # D[(i, j)] = sympy matrix
    import copy
    mg = [p for _, p in mingens]
    ms0 = {}
    for j in range(maxdeg + 1):
        ms = mons(N, j)
        ms0[j] = ms
        # cols
        cols = []
        for ei, (d, g) in enumerate(mingens):
            if d > j: continue
            for m in mons(N, j - d):
                col = [Fraction(0)] * len(ms)
                for e, c in g.items():
                    ne = tuple(a + b for a, b in zip(e, m))
                    col[ms.index(ne)] += c
                cols.append(col)
        D[(1, j)] = sp.Matrix(cols).T if cols else sp.zeros(len(ms), 0)
    # inductively build F2, F3, F4: generators in degree j = basis of ker D[i][j] mod m*(previous gens)
    # Track: for each i>=1, gen_degs[i] = list of shifts; K[i][j] = matrix whose columns express
    # basis of ker(D[i][j]) in terms of (F_i)_j basis (as column space). New shift j added with
    # multiplicity = dim ker - rank(span of m-lifts of K[i][<j gens]).
    Kbasis = {}  # Kbasis[(i, j)] = matrix cols = ker basis vectors in (F_i)_j coords
    for j in range(maxdeg + 1):
        K = D[(1, j)].nullspace()
        Kbasis[(1, j)] = sp.Matrix.hstack(*K) if K else sp.zeros(D[(1, j)].cols, 0)
    gen_shifts = {1: [d for d, _ in mingens]}
    # F2 generators: multiplicity n2j = dim ker(1,j) - sum_{s<j} n2s * (# mons of deg j-s... restricted)
    # but lifts must be computed as actual vectors: lift of gen (s, k) by monomial m = D1-structure... 
    # Since F1 basis elements map via polys, the submodule m*ker_{<j} inside (F1)_j: for each old gen g of F2
    # we need its representative vector in (F1)_{shift(g)}; then multiply by monomials.
    rep = {}  # rep[(2, idx)] = (shift, vector in (F1)_shift coords)
    n2 = {}
    F2shifts = []
    # order degrees ascending
    for j in range(maxdeg + 1):
        Kb = Kbasis[(1, j)]
        # subspace spanned by lifts of previous F2 gens
        liftcols = []
        # basis of (F1)_j:
        B1 = []
        for ei, (d, g) in enumerate(mingens):
            if d > j: continue
            for m in mons(N, j - d):
                B1.append((ei, m))
        for gi, (s, vec) in enumerate(rep.values()):
            if s > j: continue
            # vec is in (F1)_s coords with basis B1(s); lift by monomials t of deg j-s:
            Bs = []
            for ei, (d, g) in enumerate(mingens):
                if d > s: continue
                for m in mons(N, s - d):
                    Bs.append((ei, m))
            for t in mons(N, j - s):
                # (ei, m) -> sum over (ei, m+t): coefficient vec[Bs.index(ei,m)]
                col = [Fraction(0)] * len(B1)
                pos = {b: k for k, b in enumerate(B1)}
                for k, (ei, m) in enumerate(Bs):
                    ne = tuple(a + b for a, b in zip(m, t))
                    if (ei, ne) in pos:
                        col[pos[(ei, ne)]] += vec[k]
                liftcols.append(col)
        L = sp.Matrix(liftcols).T if liftcols else sp.zeros(len(B1), 0)
        if Kb.cols == 0:
            n2[j] = 0
            continue
        # dim ker = Kb.cols; new = dim ker - rank(L as subspace of ker)
        # rank of lifts inside ker: rank([Kb L]) - ... compute projection: new = Kb.cols - dim(col(L) cap col(Kb)); col(L) subset ker mathematically.
        if L.cols == 0:
            new = Kb.cols
        else:
            rK = Kb.rank()
            rKL = Kb.row_join(L).rank()
            # dim intersection = rK + rank(L) - rKL; new = rK - diminter = rKL - rank(L)
            new = rKL - L.rank()
        n2[j] = new
        # choose representatives: extend L to span ker: take columns of Kb not in span(L)
        cur = L
        cur_rank = cur.rank()
        for c in range(Kb.cols):
            col = Kb.col(c)
            if cur.cols == 0:
                trial = col
            else:
                trial = cur.row_join(col)
            if trial.rank() > cur_rank:
                # new generator with representative col (in (F1)_j coords)
                rep[(2, len(F2shifts))] = (j, [col[k] for k in range(col.rows)])
                F2shifts.append(j)
                cur = trial
                cur_rank += 1
                if len([s for s in F2shifts if s == j]) >= new:
                    break
    shifts.append(F2shifts)
    return shifts, D, Kbasis, rep, n2

if __name__ == "__main__":
    from apolar import ann_gens_binomial, min_gens_of_ideal
    CASES = {
     "T111a": ((3,1,0,0),(0,0,3,1)),
     "T111b": ((2,2,0,0),(0,0,2,2)),
     "T21a": ((2,1,1,0),(0,0,2,2)),
     "T31a": ((1,1,1,1),(0,0,0,4)),
     "T22disj": ((2,0,2,0),(0,2,0,2)),
    }
    for name, (u, v) in CASES.items():
        gens = ann_gens_binomial(u, v, 4, maxdeg=sum(u))
        kept = min_gens_of_ideal(gens, 4)
        shifts, D, K, rep, n2 = minimal_resolution(kept, sum(u))
        print(name, "F1 shifts:", sorted(shifts[1]), "F2 shifts:", sorted(shifts[2]))
