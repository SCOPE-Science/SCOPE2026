#!/usr/bin/env python3
"""Replayable verification for lane-47 (6,2)/F2 2-step census. Stdlib only, deterministic. Runs in <2 min."""
import math, json, sys

PAIRS = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]

def mat_from_bits(b):
    M = [[0]*4 for _ in range(4)]
    for k,(i,j) in enumerate(PAIRS):
        if (b >> k) & 1:
            M[i][j] ^= 1; M[j][i] ^= 1
    return M

def bits_from_mat(M):
    b = 0
    for k,(i,j) in enumerate(PAIRS):
        b |= (M[i][j] & 1) << k
    return b

def rank_gf2(A, n, m=None):
    M = [row[:] for row in A]
    r = 0; cols = len(M[0])
    for c in range(cols):
        piv = None
        for i in range(r, len(M)):
            if M[i][c]: piv = i; break
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(len(M)):
            if i != r and M[i][c]:
                for j in range(c, cols): M[i][j] ^= M[r][j]
        r += 1
        if r == n: break
    return r

def gen_gl(n):
    out = []
    for bits in range(1 << (n*n)):
        M = [[(bits >> (i*n+j)) & 1 for j in range(n)] for i in range(n)]
        if rank_gf2(M, n) == n:
            out.append(M)
    return out

def apply_cong(b, P):
    M = mat_from_bits(b)
    R = [[sum(M[i][k]*P[k][j] for k in range(4)) % 2 for j in range(4)] for i in range(4)]
    N = [[sum(P[k][i]*R[k][j] for k in range(4)) % 2 for j in range(4)] for i in range(4)]
    return bits_from_mat(N)

def apply_GL2(a, b, S):
    return ((a if S[0][0] else 0) ^ (b if S[0][1] else 0),
            (a if S[1][0] else 0) ^ (b if S[1][1] else 0))

def rank_of(b):
    return rank_gf2(mat_from_bits(b), 4)

def radical_dim(a, b):
    A = mat_from_bits(a); B = mat_from_bits(b)
    n = 0
    for v in range(16):
        vv = [(v >> i) & 1 for i in range(4)]
        sa = [sum(A[i][j]*vv[j] for j in range(4)) % 2 for i in range(4)]
        sb = [sum(B[i][j]*vv[j] for j in range(4)) % 2 for i in range(4)]
        if all(x == 0 for x in sa) and all(x == 0 for x in sb): n += 1
    return int(math.log2(n))

def derived_dim(a, b):
    if a == 0 and b == 0: return 0
    if a == 0 or b == 0 or a == b: return 1
    return 2

def build_bracket(a, b):
    c = [[[0]*6 for _ in range(6)] for _ in range(6)]
    A = mat_from_bits(a); B = mat_from_bits(b)
    for i in range(4):
        for j in range(4):
            c[i][j][4] ^= A[i][j]; c[i][j][5] ^= B[i][j]
    return c

def centre_derived_from_tensor(c):
    cen = []
    for v in range(64):
        vv = [(v >> i) & 1 for i in range(6)]
        ok = True
        for j in range(6):
            for k in range(6):
                s = 0
                for i in range(6): s ^= (vv[i] & c[i][j][k])
                if s: ok = False; break
            if not ok: break
        if ok: cen.append(v)
    cdim = int(math.log2(len(cen)))
    vecs = set(tuple(c[i][j][k] for k in range(6)) for i in range(6) for j in range(6))
    span = {tuple([0]*6)}
    for v in vecs:
        span = {tuple((s[k]+w[k]) % 2 for k in range(6)) for s in list(span) for w in (tuple([0]*6), v)}
    ddim = int(math.log2(len(span)))
    return cdim, ddim, cen

def jacobi_check(c):
    n = 0
    for i in range(6):
        for j in range(6):
            for k in range(6):
                n += 1
                for m in range(6):
                    s = 0
                    for ell in range(6):
                        s ^= (c[i][j][ell] & c[ell][k][m]) ^ (c[j][k][ell] & c[ell][i][m]) ^ (c[k][i][ell] & c[ell][j][m])
                    assert s == 0, (i, j, k, m, s)
    return n

def main():
    print("== lane-47 verify_census.py ==")
    GL2 = gen_gl(2); GL4 = gen_gl(4)
    print(f"GL(2,F2) order = {len(GL2)} (expect 6)")
    print(f"GL(4,F2) order = {len(GL4)} (expect 20160)")
    assert len(GL2) == 6 and len(GL4) == 20160
    cong = [[apply_cong(b, P) for b in range(64)] for P in GL4]
    print("congruence table ok")
    # fibre
    good = [(a,b) for a in range(64) for b in range(64) if radical_dim(a,b) == 0]
    print(f"Rad0 pairs = {len(good)} (expect 3360)")
    assert len(good) == 3360
    goodset = set(good)
    from collections import Counter
    print("derived dist:", dict(Counter(derived_dim(a,b) for a,b in good)), "(expect {2:3276,1:84})")
    assert Counter(derived_dim(a,b) for a,b in good) == {2:3276, 1:84}
    def rt(a,b): return tuple(sorted([rank_of(a), rank_of(b), rank_of(a^b)]))
    print("ranktype dist:", {k: v for k,v in sorted(Counter(rt(a,b) for a,b in good).items())})
    assert dict(Counter(rt(a,b) for a,b in good)) == {(0,4,4):84,(2,4,4):1260,(2,2,4):1680,(4,4,4):336}
    reps = [(0,12),(1,12),(1,32),(12,22)]
    for r in reps: assert r in goodset
    # orbits + stabilizers
    orbits = []
    for rep in reps:
        full = set()
        for S in GL2:
            q = apply_GL2(rep[0], rep[1], S)
            for pi in range(len(GL4)):
                full.add((cong[pi][q[0]], cong[pi][q[1]]))
        orbits.append(full)
    for i,f in enumerate(orbits): print(f"orbit {i} rep {reps[i]} size {len(f)} rt {rt(*reps[i])} derived {derived_dim(*reps[i])}")
    assert [len(f) for f in orbits] == [84,1260,1680,336]
    assert sum(len(f) for f in orbits) == 3360
    for i in range(4):
        for j in range(i+1,4):
            assert orbits[i].isdisjoint(orbits[j]), (i,j)
    assert set.union(*orbits) == goodset
    print("partition: 4 orbits cover 3360 Rad0 pairs, disjoint. COMPLETE.")
    # stabilizers -> Aut orders
    for idx,rep in enumerate(reps):
        a,b = rep; stab = 0
        for S in GL2:
            q = apply_GL2(a,b,S)
            for pi in range(len(GL4)):
                if cong[pi][q[0]] == a and cong[pi][q[1]] == b: stab += 1
        assert stab * len(orbits[idx]) == 120960, (rep, stab)
        print(f"rep {rep}: stab {stab}, orbit {len(orbits[idx])}, |Aut| = 256*{stab} = {256*stab}")
    expected_aut = {(0,12):368640,(1,12):24576,(1,32):18432,(12,22):92160}
    # tensor checks
    for rep in reps:
        c = build_bracket(*rep)
        n = jacobi_check(c)
        cdim, ddim, cen = centre_derived_from_tensor(c)
        print(f"rep {rep}: Jacobi triples {n} all zero (=1296 scalar checks); centre dim {cdim}; derived dim {ddim}")
        assert n == 216 and cdim == 2  # 216 triples = 1296 scalar (i,j,k,m) checks
    assert centre_derived_from_tensor(build_bracket(0,12))[1] == 1
    # invariant separation
    invs = [(derived_dim(a,b), rt(a,b)) for a,b in reps]
    assert len(set(invs)) == 4
    print("invariants separate all 4 orbits. pairwise non-isomorphism certified.")
    # explicit reduction demo: for first non-rep member of each orbit, find block-diag 6x6 G by direct search
    import itertools
    def find_iso(tgt, rep):
        ct, cr = build_bracket(*tgt), build_bracket(*rep)
        def applyM(M,v): return [sum(M[i][j]*v[j] for j in range(len(v))) % 2 for i in range(len(M))]
        for S in GL2:
            for P in GL4:
                G = [[0]*6 for _ in range(6)]
                for i in range(4):
                    for j in range(4): G[i][j] = P[i][j]
                for i in range(2):
                    for j in range(2): G[4+i][4+j] = S[i][j]
                ok = True
                for i in range(6):
                    for j in range(6):
                        lhs = applyM(G, ct[i][j])
                        ei = [1 if k==i else 0 for k in range(6)]; ej=[1 if k==j else 0 for k in range(6)]
                        gi, gj = applyM(G,ei), applyM(G,ej)
                        rhs = [0]*6
                        for pp in range(6):
                            for qq in range(6):
                                if gi[pp] and gj[qq]:
                                    for m in range(6): rhs[m] ^= cr[pp][qq][m]
                        if lhs != rhs: ok=False; break
                    if not ok: break
                if ok: return G
        return None
    for idx,rep in enumerate(reps):
        orb = sorted(orbits[idx])
        tgt = orb[1] if orb[0] == rep else orb[0]
        if tgt == rep: tgt = orb[-1]
        G = find_iso(tgt, rep)
        assert G is not None and rank_gf2(G,6) == 6
        # verify G is iso tgt -> rep: G([x,y]_tgt) == [Gx,Gy]_rep
        ct, cr = build_bracket(*tgt), build_bracket(*rep)
        def applyM(M,v): return [sum(M[i][j]*v[j] for j in range(len(v))) % 2 for i in range(len(M))]
        for i in range(6):
            for j in range(6):
                lhs = applyM(G, ct[i][j])
                ei = [1 if k==i else 0 for k in range(6)]; ej=[1 if k==j else 0 for k in range(6)]
                gi, gj = applyM(G,ei), applyM(G,ej)
                rhs = [0]*6
                for p in range(6):
                    for q2 in range(6):
                        if gi[p] and gj[q2]:
                            for m in range(6): rhs[m] ^= cr[p][q2][m]
                assert lhs == rhs, (idx,tgt,rep,i,j)
        assert rank_gf2(G,6) == 6
        print(f"orbit {idx}: reduction {tgt} -> {rep} verified via block-diag(P,S) 6x6, det!=0.")
    print("ALL CHECKS PASSED. N=4 exact.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
