---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Disk supports add. Central symmetry and the squared distances to an antipodal pair of maximal norm force the unique enclosing-ball center to be zero. As an independent route to the global maximizer, write z_i=u_i² and s=sum_A z_i. At fixed s, Cauchy–Schwarz bounds the two edge sums separately by sqrt(binomial(a,2)(a−1)s) and sqrt(ab[bs+a(1−s)]). Both bounds are attained at classwise equal squared coordinates. Equality in the positively weighted cross sum forces all z_i+z_j constant over cross edges, hence all z_i equal within each class, including a=2 or b=1. Maximizing the resulting scalar function yields s=1 for b≥a, or for b<a below and at the stated threshold; the derivative at 1 has sign (a−1)/sqrt(2)−τ(a−b), and strict concavity with positive infinite derivative at 0 gives the unique interior solution beyond the threshold. An attaining support direction gives exactly the contact Ru by equality in Cauchy–Schwarz, and the reverse map is x↦x/R. Thus the contact counts and their antipodal diameter counts exhaust the possibilities. The formal squared branch difference is ab(a−b)(τ−τ_c)², giving the second derivative jump, and the derivative of (1−s)/b at τ_c from above is 2sqrt(2)(a−b)/[a(a−1)], giving the square-root onset.

## originality

PASS

The nearest source-level comparisons provide discotope support/facial machinery, an exact regular unit-weight outer sphere, or a biregular bipartite exact outer ellipsoid. The complete-split graph contains a triangle; for b≥2 its class degrees are a−1+b and a. The nonregular weighted radius and contact transition is therefore outside those exact classifications. The regular specialization b=1, τ=1 is already covered and is credited. Priority is bounded by the inspected literature and corpus.

## value

PASS

The enclosing ball and its contacts are intrinsic metric quantities of graph-indexed disk sums. With the edge set fixed and every disk radius positive, varying just the cross weight changes which coordinates can appear at a contact, producing exactly a jump from 2^a to 2^(a+b) contacts and a sharp loss of radial smoothness. The quantitative onset and complete equality cases add geometric information beyond solving a single radius example or bounding it by an ellipsoid.

The dated certificate retains the supplied scientific assessment, sources and limitations.
