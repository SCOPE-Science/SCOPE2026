"""General Massey solver: given (a,b,c) cocycle vecs in bases, find defining system + Massey class + indeterminacy test."""
import sys, sympy
sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-162/output/artifacts")
from rmodel import faces_of, basis_J, deg_of, diff_mat, sgn_union
from cup import prod_on_basis, to_vec, is_coboundary, solve_preimage


def basis_bydeg(B, FACES):
    bydeg = {}
    for b in B:
        bydeg.setdefault(deg_of(*b), []).append(b)
    return bydeg


def cup_vecs(va, Ba, vb, Bb, BJL, FACES):
    idx = {b: k for k, b in enumerate(BJL)}
    acc = {}
    la = [va[i] for i in range(len(Ba))]
    lb = [vb[i] for i in range(len(Bb))]
    for i, ba in enumerate(Ba):
        for j, bb in enumerate(Bb):
            if la[i] == 0 or lb[j] == 0:
                continue
            for b, s in prod_on_basis(ba, bb, FACES, idx).items():
                acc[b] = acc.get(b, 0) + s * la[i] * lb[j]
    return sympy.Matrix([acc.get(b, 0) for b in BJL]), acc


def massey(va, Ba, Ja, da, vb, Bb, Jb, db, vc, Bc, Jc, dc, FACES, BB):
    """Returns dict with status. Degrees: |x|=da etc. Boundaries: d(s)=-(-1)^|a| ab... use convention d(s) = -(-1)^{da} ab, d(t) = -(-1)^{db} bc; m = s c + (-1)^{da+1} a t."""
    from cup import is_coboundary as isc
    J_ab = Ja | Jb
    J_bc = Jb | Jc
    J_abc = Ja | Jb | Jc
    if (Ja & Jb) or (Jb & Jc):
        B_ab = BB[J_ab]
        vab, _ = cup_vecs(va, Ba, vb, Bb, B_ab, FACES)
        B_bc = BB[J_bc]
        vbc, _ = cup_vecs(vb, Bb, vc, Bc, B_bc, FACES)
        ab_zero = all(x == 0 for x in vab)
        bc_zero = all(x == 0 for x in vbc)
        if not (ab_zero and bc_zero):
            # still need exactness check if nonzero
            pass
    B_ab = BB[J_ab]
    vab, _ = cup_vecs(va, Ba, vb, Bb, B_ab, FACES)
    B_bc = BB[J_bc]
    vbc, _ = cup_vecs(vb, Bb, vc, Bc, B_bc, FACES)
    dab = da + db
    dbc = db + dc
    # exactness of vab in deg dab, vbc in deg dbc
    res = {"vab_zero": all(x == 0 for x in vab), "vbc_zero": all(x == 0 for x in vbc)}
    # find bounding cochains: d: deg-1 -> deg
    for tag, vv, JJ, dd in [("ab", vab, J_ab, dab), ("bc", vbc, J_bc, dbc)]:
        B = BB[JJ]
        by = basis_bydeg(B, FACES)
        Bd = [b for b in B if deg_of(*b) == dd]
        BdP = [b for b in B if deg_of(*b) == dd - 1]
        Di = diff_mat(JJ, BdP, FACES, Bd) if BdP else sympy.zeros(len(Bd), 0)
        i2 = {b: k for k, b in enumerate(Bd)}
        v = sympy.Matrix([0] * len(Bd))
        for b, k in i2.items():
            v[k] = vv[B.index(b)]
        res[tag + "_exact"] = isc(v, Di)
        res[tag + "_Di"] = Di
        res[tag + "_Bd"] = Bd
        res[tag + "_BdP"] = BdP
        res[tag + "_v"] = v
    if not (res["ab_exact"] and res["bc_exact"]):
        res["status"] = "cups-not-exact"
        return res
    # solve s,t with d s = -(-1)^da vab ; d t = -(-1)^db vbc
    sa = -1 if da % 2 else 1  # -(-1)^da
    sb = -1 if db % 2 else 1
    s = solve_preimage(sa * res["ab_v"], res["ab_Di"])
    t = solve_preimage(sb * res["bc_v"], res["bc_Di"])
    res["s"] = s
    res["t"] = t
    # Massey cocycle in J_abc, deg da+db+dc-1: m = s·c + (-1)^{da+1} a·t
    B_abc = BB[J_abc]
    dm = da + db + dc - 1
    # embed s (in BdP_ab basis) as form over B_ab; t similarly
    fa = {b: s[k] for k, b in enumerate(res["ab_BdP"]) if s[k] != 0}
    fb = {b: t[k] for k, b in enumerate(res["bc_BdP"]) if t[k] != 0}
    fva = {b: va[k] for k, b in enumerate(Ba) if va[k] != 0}
    fvc = {b: vc[k] for k, b in enumerate(Bc) if vc[k] != 0}
    idx = {b: k for k, b in enumerate(B_abc)}
    acc = {}
    for b1, c1 in fa.items():
        for b2, c2 in fvc.items():
            for b, sg in prod_on_basis(b1, b2, FACES, idx).items():
                acc[b] = acc.get(b, 0) + sg * c1 * c2
    sgn = -1 if da % 2 == 0 else 1  # (-1)^{da+1}
    for b1, c1 in fva.items():
        for b2, c2 in fb.items():
            for b, sg in prod_on_basis(b1, b2, FACES, idx).items():
                acc[b] = acc.get(b, 0) + sgn * sg * c1 * c2
    vm = sympy.Matrix([acc.get(b, 0) for b in B_abc])
    res["m"] = vm
    res["B_abc"] = B_abc
    res["dm"] = dm
    # check m is cocycle and whether exact
    by = basis_bydeg(B_abc, FACES)
    Bd = [b for b in B_abc if deg_of(*b) == dm]
    BdN = [b for b in B_abc if deg_of(*b) == dm + 1]
    BdP = [b for b in B_abc if deg_of(*b) == dm - 1]
    Do = diff_mat(J_abc, Bd, FACES, BdN) if BdN else sympy.zeros(0, len(Bd))
    Di = diff_mat(J_abc, BdP, FACES, Bd) if BdP else sympy.zeros(len(Bd), 0)
    i2 = {b: k for k, b in enumerate(Bd)}
    v = sympy.Matrix([0] * len(Bd))
    for b, k in i2.items():
        v[k] = vm[B_abc.index(b)]
    res["m_cocycle"] = (Do * v).is_zero_matrix
    res["m_exact"] = isc(v, Di)
    res["m_vec"] = v
    res["m_Di"] = Di
    res["status"] = "computed"
    return res
