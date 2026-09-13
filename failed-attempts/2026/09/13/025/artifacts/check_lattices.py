"""Reproducible lattice/dimension check for lane-1522 (corrected).

Geometric inputs (cited, not proved here):
 - Gr(2,5) Schubert count gives H^4(Gr) rank 2; by Lefschetz + vanishing
   cycles a smooth GM fourfold X has H^4(X,Z) of rank 24 (2 from Gr plus
   rank-22 vanishing lattice). Hence even Betti sum = 1+1+24+1+1 = 28.
 - Db(X) = <Ku(X), O, U*, O(1), U*(1)>: exceptional block length 4, so
   K_top(Ku(X)) (Mukai lattice) has rank 24 = 28 - 4, i.e. U^4+E8(-1)^2.
 - Very general X in a divisor GM_d: algebraic Mukai rank 3 (lambda1,
   lambda2 + labeling), transcendental 21, unpolarized Ku period dim 17+2=19.
 - Debarre-Kuznetsov: D_d has dimension 19.

CORRECTED CONSEQUENCE: Ku-period dim (19) EQUALS D_d dim (19); the forgetful
map has no positive-dimensional fibers. The earlier claim (>= 2-dim fibers,
based on an erroneous H^4 rank of 22) is withdrawn. Cross-fiber
Hodge-isometric configurations with canonical-class-compatible isometries
are therefore NOT established by dimension count, blocking the EPW route.
"""
import json

# Corrected GM fourfold even Betti numbers: b0=b2=b6=b8=1, b4=24.
b = {0: 1, 2: 1, 4: 24, 6: 1, 8: 1}
rank_Db = sum(b.values())          # topological K rank of Db(X)
n_exc = 4                          # <O, U*, O(1), U*(1)> in Db(X)=<Ku, ...>
rank_Ku = rank_Db - n_exc          # Mukai lattice rank
assert rank_Db == 28, rank_Db
assert rank_Ku == 24, rank_Ku

# Divisor case: algebraic rank 3, transcendental 21, K3-type domain dim 19.
alg_rank = 3
tr_rank = rank_Ku - alg_rank
assert tr_rank == 21, tr_rank
ku_period_dim = tr_rank - 2
assert ku_period_dim == 19

# Classical GM period dimensions (Debarre-Kuznetsov).
dim_M, dim_D = 24, 20
dim_GMd, dim_Dd = 23, 19
assert dim_M - dim_D == 4
assert dim_GMd - dim_Dd == 4
forget_fiber = dim_Dd - ku_period_dim
assert forget_fiber == 0, forget_fiber  # NO positive-dimensional fibers

# Brauer-free discriminant witness: 8|d excludes (twisted) associated K3.
d = 24
assert d % 8 == 0
assert d % 8 not in (2, 4)

hh_identification_exists = True  # deformation invariance premise (cited)

out = {
    "rank_Db": rank_Db,
    "rank_Ku_Mukai": rank_Ku,
    "algebraic_rank_divisor": alg_rank,
    "transcendental_rank": tr_rank,
    "ku_unpolarized_period_dim": ku_period_dim,
    "GM_moduli_dim": dim_M,
    "GM_period_dim": dim_D,
    "GM_period_fiber_dim": dim_M - dim_D,
    "GMd_moduli_dim": dim_GMd,
    "GMd_period_dim": dim_Dd,
    "forgetful_fiber_dim": forget_fiber,
    "positive_fibers": False,
    "witness_discriminant": d,
    "d_mod_8": d % 8,
    "fails_twisted_assoc_K3": True,
    "HH_identification_exists": hh_identification_exists,
}
print(json.dumps(out, indent=2))
