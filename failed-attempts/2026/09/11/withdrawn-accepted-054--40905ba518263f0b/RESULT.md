# Divergent loop-equation edge correction for the normalized Pareto α=3 Wigner ensemble (E3)

## Context

Edge universality versus heavy-tail breakdown is a recognized frontier (Wigner–Dyson–Mehta;
Soshnikov 2004; Auffinger–Ben Arous–Peché 2009; Lee–Yin 2014): Wigner matrices with
power-law tails of index α ∈ (2,4) have finite variance but infinite fourth moment, and
the Tracy–Widom edge picture breaks down qualitatively (Poisson fringe statistics; Lee–Yin
criterion s⁴P(|x₁₂| ≥ s) → 0 fails). What was missing was a hand-checkable analytic
witness certifying the breakdown mechanism at the edge scale for one fully explicit
ensemble. This record provides a divergent fourth-cumulant loop-correction lower bound
with an explicit rate.

## Definitions

- Let Y be symmetric with density p(y) = (3/4)(1+|y|)⁻⁴ on ℝ, and X = √2·Y.
  Then E[X²] = 1 and P(|X| > t) = (1/2)(1+t/√2)⁻³ = (1+o(1))√2·t⁻³.
- Let H_N = N^{-1/2}(x_{ij}) be a real symmetric Wigner matrix with i.i.d.
  off-diagonal copies of X (diagonal arbitrary symmetric, O(1) variance).
- Let m_sc be the semicircle Stieltjes transform, m_sc² + z·m_sc + 1 = 0,
  Im m_sc > 0 for Im z > 0.
- Fix w ∈ ℂ, Im w ≥ 1, and put z_N = 2 + w·N^{-2/3} (TW edge scale).
- Let M_N = N^{1/6} and X^{≤} = X·1_{|X| ≤ M_N}. Its fourth cumulant is
  κ_N = E[(X^{≤})⁴] − 3(E[(X^{≤})²])² (odd cumulants vanish by symmetry).
- The fourth-cumulant loop functional is L_N(z_N) := κ_N·m_sc(z_N)⁴, the
  normalized k=3 monomial of the standard Wigner resolvent cumulant expansion
  (absolute combinatorial prefactor absorbed; see Limitations).

## Result

With L_N as above,

  |L_N(z_N)| ≥ (1/8)·log N   (natural logarithm)   for all N ≥ N₀(w),

with explicit N₀(w) = max{10¹², (25|w|)^{3/2}} (in particular absolute N₀ = 10¹²
works on compact w-sets with |w| ≤ 8×10⁶). For GOE the same functional is
identically 0 (all cumulants above order 2 vanish), hence O(1). Consequently no
edge-comparison argument at scale η = N^{-2/3} requiring a uniformly bounded
fourth-cumulant loop correction can apply to E3 — a quantitative Tracy–Widom
breakdown witness. The untruncated X has E[X⁴] = +∞, and the truncated proxy
κ_N in fact grows ∼ N^{1/6}, so (1/8) log N is a conservative explicit floor.

## Proof / evidence

- **Lemma 1 (normalization and tail, exact).** ∫₀^∞ y²(1+y)⁻⁴dy = 1/3 via
  antiderivative −1/u + 1/u² − 1/(3u³), u = 1+y. Hence E[Y²] = 1/2, E[X²] = 1, and
  P(|Y| > a) = (1/2)(1+a)⁻³, i.e. P(|X| > t) = (1/2)(1+t/√2)⁻³.
  This violates the Lee–Yin condition (s⁴P ∼ √2·s → ∞).
- **Lemma 2 (m_sc factor bounded below).** With m = −1+s, s² + εs − ε = 0,
  ε = wN^{-2/3}. If |ε| ≤ 1/25 then |s| ≤ 0.283, |m| ≥ 0.717, |m|⁴ > 1/4.
  The condition |ε| ≤ 1/25 ⟺ N ≥ (25|w|)^{3/2}.
- **Truncated fourth moment (exact formula + hand lower bound).** With
  u = 1+x/√2, T(M) := E[(X^{≤_M})⁴] = 6[G(U)−G(1)],
  G(u) = u − 4 ln u − 6/u + 2/u² − 1/(3u³), U = 1+M/√2; T(M)/M → 3√2
  (T(10) = 14.03, T(100) = 347.2). Hand bound using only 1.41 < √2 < 1.42:
  for x ≥ 10 the integrand density factor is ≥ 1.05×2.32, so
  T(M) ≥ 2.43(M−10) for M ≥ 10. Since E[(X^{≤})²] ≤ 1,
  κ_N ≥ 2.43(M_N−10) − 3.
- **Headline.** |L_N| ≥ κ_N/4. At N = 10¹², M_N = 100, κ_N ≥ 215.7,
  |L_N| ≥ 53.9 ≥ (1/8)ln(10¹²) = 3.46. The gap
  g(N) = 2.43(N^{1/6}−10) − 3 − (1/2)ln N has g′ > 0 for N^{1/6} > 1.24,
  so the inequality persists for all larger N.
- **GOE contrast.** Gaussian cumulants above order 2 vanish, so the literal
  functional is 0; the truncated-moment analogue is bounded (E[Z⁴1] ≤ 3).
- **Numerical cross-check (not load-bearing):** output/artifacts/verify_target.py
  (stdlib only) evaluates the exact T(M) formula, checks the hand bound, samples
  m_sc(z_N), and checks the headline on a grid; prints ALL_VERIFY_OK
  (independently re-run in audit).

## Limitations

- L_N is the normalized fourth-cumulant monomial with an absolute combinatorial
  prefactor absorbed; the true k=3 loop term is a nonzero absolute constant
  multiple of it, so log-divergence is preserved but the literal prefactor
  differs by that constant.
- No claim that the full cumulant expansion converges for E3 (its failure is the
  point), and no Tracy–Widom rate is claimed.
- The certified consequence is exactly the stated lower bound plus the GOE
  contrast, i.e. one certified divergent correction blocking any
  bounded-correction comparison route.
- N₀ = 10¹² is deliberately crude; the true growth is ∼ N^{1/6}.
- Diagonal entries are assumed symmetric with O(1) variance only.

## Reproducibility

Run `python3 output/artifacts/verify_target.py` (stdlib only) → `ALL_VERIFY_OK`.
Hand lemmas need only 1.41 < √2 < 1.42 (from 1.41² = 1.9881 < 2 < 1.42² = 2.0164),
0.283² > 0.08, and (1/0.81)⁴ > 2.3.

## References

- Soshnikov, Poisson statistics for the largest eigenvalues of Wigner random
  matrices with heavy tails (2004).
- Auffinger, Ben Arous, Péché, Poisson convergence for the largest eigenvalues
  of heavy tailed random matrices (arXiv:0710.3132).
- Lee, Yin, A necessary and sufficient condition for edge universality of Wigner
  matrices (arXiv:1206.2251; Duke Math. J. 163 (2014)).
- Schnelli, Xu, Convergence rate to the Tracy–Widom laws (2022).
- Borot, Nadal, Right tail asymptotic expansion of Tracy–Widom beta laws (2012).
