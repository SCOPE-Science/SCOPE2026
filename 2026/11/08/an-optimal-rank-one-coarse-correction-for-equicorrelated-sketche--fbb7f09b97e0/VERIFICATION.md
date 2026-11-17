---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For q,s≥2, 0<ρ<1, λ>0, m=qs with t≥2 replicated Nyström centers, H=(n/m)K²+λnK and the full within-block-sketch denominator B decompose on global G, blockwise-constant zero-sum V and within-block zero-sum U. Eigenvalues of (H,B) are h_a/d_c (q−1), h_a/d_a (m−q), h_b/d_c (1), strictly increasing. Thus κ(B⁻¹/²HB⁻¹/²)=h_b/h_a=κ(H). For any PSD rank≤1 W, a nonzero U∩ker W yields λmax≥h_a/d_a and V yields λmin≤h_a/d_c, proving κ≥d_c/d_a without alignment assumptions. Global W=τP achieves equality exactly for τ in [d_a h_b/h_a−d_c, d_c(h_b/h_a−1)], endpoints give two spectral levels. Independent dense-matrix generalized eigenanalysis at q=s=t=2,ρ=1/2,λ=1/10 reproduced spectrum [3/68,9/28,9/28,145/204] and optimum 51/7. This theorem is not a generic kernel guarantee.

## originality

PASS

Best-of-knowledge PASS for the precise new component only; earlier mathematically overlapping statements are credited in the four comparisons. Full source limitations and residual risks recorded, no failed search treated as proof.

## value

PASS

Responds to the explicitly identified inter-block coupling problem in memory-efficient sketched Nyström kernel ridge solvers. In a natural full-coherence stress family, standard block sketching cannot improve conditioning, while a single positive global correction produces an optimal block-count-independent condition bound and an exact tuning plateau. The negative-to-positive design contrast and two-eigenvalue endpoint are meaningful finite-dimensional spectral structure, not benchmark-only engineering.

The dated certificate retains the supplied scientific assessment, sources and limitations.
