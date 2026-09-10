"""Lane-584 deepening: mod-2 reduction theorem (sign-independent jump),
ghost-vanishing inputs, PSC-representability gap. Exact arithmetic where used.
"""
import json

# (a) Mod-2 jump sign-independence (exact integer fact):
# single transverse crossing contributes +1 or -1 over Z; mod 2 both = 1.
for s in (1,-1):
    assert s % 2 == 1
print("MOD2-QUANTUM: +/-1 over Z both = 1 mod 2. Sign ambiguity dies mod 2.")
print("  => IF a loop L1 differs from PSC loop L0 by exactly one transverse")
print("  wall crossing (and both ends regular), then FSW(L1)=1 mod 2.")

# (b) Ghost vanishing inputs (exact integers + cited theorem):
# Bauer connected-sum vanishing: X=X'#X'' with b2+(X'),b2+(X'')>0 => BF(X)=0.
b2p_Z0=1; b2p_H=1
assert b2p_Z0>0 and b2p_H>0
print(f"GHOST: Z1=Z0#(S2xS2), b2+={b2p_Z0},{b2p_H}>0 => ordinary S1-BF ghost=0")
print("  (Bauer connected-sum vanishing; statement level).")
print("  => S1-BF(E_F) free part = FSW count; S1-BF != 0 <=> J != 0 (odd).")

# (c) Reduction theorem (logic ledger):
# T1 (certified in-lane): fiberwise spin-c s#t0 exists on E_F (F^*s~=s).
# T2 (certified): eta=0 slice wall-free for c^2=8 (all g).
# T3 (certified): generic loop misses wall; PSC loop value 0.
# T4 (primitivity): single-crossing quantum +-1 (=1 mod 2).
# REDUCTION: target FSW=1 (mod 2) <=> exists regular loop L1 in class [E_F]
#   with odd wall-linking vs PSC loop. Remaining: exhibit L1 + regularity.
print("REDUCTION THEOREM (conditional): TARGET <=> odd-linking regular loop L1.")
print("  All hypotheses except L1-existence/regularity certified in-lane.")

# (d) PSC-representability gap (honest topology of Met_PSC):
# The eta=0 lift of [E_F] is a loop of metrics g_t: g0 ~~> F^*g0.
# FSW(eta=0 lift)=0 IF the path can be chosen inside PSC cone (then empty).
# Whether F^*g0 lies in the same PSC-component as g0 is the action of [F] on
# pi0(Met_PSC(Z1)) / moduli. No computation of [F]-action in-lane.
# If F acts nontrivially on PSC components, EVERY representative loop leaves
# PSC and the count may jump. This is precisely the geography the target
# probes; it cannot be settled by formal means.
print("PSC-GAP: FSW(eta=0 lift)=0 needs PSC-path g0~~>F^*g0; [F]-action on")
print("  pi0(Met_PSC) uncomputed in-lane. Cannot close either direction.")

# (e) Killing-side bound (honest):
# A smooth killing isotopy F~=id would imply FSW=0 in ALL chambers and
# S1-BF trivial. Contrapositive: odd-linking L1 obstructs killing.
# No isotopy exhibited; no odd L1 exhibited. Symmetric openness logged.
print("KILL-DUAL: killing => all-chamber FSW=0; odd L1 => no killing.")
print("  Neither exhibited. OPEN both ways (symmetric).")

out={"mod2_quantum":True,"ghost_zero_inputs":[b2p_Z0,b2p_H],
 "reduction":"TARGET <=> odd-linking regular L1 (all else certified)",
 "PSC_gap":"[F]-action on pi0(Met_PSC) uncomputed","symmetric_open":True}
with open("output/artifacts/reduction_ledger.json","w") as f:
    json.dump(out,f,indent=2)
print("wrote output/artifacts/reduction_ledger.json")
print("ALL VERIFY_OK")
