---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For d≥2 and continuous positive κ, the two published densities κ^a/I_a and κ^b/I_b define probabilities with a+b=1. Substitution gives H²=1−I_1/2/√(I_aI_b). Cauchy–Schwarz and equality show vanishing iff constant curvature (hence ball). F=log I_t has Fʺ(t)=Var_{μ_t}(logκ); the elementary midpoint Green-kernel identity proves −log(1−H²)=1/2∫_a^b min(t−a,b−t)Fʺ(t)dt. Similarity exponent cancellation and boundary d≥2 checked. Independent three finite weighted-curvature analogues corroborate midpoint variance, not an infinite-body proof.

## originality

FAIL

FAIL: two primary source results together already imply the entire claim by direct specialization. Hoehner specifies a=1/(d+1),b=d/(d+1) and ball rigidity; Nielsen 2024 Proposition 4 proves for ANY exponential family pθ∝exp(θT−F(θ)) the Bhattacharyya coefficient ρ=exp(−J_F(a,b)); set T=log κ and α=1/2. This is EXACTLY I_1/2/√(I_a I_b), with H²=1−ρ. Its variance integral is the ordinary midpoint second-derivative integration of the same Jensen gap and no model-specific new estimate. The original geometric formula is a direct corollary/renaming, regardless of absence of its exact wording.

## value

FAIL

FAIL: this contribution selects an off-the-shelf Hellinger metric and substitutes two existing exponential-family parameters into an existing exact divergence identity; the rest is standard log-partition variance calculus and already known constant-curvature rigidity. It supplies no new quantitative geometric stability inequality, independently unknown natural invariant, or substantive additional mechanism beyond textbook specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
