"""Bounded recovery probe for lane-684 target.

Tests one-step-mutation coincidence route on A = homogeneous 2-Nakayama,
linear reading: vertices os_ell^{(2)}, ell=(3,3,3,3,3), n=5.
  1. Quiver / vertex / canonical interval-module (M0 summand) inventory.
  2. Thin-representation Hom census (exact rational linear algebra).
  3. Dim-vector multiset audit of M0 (pairwise distinctness).
  4. Minimal right add(M0/X)-approximation at X=(2,1,0) via exact
     factorisation pruning, then kernel representation with induced maps,
     and dim-vector comparison against X.

All linear algebra is exact (sympy Rational). No external packages.
"""
import sympy as sp

N = 5
ELL = [3] * 5
KEPT = [(a, b) for a in range(N) for b in range(N)
        if a >= b and (a - b + 1) <= ELL[a]]
IDX = {v: i for i, v in enumerate(KEPT)}
ARROWS = []
for (x, y) in KEPT:
    if (x + 1, y) in IDX:
        ARROWS.append(((x, y), (x + 1, y)))
    if (x, y + 1) in IDX:
        ARROWS.append(((x, y), (x, y + 1)))
LAMS = [(a, b, c) for a in range(N) for b in range(N) for c in range(N)
        if a >= b >= c and (a - c + 1) <= ELL[a]]


def supp(lam):
    l1, l2, l3 = lam
    return frozenset(v for v in KEPT if l2 <= v[0] <= l1 and l3 <= v[1] <= l2)


S = {l: supp(l) for l in LAMS}


def hom_equations(l, mu):
    """Homogeneous linear equations for Hom(M_l, M_mu) in overlap scalars."""
    Sl, Smu = S[l], S[mu]
    ov = sorted(Sl & Smu)
    if not ov:
        return [], []
    m = {v: i for i, v in enumerate(ov)}
    rows = []
    for (u, v) in ARROWS:
        sl = 1 if (u in Sl and v in Sl) else 0
        sm = 1 if (u in Smu and v in Smu) else 0
        if u in m and v in m:
            r = [sp.Rational(0)] * len(ov)
            r[m[v]] += sl
            r[m[u]] -= sm
            rows.append(r)
    for (u, v) in ARROWS:
        if u in Sl and u not in Smu and v in m:
            r = [sp.Rational(0)] * len(ov)
            r[m[v]] = sp.Rational(1)
            rows.append(r)
    return rows, ov


def hom_basis(l, mu):
    rows, ov = hom_equations(l, mu)
    if not ov:
        return []
    if not rows:
        return [([sp.Rational(1) if i == j else sp.Rational(0)
                  for j in range(len(ov))], ov) for i in range(len(ov))]
    M = sp.Matrix(rows)
    ns = M.nullspace()
    return [(list(v), ov) for v in ns]


def hom_dim(l, mu):
    return len(hom_basis(l, mu))


def dimvec(lam):
    return tuple(1 if v in S[lam] else 0 for v in KEPT)


def main():
    out = []
    out.append(f"vertices (|K0 proj|) = {len(KEPT)}")
    out.append(f"quiver arrows = {len(ARROWS)}")
    out.append(f"M0 summands = {len(LAMS)}")
    # Hom census
    dims = {}
    for l in LAMS:
        for mu in LAMS:
            dims[(l, mu)] = hom_dim(l, mu)
    out.append(f"Hom dims occurring = {sorted(set(dims.values()))}")
    out.append(f"End dims = {sorted(set(dims[(l, l)] for l in LAMS))}")
    # Dim-vector audit
    dvs = {l: dimvec(l) for l in LAMS}
    seen = {}
    dup = False
    for l, d in dvs.items():
        if d in seen:
            dup = True
            out.append(f"DUPLICATE dimvec: {l} and {seen[d]}")
        seen.setdefault(d, l)
    out.append(f"M0 dim vectors pairwise distinct = {not dup}")
    # Approximation fan at X
    X = (2, 1, 0)
    sources = [Y for Y in LAMS if Y != X and dims[(Y, X)] == 1]
    out.append(f"sources mapping to X={X}: n={len(sources)} {sources}")
    fYX = {}
    for Y in sources:
        (b, ov) = hom_basis(Y, X)[0]
        fYX[Y] = ({v: b[i] for i, v in enumerate(ov)}, set(ov))

    def factors_through(Y, rest):
        """Does basis map Y->X factor through (+) rest? Exact linear solve."""
        unknowns, cols = [], []
        for Z in rest:
            (bz, ovz) = hom_basis(Y, Z)[0] if hom_dim(Y, Z) == 1 else (None, None)
            if bz is None:
                continue
            # need Hom(Y,Z) basis only if dim==1; higher dims unrolled (never occurs here)
            for _ in [0]:
                unknowns.append(Z)
                cols.append(({v: bz[i] for i, v in enumerate(ovz)}, set(ovz)))
        if not unknowns:
            return False
        (rz, ovx) = hom_basis(Y, X)[0], None
        t = fYX[Y][0]
        eqs, rhs = [], []
        for v in sorted(S[Y] & S[X]):
            row = []
            for (Z, (sv, oz)) in zip(unknowns, cols):
                r = fYX[Z][0].get(v, sp.Rational(0)) if v in S[Z] else sp.Rational(0)
                s = sv.get(v, sp.Rational(0))
                row.append(r * s)
            # unknowns here are COEFFICIENTS c_Z multiplying basis maps g_Z;
            # composite scalar at v = sum_Z c_Z * r_Z(v) * s_Z(v). Linear in c.
            eqs.append(row)
            rhs.append(t.get(v, sp.Rational(0)))
        M, b = sp.Matrix(eqs), sp.Matrix(rhs)
        # solvable iff rhs in column space
        aug = M.row_join(b)
        return M.rank() == aug.rank()

    # greedy prune to minimal approximation set
    rest = list(sources)
    changed = True
    while changed:
        changed = False
        for Y in list(rest):
            others = [Z for Z in rest if Z != Y]
            if factors_through(Y, others):
                rest.remove(Y)
                changed = True
                break
    out.append(f"minimal approximation summands n={len(rest)} {rest}")
    # kernel representation with induced maps
    minset = rest
    ker_basis = {}  # v -> list of coordinate vectors in fiber basis
    fib_index = {}  # v -> {Z: position}
    for v in KEPT:
        cols = [Z for Z in minset if v in S[Z]]
        fib_index[v] = {Z: j for j, Z in enumerate(cols)}
        if v in S[X] and cols:
            row = [[fYX[Z][0].get(v, sp.Rational(0)) for Z in cols]]
            M = sp.Matrix(row)
            ns = M.nullspace()
            ker_basis[v] = [list(w) for w in ns]
        elif v in S[X] and not cols:
            ker_basis[v] = None  # approximation fails to cover
        else:
            ker_basis[v] = [[sp.Rational(1) if j == k else sp.Rational(0)
                             for j in range(len(cols))] for k in range(len(cols))]
    uncovered = [v for v in KEPT if ker_basis[v] is None]
    out.append(f"vertices uncovered by minimal fan = {uncovered}")
    kdim = {v: (len(ker_basis[v]) if ker_basis[v] is not None else -1)
            for v in KEPT}
    out.append(f"kernel dim vector = {tuple(kdim[v] for v in KEPT)}")
    out.append(f"X dim vector      = {dvs[X]}")
    out.append(f"kernel==X as vectors = "
               f"{tuple(kdim[v] for v in KEPT) == dvs[X]}")
    kdect = sum(v for v in kdim.values() if v > 0)
    out.append(f"total kernel dim = {kdec if False else kdect}")
    print("\n".join(out))


if __name__ == "__main__":
    main()
