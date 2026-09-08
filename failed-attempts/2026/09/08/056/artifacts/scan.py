"""Scan ordered triples for nontrivial Massey (affine m(tau) vs D+Ind)."""
import sys, itertools, sympy
sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-162/output/artifacts")
from rmodel import faces_of, basis_J, deg_of, diff_mat
from cup import prod_on_basis, is_coboundary
from massey import cup_vecs, massey


def Hdata(FACES, BB):
    out = {}
    for J in range(64):
        B = BB[J]
        by = {}
        for b in B:
            by.setdefault(deg_of(*b), []).append(b)
        for d, Bd in by.items():
            BdN = by.get(d + 1, [])
            BdP = by.get(d - 1, [])
            Do = diff_mat(J, Bd, FACES, BdN) if BdN else sympy.zeros(0, len(Bd))
            Di = diff_mat(J, BdP, FACES, Bd) if BdP else sympy.zeros(len(Bd), 0)
            ns = Do.nullspace()
            if len(ns) - Di.rank() > 0:
                out[(J, d)] = (Bd, ns, Di, Do)
    return out


def restrict_to_deg(B63_full_vec, B63, dm):
    idx = [k for k, b in enumerate(B63) if deg_of(*b) == dm]
    return sympy.Matrix([B63_full_vec[k] for k in idx]), idx


def scan(EM, tmask, name, max_tests=200):
    FACES = faces_of(EM, tmask)
    BB = {J: basis_J(J, FACES) for J in range(64)}
    HD = Hdata(FACES, BB)
    keys = [k for k in HD if k[0] != 0]
    tests = 0
    hits = []
    for ka, kb, kc in itertools.product(keys, keys, keys):
        if tests >= max_tests:
            break
        (Ja, da), (Jb, db), (Jc, dc) = ka, kb, kc
        # need |union|<=63 trivially; skip if deg sum-1 out of range
        Ba, nsa, _, _ = HD[ka]
        Bb, nsb, _, _ = HD[kb]
        Bc, nsc, _, _ = HD[kc]
        try:
            r = massey(nsa[0], Ba, Ja, da, nsb[0], Bb, Jb, db, nsc[0], Bc, Jc, dc, FACES, BB)
        except Exception as e:
            continue
        tests += 1
        if r["status"] != "computed":
            continue
        m = r["m_vec"]
        D = r["m_Di"]
        # indeterminacy cols: a*H(Jbc)+H(Jab)*c restricted to deg dm — build via cup_vecs on full B then restrict
        J_ab = Ja | Jb
        J_bc = Jb | Jc
        dm = r["dm"]
        B_abc = r["B_abc"]
        iab = HD.get((J_ab, da + db - 1), None)
        ibc = HD.get((J_bc, db + dc - 1), None)
        cols = []
        nsym = {}
        if iab is not None:
            Bd_ab, ns_ab, Di_ab, _ = iab
            for w in ns_ab:
                v, _ = cup_vecs(w, Bd_ab, nsc[0], Bc, B_abc, FACES)
                vv, _ = restrict_to_deg(v, B_abc, dm)
                cols.append(vv)
        if ibc is not None:
            Bd_bc, ns_bc, Di_bc, _ = ibc
            for w in ns_bc:
                v, _ = cup_vecs(nsa[0], Ba, w, Bd_bc, B_abc, FACES)
                vv, _ = restrict_to_deg(v, B_abc, dm)
                cols.append(vv)
        if cols:
            Ind = sympy.Matrix.hstack(*cols)
            M = sympy.Matrix.hstack(D, Ind) if D.cols else Ind
        else:
            M = D
        # m affine in taus: sample tau=0 (particular) — but must use GENERAL: m(tau)=m0+K tau; check whether m0 in col(M)+col(K)? Proper test: rank([M K]) vs rank([M K m0])... if m0 in span(M,K) then some choice kills it; else NONTRIVIAL.
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
    OCT = K6 & ~((1 << EIDX[(0, 1)]) | (1 << EIDX[(2, 3)]) | (1 << EIDX[(4, 5)]))
    C6 = E((0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0))
    import sys as s
    which = s.argv[1] if len(s.argv) > 1 else "C6"
    EM = {"C6": C6, "OCT": OCT, "K6": K6, "P6": (1 << 0) | (1 << 5) | (1 << 9) | (1 << 12) | (1 << 14)}[which]
    t, h = scan(EM, 0, which, max_tests=int(s.argv[2]) if len(s.argv) > 2 else 200)
    print(which, "tests:", t, "hits:", len(h))
    for x in h[:10]:
        print(x)
