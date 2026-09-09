"""GF(2) binary-matroid toolkit for lane-433 (stdlib only).

Representation: a matroid is (r, cols) with cols = list of ints (bit i = row i).
"""
import itertools


def gf2_rank(cols):
    basis = {}
    r = 0
    for v in cols:
        x = v
        while x:
            b = x.bit_length() - 1
            if b in basis:
                x ^= basis[b]
            else:
                basis[b] = x
                r += 1
                break
    return r


def mat_rank(M):
    return gf2_rank(M[1])


def delete1(M, e):
    r, cols = M
    return (r, cols[:e] + cols[e + 1:])


def contract1(M, e):
    """Contract element e (requires cols[e] != 0). Returns new (r-1, cols)."""
    r, cols = M
    v = cols[e]
    assert v != 0, "cannot contract a loop"
    piv = (v & -v).bit_length() - 1  # lowest set row as pivot
    out = []
    for k, c in enumerate(cols):
        if k == e:
            continue
        if (c >> piv) & 1:
            c ^= v
        lo = c & ((1 << piv) - 1) if piv > 0 else 0
        hi = c >> (piv + 1)
        out.append(lo | (hi << piv))
    return (r - 1, out)


def contract_set(M, C):
    for e in sorted(C, reverse=True):
        v = M[1][e]
        if v == 0:
            M = delete1(M, e)  # loop: contraction = deletion
        else:
            M = contract1(M, e)
    return M


def simplify(M):
    r, cols = M
    seen = set()
    newcols, dropped = [], []
    for i, c in enumerate(cols):
        if c == 0 or c in seen:
            dropped.append(i)
        else:
            seen.add(c)
            newcols.append(c)
    return (r, newcols), dropped


def is_simple(M):
    _, cols = M
    if any(c == 0 for c in cols):
        return False
    return len(set(cols)) == len(cols)


def nbases(M):
    r, cols = M
    n = len(cols)
    if r == 0:
        return 1
    cnt = 0
    for combo in itertools.combinations(range(n), r):
        if gf2_rank([cols[i] for i in combo]) == r:
            cnt += 1
    return cnt


def bases_set(M):
    r, cols = M
    n = len(cols)
    out = set()
    for combo in itertools.combinations(range(n), r):
        if gf2_rank([cols[i] for i in combo]) == r:
            out.add(tuple(sorted(combo)))
    return out


def lambda_of(M, X):
    r, cols = M
    n = len(cols)
    Xs = set(X)
    Y = [j for j in range(n) if j not in Xs]
    return gf2_rank([cols[i] for i in X]) + gf2_rank([cols[j] for j in Y]) - gf2_rank(cols)


def conn_check(M):
    """Return (ok, info). ok=True iff no 1- or 2-separation (plus |E|>=4)."""
    r, cols = M
    n = len(cols)
    if n < 4:
        return False, {'reason': 'fewer than 4 elements'}
    R = gf2_rank(cols)
    lambmins = {}
    viols = []
    # Every partition {X,Y} has exactly one side containing element 0, so
    # iterating all X ni 0 covers each partition once (no size skip: the
    # 0-side may be the large side, and lambda/min-size are symmetric).
    for mask in range(1, (1 << n) - 1):
        if not (mask & 1):
            continue  # symmetry halve: require 0 in X
        X = [j for j in range(n) if (mask >> j) & 1]
        s = len(X)
        lam = gf2_rank([cols[i] for i in X]) + gf2_rank(
            [cols[j] for j in range(n) if not ((mask >> j) & 1)]) - R
        k = min(s, n - s)
        if k not in lambmins or lam < lambmins[k]:
            lambmins[k] = lam
        if k >= 1 and lam < 1:
            viols.append(('1-sep', X, lam))
        elif k >= 2 and lam < 2:
            viols.append(('2-sep', X, lam))
    ok = not viols
    return ok, {'lambda_min_by_size': lambmins, 'violations': viols[:6],
                'nviol': len(viols), 'n': n, 'rank': R}


# ---------------- standards ----------------
def std_F7():
    cols = [0b001, 0b010, 0b100, 0b011, 0b101, 0b110, 0b111]
    return (3, cols)


def std_MK5():
    cols = []
    for i in range(5):
        for j in range(i + 1, 5):
            v = 0
            if i < 4:
                v |= (1 << i)
            if j < 4:
                v ^= (1 << j)
            cols.append(v)
    return (4, cols)


F7_BASES = None


def f7_bases():
    global F7_BASES
    if F7_BASES is None:
        F7_BASES = bases_set(std_F7())
    return F7_BASES


def iso_to_std_F7(M):
    """If M is a 3x7 matroid isomorphic to F7, return perm list; else None."""
    r, cols = M
    if r != 3 or len(cols) != 7:
        return None
    if len(bases_set(M)) != 28:
        return None
    F = f7_bases()
    B = bases_set(M)
    for p in itertools.permutations(range(7)):
        ok = True
        for b in B:
            if tuple(sorted(p[i] for i in b)) not in F:
                ok = False
                break
        if ok:
            return list(p)
    return None


def find_F7_model(M):
    """Search contract-set C (|C| = r-3) + keep-set S (|S|=7) with (M/C)|S ~= F7.
    Returns (C, S, perm) or None."""
    r, cols = M
    n = len(cols)
    if r < 3 or n < 7:
        return None
    need = r - 3
    E = list(range(n))
    for S in itertools.combinations(E, 7):
        Sset = set(S)
        rest = [j for j in E if j not in Sset]
        if len(rest) < need:
            continue
        for C in itertools.combinations(rest, need):
            if gf2_rank([cols[j] for j in C]) != need:
                continue
            Mc = contract_set(M, list(C))
            # remap S indices into contracted matrix
            rem = [j for j in E if j not in set(C)]
            pos = {v: k for k, v in enumerate(rem)}
            sub = (Mc[0], [Mc[1][pos[j]] for j in S])
            if gf2_rank(sub[1]) != 3:
                continue
            if len(bases_set(sub)) != 28:
                continue
            p = iso_to_std_F7(sub)
            if p is not None:
                return (list(C), list(S), p)
    return None


def mk5_search_stats(M):
    """Exhaustive M(K5)-minor-model search. Returns dict with found flag.
    M(K5): rank 4, 10 elements, 125 bases."""
    r, cols = M
    n = len(cols)
    stat = {'n': n, 'rank': r, 'models_examined': 0, 'rank4_10elt_minors': 0,
            'max_bases_seen': 0, 'found': False}
    if n < 10 or r < 4:
        stat['note'] = 'too small to host 10-element minor' if n < 10 else 'rank<4'
        return stat
    need = r - 4
    E = list(range(n))
    for S in itertools.combinations(E, 10):
        Sset = set(S)
        rest = [j for j in E if j not in Sset]
        for t in range(need, len(rest) + 1):
            for C in itertools.combinations(rest, t):
                if gf2_rank([cols[j] for j in C]) != need:
                    continue
                Mc = contract_set(M, list(C))
                rem = [j for j in E if j not in set(C)]
                pos = {v: k for k, v in enumerate(rem)}
                sub = (Mc[0], [Mc[1][pos[j]] for j in S])
                if gf2_rank(sub[1]) != 4:
                    continue
                stat['models_examined'] += 1
                stat['rank4_10elt_minors'] += 1
                nb = nbases(sub)
                if nb > stat['max_bases_seen']:
                    stat['max_bases_seen'] = nb
                if nb == 125:
                    stat['found'] = True
                    stat['witness'] = (list(C), list(S))
                    return stat
    return stat


def counting_MK5_note(M):
    r, cols = M
    n = len(cols)
    # Hosting M(K5) (rank 4, 10 elt) from rank r needs contract-set C with
    # r(C)=r-4 (|C|>=r-4) and n-|C|>=10. Impossible iff n-(r-4)<10.
    return {'n_minus_contract_needed': n - (r - 4), 'threshold': 10,
            'impossible_by_counting': (n - (r - 4)) < 10}
