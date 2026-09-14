"""Minimal free resolution + Tor-algebra products for A=S/I over QQ, S=QQ[x,y,z,w].
Strategy: compute with Macaulay-style linear algebra in fixed internal degree windows.
F_i = direct sum over shifts S(-j)^{b_ij}. Differentials from syzygies.
We implement the standard minimal-resolution recursion:
  - K0 = S; F0 = S.
  - Given F_0..F_i with differentials, the generators of F_{i+1} in degree j are a basis
    of the homology ker/hypothesis... Instead we use the Eliahou-Kervaire-free generic
    approach: compute Tor_i(A,K)_j = homology of Koszul complex K_.\otimes A directly,
    and products via explicit Koszul lifts.
Koszul model: K_p = exterior^p(V) \otimes S, V = span{x1..x4}, differential contraction.
Tor_p(A,K)_j = H_p(K_. \otimes A)_j. Products induced by wedge product on K_..
This avoids building the S-resolution entirely: Tor dimensions = Betti numbers,
and the Tor-algebra product is the wedge product on Koszul homology classes.
"""
from fractions import Fraction
from itertools import combinations
import sympy as sp
import sys
sys.path.insert(0, 'output/artifacts')
from apolar import mons

VARS = ('x','y','z','w')
N = 4

def koszul_basis(p):
    return list(combinations(range(N), p))

def mon_basis_A(I_gens, deg):
    """Monomial-vector-space basis of A_deg via quotient S_deg / I_deg (exact rank computation)."""
    ms = mons(N, deg)
    # subspace I_deg spanned by multiples of gens
    rows = []
    for g in I_gens:
        dg = max(sum(e) for e in g)
        if dg > deg: continue
        for m in mons(N, deg - dg):
            row = [Fraction(0)] * len(ms)
            for e, c in g.items():
                ne = tuple(a + b for a, b in zip(e, m))
                row[ms.index(ne)] += c
            rows.append(row)
    M = sp.Matrix(rows) if rows else sp.zeros(0, len(ms))
    # column-pivot complement = basis of quotient
    pivs = set(M.rref()[1]) if rows else set()
    qb = [ms[j] for j in range(len(ms)) if j not in pivs]
    return ms, qb, M

def proj_to_quotient(poly, ms, M, qb):
    """Project poly (dict) in degree deg to coordinate vector on quotient basis qb."""
    v = sp.Matrix([poly.get(e, Fraction(0)) for e in ms])
    if M.rows == 0:
        return [v[ms.index(e)] for e in qb]
    # solve: find w with v - M.T*c supported on qb... use rref of augmented
    # Simplest: quotient coords via row-reduce [M; v^T] and read off free positions.
    A = M.col_join(v.T)
    _, pivs = A.rref()
    pivs = set(pivs)
    # coordinates of class: restrict v to non-pivot cols after eliminating pivot part
    # Do: find c with M.T? Actually rows span relations; class coords = values on free cols
    # after subtracting combination killing pivot entries. Compute c solving M[:,piv]*c = v[piv].
    piv = sorted(set(M.rref()[1]))
    free = [j for j in range(len(ms)) if j not in piv]
    Mp = M.extract(list(range(M.rows)), piv) if piv else sp.zeros(M.rows, 0)
    vp = sp.Matrix([v[i] for i in piv]) if piv else sp.zeros(M.rows, 0)
    if piv:
        # least-squares exact: solve via rref augmented
        aug = Mp.row_join(vp)
        r, p2 = aug.rref()
        # check consistency implicitly; extract solution for pivot vars
        sol = [Fraction(0)] * len(piv)
        for i, pc in enumerate(p2):
            if pc < len(piv):
                sol[pc] = r[i, -1]
        c = sp.Matrix(sol)
        v = v - (M.extract(list(range(M.rows)), piv) * c if False else _matvec(M, piv, c, len(ms)))
    return [v[ms.index(e)] for e in qb]

def _matvec(M, piv, c, ncols):
    out = sp.zeros(ncols, 1)
    for j, pc in enumerate(piv):
        for i in range(M.rows):
            out[pc, 0] += M[i, j] * c[j]
    return out

def koszul_homology(I_gens, deg_max):
    """Return dict (p, j) -> {'cycles': Matrix (cols=basis of H), 'coords': ...}.
    Chain C_p,j = wedge^p \otimes A_j-p... use internal degree j: basis e_I \otimes m, |m| = j - p... careful: exterior generators have degree 1 each.
    So C_{p, j} has basis e_I (x_{i1}\wedge...) \otimes monomials m of degree j - p.
    Differential d(e_I \otimes m) = sum_k (-1)^{..} e_{I\k} \otimes x_k m."""
    from collections import defaultdict
    H = {}
    # precompute quotient bases per degree
    Q = {}
    for d in range(deg_max + 1):
        ms, qb, M = mon_basis_A(I_gens, d)
        Q[d] = (ms, qb, M)
    for p in range(0, 5):
        for j in range(0, deg_max + 1):
            if j - p < 0: continue
            Ib = koszul_basis(p)
            ms, qb, M = Q[j - p]
            dim = len(Ib) * len(qb)
            if dim == 0:
                H[(p, j)] = {'dim': 0}
                continue
            # build differential matrices d_p: C_p -> C_{p-1} and d_{p+1}: C_{p+1} -> C_p
            def diff_matrix(pp, jj):
                # returns matrix (rows = dim C_{pp-1,jj}, cols = dim C_{pp,jj})
                if pp == 0: return None
                Ibb = koszul_basis(pp); Ibm = koszul_basis(pp - 1)
                ms0, qb0, M0 = Q[jj - pp]
                ms1, qb1, M1 = Q[jj - pp + 1]
                pos1 = {e: i for i, e in enumerate(qb1)}
                D = sp.zeros(len(Ibm) * len(qb1), len(Ibb) * len(qb0))
                for ci, I in enumerate(Ibb):
                    for cm, m in enumerate(qb0):
                        col = ci * len(qb0) + cm
                        for k, var in enumerate(I):
                            sign = (-1) ** k
                            J = tuple(v for t, v in enumerate(I) if t != k)
                            # x_var * m projected to A
                            ne = list(m); ne[var] += 1; ne = tuple(ne)
                            msJ, qbJ, MJ = Q[jj - pp + 1]
                            # express ne in quotient basis
                            coeffs = proj_to_quotient({ne: Fraction(1)}, msJ, MJ, qbJ)
                            ri = Ibm.index(J)
                            for rr, c in enumerate(coeffs):
                                row = ri * len(qbJ) + rr
                                D[row, col] += sign * c
                return D
            Dp = diff_matrix(p, j)
            Dp1 = diff_matrix(p + 1, j)
            ncols = dim
            ker = None
            if Dp is None:
                ker = sp.eye(ncols)
            else:
                ker = Dp.nullspace()
                ker = ker if ker else []
            if not ker or (isinstance(ker, list) and len(ker) == 0):
                H[(p, j)] = {'dim': 0}
                continue
            K = sp.Matrix.hstack(*ker) if isinstance(ker, list) else ker
            if Dp1 is None or Dp1.cols == 0:
                hdim = K.cols
                H[(p, j)] = {'dim': hdim, 'rep': K, 'Q': Q, 'j': j, 'p': p}
            else:
                # homology dim = dim ker - rank(Dp1 restricted)... rank of image inside ker = rank([K | Dp1]) - ... use quotient
                img = Dp1
                # image contained in ker? project: homology dim = ncols_ker - rank of map img -> ker-quotient
                # compute rank of augmented [K, img]: dim ker + dim img - dim(K+img); hdim = dim ker - dim(img ∩ ker)
                # dim(img ∩ ker): image of D restricted... since Dp*Dp1 = 0 in exact arithmetic (up to quotient projection), assume img ⊆ ker; verify
                KK = K
                aug = KK.row_join(img)
                hdim = KK.cols - (aug.rank() - KK.cols + (img.cols - aug.rank() + KK.cols) - 0)
                # simpler: hdim = rank([K img]) ... let r1 = rank(K), r2 = rank(img), r12 = rank([K img]); h = r1 - (r12 - r1... no.
                r1 = KK.rank(); r12 = aug.rank()
                # dim(K + img) = r12; dim img∩ker ≤ rank(img); assume img ⊆ ker so hdim = r1 - rank(img)
                hdim = r1 - img.rank()
                H[(p, j)] = {'dim': hdim, 'rep': K, 'img': img, 'Q': Q, 'j': j, 'p': p}
    return H, Q
