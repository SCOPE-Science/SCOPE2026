"""Minimal free resolution of K over Artinian A (exact QQ), Betti b_0..b_4."""
import sys; sys.path.insert(0, 'output/artifacts')
from fractions import Fraction
from apolar import mons
import sympy as sp
from quot import QA

class FreeMod:
    def __init__(self, A):
        self.A = A
        self.shifts = []   # per generator: internal degree
        self.diffcols = [] # per generator: dict {row_gen: poly dict} expressing d(e_new) in F_prev basis

def basis_F(Fmod, j):
    """Basis of (Fmod)_j: list of (gen_idx, mon_exp) with deg = j - shift."""
    out = []
    for g, s in enumerate(Fmod.shifts):
        if s > j: continue
        for m in mons(Fmod.A.n, j - s):
            out.append((g, m))
    return out

def diff_matrix(Fprev, Fmod, j):
    """Matrix of d: (Fmod)_j -> (Fprev)_j in monomial bases. Fmod.diffcols[g] = {h: poly}."""
    Bsrc = basis_F(Fmod, j)
    Bdst = basis_F(Fprev, j)
    pos = {b: k for k, b in enumerate(Bdst)}
    A = Fmod.A
    D = sp.zeros(len(Bdst), len(Bsrc))
    for c, (g, m) in enumerate(Bsrc):
        for h, poly in Fmod.diffcols[g].items():
            degA = j - Fprev.shifts[h]
            if degA < 0: continue
            A._ensure(degA)
            # total poly t = poly*m ; project to A_{degA}
            tot = {}
            for e, ce in poly.items():
                t = tuple(a + b for a, b in zip(e, m))
                tot[t] = tot.get(t, Fraction(0)) + ce
            v = A.proj(tot, degA)  # coords on A_{degA} basis = free[degA]
            for r, mexp in enumerate(A.free[degA]):
                if v[r] != 0 and (h, mexp) in pos:
                    D[pos[(h, mexp)], c] += v[r]
    return D, Bsrc, Bdst

def min_gens_kernel(Fprev, Fmod, j, old_reps):
    """Kernel of d:(Fmod)_j->(Fprev)_j; quotient by A_+-span of old_reps (each = vector in (Fmod)_{s} coords + shift s).
    Returns (new_count, new_rep_vectors_in_Bsrc_coords)."""
    D, Bsrc, Bdst = diff_matrix(Fprev, Fmod, j)
    if D.cols == 0:
        return 0, []
    K = D.nullspace()
    if not K:
        return 0, []
    Kb = sp.Matrix.hstack(*K)
    # lifts of old reps
    liftcols = []
    pos = {b: k for k, b in enumerate(Bsrc)}
    A = Fmod.A
    Bsrc_by_gen = {}
    for k, (g, m) in enumerate(Bsrc):
        Bsrc_by_gen.setdefault(g, []).append((k, m))
    for (s, vec, Bsrc_s) in old_reps:
        if s > j: continue
        poss = {b: k for k, b in enumerate(Bsrc_s)}
        for t in mons(A.n, j - s):
            if sum(t) == 0: continue  # only A_+ multiples
            col = [Fraction(0)] * len(Bsrc)
            for (g, m), coeff in zip(Bsrc_s, vec):
                if coeff == 0: continue
                ne = tuple(a + b for a, b in zip(m, t))
                if (g, ne) in pos:
                    col[pos[(g, ne)]] += coeff
            liftcols.append(col)
    L = sp.Matrix(liftcols).T if liftcols else sp.zeros(len(Bsrc), 0)
    rL = L.rank()
    rKL = Kb.row_join(L).rank() if L.cols else Kb.rank()
    new = rKL - rL
    # pick representatives
    reps = []
    cur = L
    cur_rank = rL
    for c in range(Kb.cols):
        col = Kb.col(c)
        trial = cur.row_join(col) if cur.cols else col
        if trial.rank() > cur_rank:
            reps.append([col[k] for k in range(col.rows)])
            cur = trial
            cur_rank += 1
            if len(reps) >= new:
                break
    return new, reps

def betti_K(mingens, nsteps=4, verbose=False):
    A = QA(mingens)
    d = A.socle
    if verbose: print("  dims A:", [A.dim[j] for j in range(A.dmax + 1)], "socle:", d)
    F = [FreeMod(A) for _ in range(nsteps + 1)]
    F[0].shifts = [0]; F[0].diffcols = [{}]
    # F1: 4 gens shift 1, diff = vars
    F[1].shifts = [1, 1, 1, 1]
    F[1].diffcols = [{0: {(0,)*w + (1,) + (0,)*(A.n - 1 - w): Fraction(1)}} for w in range(A.n)]
    betti = [1, 4]
    maxdeg = d + nsteps + 2
    for i in range(1, nsteps):
        Fi, Fnext = F[i], F[i + 1]
        old_reps = []  # (shift, vec, Bsrc_at_shift)
        total = 0
        for j in range(i + 1, maxdeg + 1):
            Bsrc = basis_F(Fi, j)
            new, reps = min_gens_kernel(F[i - 1] if i >= 1 else None, Fi, j, old_reps) if i >= 1 else (0, [])
            for rep in reps:
                # diff col: express rep (coeffs on Bsrc=(g,m)) as {g: poly(m)}
                col = {}
                for (g, m), coeff in zip(Bsrc, rep):
                    if coeff != 0:
                        col.setdefault(g, {})[m] = col.setdefault(g, {}).get(m, Fraction(0)) + coeff
                Fnext.shifts.append(j)
                Fnext.diffcols.append(col)
                old_reps.append((j, rep, list(Bsrc)))
                total += 1
        betti.append(total)
        if verbose: print(f"  F{i+1} shifts:", sorted(Fnext.shifts))
    return betti, A

if __name__ == "__main__":
    from apolar import ann_gens_binomial, min_gens_of_ideal
    import sys
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    CASES = {
     "CI11": ((2,1,1,0),(0,1,1,2)),
     "CI21": ((1,1,1,1),(0,0,1,3)),
     "CI31": ((1,1,1,2),(0,0,0,5)),
     "N22a": ((3,1,0,0),(0,0,3,1)),
     "N22b": ((2,2,0,0),(0,0,2,2)),
     "N22c": ((2,0,2,0),(0,2,0,2)),
     "N21a": ((2,1,1,0),(0,0,2,2)),
     "N21b": ((3,1,0,0),(1,0,1,2)),
     "N31": ((1,1,1,1),(0,0,0,4)),
     "N15": ((4,1,0,0),(0,0,4,1)),
    }
    for name, (u, v) in CASES.items():
        if which != "all" and which != name: continue
        print("=" * 60); print(name, u, v)
        gens = ann_gens_binomial(u, v, 4, maxdeg=sum(u))
        kept = min_gens_of_ideal(gens, 4)
        from apolar import ann_basis
        from fractions import Fraction as Fr
        Ff = {tuple(u): Fr(1), tuple(v): Fr(-1)}
        ns, _ = ann_basis(Ff, 4, 1, sum(u))
        print("  Ann_1 dim:", len(ns), " mu:", len(kept))
        b, A = betti_K(kept, 4, verbose=True)
        print("  Betti Tor^A(K,K):", b)
