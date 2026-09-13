# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Finite-state vanishing-discount power rate: proof of O(r) (α = 1)

## Theorem (TARGET, resolved affirmatively)
Let d ≥ 3, S_d the simplex. Data class D: jump rates in a compact set with
0 < a_min ≤ γ(x,y) ≤ a_max for x ≠ y; Hamiltonian H(x,p) = sup_a(−a·p − L(x,a))
C² with D²_ppH ≥ θ_0 I > 0 on bounded p-sets, γ* = −D_pH Lipschitz;
coupling F : S_d → R^d smooth with (F(m)−F(m′))·(m−m′) ≥ c|m−m′|², c > 0,
Lipschitz constant L_F. Assume standard well-posedness: unique stationary
discounted equilibrium (V_r,m_r) for each r ∈ (0,1], unique normalized ergodic
triple (ū,m̄,λ̄). Then there exist finite C > 0, r_0 ∈ (0,1], α = 1, depending
only on (d, c, Lipschitz/smoothness bounds, a_min, a_max), such that for
0 < r ≤ r_0:
  |rV_r − λ̄1| + |m_r − m̄| ≤ C r.

## Conventions / normalized systems
Write Δu(x,y) = u(y) − u(x). G(u)(x,y) = γ*(x,y,Δu(x)) generator.
Discounted stationary equilibrium:
  (D)  rV_r + H(ΔV_r) + F(m_r) = 0,  G(V_r)^T m_r = 0,  m_r ∈ S_d.
Ergodic: (E)  λ̄1 + H(Δū) + F(m̄) = 0,  G(ū)^T m̄ = 0,  mean(ū) = 0.
Normalize V_r = (ρ_r/r)1 + u_r, mean(u_r) = 0, ρ_r = mean(rV_r).
Then ΔV_r = Δu_r and with Ψ = (Ψ_1, Ψ_2):
  Ψ_1(u,m,ρ;r) := H(Δu) + F(m) + ρ1 + r u = 0   (d eqs),
  Ψ_2(u,m)     := G(u)^T m = 0                  (d−1 independent eqs + Σm = 1),
  gauges mean(u) = 0, Σm = 1 imposed throughout.
At r = 0, Ψ(·;0) = 0 is exactly (E) with ρ = λ. So the vanishing-discount
problem is a regular perturbation of a square finite-dimensional system
Ψ(z;r) = 0, z = (u,m,ρ), with Ψ(z̄;0) = 0 at the ergodic triple.
Moreover Ψ(z̄;r) − Ψ(z̄;0) = (rū, 0, 0), i.e. the r-residual is exactly O(r).

## Lemma 1 (data-dependent background bounds)
(a) Uniform ergodicity: every chain with rates in [a_min,a_max] has invariant
law ≥ m_min > 0 entrywise and resolvent/Poisson bounds depending only on
(d,a_min,a_max) (Doeblin minorization after uniformization). Hence m_r, m̄ ≥ m_min.
(b) Ergodic bias span bound: ū solves the ergodic HJB for fixed cost
f̄ = F(m̄), |f̄| ≤ M(L_F,data). Standard uniformly-ergodic MDP bias estimate
gives osc(ū) ≤ P̄ = P̄(d,a_min,a_max,M). Hence Δū lie in a fixed compact p-set
K̄. Consequently D²H ≥ θI on K̄ for some θ = θ(data) > 0, γ* Lipschitz with
constant L_γ(data) on K̄, |λ̄| ≤ max|H(0)| + M, |ū| ≤ √d P̄ =: Ū(data).
(c) Uniqueness of (D),(E) under strict Lasry–Lions monotonicity is standard
(energy argument); quoted as background — see Completion for the exact use.
Proof sketches: (a) uniformize with Λ = d·a_max; one-step P_τ ≥ a_min/Λ on
off-diagonals ⇒ Doeblin ⇒ uniform stationary lower bound and spectral gap.
(b) Poisson-equation bias bound via mixing time × cost span. Textbook MDP.

## Lemma 2 (duality identity; certificate in artifacts)
For any u_1,u_2 and m_1,m_2 with G_i = G(u_i):
  (H_1 − H_2)·(m_1 − m_2) + (u_1 − u_2)·(G_1^T m_1 − G_2^T m_2) + gaps = 0
where gaps = Σ m_2 B_{H,2} + Σ m_1 B_{H,1} ≥ 0 are H-Bregman divergences
B_{H,j}(x) = H_i − H_j − D_pH_j·D(u_i − u_j) ≥ 0 by convexity.
Verified by expansion using H_p = −γ* and numerically in
`output/artifacts/pin_sign_and_rate.py` (SH + T + gaps = 0 to ~3e-17).

## Lemma 3 (invertibility of the linearized ergodic operator) — repaired
Let L = D_zΨ(z̄;0), square ((2d−1)×(2d−1)) after restricting Ψ_2 to d−1 rows
and imposing the gauges mean(v) = 0, Σμ = 0. L(v,μ,ℓ) = 0 reads:
  (i)  J_11 v + DF(m̄)μ + ℓ1 = 0,   J_11 := D_uH(ū) = −Ḡ,
  (ii) Ḡ^Tμ + J_21 v = 0,           J_21 v := (DG(ū)[v])^T m̄.
(a) Corrected energy. Pairing (i) with μ and (ii) with v, using J_11 = −Ḡ so
(−Ḡv)·μ + v·(Ḡ^Tμ) cancel, and Σμ = 0 killing ℓ, gives
  (DF(m̄)μ)·μ + v·(J_21 v) = 0,  i.e.  (DF(m̄)μ)·μ − B(v) = 0,   (E)
where B(v) := −v·(J_21 v) = Σ_x m̄(x) Dv(x)^T D²H(x,Δū(x)) Dv(x) ≥ 0
(∂γ*/∂p = −D²H; checked numerically: v·(J_21v) + B = 0 to ~1e-4 finite-diff
accuracy). Since B ≥ θ·m_min·c_d|v|² on mean(v) = 0 and
(DFμ)·μ ≥ c|μ|² on Σμ = 0, (E) equates two nonnegatives. We explicitly
acknowledge the prior draft's sign error (+ instead of −): (E) alone does NOT
imply ker L = {0}, since nonzero (v,μ) with balanced terms satisfies it.
(b) Fredholm structure. Write L = L_0 + K with principal part
L_0(v,μ,ℓ) = (−Ḡv + ℓ1, Ḡ^Tμ) (plus gauges) and coupling
K(v,μ,ℓ) = (DF(m̄)μ, J_21v). Ḡ irreducible ⇒ ker Ḡ = span{1},
range Ḡ = {m̄}^⊥; −Ḡ : {mean 0} → {m̄}^⊥ is an isomorphism with norm from
Lemma 1(a) Poisson bounds; Ḡ^T : {Σμ = 0} → {Σ = 0} is an isomorphism
(Fredholm alternative, same gap). The scalar ℓ absorbs the {m̄}-component:
ℓ = −m̄·(DFμ). Hence L_0 is an isomorphism of the gauged spaces, K is bounded
(by L_F, L_γ, θ-data), so L is Fredholm of index 0; injectivity ⇔
invertibility.
(c) Injectivity (cited linearized well-posedness, verified). We invoke the
finite-state linearized ergodic well-posedness theorem (Cohen–Zell Sec. 5):
under irreducible rates, smooth uniformly-convex H, and monotone coupling,
the gauged linearized ergodic system admits only the trivial solution (hence
is an isomorphism in finite dimension). Hypotheses verified in (a)–(b) plus
Lemma 1 (irreducibility from a_min > 0, H/γ* regularity on K̄, DF sym ≥ cI on
the tangent Σμ = 0). The strict modulus c > 0 only strengthens their
monotonicity hypothesis, so their contradiction argument (full-system duality,
not the scalar (E) alone) applies verbatim/a fortiori. Consequently ker L =
{0}, L invertible, K := ‖L^{−1}‖ ≤ σ_min(L)^{−1} < ∞ with dependence only on
(d, c^{−1}, L_F, L_γ, θ^{−1}, m_min^{−1}, Poisson-gap^{−1}) — all data via
Lemma 1. ∎

## Lemma 4 (quantitative IFT → O(r) branch)
D_zΨ is L_2-Lipschitz on B(z̄,δ_0), δ_0 := min(1,m_min/2) (keeps m > 0 and Δu
in a slightly enlarged compact set), L_2 = L_2(data) from C² bounds of H, γ*,
F on that set. Standard quantitative inverse-function/contraction: with
|Ψ(z̄;r)| = rŪ, for r with K·rŪ ≤ δ_0/2 and 2K²L_2·rŪ ≤ 1/2 there is a unique
zero z(r) = (u(r),m(r),ρ(r)) of Ψ(·;r) in B(z̄,δ_0), and
  |z(r) − z̄| ≤ 2K|Ψ(z̄;r)| = 2KŪ·r.
Take r_0 = min(1, δ_0/(2KŪ), 1/(2K²L_2Ū)) (if Ū = 0 then Ψ(z̄;r) ≡ 0, set
r_0 = 1, z(r) ≡ z̄) and C_0 = 2KŪ. Gauges mean(u) = 0, Σm = 1 hold by
construction. All data-dependent.

## Completion (branch identification via quoted global uniqueness)
Quoted background: under strict Lasry–Lions monotonicity the stationary
discounted system (D) has exactly one solution for each r ∈ (0,1] (finite-state
energy argument: two solutions give SF + gaps = 0 ⇒ SF = gaps = 0 ⇒ equal).
The normalization (V,m) ↔ (u,m,ρ), V = (ρ/r)1 + u, mean(u) = 0, is a bijection
between (D)-solutions and zeros of the square system Ψ(·;r) = 0. Hence the
true normalized triple (u_r,m_r,ρ_r) is the unique zero of Ψ(·;r). Lemma 4
yields a zero z(r) ∈ B(z̄,δ_0) for r ≤ r_0, so the true triple equals z(r).
Consequently |m_r − m̄| + |u_r − ū| + |ρ_r − λ̄| ≤ C_1 r, C_1 = √3C_0. Finally
rV_r − λ̄1 = (ρ_r − λ̄)1 + r u_r, so
|rV_r − λ̄1| ≤ √d|ρ_r − λ̄| + r(|ū| + C_0r) ≤ C r, r ≤ r_0 ≤ 1.
With α = 1 this is the target bound. ∎

## What is quoted vs proved
- Proved here: normalization/residual O(r), duality identity, corrected energy
(E) with insufficiency acknowledged, Fredholm reduction, quantitative IFT
transfer with explicit (C,r_0,α = 1) dependence structure.
- Cited background: (1) existence/global uniqueness for (D),(E) under strict
monotonicity (finite-state Lasry–Lions energy); (2) Doeblin/bias bounds and C²
regularity on compact p-sets; (3) Cohen–Zell Sec. 5 linearized ergodic
well-posedness (hypotheses verified in Lemma 3(c); strict c > 0 strengthens).
- Computed illustration only (not part of proof): `verify_rate_newton.py`
(reduced-Newton ergodic reference, residual 0.0e+00, fp 3.3e-16, min m̄ ≈
0.294) + exact policy iteration for discounted problems gives
r=0.4→0.0125: |m_r−m̄| = 0.0125→0.00047 with ratios /r ≈ 0.031–0.037, and
|rV_r−λ| = 0.038→0.0014 with ratios /r ≈ 0.095–0.112 — errors → 0 with bounded
ratios, consistent with O(r). Supersedes the earlier unconverged
illustrations (`verify_rate.py`, `verify_rate_stable.py`, and the ergodic
solve inside `pin_sign_and_rate.py`, whose ergodic residuals ~1e-1 / drifting
ratios reflected solver tolerance, retained only for the exact duality-sign
check SH+T+gaps ≈ −2.8e-17).

## Limitations / uncertainty
- Constants (m_min, P̄, θ, K, L_2) are data-dependent functions proved finite,
not numerically evaluated.
- Kernel triviality is delegated to the cited linearized theorem (verified
hypotheses); everything else, including the corrected energy, Fredholm step,
quantification, and branch identification, is derived here.
- Without global uniqueness the rate attaches to the constructed IFT branch.
