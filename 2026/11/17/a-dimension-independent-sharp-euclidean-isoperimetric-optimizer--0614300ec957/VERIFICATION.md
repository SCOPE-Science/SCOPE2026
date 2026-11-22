---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Checked the primary transfer matrix Tr(prod [[a_i,−ell²/2],[1,0]]) for open chamber 0<2ell<min a_i and the correct dimensional normalization. For each upper coordinate facet x_i=a_i, support motion ∂V/∂a_i contributes U_i+D_i/sqrt(2); ∂V/∂ell=−ΣD_i/sqrt(2). Divergence/normal equilibrium dotted with all-ones gives ΣU_i=ΣL_i (diagonal normals sum zero in that direction), so total ordinary Euclidean S=2Σ∂_{a_i}V+(2−sqrt(2))∂_ell V. Homogeneous uniform scaling A with fixed ell=t gives Σ∂_{a_i}V=sf_s−tf_s′, so S_s formula follows. Tr(M(t)^s) eigenvalues λ±=(1±sqrt(1−2t²))/2. Brunn–Minkowski makes h=f_s^{1/s} concave under affine interpolation; strictness follows because different t have distinct volumes but all coordinate widths are exactly 1, so two bodies cannot be positive homothets. The derivative Q′=s(2−sqrt(2)−2t)h″, h″≤0 and not identically zero on any interval, yields strict descent then ascent across t*=1−1/sqrt(2). At optimum the derivative term vanishes. Formula and continuity at t=0,1/2 are not illegitimate differentiation across chamber boundaries. Independently checked transfer matrix trace numerically in 25 sample (s,t) cases and symbolic derivative algebra; finite cases do not prove global uniqueness.

## originality

PASS

Compared the exact statement and normalization with primary literature, published mathematical findings and indexed aliases; novelty assessed for the unrestricted claimed quantitative family rather than for credited intermediate lemmas. Residual priority risk is explicit. A sharp, dimension-independent unique shape optimizer for the natural chainlink family under fixed-volume normalization, including an explicit measurable Euclidean surface area and asymptotic improvement over the equal-volume cube, is a nontrivial global varia

## value

PASS

A sharp, dimension-independent unique shape optimizer for the natural chainlink family under fixed-volume normalization, including an explicit measurable Euclidean surface area and asymptotic improvement over the equal-volume cube, is a nontrivial global variational and geometric fact. Known volume identities alone do not identify this universal stationary point or prove strict optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
