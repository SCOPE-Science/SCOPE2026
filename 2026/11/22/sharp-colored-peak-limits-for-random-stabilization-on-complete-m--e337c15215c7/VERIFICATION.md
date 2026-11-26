---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For the repaired finding, recoloring introduces no conflict edge, so a random permutation thinned to currently conflicting vertices induces the uniform sequential process. A vertex survives exactly when last among its initial conflicting neighbors and itself; reversing order gives the initial same-part run within each color. Exchangeability of ordered prefixes conditioned on enough vertices of each color gives the falling-factorial evaluation. The accept-unused-identity coupling yields a uniform permutation and agrees with the replacement stream until its first collision. In the replacement stream the disjoint color subsequences are independent conditional on the marks and their laws do not depend on those marks. The first occurrence of a given color and the subsequent wait for a different part have geometric second moments bounded by 2k² and 2k²/ε². Consequently E[H²]≤4k³(1+ε⁻²) for the maximum completion time; summing the predictable collision hazards yields the stated upper bound. For a named color, the exact two-vertex tail is the color-occupancy factor times (NΣp_i²−1)/(N−1), giving the lower bound after dropping the factor and taking complements. It is at least ε/(N−1) in the upper bound's regime. Independent rational enumeration of actual activation with a valid maximum-unused-color rule matched all 183 tested joint tails and the marginal obstruction in four small distinct parameter cases. The coupling proof, not this finite check, gives the uniform bound.

## originality

PASS

Best-of-knowledge pass for the repaired sharp-order two-sided total-variation result, not for novelty of the exact law or the qualitative limit. The strongest overlapping text supplies the whole finite distribution by averaging conditional laws and obtains the same qualitative limit, but neither proves a finite-profile O(1/N) error nor the matching multicolor obstruction.

## value

PASS

The repaired comparison gives information not conveyed by the qualitative law: it approximates the full vector of dependent finite color counts by independent variables at a uniform inverse-size rate without replacing the empirical part proportions by their limits. A single identified marginal discrepancy proves that rate cannot be improved in order, including all profiles with a fixed non-dominance margin. The error bound also transfers to observables such as the stabilization count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
