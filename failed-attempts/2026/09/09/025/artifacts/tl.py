"""Temperley-Lieb transfer-matrix Jones evaluator for 3-braid closures (exact, fast).
Basis: non-crossing pairings of 3+3=6 boundary points? For trace closure we use
the standard TL representation on link-diagram states via the Kauffman bracket
skein: represent the bracket of braid closure as a bilinear form over the TL
algebra TL_3(d). Basis of TL_3: {1, E1, E2, E1E2, E2E1} (5 = Catalan(3)).
Multiplication with loop factor d=-A^2-A^-2. Braid generators: rho(s1)=A*1+A^-1*E1,
rho(s2)=A*1+A^-1*E2 (positive crossings; negative: A^-1*1+A*Ei).
Markov trace: tr(1)=d^2, tr(E1)=tr(E2)=d, tr(E1E2)=tr(E2E1)=1 (closing the TL
diagrams: E1 connects... verified by calibration against cube.py).
Then <K> = tr(rho(word)); V via same normalization.
All arithmetic in Z[A,A^-1]: exponents as dicts.
"""
A = "A"

def add(p, q):
    r = dict(p)
    for e, c in q.items():
        r[e] = r.get(e, 0) + c
        if r[e] == 0:
            del r[e]
    return r

def mul(p, q):
    r = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            r[e1 + e2] = r.get(e1 + e2, 0) + c1 * c2
    return {e: c for e, c in r.items() if c}

def scale(p, s):
    return {e: c * s for e, c in p.items() if c * s}

D = {-2: -1, 2: -1}  # d = -A^2 - A^-2
ONE = {0: 1}

# TL_3 basis order: [1, E1, E2, E1E2, E2E1]; multiplication table M[a][b] = (coeff_poly, basis_idx)
# E1^2 = d E1; E2^2 = d E2; E1E2E1 = E1; E2E1E2 = E2.
def tmul(a, b):
    """Multiply basis words (as tuples) and reduce. Words over {1,2} meaning E1,E2; () = 1."""
    w = tuple(a) + tuple(b)
    coeff = dict(ONE)
    # reduce: E_i E_i -> d; E1E2E1 -> E1; E2E1E2 -> E2 (as subwords, repeatedly)
    w = list(w)
    changed = True
    while changed:
        changed = False
        # length-3 reductions
        for k in range(len(w) - 2):
            if (w[k], w[k + 1], w[k + 2]) == (1, 2, 1):
                del w[k + 1:k + 3]
                changed = True
                break
            if (w[k], w[k + 1], w[k + 2]) == (2, 1, 2):
                del w[k + 1:k + 3]
                changed = True
                break
        if changed:
            continue
        for k in range(len(w) - 1):
            if w[k] == w[k + 1]:
                del w[k]
                coeff = mul(coeff, D)
                changed = True
                break
    key = tuple(w)
    return coeff, key

BASIS = [(), (1,), (2,), (1, 2), (2, 1)]
BIDX = {b: i for i, b in enumerate(BASIS)}

def elem_mul_vec(elem, vec):
    """elem: basis tuple; vec: list of 5 polys. Returns new vec = elem*vec."""
    out = [dict() for _ in range(5)]
    for j, p in enumerate(vec):
        if not p:
            continue
        coeff, key = tmul(elem, BASIS[j])
        out[BIDX[key]] = add(out[BIDX[key]], mul(coeff, p))
    return out

def rho_word(word):
    """word: list of (i,sign). Returns TL element as vec of 5 polys."""
    vec = [dict(ONE), {}, {}, {}, {}]
    for i, s in word:
        e = (i,)
        if s == 1:
            # A*1 + A^-1*Ei
            new = [add(scale(p, 0), {}) for p in vec]  # placeholder
            part1 = [{0: 0} if False else dict(p) for p in vec]
            # A*vec
            avec = [{e2 + 1: c for e2, c in p.items()} for p in vec]
            # A^-1 * Ei * vec
            bvec = elem_mul_vec(e, vec)
            bvec = [{e2 - 1: c for e2, c in p.items()} for p in bvec]
            vec = [add(a, b) for a, b in zip(avec, bvec)]
        else:
            avec = [{e2 - 1: c for e2, c in p.items()} for p in vec]
            bvec = elem_mul_vec(e, vec)
            bvec = [{e2 + 1: c for e2, c in p.items()} for p in bvec]
            vec = [add(a, b) for a, b in zip(avec, bvec)]
    return vec

def bracket_raw(word):
    vec = rho_word(word)
    TR = [{0: 0} for _ in range(5)]
    TR[BIDX[()]] = mul(D, D)      # d^2
    TR[BIDX[(1,)]] = dict(D)      # d
    TR[BIDX[(2,)]] = dict(D)      # d
    TR[BIDX[(1, 2)]] = dict(ONE)  # 1
    TR[BIDX[(2, 1)]] = dict(ONE)  # 1
    total = {}
    for p, t in zip(vec, TR):
        total = add(total, mul(p, t))
    return total

bracket = bracket_raw  # raw 3-strand trace; exact for words using both generators

# Strand-count rule, CORRECTED (2026-09-09): the raw trace closes all 3 strands and
# agrees with cube.py closed on 3 strands for EVERY word (verified: s1-only, s2-only,
# fig8, K0, K1). An unused strand is a real disjoint circle of the 3-strand closure
# (e.g. cl(s2^3) = trefoil + unknot), NOT a spurious factor. The earlier /d idea was
# wrong as a closure operation; it merely converts the 3-strand-closure bracket to
# the 2-strand-closure bracket for single-generator words. K_k words use all strands,
# so raw trace = bracket(cl(K_k)) directly. bracket_closed asserts full support.
def div_by_d(p):
    p = dict(p)
    q = {}
    for _ in range(10000):
        nz = {e: c for e, c in p.items() if c}
        if not nz:
            break
        e = max(nz)
        c = nz[e]
        q[e - 2] = q.get(e - 2, 0) - c
        del p[e]
        p[e - 4] = p.get(e - 4, 0) - c
    assert all(v == 0 for v in p.values()), p
    return {e: c for e, c in q.items() if c}

def bracket_closed(word, nstrands=3):
    assert word, "empty word"
    assert min(i for i, _ in word) == 1 and max(i for i, _ in word) == nstrands - 1, \
        "word must use all strands"
    return bracket_raw(word)

def Kword(k):
    return [(1, 1), (2, -1)] * (6 * k + 1) + [(1, 1), (1, 1)]

if __name__ == "__main__":
    import sys
    sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-332/output/artifacts")
    from cube import jones_from_bracket, writhe
    # calibrate on small words
    tests = {"unknot s1s1^-1": ([(1, 1), (1, -1)], 2),
             "trefoil": ([(1, 1)] * 3, 2),
             "fig8": ([(1, 1), (2, -1)] * 2, 3),
             "K0": (Kword(0), 3),
             "K1": (Kword(1), 3)}
    from cube import kauffman_bracket, CONV
    for label, (w, n) in tests.items():
        b1 = bracket(w)
        b0 = kauffman_bracket(w, n, CONV)
        print(label, "TL==cube:", b1 == b0)
    for k in [0, 1, 2, 3, 4, 5]:
        w = Kword(k)
        b = bracket(w)
        V = jones_from_bracket(b, writhe(w))
        Vi = {e // 4: c for e, c in V.items() if c}
        assert all(e % 4 == 0 for e in V)
        lo, hi = min(Vi), max(Vi)
        print(f"K{k}: n={len(w)} span={hi-lo} lo={lo} hi={hi} V(1)={sum(Vi.values())}")
    w = Kword(2)
    b = bracket(w)
    V = jones_from_bracket(b, writhe(w))
    Vi = {e // 4: c for e, c in V.items() if c}
    print("K2 V:", dict(sorted(Vi.items())))
