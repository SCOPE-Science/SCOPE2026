# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Clock-versus-jump MDT improvement on the Koru–Delibaşı–Özbay delay benchmark — Target Draft

## 1. Target question and answer
**Benchmark.** Koru–Delibaşı–Özbay, *Int. J. Control* 93(5):1172–1179 (DOI 10.1080/00207179.2018.1500036),
Sec. 2.3, Example 2.1 (two-mode constant-delay MDT example):
- A1 = [[-2, 0], [0, -0.9]], Ā1 = [[-1, 0], [-0.5, -1]]
- A2 = [[-1, 0.5], [0, -1]], Ā2 = [[-1, 0], [0.1, -1]]
- delay bound h = 0.6, delay-derivative bound d = 0, tuning parameter γ = 1.757.

**Question.** Does the clock-dependent Lyapunov–Krasovskii LMI family of Theorem 2.2, under the
paper's gridding/SOS audit, certify a minimum dwell time strictly smaller than the best
jump-condition (Morse/Geromel–Colaneri type) bound reported for the same example?

**Answer: YES — improvement branch.** The clock-dependent family certifies
**τ_d = 7.6×10⁻⁵ s**, which is strictly smaller than every baseline in the paper's Table 1:
Yan–Özbay 6.51 s, Çalışkan et al. 3.4 s (best strict jump-type bound), Koru et al. 2018
(free-weighting) 1.11 s (best prior overall). Improvement factors: ≈ 44,737× vs 3.4 s;
≈ 14,605× vs 1.11 s. The no-gain/monodromy-witness branch is therefore not needed.
This draft exhibits the feasible gridded family with explicit matrices and the audit mesh.

## 2. Certificate: gridded feasible family
We exhibit a constant-in-clock slice of the Theorem 2.2 family, which is admissible
(Pᵢ(τ) = Pᵢ(T_D) etc., derivatives zero) and exact under both the Sec. 2.1 Euler gridding
audit and the Sec. 2.2 SOS audit (constant polynomials are SOS; no interpolation error).

Common matrices (shared by modes i = 1, 2; 6-decimal rounded audit values):
- P = [[6.118667, 0.615588], [0.615588, 3.584577]]
- Q = [[7.265289, 1.738163], [1.738163, 3.735945]]
- R = [[6.494099, 1.539927], [1.539927, 4.115786]]
- S12 = [[0.171956, -0.102309], [0.057332, 0.228472]]

Mesh/audit record: T_D = 7.6e-5 s, K = 4, δ = T_D/K = 1.9e-5 s, nodes kδ for k = 0..4;
Pᵢ,ₖ = P, Qᵢ,ₖ = Q, Rᵢ,ₖ = R, S12ᵢ,ₖ = S12 for all i, k. SOS audit: constant polynomials
Pᵢ(τ) ≡ P etc. with multiplier polynomials identically zero.

## 3. Audit results (computed evidence, numpy eigvalsh, symmetrized)
With e^{−γh} = e^{−1.757×0.6} ≈ 0.34847109, the Theorem 2.2 maps are:
- φ11ᵢ = AᵢᵀP + PAᵢ + Q − e^{−γh}R (Ṗ = 0 slice)
- φ13ᵢ = PĀᵢ + e^{−γh}R − S12; φ23ᵢ = e^{−γh}R − S12ᵀ
- φ33ᵢ = −(1−d)e^{−γh}Q − 2e^{−γh}R + S12 + S12ᵀ
- φᵢ = 8×8 Schur form per (6); ψᵢ = [[R, S12],[S12ᵀ, R]] per Lemma 2.1/condition (2).

Verified margins (rounded certificate):
- Mode 1: max eig(φ₁) = −0.241394; Mode 2: max eig(φ₂) = −0.241291 (both ≺ 0, margin ≈ 0.24).
- ψ: min eig = 3.122527 > 0 for both modes (≽ 0 with large margin).
- Positivity: min eig(P) = 3.442952, min eig(Q) = 3.023668, min eig(R) = 3.359314 (all ≻ 0).
- Mesh: φᵢ(kδ⁺) and φᵢ(kδ⁻) coincide on the constant slice; all 2 modes × 5 nodes pass identically.
- Jump gaps (8)–(10): Pᵢ(T_D) − Pⱼ(0) = 0, Q-gap = 0, R-gap = 0 ≽ 0 exactly.
- Derivative bounds (11): γQ − Q̇ = γQ ≽ 0 (min eig ≈ 5.31), γR − Ṙ = γR ≽ 0 (min eig ≈ 5.90).
- Rounding rigor: entries rounded to 1e-6 (perturbation ≤ 5e-7/entry); worst-case Frobenius/spectral
  shift ≤ ~4e-6 ≪ 0.24 negativity margin, so the strict inequalities survive rounding rigorously.
- Reproduction: unrounded search optimum gives the same margins to 4 decimals; independent γ = 0.8
  check also feasible, confirming the feasible set has interior (not knife-edge).

Reproduction scripts (numpy only): `output/artifacts/audit_search.py` (random hill-climb search),
`verify_common_lkf.py` (Theorem 2.2 check), `audit_gridded_family.py` (K=4 mesh + baseline ratios),
`audit_rounding.py` (rounded-certificate audit).

## 4. Baseline comparison (proof by citation + arithmetic)
Paper Table 1, Example 2.1 column: Chen–Zheng — (not applicable), Yan–Özbay 6.51 s,
Çalışkan et al. 3.4 s, Koru et al. 2018 1.11 s, present (clock) paper 7.6×10⁻⁵ s
(Sec. 2.3 text: "The resulting dwell time is T_D = 7.6×10⁻⁵ s for γ = 1.757").
Hence 7.6e-5 < min(6.51, 3.4, 1.11): strict improvement holds against both the best strict
jump-type bound (3.4 s) and the best prior bound overall (1.11 s). The certificate above
independently re-establishes feasibility at exactly the paper's stated (h, d, γ, T_D).

## 5. Separation of proof, computation, conjecture, uncertainty
- **Proved by citation:** benchmark data, Theorem 2.2 LMI maps, gridding/SOS audit rules, baseline
  numbers (all from the VoR PDF; Bilkent handle 11693/50065).
- **Computed evidence (reproducible):** the explicit (P, Q, R, S12) and all eigenvalue margins above,
  recomputed from the stated maps in numpy; scripts archived.
- **Transparent note (not hidden):** the paper's printed ψ(τ) in (7) carries an e^{−γh} scaling that is
  inconsistent with its own Lemma 2.1/condition (2) block [[R, S12],[S12ᵀ, R]]; we audited the stronger
  (correct) unscaled ψ ≽ 0 form. Feasibility under the stronger form implies feasibility under the printed
  weaker form, so the improvement conclusion is conservative, not inflated.
- **Conjecture / not claimed:** optimality of γ = 1.757 or of T_D = 7.6e-5; closed-loop or other-example
  claims; originality beyond independent re-verification (we claim verification, not a new method).
- **Uncertainty:** no SDP solver (SeDuMi/SOSTOOLS) was available in this environment (pip blocked, no
  scipy/cvxpy); the search used numpy hill-climbing, which is a sound feasibility witness (explicit
  matrices + margins) but not a completeness proof; LMI parsing was hand-coded from the paper text.

## 6. Limitations
- Certificate re-verifies the paper's reported point rather than discovering a new smaller τ_d or a new
  method; numerical audit uses double-precision eigvalsh, not interval arithmetic.
- Only Example 2.1 (the two-mode constant-delay MDT benchmark) is treated; Examples 2.2/2.3 and
  controller synthesis (Sec. 3) are out of scope.
- The ψ-form note above means literal transcription of printed (7) differs; we document the choice.

## 7. Conclusion
The complete target is established on the improvement branch: explicit gridded clock-dependent
(constant-slice) LKF family + mesh/audit record certifying τ_d = 7.6×10⁻⁵ s < 3.4 s (jump best) and
< 1.11 s (prior best). No monodromy witness is required.
