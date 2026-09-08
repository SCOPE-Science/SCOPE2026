"""Cup products + Massey defining-system solver in R(K). Extends rmodel."""
import sys, itertools, sympy
sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-162/output/artifacts")
from rmodel import faces_of, basis_J, sgn_remove, sgn_union, deg_of, diff_mat


def prod_on_basis(b1, b2, FACES, Bidx):
    (S, F), (T, Gc) = b1, b2
    if (S | T) != (S ^ T):
        return {}
    if (F | Gc) != (F ^ Gc):
        return {}
    H = F | Gc
    if H not in FACES:
        return {}
    b = ((S | T), H)
    if b not in Bidx:
        return {}
    return {b: sgn_union(S, T)}


def to_vec(form, Bidx):
    v = [0] * len(Bidx)
    for b, c in form.items():
        v[Bidx[b]] = c
    return sympy.Matrix(v)


def from_vec(v, B):
    return {b: v[i] for i, b in enumerate(B) if v[i] != 0}


def ker_basis(M):
    return M.nullspace()


def is_coboundary(vec, D_in):
    # vec in image(D_in)?
    if D_in.cols == 0:
        return vec.is_zero_matrix
    aug = D_in.row_join(vec)
    return aug.rank() == D_in.rank()


def solve_preimage(vec, D_in):
    # find x with D_in x = vec (assumes solvable); returns dict-free vector
    if D_in.cols == 0:
        return None
    x, params = D_in.gauss_jordan_solve(vec)
    return x


def cup_classes(emask, tmask, J1, d1, J2, d2, FACES=None, cache={}):
    FACES = FACES or faces_of(emask, tmask)
    key = (emask, tmask)
    if key not in cache:
        BB = {}
        for J in range(64):
            BB[J] = basis_J(J, FACES)
        cache[key] = (FACES, BB)
    FACES, BB = cache[key]
    return FACES, BB
