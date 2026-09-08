"""Scan with ALL quotient reps (ns[k]) on chosen complexes, indeterminacy-aware."""
import sys, itertools, sympy
sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-162/output/artifacts")
from rmodel import faces_of, basis_J, deg_of, diff_mat
from massey import cup_vecs, massey
from scan import Hdata, restrict_to_deg


def scan_full(EM, tmask, max_tests=400):
    FACES = faces_of(EM, tmask)
    BB = {J: basis_J(J, FACES) for J in range(64)}
    HD = Hdata(FACES, BB)
    # expand to quotient rep list per slot: use ns vectors (over-approx; fine for search)
    items = []
    for k, (Bd, ns, Di, Do) in HD.items():
        if k[0] == 0:
            continue
        for i, v in enumerate(ns):
            items.append((k, Bd, v))
    tests = 0
    hits = []
    for (ka, Ba, va), (kb, Bb, vb), (kc, Bc, vc) in itertools.product(items, items, items):
        if tests >= max_tests:
            break
        (Ja, da), (Jb, db), (Jc, dc) = ka, kb, kc
        try:
            r = massey(va, Ba, Ja, da, vb, Bb, Jb, db, vc, Bc, Jc, dc, FACES, BB)
        except Exception:
            continue
        tests += 1
        if r["status"] != "computed":
            continue
        m = r["m_vec"]
        D = r["m_Di"]
        J_ab = Ja | Jb
        J_bc = Jb | Jc
        dm = r["dm"]
        B_abc = r["B_abc"]
        cols = []
        for key, other_Bd, other_v, left in [((J_ab, da + db - 1), Bc, vc, False), ((J_bc, db + dc - 1), Ba, va, True)]:
            pass
        for (Jq, dq) in [(J_ab, da + db - 1), (J_bc, db + dc - 1)]:
            ent = HD.get((Jq, dq))
            if ent is None:
                continue
            Bdq, nsq, _, _ = ent
            for w in nsq:
                if Jq == J_ab:
                    v, _ = cup_vecs(w, Bdq, vc, Bc, B_abc, FACES)
                else:
                    v, _ = cup_vecs(va, Ba, w, Bdq, B_abc, FACES)
                vv, _ = restrict_to_deg(v, B_abc, dm)
                cols.append(vv)
        M = sympy.Matrix.hstack(D, *cols) if (D.cols and cols) else (sympy.Matrix.hstack(*cols) if cols else D)
        taus = list(m.free_symbols)
        if taus:
            K = m.jacobian(taus)
            m0 = m.subs({t: 0 for t in taus})
            MK = sympy.Matrix.hstack(M, K) if M.cols else K
        else:
            m0 = m
            MK = M
        r1 = MK.rank()
        r2 = MK.row_join(m0).rank() if MK.cols else (0 if m0.is_zero_matrix else 1)
        if r2 > r1:
            hits.append((ka, kb, kc, str(m0.T), r1, r2))
    return tests, hits


if __name__ == "__main__":
    EDGES = [(i, j) for i in range(6) for j in range(i + 1, 6)]
    EIDX = {e: k for k, e in enumerate(EDGES)}

    def E(*es):
        return sum(1 << EIDX[(min(a, b), max(a, b))] for a, b in es)

    K6 = (1 << 15) - 1
    C6 = E((0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0))
    P6 = (1 << 0) | (1 << 5) | (1 << 9) | (1 << 12) | (1 << 14)
    S5 = E((0, 1), (0, 2), (0, 3), (0, 4), (0, 5))
    D = {"C6": C6, "K6": K6, "P6": P6, "S5": S5}
    which = sys.argv[1]
    t, h = scan_full(D[which], 0, int(sys.argv[2]))
    print(which, "tests:", t, "hits:", len(h))
    for x in h[:10]:
        print(x)
