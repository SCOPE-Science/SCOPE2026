"""Exact twisted Betti t_7(k) for large k using block-disjointness (audited):
D_7: F7(g only) -> F8^x4 (x-monoids E=4); J_8 (x*Arn) lives in gg*x block,
so rank([D|J8]) = rank(D)+rank(J8) and J8 cancels from h. Only F6,F7,F8^x4 used.
Single-G/x orbits are always sign-consistent (m even => all +1), so no drops
at d=7; F6 gg-block drops checked separately (lane1610_dropcheck).

Usage: python3 lane1610_h7big.py K [K ...]
"""
import sys
sys.path.insert(0, '.')
import lane1610_totaro as T
from fractions import Fraction
import time

def twisted7(k):
    t0 = time.time()
    T.len_zero[0] = k
    out = {}
    for gg in ['fix', 'full']:
        G = T.gens(k, gg)
        F = T.build_F(k, 7)                      # g-keys, E=2 only
        FX8 = [('x', e) for e in T.monomials(k, 4)]  # D-target block only
        Fm = T.build_F(k, 6)                     # x E=3 + gg E=0
        R = T.build_R1(k, 7)                     # -> F7
        Rm = T.build_R1(k, 6) + T.build_Arn(k, 6)  # -> F6 (R1 empty, Arn triples)
        Rp_unused = None
        Fv, Fl, Fs = T.orbit_decomp(F, T.act_F, G)
        Xv, Xl, Xs = T.orbit_decomp(FX8, T.act_F, G)
        Fmv, Fml, Fms = T.orbit_decomp(Fm, T.act_F, G)
        Rv, Rl, Rs = T.orbit_decomp(R, T.act_R, G)
        Rmv, Rml, Rms = T.orbit_decomp(Rm, T.act_R, G)
        b = len(Fv)
        # D_7 restricted to x-block rows (exact: all D targets are x-type)
        D = T.proj_matrix_D(Fv, Fl, Xl, Xs, T.D_F)
        Dprev = T.proj_matrix_D(Fmv, Fml, Fl, Fs, T.D_F)
        J = T.proj_matrix_J(Rv, Fl, Fs, T.relvec)
        Jm = T.proj_matrix_J(Rmv, Fml, Fms, T.relvec)
        rD = T.rank_frac(D)
        rDJ = T.aug_rank(Dprev, J)
        h = b - rD - rDJ
        out[gg] = (h, b, rD, rDJ, len(F), len(Fm))
        print(f"  k={k} {gg}: h={h} b={b} rankD={rD} rank[Dprev|J7]={rDJ} |F7|={len(F)} |F6|={len(Fm)} ({time.time()-t0:.0f}s)", flush=True)
    t = out['fix'][0] - out['full'][0]
    print(f"k={k}: t_7 = {t} (fix={out['fix'][0]}, full={out['full'][0]})", flush=True)
    return t

if __name__ == '__main__':
    for k in [int(x) for x in sys.argv[1:]]:
        twisted7(k)
