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

The state types (B,M) have multiplicities 1 for (3,±3) and 3 for (−1,±1). Their covariance gives the two-parameter Fisher matrix for dimensionless coupling and common offset. Spin reversal preserves the two diagonal entries and changes the sign of the nonzero cross-entry at y>0, making w=1/2 uniquely optimal for a fixed y>0; all allocations coincide at zero field. Direct rational differentiation gives F'_a with the asserted quartic numerator. The coefficient thresholds appear in ascending order for decreasing degree, so there is one sign variation even at a zero coefficient. Descartes plus the signs at zero and infinity give exactly one simple positive root. The factorization P_a(1)=(a+3)(39a²−46a−9) gives the exact physical threshold, and at equality the derivative is strictly negative for q>1. In the limit a down to 0, the rescaled polynomial changes sign across aq=3, trapping the unique root; the scaled determinant converges locally uniformly around that root, so the maximum tends to 4. Converting q to y gives the stated field scale. For every single field, G_a≤64a/3 for a≤1, with matching limit at q=a^−1/2. This uniform comparison allows a field depending on a. The ratio uses identical total observation counts and the same parameterization.

## originality

PASS

The Gibbs model, single-field metric and determinant are prior, and the single-field asymptotic follows directly from that known determinant. Symmetrized allocation is a standard information-design argument. The distinct contribution is the exact global magnitude classification within paired opposite equal-magnitude fields and the resulting strong-antiferromagnetic information rescue relative to all single fields, not the ingredients alone.

## value

PASS

The exact paired design threshold solves a natural local joint-estimation problem and selects a nonzero probe magnitude even for a range of weak ferromagnetic couplings. In strong frustration the design changes a vanishing best single-field information determinant into a finite one, a qualitative improvement under the same sample budget.

The dated certificate retains the supplied scientific assessment, sources and limitations.
