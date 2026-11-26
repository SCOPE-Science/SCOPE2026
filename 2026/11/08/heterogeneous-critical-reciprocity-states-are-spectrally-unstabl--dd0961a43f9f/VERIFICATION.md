---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Differentiate the ordered payoff with respect to its first argument before identifying the slots in a self-game. This gives both frozen gradient formulas with the common factor br_j−c. It vanishes at the interior critical profile, and a whole neighborhood of the fixed point has inactive projection by continuity. In the subsequent population Jacobian, including when i=j, only the derivative of this factor survives. Subtracting the two strategy increments gives M_ij=a_i(2αq_i+2q_j−s), with s=1−α² and a_i=bη_i/(Ns²). For M factored into the columns a_i(2αq_i−s), 2a_i and rows 1, q_j, the reversed 2×2 product has trace CS and determinant 4α[(Σa_iq_i)²−(Σa_i)(Σa_iq_i²)]=−4αC²σ_w². The variance is strictly positive exactly for nonconstant q_i because all rates are positive. Two distinct nonzero shifts of opposite signs follow; the determinant identity for the full product transfers these shifts with multiplicities to the 2N-dimensional Jacobian, all remaining multipliers being one. The positive shift gives μ_+>1 and hence local linear instability even for very small positive rates. Symbolic replay: python /workspace/audit_evidence/reconstruct.py (payoff_jacobian); independently differentiates the payoff, with self-play identified after the first derivative, and checks the frozen exact two-player example. Only the analytic rank calculation proves the all-N claim.

## originality

PASS

The ordered updating rule, its critical gradient factor and the continuum of zero-gradient points are prior ingredients. The distinct supported claim is the exact rank-two spectrum at every heterogeneous interior critical-reciprocity profile for every strictly positive rate vector. The closest same-rule primary passages do not state this calculation, and the nearest spectral comparisons use different update laws or interaction populations.

## value

PASS

A structurally natural continuum of zero-gradient equilibria need not be robust. The exact variance identity proves that changing positive learning rates cannot stabilize any of its forgiveness-heterogeneous interior profiles and provides both transverse multipliers, rather than only a sampled example or a sufficient bound on step size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
