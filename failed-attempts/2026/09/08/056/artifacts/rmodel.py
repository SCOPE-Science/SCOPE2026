"""Koszul–Taylor dga model R(K) in squarefree multidegrees + Massey engine (exact, sympy QQ).
Basis of R^{-i,2J}: u_S v_{J\\S}, S subset J, F=J\\S a face of K (faces: emptyset, verts, edges, tris).
d(u_S v_F) = sum_{i in S, F+{i} face} sgn(i,S) u_{S\\{i}} v_{F+{i}}, sgn=(-1)^{#{s in S: s<i}}.
product (disjoint J,L only): (u_S v_F)(u_T v_G) = sgn(S,T) u_{S|T} v_{F|G} if (F|G face) else 0,
  sgn(S,T)=(-1)^{#{s in S, t in T: s>t}} (move T past S: u_S u_T = sgn u_{S|T}). v-part commutative.
"""
import itertools, sympy


def faces_of(emask, tmask):
    F = {0}
    for i in range(6):
        F.add(1 << i)
    for e, (a, b) in enumerate([(i, j) for i in range(6) for j in range(i + 1, 6)]):
        if (emask >> e) & 1:
            F.add((1 << a) | (1 << b))
    for t, (a, b, c) in enumerate([t for t in itertools.combinations(range(6), 3)]):
        if (tmask >> t) & 1:
            F.add((1 << a) | (1 << b) | (1 << c))
    return F


def basis_J(J, FACES):
    out = []  # (S mask, F mask)
    s = J
    while True:
        F = J ^ s  # J\\S since S subset J
        if F in FACES:
            out.append((s, F))
        if s == 0:
            break
        s = (s - 1) & J
    return out


def sgn_remove(i, S):
    return -1 if bin(S & ((1 << i) - 1)).count("1") % 2 else 1


def sgn_union(S, T):
    n = 0
    t = T
    while t:
        lsb = t & (-t)
        i = lsb.bit_length() - 1
        n += bin(S & ~((1 << (i + 1)) - 1)).count("1")
        t ^= lsb
    return -1 if n % 2 else 1


def diff_mat(J, B, FACES, B2=None):
    """Matrix of d: R(J)[B] -> R(J)[B2] (B2=basis in degree+1... here full: return dict). Returns M with M[r,c]."""
    if B2 is None:
        B2 = B
    idx = {b: k for k, b in enumerate(B2)}
    M = sympy.zeros(len(B2), len(B))
    for c, (S, F) in enumerate(B):
        s = S
        while s:
            lsb = s & (-s)
            i = lsb.bit_length() - 1
            s ^= lsb
            if (F >> i) & 1:
                continue
            FF = F | (1 << i)
            if FF not in FACES:
                continue
            r = idx.get((S ^ (1 << i), FF))
            if r is not None:
                M[r, c] += sgn_remove(i, S)
    return M


def deg_of(S, F):
    return bin(S).count("1") + 2 * bin(F).count("1")


def cohomology_dims(emask, tmask=0):
    FACES = faces_of(emask, tmask)
    dims = {}
    for J in range(64):
        B = basis_J(J, FACES)
        bydeg = {}
        for b in B:
            bydeg.setdefault(deg_of(*b), []).append(b)
        for d, Bd in bydeg.items():
            BdN = bydeg.get(d + 1, [])
            D_out = diff_mat(J, Bd, FACES, BdN) if BdN else sympy.zeros(0, len(Bd))
            BdP = bydeg.get(d - 1, [])
            D_in = diff_mat(J, BdP, FACES, Bd) if BdP else sympy.zeros(len(Bd), 0)
            ker = len(Bd) - D_out.rank()
            im = D_in.rank()
            if ker - im:
                dims[(J, d)] = ker - im
    return dims


def total_betti(emask, tmask=0):
    return sum(cohomology_dims(emask, tmask).values(), 1)  # +1 for J=0 class
