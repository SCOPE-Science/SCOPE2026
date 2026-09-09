# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Conditional Mattila–Wolff reduction for AD-regular Falconer in R³
## An explicit, fully proved energy-to-positivity fragment with falsification audit of the 1/20 dyadic-decay tiers

## 1. What is proved (and what is not)

**Proved (Theorem R, self-contained, §2):** an explicit conditional reduction.
Let `E ⊂ B(0,1) ⊂ R³` be compact Ahlfors–David `s`-regular with constant
`C_AD ≤ 10`, `s = 69/40`. Let `μ = H^s|_E / H^s(E)` and

```
S(r) = ∫_{S²} |μ̂(rω)|² dσ(ω),   M_T = ∫_T^{2T} S(r)² r² dr   (dσ normalized).
```

**Assume** `M_T ≤ 10·T^{−1/20}` for every dyadic `T = 2^j ≥ 1`.
**Then** `|Δ(E)| ≥ 2.0×10^{−6}` (explicitly `≥ 0.3758/(64π²I) ≈ 2.02×10^{−6}`
with `I = 1/3 + 10/(1−2^{−1/20}) ≈ 293.90`).
Constants proved: Frostman sup-ball bound `A′ = C_AD² = 100` exactly;
tail `10/(1−2^{−1/20}) ∈ (293, 294)`; `‖w‖²_{L²[0.04,2]} ≤ 185645`;
distance mass on `[0.04, 2]` at least `0.6122`.

**Not proved:** the full target (positivity for all AD `s`-regular `E` at
`s > 69/40` via decoupling → Orponen projection → energy) and the preset
six-block decay `D(T,μ) ≤ 10·T^{−1/20}` (see §4 for why its numerology cannot
be reached from any cited technology — an obstruction diagnosis, not a
disproof). No unconditional Falconer threshold is claimed.

## 2. Proof of the conditional reduction (Theorem R)

*Fourier normalization:* `μ̂(ξ) = ∫ e^{−2πix·ξ} dμ`, `f ∈ C_c^∞`,
`F(z) = f(|z|)` radial, `S²` carrying normalized `dσ` (total mass 1) and
`S_full = 4πS` the unnormalized average. Continuous compactly supported
functions extend by density; all swaps below are Fubini on compact sets.

**Step 1 — Frostman data (exact).**
For `x ∈ E`, `E ⊂ B(x, 2)`, so `H^s(E) ≥ C_AD^{−1}2^s ≥ 0.3306`.
For the normalized probability `μ`, cover `B(x,r)` by `B(y,2r)`
(`y ∈ B(x,r) ∩ E`, trivial if empty) to get the uniform bound

```
sup_x μ(B(x,r)) ≤ 100·r^s,   i.e. A′ = C_AD² = 100 exactly.
```

**Step 2 — radial pushforward density.**
Angular integration gives `F̂(ξ) = (2/r)∫₀^∞ f(t)t sin(2πr t)dt` with
`r = |ξ|`. Hence with `S_full = 4πS` and `g(r) = r·S_full(r) ≥ 0`,

```
ν(f) := ∫∫ f(|x−y|) dμdμ = ∫₀^∞ F̂(r) S_full(r) r² dr
     = ∫₀^∞ w(t) f(t) dt,   w(t) = 2t·∫₀^∞ g(r) sin(2πrt) dr.
```

**Step 3 — sine-isometry L² bound.**
Odd extension plus unitarity of the Fourier transform gives
`∫₀^∞|(Sg)(t)|²dt = (1/4)∫₀^∞|g|²dr` for `(Sg)(t)=∫₀^∞g(r)sin(2πrt)dr`
(closed-form check: `g = re^{−r}` gives `‖g‖² = 1/4`, `∫(Sg)² = 1/16`).
Since `w(t) = 2t·(Sg)(t)`,

```
∫₀^∞ w²t^{−2} dt = ∫₀^∞ r²S_full² dr,
‖w‖²_{L²[δ,2]} ≤ 4∫₀^∞ r²S_full² dr = 64π²I,  I = ∫₀^∞ S²r²dr.
```

**Step 4 — conditional tail.** `S ≤ 1` on `[0,1]` (probability measure) gives
`∫₀¹ S²r² ≤ 1/3`; the hypothesis gives
`tail = Σ_{j≥0} 10·2^{−j/20} = 10/(1−2^{−1/20}) ∈ (293, 294)`.
So `I ≤ 293.91` and `‖w‖² ≤ 64π²I ≤ 185645`.

**Step 5 — mass and Cauchy–Schwarz.**
`ν([0,δ]) ≤ 100·δ^s`; `δ = 0.04` gives `≤ 0.3878`, so mass on `[δ,2]` is at
least `0.6122`. Hence

```
|Δ(E) ∩ [0.04,2]| ≥ mass²/‖w‖²₂ ≥ 0.3758/185645 ≥ 2.019×10^{−6} > 0. ∎
```

## 3. Numerology that locates the result (computed, replayable)

- Threshold identities: `69/40 = 7/4 − 1/40 = 1.725`; gap `3/40 = 0.075`
  below the general R³ best `9/5 = 1.8` (Du–Guth–Ou–Wang–Wilson–Zhang,
  arXiv:1802.10186, Thm 1.2); gain `1/40` over the `7/4` baseline, doubled to
  `1/20` by the `S²` squaring — `artifacts/check_numerology.py`.
- The `M_T ≤ 10T^{−1/20}` hypothesis is equivalent to spherical-average decay
  `β ≥ 61/40 = 1.525`; the bare-`2α/3` input breaks even only at `s = 9/4`;
  at `s = 69/40` the dividend owed by AD/decoupling/Orponen over `2α/3` is
  exactly `3/8 = 0.375` — `artifacts/required_beta.py`.
- Classical Mattila route (Thm 2.2 of the cited paper: hypothesis
  `S(R) ≲ R^{α−d}` plus finite `α`-energy) needs only `β ≥ 51/40 = 1.275` at
  the target, i.e. dividend `1/8` — one third of the strong-route burden;
  the Mattila-method cap `5/3 ≈ 1.667` (Remark 2.4) lies below `69/40`, so the
  target sits in the method's reachable zone —
  `artifacts/mattila_threshold_routes.py`.

## 4. Obstruction diagnosis (why the 1/20 tiers are unreachable from cited inputs)

Isolating exactly what the two decay tiers demand, with the cited
`β₃` bounds (`Du et al Thm 1.7`: `β₃(α) ≥ 2α/3` for `α ≤ 2`;
Erdoğan: `β₃(7/4) = 9/8`):

- `M_T ≤ 10T^{−1/20}` needs `β ≥ 61/40`; over `2α/3` at `69/40` that is the
  `3/8` dividend of §3.
- The exact fallback normalization `D(T,μ) = T³∫_T^{2T} S²` needs
  `β = 81/40 = 2.025`, i.e. dividend `103/120 ≈ 0.858` over `7/6` and
  `9/10 = 0.9` over `9/8`; the attainable envelope `T^{5/3}` exceeds the
  claimed `≈ 7–8.4` bounds by `38×` at `T = 32` up to `≈ 14700×` at `T = 1024`
  — `artifacts/fallback_falsification.py` (ALL_CHECKS_PASS).
- Decoupling `R^ε` losses are break-even at `ε = 1/20` and smaller above it,
  so the loss alone never supplies the needed decay — `artifacts/check_numerology.py` (N4).
- Auxiliary exact-Fourier planar-model probes (Cantor-dust × interval
  approximants) were run as target-directed diagnostics only: the single
  atomic-discretization violator was not Frostman-certified, and the exact
  continuous-Fourier models decayed rather than saturated. Those exploratory
  scripts are not retained as verification artifacts.
  **No certified counterexample to the fallback or the target is claimed.**

## 5. How to replay

```
python3 output/artifacts/check_numerology.py
python3 output/artifacts/mattila_constants.py
python3 output/artifacts/required_beta.py
python3 output/artifacts/mattila_threshold_routes.py
python3 output/artifacts/fallback_falsification.py
```

All five print `ALL_CHECKS_PASS` with exit 0 (stdlib only).

## 6. References

- Du–Guth–Ou–Wang–Wilson–Zhang, *Weighted restriction estimates and
  application to Falconer distance set problem*, arXiv:1802.10186 (Thms 1.2,
  1.4, 1.7, 1.8; §2 Mattila approach, Prop 2.3, Remarks 2.4–2.5).
- Orponen, *On the projections of Ahlfors regular sets in the plane*,
  arXiv:2410.06872 (planar δ-discretised input; no R³ distance numerology).
- Orponen–Ren, *On the projections of almost Ahlfors regular sets*,
  arXiv:2411.04528 (bounded- vs almost-regularity distinction).
- Orponen–Shmerkin–Wang, arXiv:2209.00348 (radial projections/Beck).
- Borges et al., arXiv:2607.00153; Fraser–Pham, arXiv:2604.19486
  (adjacent programs; different hypotheses/functionals).
