---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The unit simplex tight-frame map identifies squared directional residuals with any zero-sum z of fixed norm S=(n+1)/n. One-step orthogonal projection loses exactly the sampled maximum z_i^2. When m=n+1 odd, the nonstandard inequality D=sum_{i<j}|z_i^2-z_j^2| >= S follows from sorted magnitudes: one sign carries at most (m-1)/2 positions but half the absolute mass, forcing the large-magnitude gap constraint; summation by parts has coefficients c_i=(i-1)(m-i)>=(m-1)h_i/2. The two-sample expected maximum is S/m+D/[m(m-1)]; equality is attained by opposite pairs ±a plus one zero, with every β≥2 sample meeting a nonzero. Even m has balanced ±a and constant squares, giving 1/n for all β. β=1 follows by tightness. Independently checked 60,000 bounded random integer zero-sum vectors in odd cardinalities and inspected exact-grid source checker; analytic lemma, not bounded checking, proves all dimensions.

## originality

PASS

The complete dimension-parity phase diagram with sharp β=2 saturation on a regular-simplex frame is not implied by general sampled Motzkin/Kaczmarz dynamic-range bounds or existing cost-weighted fixed i.i.d. optimal-sampling simplex theorems. Best-of-knowledge risk from an unindexed sharp zero-sum dispersion inequality.

## value

PASS

A two-sample versus full-greedy threshold gives a sharp, interpretable sampling-efficiency frontier for a canonical equiangular tight frame. The parity split and optimal configurations are mathematically specific and not routine from the frame identity; the odd-cardinality inequality is a motivated extremal lemma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
