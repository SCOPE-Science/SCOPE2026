---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Reconstructed RESULT.md §§1–3. P−Q has derivative (1−t)(1−t²)^(-α) and endpoint constant d; integrating the derivative of (1−t)(1−t²)^(1−α) confirms the beta formula d=πδ+O(δ²). In the transformed M, put v=1−y and w=1−ry≥v; the derivative is bounded by a constant times v y^(1−α) w^(α−3), hence by the integrable y^(−1/2−η)v^(−1/2). Taking r→1 gives the two beta terms in M′(1) and value π at α=3/2. For R/ε the scaled integrand is dominated uniformly by a multiple of u^(1/2−η)/(1+u)^2 for u≤1 and u^(1/2)/(1+u)^2 for u≥1; the limiting beta coefficient at α=3/2 is also π. This justifies the uniform −2πε limiting correction and the profile 2^(3/2)π√x−2πx when ε=δ²x, including (δ²x)^δ→1 uniformly on compact positive x-intervals. The transformed M is strictly increasing at the critical parameter, with d=0 and R>0 in the interior, so all maximizing radii approach 1 by joint continuity. Comparing the trial x=1/2 with the uniform upper bound Cδ√ε−cε traps every scaled maximizing radius in one compact subset of (0,∞). The unique limiting optimizer is 1/2 and its gain is π in the stated full norm. The support script was inspected, not executed; numerical agreement is not needed for the joint-limit proof.

## originality

FAIL

The two coupled limits, including the all-maximizers quantifier and norm normalization, are exactly covered by a distinct indexed Resultary report. The dated catalogue paths do not establish precedence or derivation; the verdict is against distinct scientific content in the submitted finding, not a finding that the indexed report predates it. The main cited paper establishes the transition but not these two coupled limits in the inspected statements.

## value

PASS

As mathematics the result gives sharp onset constants for a natural exact operator norm at the transition, and controls all optimizers without postulating uniqueness. The uniform negative linear correction and global localization answer questions not resolved by qualitative interior attainment; this structural value is separate from the duplicate coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
