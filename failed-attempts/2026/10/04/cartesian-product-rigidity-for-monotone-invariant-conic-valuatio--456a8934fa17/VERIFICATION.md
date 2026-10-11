---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

In dimension one, orthogonal invariance and the valuation identity determine the values on the zero cone, rays, and the full line. Lotz’s fixed-dimensional classification then writes each \(\mu_d\) uniquely as \(\sum_k a_{d,k}v_k\) with nondecreasing coefficients. Evaluating on a k-plane gives \(a_{d,k}=\mu_d(L_k)\); product additivity on k full-line and d-k zero-cone factors forces \(a_{d,k}=k\beta+(d-k)\alpha\). Intrinsic-volume normalization gives \(\mu_d=\alpha d+(\beta-\alpha)\delta\), and the convolution rule proves the converse.

## originality

FAIL

Lotz’s prior theorem already completely classifies every monotone invariant conic valuation in each dimension by its nondecreasing intrinsic-volume coefficient vector. The audited cross-dimensional statement is the immediate restriction of that complete classification under the claim’s additional Cartesian-product hypothesis: evaluating on product decompositions of linear subspaces forces the coefficient vectors to be affine in k. Under an implication-based novelty standard, this is a direct corollary of a stronger prior classification plus the standard product rule.

## value

PASS

Cartesian-product compatibility is a natural cross-dimensional structural requirement, and identifying statistical dimension as the normalized monoidal member of the full monotone-invariant valuation class is mathematically meaningful. The claim is rejected for prior implication, not for lack of intrinsic mathematical interest.

The dated certificate retains the supplied scientific assessment, sources and limitations.
