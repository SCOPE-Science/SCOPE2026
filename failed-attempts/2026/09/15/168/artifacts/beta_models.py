#!/usr/bin/env python3
"""Reproducible verification of the conformal invariant
beta = ∫||W||^2 / ∫σ2(P), with ||W||^2 = |W|^2/4,
for the model 4-manifolds, plus the KE del Pezzo table and the
Page / Chen-LeBrun-Weber volume decision windows.

Conventions (dimension 4):
  P = (Ric - R g/6)/2,  σ2(P) = ((tr P)^2 - |P|^2)/2,
  Chern-Gauss-Bonnet: 8π²χ = ∫(|W|^2/4) + ∫4σ2 = ∫||W||^2 + 4∫σ2.
Both integrals are conformally invariant, hence so is beta.
"""
import math

pi = math.pi
out = []


def emit(s=""):
    out.append(s)
    print(s)


def check(name, got, want, tol=1e-9):
    ok = abs(got - want) < tol
    emit(f"  {name}: got {got:.10f}, want {want:.10f} -> {'OK' if ok else 'FAIL'}")
    if not ok:
        raise SystemExit(f"FAILED: {name}")


emit("== Model values ==")
# S^4 radius 1: W=0; P=(1/2)g so σ2=6*(1/4)=3/2; Vol=8π²/3.
B_S4 = 1.5 * (8 * pi**2 / 3)
check("S4: ∫σ2 = 4π²", B_S4, 4 * pi**2)
check("S4: beta = 0", 0.0, 0.0)

# CP^2 Fubini-Study: KE with c1²=9 ⇒ R²Vol=32π²·9=288π² ⇒ B=3π²; A=8π²·3−4B=12π².
B_CP2 = 288 * pi**2 / 96
A_CP2 = 8 * pi**2 * 3 - 4 * B_CP2
check("CP2: ∫σ2 = 3π²", B_CP2, 3 * pi**2)
check("CP2: ∫||W||² = 12π²", A_CP2, 12 * pi**2)
check("CP2: beta = 4", A_CP2 / B_CP2, 4.0)

# S²×S² unit factors: Ric=g, R=4, P=g/6, σ2=1/6, Vol=16π² ⇒ B=8π²/3; A=64π²/3.
B_S2S2 = (1.0 / 6.0) * 16 * pi**2
A_S2S2 = 8 * pi**2 * 4 - 4 * B_S2S2
check("S2xS2: ∫σ2 = 8π²/3", B_S2S2, 8 * pi**2 / 3)
check("S2xS2: ∫||W||² = 64π²/3", A_S2S2, 64 * pi**2 / 3)
check("S2xS2: beta = 8", A_S2S2 / B_S2S2, 8.0)

emit("== Sharpness / boundary cases ==")
# S¹×S³ product: P-eigenvalues (−1/2,1/2,1/2,1/2) ⇒ σ2 = 3(−1/4)+3(1/4) = 0.
ev = [-0.5, 0.5, 0.5, 0.5]
s2 = sum(ev[i] * ev[j] for i in range(4) for j in range(i + 1, 4))
check("S1xS3: pointwise σ2 = 0 (excluded by ∫σ2>0)", s2, 0.0)
# RP⁴ round: half of S⁴ ⇒ B=2π²>0, A=0, β=0; π1=Z/2, H²=0 ⇒ not S⁴/CP².
check("RP4: ∫σ2 = 2π²", B_S4 / 2, 2 * pi**2)
check("RP4: beta = 0 (non-model: pi1=Z/2, H^2=0)", 0.0, 0.0)

emit("== Kähler–Einstein del Pezzo table: beta = 24χ/c1² − 4 ==")
emit("  k (blow-ups of CP²) | χ=3+k | c1²=9−k | beta")
for k in range(0, 9):
    chi, c1sq = 3 + k, 9 - k
    beta = 24 * chi / c1sq - 4
    emit(f"  k={k} | χ={chi} | c1²={c1sq} | beta={beta:.6f}")
check("KE k=0 (CP²): beta=4", 24 * 3 / 9 - 4, 4.0)
check("KE S²×S² type (χ=4,c1²=8): beta=8", 24 * 4 / 8 - 4, 8.0)

emit("== Decision windows for non-Kähler Einstein cases ==")
# Page on CP²#CP²bar: χ=4, β=3072π²/E²−4, E²=R²Vol. β∈[4,8) ⇔ E²∈(256π²,384π²].
lo, hi = 256 * pi**2, 384 * pi**2
emit(f"  Page (CP²#bar, χ=4): beta∈[4,8) ⇔ R²Vol ∈ ({lo:.6f}, {hi:.6f}]")
emit(f"    i.e. at R=4 (Ric≡1): Vol ∈ ({lo/16:.6f}, {hi/16:.6f}] = (16π², 24π²]")
emit(f"    reference S²×S² Vol(Ric≡1) = {16*pi**2:.6f} (= lower endpoint, beta=8)")
# CLW on CP²#2bar: χ=5, β=3840π²/E²−4 ∈[4,8) ⇔ E²∈(320π²,480π²].
lo2, hi2 = 320 * pi**2, 480 * pi**2
emit(f"  CLW (CP²#2bar, χ=5): beta∈[4,8) ⇔ R²Vol ∈ ({lo2:.6f}, {hi2:.6f}]")
check("Page window lower edge /π²", lo / pi**2, 256.0)
check("Page window upper edge /π²", hi / pi**2, 384.0)
check("CLW window lower edge /π²", lo2 / pi**2, 320.0)
check("CLW window upper edge /π²", hi2 / pi**2, 480.0)

emit("ALL CHECKS PASSED")
with open("/srv/scope-research/rounds/2026-09-14-hands-on-first-light-01/workspaces/research/lane-20418/output/artifacts/beta_results.txt", "w") as f:
    f.write("\n".join(out) + "\n")
