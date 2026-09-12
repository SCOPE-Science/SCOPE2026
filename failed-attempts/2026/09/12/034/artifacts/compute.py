#!/usr/bin/env python3
"""Obstructed puncture-cycle witness on a punctured-torus gentle algebra A0.

Exact rational (characteristic-zero) computation in the E-relative normalized
bar complex, E = k^3. Computes HH^2(A0), HH^3(A0), Gerstenhaber squares
[theta,theta] = 2 theta circ theta, and certifies (non-)vanishing in cohomology
with left-kernel (non-coboundary) certificates.

A0: vertices {1,2,3}; arrows a1,a2 : 1 -> 2 (parallel pair), b : 2 -> 3,
c : 3 -> 1; relations I = <a1 b, b c, c a1>.
Gentle check, finite dimension (dim 10), quiver has oriented 3-cycles and a
parallel pair, so loop-free formality (Bocklandt-van de Kreeke) and acyclic
quiver Maurer-Cartan results do not apply.
"""
from fractions import Fraction
import json

verts = [1, 2, 3]
arrows = {'a1': (1, 2), 'a2': (1, 2), 'b': (2, 3), 'c': (3, 1)}
rels = {('a1', 'b'), ('b', 'c'), ('c', 'a1')}

# ---- path basis ----
basis = []
index = {}
def add(s, t, p):
    if (s, t, p) not in index:
        index[(s, t, p)] = len(basis)
        basis.append((s, t, p))
for v in verts:
    add(v, v, ())
front = [(v, v, ()) for v in verts]
while front:
    nxt = []
    for (s, t, p) in front:
        for an, (u, v) in arrows.items():
            if u != t:
                continue
            q = p + (an,)
            if any(tuple(q[k:k + 2]) in rels for k in range(len(q) - 1)):
                continue
            if (s, v, q) not in index:
                add(s, v, q)
                nxt.append((s, v, q))
    front = nxt
NB = len(basis)
src = [s for (s, t, p) in basis]
tgt = [t for (s, t, p) in basis]
arr = [p for (s, t, p) in basis]
plus = [i for i in range(NB) if arr[i]]

def pmul(i, j):
    if tgt[i] != src[j]:
        return None
    q = arr[i] + arr[j]
    if any(tuple(q[k:k + 2]) in rels for k in range(len(q) - 1)):
        return None
    return index[(src[i], tgt[j], q)]

def pname(i):
    s, t, p = basis[i]
    return ("e%d" % s) if not p else "".join(p)

print("dim A0 =", NB, "basis:", [pname(i) for i in range(NB)])

# ---- E-relative normalized cochain spaces ----
def space(n):
    elts = []
    lut = {}
    def rec(cur):
        if len(cur) == n:
            s = src[cur[0]]
            t = tgt[cur[-1]]
            for o in range(NB):
                if src[o] == s and tgt[o] == t:
                    lut[(tuple(cur), o)] = len(elts)
                    elts.append((tuple(cur), o))
            return
        for p in plus:
            if cur and tgt[cur[-1]] != src[p]:
                continue
            rec(cur + [p])
    rec([])
    return elts, lut

C = {}
Cl = {}
for n in (1, 2, 3, 4):
    C[n], Cl[n] = space(n)
    print("dim C^%d = %d" % (n, len(C[n])))

ZERO = Fraction(0)
ONE = Fraction(1)

def delta_col(n, xs, o):
    """Column of delta_n : C^n -> C^(n+1) for basis cochain e_{(xs,o)}.
    Returns dict Didx -> coeff. Standard bar signs (char 0)."""
    D, Dl = C[n + 1], Cl[n + 1]
    Cn, Cnl = C[n], Cl[n]
    out = {}
    if len(xs) != n:
        return out
    # value functional of f = e_{(xs,o)} on n-tuples of paths:
    def fval(args):
        if tuple(args) == tuple(xs):
            return {o: ONE}
        return {}
    for j, (ys, w) in enumerate(D):
        acc = {}
        # left term: y1 . f(y2..y_{n+1})
        r = fval(list(ys[1:]))
        for q, c in r.items():
            m = pmul(ys[0], q)
            if m is not None and m == w:
                acc[m] = acc.get(m, ZERO) + c
        # middle terms
        for i in range(1, n + 1):
            m = pmul(ys[i - 1], ys[i])
            if m is None:
                continue
            args = list(ys[:i - 1]) + [m] + list(ys[i + 1:])
            r = fval(args)
            for q, c in r.items():
                if q == w:
                    sgn = ONE if (i % 2 == 0) else Fraction(-1)
                    acc[q] = acc.get(q, ZERO) + sgn * c
        # right term
        r = fval(list(ys[:n]))
        for q, c in r.items():
            m = pmul(q, ys[n])
            if m is not None and m == w:
                sgn = ONE if ((n + 1) % 2 == 0) else Fraction(-1)
                acc[m] = acc.get(m, ZERO) + sgn * c
        if acc.get(w, ZERO) != 0:
            out[j] = acc[w]
    return out

def mat_of(n):
    rows, cols = len(C[n + 1]), len(C[n])
    M = [[ZERO] * cols for _ in range(rows)]
    for j, (xs, o) in enumerate(C[n]):
        col = delta_col(n, xs, o)
        for i, c in col.items():
            M[i][j] = c
    return M

d1 = mat_of(1)
d2 = mat_of(2)
d3 = mat_of(3)

# ---- rational linear algebra ----
def rref_rows(A):
    A = [row[:] for row in A]
    m = len(A)
    n = len(A[0]) if m else 0
    piv = []
    r = 0
    for c in range(n):
        p = None
        for i in range(r, m):
            if A[i][c] != 0:
                p = i
                break
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        v = A[r][c]
        A[r] = [x / v for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        piv.append(c)
        r += 1
    return A, piv

def mat_vec(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]

def ker_basis(M):
    m = len(M)
    n = len(M[0]) if m else 0
    R, piv = rref_rows(M)
    free = [c for c in range(n) if c not in piv]
    pivrow = {c: k for k, c in enumerate(piv)}
    out = []
    for f in free:
        v = [ZERO] * n
        v[f] = ONE
        for c in piv:
            v[c] = -R[pivrow[c]][f]
        out.append(v)
    return out

def in_span(gens, v):
    """Is v in span of gens (row vectors)? Returns (bool, coeffs)."""
    if not gens:
        return (all(x == 0 for x in v), [])
    A = [g[:] + [ZERO] for g in gens]
    # solve sum c_k g_k = v via rref of transpose system: rows gens, target v
    m = len(gens)
    n = len(gens[0])
    # build matrix gens^T augmented with v, solve normal: rref of [G | v] rows? Use: rref of stacked [G; v^T?] — do elimination on columns.
    # Standard: rref of matrix with rows = gens plus row v; v in span iff rank unchanged.
    R1, p1 = rref_rows([g[:] for g in gens])
    rank1 = len(p1)
    R2, p2 = rref_rows([g[:] for g in gens] + [v[:]])
    rank2 = len(p2)
    if rank2 != rank1:
        return (False, [])
    # find coeffs: solve G^T c = v via rref of [G^T | v]
    GT = [[gens[k][j] for k in range(m)] for j in range(n)]  # n x m
    for j in range(n):
        GT[j].append(v[j])
    R, piv = rref_rows(GT)
    # check consistency
    for i in range(len(R)):
        if all(R[i][k] == 0 for k in range(m)) and R[i][m] != 0:
            return (False, [])
    c = [ZERO] * m
    for k, pc in enumerate(piv):
        if pc < m:
            c[pc] = R[k][m]
    return (True, c)

def left_kernel(M):
    MT = [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]
    return ker_basis(MT)

def dot(u, v):
    return sum(a * b for a, b in zip(u, v))

# sanity: d^2 = 0
def mat_mul(A, B):
    m, k = len(A), len(A[0])
    n = len(B[0])
    return [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(n)] for i in range(m)]
def is_zero_mat(A):
    return all(x == 0 for row in A for x in row)
print("d2.d1 == 0:", is_zero_mat(mat_mul(d2, d1)))
print("d3.d2 == 0:", is_zero_mat(mat_mul(d3, d2)))
assert is_zero_mat(mat_mul(d2, d1)) and is_zero_mat(mat_mul(d3, d2))

# ---- cohomology ----
K2 = ker_basis(d2)
K3 = ker_basis(d3)
im1 = [[d1[i][j] for i in range(len(d1))] for j in range(len(d1[0]))]  # cols as vectors in C^2
im2 = [[d2[i][j] for i in range(len(d2))] for j in range(len(d2[0]))]  # cols as vectors in C^3

def quotient_reps(ker_vecs, im_gens):
    reps = []
    span = [g[:] for g in im_gens]
    for v in ker_vecs:
        ok, _ = in_span(span, v)
        if not ok:
            reps.append(v)
            span.append(v[:])
    return reps

H2 = quotient_reps(K2, im1)
H3 = quotient_reps(K3, im2)
print("dim ker d2 =", len(K2), " rank d1 =", len(d1[0]) - len(ker_basis(d1)),
      " dim HH^2 =", len(H2))
print("dim ker d3 =", len(K3), " rank d2 =", len(d2[0]) - len(K2),
      " dim HH^3 =", len(H3))

def show_cochain(n, v, name):
    terms = []
    for j, c in enumerate(v):
        if c != 0:
            xs, o = C[n][j]
            terms.append((str(c), "*".join(pname(p) for p in xs) + " -> " + pname(o)))
    print(name, "support size", len(terms))
    for t in terms:
        print("   ", t)

for k, v in enumerate(H2):
    show_cochain(2, v, "HH2[%d]" % k)

# ---- Gerstenhaber circle product / square ----
def cochain_val(n, vec, args):
    """Evaluate C^n cochain (full vector) on tuple of path indices (all in A_+,
    composable). Returns dict path->coeff."""
    key = tuple(args)
    acc = {}
    for j, c in enumerate(vec):
        if c == 0:
            continue
        xs, o = C[n][j]
        if xs == key:
            acc[o] = acc.get(o, ZERO) + c
    return acc

def circle_sq(t):
    """s = 2 (t circ t) in C^3: s(x,y,z) = 2[t(t(x,y),z) - t(x,t(y,z))]."""
    s = [ZERO] * len(C[3])
    for j, (ys, w) in enumerate(C[3]):
        x, y, z = ys
        total = ZERO
        # first term: t(x,y) combo -> project to A_+, splice
        c1 = cochain_val(2, t, (x, y))
        for p, cp in c1.items():
            if not arr[p]:
                continue  # normalized projection kills vertex part
            if tgt[p] != src[z]:
                continue
            c2 = cochain_val(2, t, (p, z))
            for q, cq in c2.items():
                if q == w:
                    total += cp * cq
        # second term
        c1 = cochain_val(2, t, (y, z))
        for r, cr in c1.items():
            if not arr[r]:
                continue
            if tgt[x] != src[r]:
                continue
            c2 = cochain_val(2, t, (x, r))
            for q, cq in c2.items():
                if q == w:
                    total -= cr * cq
        s[j] = 2 * total
    return s

def bracket(a, b):
    """[a,b] = a circ b - (-1)^{(|a|-1)(|b|-1)} b circ a for deg-2 cochains."""
    def circ(f, g):
        s = [ZERO] * len(C[3])
        for j, (ys, w) in enumerate(C[3]):
            x, y, z = ys
            total = ZERO
            c1 = cochain_val(2, g, (x, y))
            for p, cp in c1.items():
                if not arr[p] or tgt[p] != src[z]:
                    continue
                for q, cq in cochain_val(2, f, (p, z)).items():
                    if q == w:
                        total += cp * cq
            c1 = cochain_val(2, g, (y, z))
            for r, cr in c1.items():
                if not arr[r] or tgt[x] != src[r]:
                    continue
                for q, cq in cochain_val(2, f, (x, r)).items():
                    if q == w:
                        total -= cr * cq
            s[j] = total
        return s
    ab = circ(a, b)
    ba = circ(b, a)
    return [x - y for x, y in zip(ab, ba)]  # (|a|-1)(|b|-1) = 1 odd

results = {"dimA": NB, "dimC": {str(n): len(C[n]) for n in (1, 2, 3, 4)},
           "dimHH2": len(H2), "dimHH3": len(H3), "squares": []}
LK2 = left_kernel(d2)  # annihilator of im(d2) in C^3
print("dim leftker d2 =", len(LK2))
for k, t in enumerate(H2):
    s = circle_sq(t)
    ds = mat_vec(d3, s)
    is_coc = all(x == 0 for x in ds)
    ok, coeffs = in_span(im2, s)
    cert = None
    if not ok:
        for w in LK2:
            if dot(w, s) != 0:
                cert = [str(x) for x in w]
                break
    nz = [j for j in range(len(s)) if s[j] != 0]
    print("HH2[%d]: square cocycle=%s exact=%s nnz=%d dot=%s" %
          (k, is_coc, ok, len(nz), dot([Fraction(x) for x in (cert or [])], s) if cert else None))
    results["squares"].append({
        "theta": k, "cocycle": bool(is_coc), "exact": bool(ok),
        "square_nnz": [(j, str(s[j])) for j in nz],
        "noncoboundary_cert": cert})
    if not ok and is_coc:
        show_cochain(3, s, "square[%d]" % k)

with open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1117/output/artifacts/results.json", "w") as f:
    json.dump(results, f, indent=1)
print("wrote results.json")
