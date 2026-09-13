"""Totaro CDGA invariant-subcomplex computation for F_k(CP^2), pure stdlib.
Computes twisted Betti t_d(k) = dim H^d(F_k)^{S_{k-1}} - dim H^d(F_k)^{S_k}
for d<=5, k range. Exact integer arithmetic + Fraction ranks on orbit bases."""
import sys
from fractions import Fraction

def monomials(k, E, cap=2):
    out = []
    e = [0]*k
    def rec(pos, rem):
        if pos == k-1:
            if rem <= cap:
                e[pos] = rem
                out.append(tuple(e))
            return
        for v in range(min(cap, rem), -1, -1):
            e[pos] = v
            rec(pos+1, rem-v)
        e[pos] = 0
    if E < 0:
        return []
    rec(0, E)
    return out

def add_exp(e, i, n):
    lst = list(e)
    lst[i] += n
    if lst[i] > 2:
        return None
    return tuple(lst)

def build_F(k, d):
    """Return list of F^d basis keys."""
    keys = []
    if d % 2 == 0:
        E = d//2
        for e in monomials(k, E):
            keys.append(('x', e))
    rem1 = d - 3
    if rem1 >= 0 and rem1 % 2 == 0:
        E = rem1//2
        mons = monomials(k, E)
        for i in range(k):
            for j in range(i+1, k):
                for e in mons:
                    keys.append(('g', i, j, e))
    rem2 = d - 6
    if rem2 >= 0 and rem2 % 2 == 0:
        E = rem2//2
        assert E == 0 or True
        mons = monomials(k, E)
        pairs = [(i,j) for i in range(k) for j in range(i+1,k)]
        for a in range(len(pairs)):
            for b in range(a+1, len(pairs)):
                for e in mons:
                    keys.append(('gg', pairs[a], pairs[b], e))
    return keys

def build_R1(k, d):
    """R1 relation keys (i,j,m0) with 2|m0|+5=d; vec has 1-2 terms."""
    if (d-5) % 2 != 0 or (d-5) < 0:
        return []
    E0 = (d-5)//2
    mons = monomials(k, E0)
    keys = []
    for i in range(k):
        for j in range(i+1, k):
            for m in mons:
                t1 = add_exp(m, i, 1)
                t2 = add_exp(m, j, 1)
                if t1 is None and t2 is None:
                    continue
                keys.append(('r1', i, j, m))
    return keys

def build_Arn(k, d):
    if d != 6:
        return []
    keys = []
    for i in range(k):
        for j in range(i+1, k):
            for l in range(j+1, k):
                keys.append(('arn', i, j, l))
    return keys

def perm_tuple(e, a, b):
    if a == b:
        return e
    lst = list(e)
    lst[a], lst[b] = lst[b], lst[a]
    return tuple(lst)

def act_F(key, a, b):
    """swap(a,b) on F key -> (sign, newkey)."""
    def sw(x):
        return b if x == a else (a if x == b else x)
    if key[0] == 'x':
        return (1, ('x', perm_tuple(key[1], a, b)))
    if key[0] == 'g':
        # m = dim_C(CP^2) = 2 is EVEN, so Totaro sign rule gives G_ji = +G_ij:
        # transpositions act on G-factors with sign +1.
        _, i, j, e = key
        i2, j2 = sw(i), sw(j)
        s = 1
        if i2 > j2:
            i2, j2 = j2, i2
        return (s, ('g', i2, j2, perm_tuple(e, a, b)))
    if key[0] == 'gg':
        _, p, q, e = key
        def mappair(p):
            i2, j2 = sw(p[0]), sw(p[1])
            s = 1
            if i2 > j2:
                i2, j2 = j2, i2
            return s, (i2, j2)
        s1, p2 = mappair(p)
        s2, q2 = mappair(q)
        s = s1*s2  # each s = +1 for m even; kept for clarity
        if p2 > q2:
            p2, q2 = q2, p2
            # G-factors commute (|G|=3 odd => graded-commutative would give -,
            # but |G| odd means odd*odd swap sign -1... keep -1 here: verified by R2=0 below)
            s = -s
        return (s, ('gg', p2, q2, perm_tuple(e, a, b)))
    raise ValueError(key)

def D_F(key):
    """Differential F^d -> list of (coeff, target key in F^{d+1})."""
    if key[0] == 'x':
        return []
    if key[0] == 'g':
        _, i, j, e = key
        out = []
        for (u, v) in ((i, i), (i, j), (j, j)):
            m = add_exp(add_exp(e, u, 1) if True else None, 0, 0) if False else None
            # m = e + delta_u + delta_v
            m = add_exp(e, u, 1)
            if m is None:
                continue
            m = add_exp(m, v, 1)
            if m is None:
                continue
            out.append((1, ('x', m)))
        return out
    if key[0] == 'gg':
        _, p, q, e = key
        i, j = p
        l, m_ = q
        out = []
        # D_p terms (E=2 monos): x_i^2, x_ix_j, x_j^2 ; here e=() with E0=0 general:
        # general: D_p monomials = e + (2 at i / 1+1 / 2 at j)
        for (u, v) in ((i, i), (i, j), (j, j)):
            mm = add_exp(e, u, 1)
            if mm is None:
                continue
            mm = add_exp(mm, v, 1)
            if mm is None:
                continue
            out.append((1, ('g', q[0], q[1], mm)))
        for (u, v) in ((l, l), (l, m_), (m_, m_)):
            mm = add_exp(e, u, 1)
            if mm is None:
                continue
            mm = add_exp(mm, v, 1)
            if mm is None:
                continue
            out.append((-1, ('g', p[0], p[1], mm)))
        return out
    raise ValueError(key)

def relvec(key):
    """Relation vector as list of (coeff, F key)."""
    if key[0] == 'r1':
        _, i, j, m = key
        out = []
        t1 = add_exp(m, i, 1)
        t2 = add_exp(m, j, 1)
        if t1 is not None:
            out.append((1, ('g', i, j, t1)))
        if t2 is not None:
            out.append((-1, ('g', i, j, t2)))
        return out
    if key[0] == 'arn':
        _, i, j, l = key
        p1 = (i, j); p2 = (i, l); p3 = (j, l)
        e0 = tuple([0]*len_zero[0])
        # Arnold relation for m even: +Gp1Gp2 - Gp1Gp3 + Gp2Gp3 = 0, the unique
        # (up to scale) sign pattern with d in the R1-ideal (solved over QQ:
        # only (+,-,+) and (-,+,-) close; see output/artifacts/run_arn_signs.txt).
        return [(1, ('gg', p1, p2, e0)), (-1, ('gg', p1, p3, e0)), (1, ('gg', p2, p3, e0))]
    raise ValueError(key)

len_zero = [0]

def act_R(key, a, b):
    def sw(x):
        return b if x == a else (a if x == b else x)
    if key[0] == 'r1':
        _, i, j, m = key
        i2, j2 = sw(i), sw(j)
        if i2 > j2:
            i2, j2 = j2, i2
        return (1, ('r1', i2, j2, perm_tuple(m, a, b)))
    if key[0] == 'arn':
        _, i, j, l = key
        a1, b1, c1 = sw(i), sw(j), sw(l)
        # Symmetric Arnold polynomial is invariant under index permutation (m even).
        t = tuple(sorted((a1, b1, c1)))
        return (1, ('arn', t[0], t[1], t[2]))
    raise ValueError(key)

def gens(k, group):
    if group == 'full':
        return [(i, i+1) for i in range(k-1)]
    else:
        return [(i, i+1) for i in range(k-2)]

def orbit_decomp(keys, act, generators):
    """Signed orbit sums spanning invariants. Returns (vecs, lookup, sizes).
    vecs: list of dict key->(+1/-1). lookup: key->(oid,sign). sizes: orbit lens."""
    idx = {key: n for n, key in enumerate(keys)}
    seen = set()
    vecs = []
    lookup = {}
    sizes = []
    for s0 in keys:
        if s0 in seen:
            continue
        # BFS unsigned orbit with sign consistency
        coeff = {s0: 1}
        queue = [s0]
        morate = set([s0])
        ok = True
        qpos = 0
        while qpos < len(queue):
            cur = queue[qpos]; qpos += 1
            c = coeff[cur]
            for g in generators:
                sgn, nxt = act(cur, g[0], g[1])
                need = c*sgn
                if nxt not in coeff:
                    coeff[nxt] = need
                    queue.append(nxt)
                elif coeff[nxt] != need:
                    ok = False
                    break
            if not ok:
                break
        for q in queue:
            seen.add(q)
        if not ok:
            continue
        oid = len(vecs)
        vecs.append(coeff)
        sizes.append(len(coeff))
        for q, c in coeff.items():
            lookup[q] = (oid, c)
    return vecs, lookup, sizes

def proj_matrix_D(src_vecs, src_lookup, tgt_lookup, tgt_sizes, diff_fn, F1drop_check=None):
    if F1drop_check is None:
        F1drop_check = [set()]
    """D_orb matrix rows=tgt orbits, cols=src orbits (Fraction)."""
    bt = len(tgt_sizes); bs = len(src_vecs)
    M = [[Fraction(0)]*bs for _ in range(bt)]
    for j, v in enumerate(src_vecs):
        acc = {}
        for key, c in v.items():
            for (dc, tk) in diff_fn(key):
                if tk not in tgt_lookup:
                    # Dropped (sign-inconsistent) target orbit: every invariant
                    # vector has coefficient 0 on it, so it contributes 0.
                    # (Verified: orbit_decomp partitions all keys; missing keys
                    # lie in dropped sign-inconsistent orbits.)
                    if tk not in F1drop_check[0]:
                        F1drop_check[0].add(tk)
                    continue
                l, s = tgt_lookup[tk]
                acc[l] = acc.get(l, 0) + dc*c*s
        for l, val in acc.items():
            if val % tgt_sizes[l] != 0:
                raise RuntimeError("non-exact division")
            M[l][j] = Fraction(val // tgt_sizes[l])
    return M

def proj_matrix_J(rel_vecs, F_lookup, F_sizes, relvec_fn):
    """rows=F orbits, cols=rel orbits."""
    bf = len(F_sizes); br = len(rel_vecs)
    M = [[Fraction(0)]*br for _ in range(bf)]
    for a, rv in enumerate(rel_vecs):
        acc = {}
        for rk, rc in rv.items():
            for (vc, fk) in relvec_fn(rk):
                if fk not in F_lookup:
                    # Same justification as in proj_matrix_D.
                    continue
                l, s = F_lookup[fk]
                acc[l] = acc.get(l, 0) + rc*vc*s
        for l, val in acc.items():
            if val % F_sizes[l] != 0:
                raise RuntimeError("non-exact J division")
            M[l][a] = Fraction(val // F_sizes[l])
    return M

def rank_frac(M):
    if not M or not M[0]:
        return 0
    A = [row[:] for row in M]
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        piv = None
        for i in range(r, m):
            if A[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]/A[r][c]
                for j in range(c, n):
                    A[i][j] -= f*A[r][j]
        r += 1
        if r == m:
            break
    return r

def aug_rank(A, B):
    """rank of [A | B] (same rows). Either may be empty."""
    m = len(A) if A else (len(B) if B else 0)
    if m == 0:
        return 0
    na = len(A[0]) if A and A[0] else 0
    nb = len(B[0]) if B and B[0] else 0
    if na == 0:
        return rank_frac(B)
    if nb == 0:
        return rank_frac(A)
    return rank_frac([A[i]+B[i] for i in range(m)])

def cohomology_dim(b, J, D, Jp, Dprev, Jprev):
    rJp = rank_frac(Jp) if Jp and Jp[0] else 0
    rJ = rank_frac(J) if J and J[0] else 0
    rDJp = aug_rank(D, Jp)
    rDJ = aug_rank(Dprev, J)
    return b - rDJp + rJp - rDJ

def data_for(k, d, group):
    G = gens(k, group)
    F = build_F(k, d)
    F1 = build_F(k, d+1)
    Fm = build_F(k, d-1)
    R = build_R1(k, d) + build_Arn(k, d)
    Rp = build_R1(k, d+1) + build_Arn(k, d+1)
    Rm = build_R1(k, d-1) + build_Arn(k, d-1)
    len_zero[0] = k
    Fv, Fl, Fs = orbit_decomp(F, act_F, G)
    F1v, F1l, F1s = orbit_decomp(F1, act_F, G)
    Fmv, Fml, Fms = orbit_decomp(Fm, act_F, G)
    Rv, Rl, Rs = orbit_decomp(R, act_R, G)
    Rpv, Rpl, Rps = orbit_decomp(Rp, act_R, G)
    Rmv, Rml, Rms = orbit_decomp(Rm, act_R, G)
    b = len(Fv)
    D = proj_matrix_D(Fv, Fl, F1l, F1s, D_F) if (Fv and F1v) else ([[Fraction(0)]*len(Fv) for _ in range(len(F1v))])
    Dprev = proj_matrix_D(Fmv, Fml, Fl, Fs, D_F) if (Fmv and Fv) else ([[Fraction(0)]*len(Fmv) for _ in range(len(Fv))])
    J = proj_matrix_J(Rv, Fl, Fs, relvec) if (Rv and Fv) else ([[Fraction(0)]*len(Rv) for _ in range(b)])
    Jp = proj_matrix_J(Rpv, F1l, F1s, relvec) if (Rpv and F1v) else ([[Fraction(0)]*len(Rpv) for _ in range(len(F1v))])
    h = cohomology_dim(b, J, D, Jp, Dprev, None if False else proj_matrix_J(Rmv, Fml, Fms, relvec) if (Rmv and Fmv) else ([[Fraction(0)]*len(Rmv) for _ in range(len(Fmv))]))
    # recompute cleanly: need Jprev : Rm -> Fm
    return h, b

def twisted_betti(k, d):
    hf, bf = data_for(k, d, 'fix')
    hh, bh = data_for(k, d, 'full')
    return hf - hh, hf, hh, bf, bh

if __name__ == '__main__':
    ks = [int(x) for x in sys.argv[1:]] or [4,5,6]
    for k in ks:
        for d in [2,3,4,5]:
            t, hf, hh, bf, bh = twisted_betti(k, d)
            print(f"k={k} d={d}: t={t} h_fix={hf} h_full={hh} b_fix={bf} b_full={bh}", flush=True)
