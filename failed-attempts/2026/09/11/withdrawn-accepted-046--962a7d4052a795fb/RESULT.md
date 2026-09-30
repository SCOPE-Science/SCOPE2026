# Impossibility of a uniform +0.05 floor for the one-sided linearized monotonicity test

## Context
Full-boundary Dirichlet-to-Neumann (DtN) data are an idealization; practical EIT
often accesses only part of the boundary. The admitted target asked whether, with
accessible boundary Γ⁺ = {x ∈ ∂B₁ : x₂ ≥ 0}, inclusion D* the axis-aligned square
|x₁| ≤ 0.15, x₂ ∈ [0.30, 0.60] (center (0,0.45), side 0.3), conductivity
σ* = 1 + 3·1_{D*}, and linear Carleman weight φ(x) = x₂ with M* ≤ 4.0, the
restricted linearized monotonicity operators satisfy simultaneously

  min spec(Λ^{Γ⁺}(σ*) − Λ^{Γ⁺}₀ − 2·DΛ^{Γ⁺}₀(1_{C_in})) ≤ −0.05 (accept C_in),
  min spec(Λ^{Γ⁺}(σ*) − Λ^{Γ⁺}₀ − 2·DΛ^{Γ⁺}₀(1_{C_out})) ≥ +0.05 (reject C_out),

where C_in ⊂ D* (side 0.15) and C_out is the mirror |x₁| ≤ 0.15,
x₂ ∈ [−0.60,−0.30]. C_out is the hardest false-positive control.

## Definitions
- Ω = B₁ ⊂ ℝ²; H = H^{1/2}₀(Γ⁺) = {f ∈ H^{1/2}(∂Ω) : supp f ⊂ Γ⁺̅}, infinite-dimensional.
- E: H → H^{1/2}(∂Ω) extension by zero; R restriction to H*.
- Λ(σ*), Λ₀ full-boundary DtN maps; DΛ₀(1_C) Fréchet derivative at background with
  form ⟨DΛ₀(1_C)f,g⟩ = ∫_C ∇u⁰_f·∇u⁰_g (sign convention irrelevant).
- L_out = R(Λ(σ*)−Λ₀)E − 2R·DΛ₀(1_{C_out})E : H → H*.
- For any Riesz isomorphism J: H → H*, K_out = J^{−1}L_out bounded self-adjoint on H;
  "min spec ≥ +0.05" means inf σ(K_out) ≥ 0.05 under any equivalent J.

## Result
inf σ(K_out) ≤ 0. Hence the target's second conjunct (uniform floor ≥ +0.05) is
impossible for every Carleman weight φ and every constant M*; the full target
conjunction (both gaps plus acceptance/rejection) is rigorously false. No claim is
made about the C_in conjunct alone (a compact operator can have finitely many
eigenvalues below −0.05).

## Proof / evidence
**Lemma A (background derivative compact).** T_C: f ↦ ∇u⁰_{Ef}|_C : H → L²(C)² is
compact for C ⋐ Ω: f ↦ u⁰_{Ef} ∈ H¹(Ω) bounded; harmonic interior H² regularity
‖u‖_{H²(Ω')} ≤ C‖u‖_{H¹(Ω)} (Evans §6.3; McLean Thm 4.10) makes
f ↦ ∇u⁰|_{Ω'} bounded H → H¹(Ω')²; Rellich H¹(Ω') ⋐ L²(C) gives compactness.
P_C = R·DΛ₀(1_C)E = T_C*T_C (up to bounded maps) is compact.

**Lemma B (difference compact despite discontinuity).** A = R(Λ(σ*)−Λ₀)E compact.
Alessandrini identity: ⟨(Λ(σ*)−Λ₀)Ef,Eg⟩ = ∫_Ω(σ*∇u*_f − ∇u⁰_f)·∇u⁰_g.
Write σ*∇u*_f − ∇u⁰_f = 3·1_{D*}∇u*_f + ∇w_f, w_f = u*_f − u⁰_f ∈ H¹₀(Ω);
∫_Ω∇w_f·∇u⁰_g = 0 (u⁰_g harmonic), leaving ⟨Af,g⟩ = ∫_{D*}3∇u*_f·∇u⁰_g.
Split ∇u*_f = ∇u⁰_f + ∇w_f on D*: S₀: f ↦ ∇u⁰_f|_{D*} compact by Lemma A;
G = 3∇u⁰_f1_{D*} compact H → L²(Ω); corrector div(σ*∇w_f) = −div G weakly with
Lax–Milgram bound G ↦ w_f L² → H¹₀ (no H² across square interface used), so
S₁: f ↦ ∇w_f|_{D*} compact. A = T*M(S₀+S₁), T compact by Lemma A, M bounded
multiplication by 3. Restriction preserves compactness.

**Spectral conclusion.** L_out = A − 2P_{C_out} compact H → H*; K_out compact
self-adjoint on infinite-dimensional H. By Riesz–Schauder (Reed–Simon I,
Thm VI.16), σ(K_out) = {0} ∪ {λ_j}, λ_j → 0, 0 ∈ σ(K_out); for self-adjoint K,
inf σ(K) = inf_{‖f‖=1}⟨Kf,f⟩ ≤ 0. Uses only C_out,D* ⋐ Ω (corner norm
√(0.15²+0.6²) ≈ 0.619 < 1); φ, M* play no role.

**Quantitative corroboration (non-rigorous, replayable).** Sine modes on Γ⁺,
harmonic extension by Fourier series: C_out Rayleigh quotients 3.57e-03 (m=1)
decaying to 5.45e-07 (m=24); finite-section generalized-eigenvalue minima
2.0e-07 (N=4) collapsing to ~0 (N=12), maxima < 0.05 — finite-section shadow of
0 ∈ σ. Replay: `python3 output/artifacts/weyl_quotients.py`.

## Limitations
- Refutes literal infinite-dimensional reading of min spec ≥ +0.05 and its
  finite-section shadows; finite-section numbers are corroboration, not a
  certified finite-dimensional theorem.
- Does not evaluate C_in ≤ −0.05 alone; does not address full-boundary
  monotonicity or reformulated finite-dimensional tests with different thresholds.
- Sign conventions for DΛ₀ do not affect the conclusion.

## Reproducibility
- Geometry check: farthest corner norm ≈ 0.619 < 1, dist ≥ 0.38 — hand-checkable.
- Lemmas cite Evans Ch. 6, McLean Thm 4.10, Reed–Simon Vol I Ch. VI–VII,
  Lax–Milgram, Rellich, Alessandrini identity.
- Numeric script `output/artifacts/weyl_quotients.py` (numpy only) reproduces
  `output/artifacts/weyl_results.json`; verified replayed exactly in audit.

## References
- L. C. Evans, Partial Differential Equations, Ch. 6.
- W. McLean, Strongly Elliptic Systems and Boundary Integral Equations.
- M. Reed & B. Simon, Methods of Modern Mathematical Physics I, Ch. VI–VII.
- Kenig–Sjöstrand–Uhlmann, Calderón problem with partial data, Ann. Math. 2007.
- Liu–Tsou, Stable determination of polygonal inclusions, Inverse Problems 2020.
- Dai–Francini–Vessella, Doubling inequality, Inverse Problems 2025.
- Harrach et al., monotonicity relations (standard/linearized tests).
