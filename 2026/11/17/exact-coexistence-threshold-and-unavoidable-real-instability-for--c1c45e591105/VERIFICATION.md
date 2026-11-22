---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-20.md",
      "INDEPENDENT_AUDIT_2026-11-20.json"
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

Positive equilibrium elimination yields q_i=d_i/[m_i+p_i s+ℓ_i u] with p_i=k_i¹(1−b_i e^(−μτ_i))≥0. The compatible infected balance defines unique u(s)>0 because g_u>0 and g_s<0, hence u′>0. H(s)=Σk_i¹q_i decreases strictly from Σk_i¹d_i/m_i to 0; when p_i=0, bounded u(s) would contradict its own balance as s→∞. The exact Schur complement of the full delayed characteristic matrix at zero is s∏D_i g_u H′(s)<0, while normalized determinant tends to +1 at large positive real z; continuity gives z*>0. Its I coordinate agrees with the linearized infected-history integral, excluding an extraneous eigenmode. Independently assembled and tested one 2-type DDE zero determinant and characteristic root z*=0.8315102274585717, and source CHECKER.py includes distinct-delay two- and three-type samples; analytical proof covers all parameters.

## originality

PASS

Bardina–Cano–Cuadrado 2026 treats the identical delayed coinfection equations, but Proposition 5.2 proves only a one-sided no-coexistence condition for general unequal latencies; Section 5.1 explicitly restricts its sufficient classification to two common-latency types. The published all-n common-latency two-equilibrium result and critical-dose center manifold result do not imply a unique positive coexistence with arbitrary unequal latencies nor the new sign-of-determinant mechanism in that domain. Best-of-knowledge original beyond those cited source claims.

## value

PASS

A sharp if-and-only-if condition and uniqueness over all unequal finite latency sets plus a guaranteed real—not merely numerically suspected—instability mechanism fills a natural open equilibrium/spectral question in the original phage-cocktail model. These are structural results under the biologically explicit nonproductive-surviving-burst regime, not fitted intervention predictions or a parameter-renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
