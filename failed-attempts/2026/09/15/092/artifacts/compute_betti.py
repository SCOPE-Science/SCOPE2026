"""Betti recovery test for lane-20313.

Target: symmetric mixed ladder determinantal ideals I_t(L), diagonal initial J=in(I).
Test instances:
  A: full 3x3 symmetric, t=2 (affine Veronese surface). I = 6 quadrics in 6 vars.
  B: symmetric ladder (drop f), t=2. I = 3 quadrics in 5 vars (2-minors of 2x3-like part).
For each: (1) verify t-minors are a Groebner basis under lex a>b>...> (a diagonal order,
i.e. every lead term is the diagonal product); (2) compare Hilbert functions of R/I,
R/J through several degrees; (3) compute full bigraded Betti tables of R/I and R/J
via Koszul homology over F_p (two primes) with Euler/Hilbert-series self-check.
"""
import itertools
import numpy as np
from math import comb
from sympy import symbols, groebner

PRIMES = [32003, 7919]

# ---------------------------------------------------------------- utilities
def add_exp(e, v, n):
    l = list(e); l[v] += 1; return tuple(l)

def divmod_term(t, lt):
    """return quotient exponent tuple if lt divides t else None"""
    if all(t[k] >= lt[k] for k in range(len(t))):
        return tuple(t[k] - lt[k] for k in range(len(t)))
    return None

def mul_dict(P, q):
    return {add_exp_t(t, q): c for t, c in P.items()}

def add_exp_t(t, q):
    return tuple(t[k] + q[k] for k in range(len(t)))

def sub_scaled(D, G, q, scale=1):
    for t, c in G.items():
        u = add_exp_t(t, q)
        D[u] = D.get(u, 0) - scale * c
        if D[u] == 0:
            del D[u]

def lt_of_poly(P, var_order):
    """lex LT with variable priority var_order[0] highest."""
    best = None
    for t in P:
        key = tuple(t[v] for v in var_order)
        if best is None or key > best[0]:
            best = (key, t)
    return best[1]

def reduce_normal(D, LTs, Gdicts):
    """Reduce exponent->coeff dict to normal form. Gdicts None => monomial ideal."""
    D = dict(D)
    if Gdicts is None:
        return {t: c for t, c in D.items()
                if not any(divmod_term(t, lt) is not None for lt in LTs)}
    # full division (divisors assumed monic in lex LT)
    while True:
        hit = None
        for t in D:
            for gi, lt in enumerate(LTs):
                q = divmod_term(t, lt)
                if q is not None:
                    hit = (t, gi, q); break
            if hit is not None:
                break
        if hit is None:
            return D
        t, gi, q = hit
        lc = D.pop(t)
        sub_scaled(D, Gdicts[gi], q, scale=lc)

def monomials_of_degree(n, d):
    out = []
    def rec(k, rem, cur):
        if k == n - 1:
            out.append(tuple(cur + [rem])); return
        for v in range(rem + 1):
            rec(k + 1, rem - v, cur + [v])
    rec(0, d, [])
    return out

def rank_modp(A, p):
    A = np.array(A, dtype=np.int64) % p
    r, c = A.shape
    rank = 0
    for col in range(c):
        piv = -1
        for row in range(rank, r):
            if A[row, col] % p != 0:
                piv = row; break
        if piv < 0:
            continue
        if piv != rank:
            A[[piv, rank]] = A[[rank, piv]]
        inv = pow(int(A[rank, col] % p), -1, p)
        A[rank] = (A[rank] * inv) % p
        for row in range(rank + 1, r):
            f = A[row, col] % p
            if f:
                A[row] = (A[row] - f * A[rank]) % p
        rank += 1
        if rank == r:
            break
    return rank

# ---------------------------------------------------------------- core
def quotient_data(nvars, LTs, Gdicts, maxdeg):
    """Monomial basis (exponent tuples) per degree + multiplication tables."""
    basis, index = {}, {}
    for d in range(maxdeg + 1):
        bl = [t for t in monomials_of_degree(nvars, d)
              if not any(divmod_term(t, lt) is not None for lt in LTs)]
        basis[d] = bl
        index[d] = {t: i for i, t in enumerate(bl)}
    mult = {}  # mult[v][d] = list per basis elt of [(coef, idx)] in deg d+1
    for v in range(nvars):
        mult[v] = {}
        for d in range(maxdeg):
            table = []
            for t in basis[d]:
                r = reduce_normal({add_exp(t, v, nvars): 1}, LTs, Gdicts)
                table.append([(c % 1 if False else c, index[d + 1][u]) for u, c in r.items()])
            mult[v][d] = table
    return basis, mult

def koszul_ranks(nvars, basis, mult, p, imax, jmax, maxdeg):
    from itertools import combinations
    subs = {i: list(combinations(range(nvars), i)) for i in range(imax + 2)}
    sidx = {i: {s: k for k, s in enumerate(subs[i])} for i in subs}
    R = {}
    for i in range(1, imax + 2):
        for j in range(jmax + 1):
            d = j - i
            if d < 0 or d + 1 > maxdeg:
                R[(i, j)] = None; continue
            ncols = len(subs[i]) * len(basis[d])
            nrows = len(subs[i - 1]) * len(basis[d + 1])
            if ncols == 0 or nrows == 0:
                R[(i, j)] = 0; continue
            M = np.zeros((nrows, ncols), dtype=np.int64)
            for cs, S in enumerate(subs[i]):
                for cm, m in enumerate(range(len(basis[d]))):
                    col = cs * len(basis[d]) + cm
                    for pos, v in enumerate(S):
                        T = tuple(x for k, x in enumerate(S) if k != pos)
                        rt = sidx[i - 1][T]
                        for (c, m2) in mult[v][d][m]:
                            row = rt * len(basis[d + 1]) + m2
                            M[row, col] = (M[row, col] + ((-1) ** pos) * int(c)) % p
            R[(i, j)] = rank_modp(M, p)
    return R, subs

def betti_table(nvars, basis, mult, p, imax, jmax, maxdeg):
    R, subs = koszul_ranks(nvars, basis, mult, p, imax, jmax, maxdeg)
    B = {}
    for i in range(imax + 1):
        for j in range(jmax + 1):
            d = j - i
            if d < 0 or d > maxdeg:
                B[(i, j)] = 0; continue
            dim = len(subs[i]) * len(basis[d])
            ri = R.get((i, j), 0) or 0
            rinext = R.get((i + 1, j), 0) or 0
            B[(i, j)] = (dim - ri) - rinext
    return B

def euler_check(nvars, basis, B, imax, jmax):
    ok = True
    for j in range(jmax + 1):
        lhs = sum(((-1) ** i) * B[(i, j)] for i in range(imax + 1))
        rhs = sum(((-1) ** k) * comb(nvars, k) * len(basis[j - k])
                  for k in range(min(nvars, j) + 1) if j - k in basis)
        if lhs != rhs:
            ok = False
            print(f"    EULER MISMATCH j={j}: betti alternating {lhs} vs HS {rhs}")
    return ok

def show(title, nvars, basis, B, imax, jmax):
    print(f"  --- {title} (nvars={nvars}, h={ [len(basis[d]) for d in sorted(basis)] })")
    for i in range(imax + 1):
        row = {j: B[(i, j)] for j in range(jmax + 1) if B[(i, j)]}
        print(f"    i={i}: {row}")

def run_case(name, varnames, minors, diag_leads, imax, jmax, maxdeg):
    n = len(varnames)
    print(f"===== case {name}: {n} vars, {len(minors)} minors =====")
    G = groebner(minors, *varnames, order='lex')
    print(f"  groebner basis size: {len(G.polys)} (input {len(minors)})")
    order = list(range(n))  # lex with varnames[0] highest
    Gdicts, LTs = [], []
    for q in G.polys:
        D = {t: int(c) for t, c in q.as_dict().items()}
        lt = lt_of_poly(D, order)
        lc = D[lt]
        assert lc in (1, -1), f"non-monic GB element, lc={lc}"
        if lc == -1:
            D = {t: -c for t, c in D.items()}
        Gdicts.append(D); LTs.append(lt)
    print(f"  lead terms: {[''.join(v.name + (f'^{e}' if e > 1 else '') for v, e in zip(varnames, t) if e) for t in LTs]}")
    print(f"  minors already a Groebner basis: {len(G.polys) == len(minors)}")
    # diagonal initial ideal from theory
    JLTs = [t for t in diag_leads]
    res = {}
    for p in PRIMES:
        bI, mI = quotient_data(n, LTs, Gdicts, maxdeg)
        bJ, mJ = quotient_data(n, JLTs, None, maxdeg)
        BI = betti_table(n, bI, mI, p, imax, jmax, maxdeg)
        BJ = betti_table(n, bJ, mJ, p, imax, jmax, maxdeg)
        res[p] = (bI, bJ, BI, BJ)
    bI, bJ, BI, BJ = res[PRIMES[0]]
    print("  Hilbert functions deg 0..%d:" % maxdeg)
    print(f"    R/I: {[len(bI[d]) for d in range(maxdeg+1)]}")
    print(f"    R/J: {[len(bJ[d]) for d in range(maxdeg+1)]}")
    print(f"    HF equal: {[len(bI[d]) for d in range(maxdeg+1)] == [len(bJ[d]) for d in range(maxdeg+1)]}")
    for p in PRIMES:
        bI, bJ, BI, BJ = res[p]
        print(f"  -- prime {p}: euler I: {euler_check(n, bI, BI, imax, jmax)}, "
              f"euler J: {euler_check(n, bJ, BJ, imax, jmax)}")
        show("beta(R/I)", n, bI, BI, imax, jmax)
        show("beta(R/J)", n, bJ, BJ, imax, jmax)
        diff = {(i, j): (BI[(i, j)], BJ[(i, j)]) for i in range(imax + 1)
                for j in range(jmax + 1) if BI[(i, j)] != BJ[(i, j)]}
        print(f"    Betti tables equal: {not diff}" + (f", diffs (I,J): {diff}" if diff else ""))
        assert all(res[p][2][k] == res[PRIMES[0]][2][k] for k in res[p][2]), "I varies with p!"
        assert all(res[p][3][k] == res[PRIMES[0]][3][k] for k in res[p][3]), "J varies with p!"
    print(f"  prime-independence verified over {PRIMES}")
    return res

a, b, c, d, e, f = symbols('a b c d e f')
# Case A: full 3x3 symmetric t=2. matrix [[a,b,c],[b,d,e],[c,e,f]]
A_minors = [a*d - b**2, a*e - b*c, b*e - c*d, a*f - c**2, b*f - c*e, d*f - e**2]
A_leads = [(1,0,0,1,0,0), (1,0,0,0,1,0), (0,1,0,0,1,0),
           (1,0,0,0,0,1), (0,1,0,0,0,1), (0,0,0,1,0,1)]
run_case("A full-3x3-sym-t2", [a, b, c, d, e, f], A_minors, A_leads,
         imax=4, jmax=6, maxdeg=7)

# Case B: symmetric ladder dropping f (vars a,b,c,d,e), t=2
B_minors = [a*d - b**2, a*e - b*c, b*e - c*d]
B_leads = [(1,0,0,1,0), (1,0,0,0,1), (0,1,0,0,1)]
run_case("B ladder-drop-f-t2", [a, b, c, d, e], B_minors, B_leads,
         imax=3, jmax=5, maxdeg=6)
print("ALL CASES DONE")
