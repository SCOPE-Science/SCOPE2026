# Exact transmission singularity exponent at the fixed 270° Calderón vertex (contrast 4:1)

## Context
Convex-corner determination for Calderón (conductivity) inclusions is standard, but realistic polygonal inclusions have reentrant (concave) vertices where the corner coefficient can degenerate. The admitted target was a smooth-template single-Cauchy-pair jump formula at the canonical symmetric L-shape 270° vertex with jump η=3 (σ=1 outside, σ=4 inside). Executing that bounded attack blocked the template: the formal constant disagreed with the prescribed value, quadrature showed remainder dominance at all τ≤10, and an 8×8 transmission-determinant scan located a leading exponent λ₁≈0.806<1. This record certifies that exponent exactly, plus a no-decay lemma, with an explicitly conditional obstruction to the smooth-template formula.

## Definitions
- Vertex at origin, opening angle 3π/2: Q₁={0<θ<π/2} has σ=1; Q₂,Q₃,Q₄ (the other three quadrants) have σ=4 (jump η=3, value 4 inside). Inclusion cone K={π/2<θ<2π}.
- Seek separated transmission solutions u=r^λ v(θ) of div(σ∇u)=0 near the vertex: v″+λ²v=0 per sector with v and σv′ continuous across the four interfaces.
- State Y=[v,σv′]ᵀ; sector propagator over angle π/2 with conductivity s₀: T(s₀)=[[c,s/(s₀λ)],[-s₀λs,c]], c=cos(λπ/2), s=sin(λπ/2). With Sₐ=T(1), S_b=T(4), full-turn monodromy M=S_b³Sₐ (det M=1).

## Result
(a) The smallest positive homogeneity exponent is exactly λ₁=(2/π)arcsin(√91/10)≈0.8060266320, unique in (0,1); the next root in (1,2) is λ₂=2−λ₁≈1.1939733680.

(b) No-decay lemma: no nonzero linear phase e^{τρ·x} decays on the 270° cone K; max_{x̂∈K} d·x̂ ≥ 1/√2 > 0 for every unit vector d.

(c) Conditional structural obstruction (explicitly conditional): since λ₁<1, the smooth-Taylor derivation (∇u(0)=e₁) is invalid because the corner expansion generically contains an r^{λ₁} term with r^{λ₁−1} gradient blow-up. IF the singular coefficient A(f₀)≠0 then the true corner-moment scaling τ^{−λ₁/α} dominates the claimed τ^{−1/α} with a solution-dependent prefactor. No certified lower bound A(f₀=x₁)≠0 is proved, so (c) is a conditional obstruction, not an unconditional falsity proof.

## Proof / evidence
- Exact symbolic expansion (sympy, exact rational arithmetic): tr M = 2cos⁴w + (17/4)sin⁴w − (75/16)sin²(2w), w=λπ/2; with the proved rule sin²(2w)=4sin²w(1−sin²w), tr M − 2 = s(100s−91)/4, s=sin²(λπ/2). Both steps verified exactly in `output/artifacts/verify_lambda1.py` (S1: both residuals identically 0; independently re-verified numerically by the auditor).
- Hence for λ>0, tr M=2 (⇔ det(M−I)=0 for 2×2 det-1) iff s=0 (λ∈2ℤ, trivial, excluded) or s=91/100. Strict increase of s on (0,1) gives the unique root λ₁ above; symmetry s(2−λ)=s(λ) gives λ₂.
- Independent 8×8 interface-determinant computation: min-SV ratio ~4×10⁻¹⁷ at λ₁ and λ₂ versus 6.3×10⁻² at λ=1 (control non-root) (S4).
- No-decay lemma: analytic case split (see DRAFT.md proof) giving max ≥1/√2 in all cases; 721-direction scan witnesses 0.707107 (S5).
- Replay: `python3 output/artifacts/verify_lambda1.py` → ALL VERIFY_OK (needs numpy, sympy).
- Supporting experimental motivation only (not proof of falsity): formal smooth-template constant Re c_R≈−1.064 (off target −0.42±0.05) and quadrature table τ^μRe I(τ) flipping sign across τ≤10.

## Limitations
- Fixed contrast 4:1 quadrant geometry only; other contrasts give a different (analogous) polynomial.
- Singular coefficient A(f₀=x₁) carries no certified lower bound; claim (c) is explicitly conditional (IF A(f₀)≠0).
- No new jump-recovery formula is claimed; the finding is an exact exponent plus conditional obstruction needed by any corrected formula.
- Prior qualitative concave-scattering results (Blasten 2018, Xiao 2022) are not contradicted.

## Reproducibility
- `output/artifacts/verify_lambda1.py` (S1–S5), re-run unchanged for this audit: ALL VERIFY_OK.
- Discovery chain retained in inputs: `cgo_constant.py` (formal constant), `probe_singularity.py` (determinant scan locating λ₁≈0.806).

## References
- E. Blåsten, Nonradiating sources and transmission eigenfunctions vanish at corners and edges, SIAM J. Math. Anal. 2018.
- J. Xiao, A new type of CGO solutions and its applications in corner scattering, Inverse Problems 2022.
- E. Blåsten, H. Liu, On vanishing near corners of transmission eigenfunctions, J. Funct. Anal. 2017.
- F. Cakoni, J. Xiao, On corner scattering for operators of divergence form (arXiv:1905.02558).
