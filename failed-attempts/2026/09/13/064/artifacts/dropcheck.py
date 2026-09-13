"""Pre-check: F6 gg-block has no sign-inconsistent drops for k in 17..20, both groups (needed by h7big Dprev)."""
import sys
sys.path.insert(0, '.')
import lane1610_totaro as T
for k in [17, 18, 19, 20]:
    T.len_zero[0] = k
    for gg in ['fix', 'full']:
        G = T.gens(k, gg)
        F = T.build_F(k, 6)
        F1 = T.build_F(k, 7)
        Fv, Fl, Fs = T.orbit_decomp(F, T.act_F, G)
        F1v, F1l, F1s = T.orbit_decomp(F1, T.act_F, G)
        keep = set(F1l.keys())
        missed = [tk for key in F for (c, tk) in T.D_F(key) if tk not in keep]
        print(f"k={k} {gg}: F6 keys={len(F)} missed D-targets={len(missed)}", flush=True)
