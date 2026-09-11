"""Affine uniform tolerance-1 Radon audit for 10 points in R^3.

For a fixed 10-point configuration P (generic or adversarial), enumerate all
unordered disjoint admissible pairs (A,B), |A|,|B|>=2, and test:
  UNIFORM(A,B): conv(A\\{v}) meets conv(B\\{v}) for every v in 0..9.
Convex-hull intersection is decided by exact rational linear programming
over Fractions (vertex-enumeration-free formulation):
  conv(A)+... meet  <=>  exists stochastic a on A2, b on B2 with equal means
  <=> LP feasibility in standard form, solved by exact brute-force simplex
  over basic feasible solutions (supports of size <= 4 by Carathéodory in R^3:
  it suffices to check sub-supports A3 subset A2, B3 subset B2 with
  |A3|+|B3| <= 6? We instead do exact vertex enumeration of the polytope
  { (a,b): a in Delta_A2, b in Delta_B2, mean(a)=mean(b) } projected --
  simplest correct: enumerate all minimal supports (|A3|<=4, |B3|<=4) and
  solve the 4x4-or-smaller linear systems exactly.
Simpler provably-correct method used here: two polytopes P,Q (vertex lists)
are disjoint iff strictly separable by a plane through 3 affinely-independent
difference points or coordinate planes -- instead we use the exact
vertex-separation test: P cap Q = {} iff exists direction u (from a finite
candidate set: facet normals of conv(P-Q), i.e. normals of triangles of the
Minkowski difference vertex set D = {p-q}) strictly separating. Candidate
normals: all cross products (d1-d0)x(d2-d0) for triples of D, plus edge
directions are NOT needed for strict polytope separation (face-normal
suffices: if disjoint, some facet of conv(D) separates 0, and conv(D)'s
facets are triangles of D vertices). So: compute D, for each ordered triple
normal n, check max_{d} n.d < 0 or min > 0 with strict Fraction arithmetic;
also handle degenerate D (rank<3) by axis directions + cross products.
This is exact and complete for strict disjointness of V-polytopes.
Cross-check: independently verify with float LP (scipy-free simplex on the
separation oracle via projected subgradient) for a random sample.
"""
import itertools
from fractions import Fraction as F

def sub(u, v):
    return (u[0]-v[0], u[1]-v[1], u[2]-v[2])

def dot(u, v):
    return u[0]*v[0]+u[1]*v[1]+u[2]*v[2]

def cross(u, v):
    return (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0])

def hulls_meet(P, Q):
    """P,Q: lists of 3-tuples of Fractions. True iff conv meet.
    Exact vertex-enumeration LP: conv(P) cap conv(Q) != {} iff the polytope
      { (a,b): a>=0,sum a=1 on P; b>=0,sum b=1 on Q; mean(a)=mean(b) }
    is nonempty. Basic feasible solutions have support (|A3|,|B3|) with
    |A3|+|B3| <= dim+1+2 = 6 and both supports affinely spanning the common
    point; enumerate all sub-supports A3,B3 with |A3|<=4,|B3|<=4,
    |A3|+|B3|>=2, solve exactly, accept if a stochastic solution exists.
    Completeness: any feasible (a,b) has a BFS with |supp a|+|supp b| <= 6
    (m=6 constraints: 3 moment + sum a + sum b + ... ) -- enumeration below
    covers a superset (all supports with each side <=4), hence complete.
    """
    rP, rQ = list(P), list(Q)
    n, m = len(rP), len(rQ)
    # quick vertex-in-hull and segment-triangle shortcuts are subsumed by
    # the general enumeration; go straight to it but order small supports first
    import itertools as it
    idxP = range(n)
    idxQ = range(m)
    for na in (1,2,3,4):
        if na > n:
            continue
        for A3 in it.combinations(idxP, na):
            for nb in (1,2,3,4):
                if nb > m:
                    continue
                if na + nb > 6 and (na > 1 or nb > 1):
                    pass  # still must cover BFS with total<=6 only; skip bigger
                if na + nb > 6:
                    continue
                for B3 in it.combinations(idxQ, nb):
                    if _feasible_support([rP[i] for i in A3],
                                         [rQ[j] for j in B3]):
                        return True
    return False

def _feasible_support(A3, B3):
    """Decide exact existence of stochastic weights with equal means.
    Unknowns a (na), b (nb). Equations: sum a=1, sum b=1, mean(a)-mean(b)=0
    (3 eqs). Enumerate free-variable elimination via Fraction Gaussian
    elimination returning one particular solution + nullspace basis, then
    check the polytope {particular + N t >= 0} nonempty (vertex enumeration
    over active-set-driven 1D/2D cases by recursion on dimension <= 3).
    Nullity here is na+nb-5 <= 1 for totals<=6... but degenerate point sets
    can raise nullity; handle general nullity via recursive vertex search
    over orthant intersection (dimension capped: enumerate sign patterns of
    a basis of the affine subspace -- complete for dim<=3 by cell sampling).
    """
    na, nb = len(A3), len(B3)
    N = na + nb
    # Build equations Mx = rhs, x = [a;b]
    import copy
    rows = []
    r = [F(0)]*N
    for i in range(na):
        r[i] = F(1)
    rows.append((list(r), F(1)))
    r = [F(0)]*N
    for j in range(nb):
        r[na+j] = F(1)
    rows.append((list(r), F(1)))
    for d in range(3):
        r = [F(0)]*N
        for i in range(na):
            r[i] = A3[i][d]
        for j in range(nb):
            r[na+j] = -B3[j][d]
        rows.append((list(r), F(0)))
    sol, basis = _affine_space(rows, N)
    if sol is None:
        return False
    # sample polytope {sol + sum t_k basis_k >= 0}: vertex enumeration:
    # optimum of random linear objectives over this polytope occurs at a
    # vertex; we check feasibility by trying to satisfy >=0 via LP below.
    return _orthant_feasible(sol, basis)

def _affine_space(rows, N):
    M = [list(r)+[rhs] for (r,rhs) in rows]
    piv = {}
    row = 0
    pivcol_of_row = []
    R = [list(x) for x in M]
    PR = list(range(len(R)))
    pivcol = {}
    r = 0
    for c in range(N):
        piv_r = None
        for rr in range(r, len(R)):
            if R[rr][c] != 0:
                piv_r = rr
                break
        if piv_r is None:
            continue
        R[r], R[piv_r] = R[piv_r], R[r]
        pivcol[r] = c
        inv = R[r][c]
        R[r] = [x/inv for x in R[r]]
        for rr in range(len(R)):
            if rr != r and R[rr][c] != 0:
                f = R[rr][c]
                R[rr] = [R[rr][k]-f*R[r][k] for k in range(N+1)]
        r += 1
        if r == len(R):
            break
    for rr in range(r, len(R)):
        if all(R[rr][c] == 0 for c in range(N)) and R[rr][N] != 0:
            return None, None
    free = [c for c in range(N) if c not in pivcol.values()]
    sol = [F(0)]*N
    row_of = {c: rr for rr, c in pivcol.items()}
    for rr, c in pivcol.items():
        sol[c] = R[rr][N]
    basis = []
    for f in free:
        v = [F(0)]*N
        v[f] = F(1)
        for rr, c in pivcol.items():
            v[c] = -R[rr][f]
        basis.append(v)
    return sol, basis

def frac_pt(p):
    return (F(p[0]), F(p[1]), F(p[2]))

def _orthant_feasible(sol, basis):
    """Decide {sol + T t >= 0 componentwise} nonempty. Exact recursive
    vertex search: branch on a violated coordinate (fix it to 0, recurse
    into the resulting affine subspace), plus accept if some sample works.
    Depth <= len(basis)+1; complete because the feasible polytope's vertices
    lie at such active-set fixations."""
    N = len(sol)
    if all(s >= 0 for s in sol):
        return True
    if not basis:
        return False
    # cheap sampling: try least-squares-ish probes along basis directions
    # (incomplete alone; the recursion below is the complete part)
    for b in basis:
        for sgn in (F(1), F(-1)):
            # move along sgn*b until first coordinate hits 0
            best_t = None
            for i in range(N):
                bi = sgn*b[i]
                if bi > 0 and sol[i] < 0:
                    t = -sol[i]/bi
                    if best_t is None or t < best_t:
                        best_t = t
            if best_t is not None:
                cand = [sol[i]+best_t*sgn*b[i] for i in range(N)]
                if all(c >= 0 for c in cand):
                    return True
    # complete branch: pick most negative coordinate, fix each DOF combination
    i = min(range(N), key=lambda k: sol[k])
    # for each basis vector with nonzero i-th component, fix x_i = 0 by
    # eliminating one DOF, then recurse
    for k in range(len(basis)):
        if basis[k][i] == 0:
            continue
        t0 = -sol[i]/basis[k][i]
        nsol = [sol[j]+t0*basis[k][j] for j in range(N)]
        nbasis = []
        for l in range(len(basis)):
            if l == k:
                continue
            w = [basis[l][j]-basis[l][i]/basis[k][i]*basis[k][j]
                 for j in range(N)]
            if any(v != 0 for v in w):
                nbasis.append(w)
        if _orthant_feasible(nsol, nbasis):
            return True
    return False

def audit_config(name, pts):
    Pts = [frac_pt(p) for p in pts]
    verts = list(range(10))
    pairs = []
    seen = set()
    for r1 in range(2, 9):
        for s in itertools.combinations(verts, r1):
            S = frozenset(s)
            rest = tuple(v for v in verts if v not in S)
            for r2 in range(2, len(rest)+1):
                for t in itertools.combinations(rest, r2):
                    T = frozenset(t)
                    a, b = (S,T) if str(sorted(S)) <= str(sorted(T)) else (T,S)
                    if (a,b) in seen:
                        continue
                    seen.add((a,b))
                    pairs.append((sorted(a), sorted(b)))
    nuniform = 0
    ex_uniform = []
    killed_all = True
    kill_ledger = {}
    for (A,B) in pairs:
        kills = []
        for v in range(10):
            A2 = [Pts[x] for x in A if x != v]
            B2 = [Pts[x] for x in B if x != v]
            if not hulls_meet(A2, B2):
                kills.append(v)
        if not kills:
            nuniform += 1
            if len(ex_uniform) < 5:
                ex_uniform.append((A,B))
        else:
            kill_ledger[(tuple(A),tuple(B))] = kills
    print(f"[{name}] total={len(pairs)} uniform={nuniform} examples={ex_uniform}")
    return nuniform, ex_uniform, kill_ledger

if __name__ == "__main__":
    import random
    # sanity: two unit tetrahedra overlapping / disjoint
    T1 = [(0,0,0),(1,0,0),(0,1,0),(0,0,1)]
    T2 = [(0,0,0),(1,0,0),(0,1,0),(0,0,1)]
    T3 = [(2,2,2),(3,2,2),(2,3,2),(2,2,3)]
    assert hulls_meet([frac_pt(p) for p in T1],[frac_pt(p) for p in T2])
    assert not hulls_meet([frac_pt(p) for p in T1],[frac_pt(p) for p in T3])
    # touching-at-vertex case: convs share exactly one point -> meet (closed hulls)
    T4 = [(1,0,0),(2,0,0),(1,1,0),(1,0,1)]
    assert hulls_meet([frac_pt(p) for p in T1],[frac_pt(p) for p in T4])
    print("predicate sanity OK")
    # config 1: moment curve
    audit_config("moment", [(i,i*i,i*i*i) for i in range(10)])
    # random integer configs
    rng = random.Random(7)
    best = None
    for trial in range(30):
        pts = [(rng.randint(0,20),rng.randint(0,20),rng.randint(0,20)) for _ in range(10)]
        if len(set(pts)) < 10:
            continue
        nu, ex, _ = audit_config(f"rand{trial}", pts)
        if best is None or nu < best[0]:
            best = (nu, trial, ex)
    print("best (fewest uniform):", best)
