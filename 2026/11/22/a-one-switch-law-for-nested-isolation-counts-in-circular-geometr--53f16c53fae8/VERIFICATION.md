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

The unchanged covariance, phase diagram and sparse root hold with the repaired proof in /workspace/repairs/2/RESULT.md. Anchor the cyclic order at a sampled label, rotate it to zero, and use the spacings of the other n−1 iid uniforms with endpoints 0 and 1. The Dirichlet premise is generally not true with the wrap gap distinguished by a fixed spatial origin; the cyclic count is independent of indexing. The ordered-pair classes are n (same vertex; bound 2s), 2n (adjacent; bound t+2s), and n(n−3) (disjoint; bound 2t+2s). The last class vanishes exactly when n=3. Translation in the simplex proves the mixed moment; subtracting the product of the means yields Eq. (1), including −63/1250 at n=3,t=1/10,s=2/5. At s=t there is nonzero variance: all points can lie in a sufficiently short arc, or one can lie separated from a cluster by more than t in both directions. With the positive factor nP_n(2s) removed, the result decreases strictly up to z=t/(1−2s)=1 and is then constant at 1−nP_n(2t). This gives all three sign regimes and the stated plateau. The exponent expansion in 1/n gives the disjoint-minus-product coefficient −3−4xy; the other two contributions give e^(2x)+2e^x in the same normalization. The original shortcut to y_c(x)>x drops the term 2e^x−3, which can be negative. The revision proves h=e^(2x)+2e^x−3−4x² is positive using h(0)=0 and h′≥4−2x+4x²>0, then brackets the finite root at fixed arguments on either side of the limit root. This proves the same claims without numerics. Independent derivation notes: /workspace/branches/1acfebe7-fa85-4c7f-b875-03de8a4f304d/ordinal2-evidence-status.txt. The frozen verifier was inspected, not run. Corrected three malformed reference URLs in the replacement. No claims about Poisson or soft graphs, n<3, or independence follow.

## originality

PASS

Best-of-knowledge pass for the exact cross-scale isolation covariance and sharp fixed-count sign classification. The corrected proof does not change the claim. The Dirichlet survival calculation and the general one-switch method are not new. The prior one-gap law even shares the expected-count-one condition after rescaling the thresholds, but it does not give the adjacent-pair observable, its covariance or its sparse crossover.

## value

PASS

Isolation is a natural connectivity diagnostic across radii. Besides exhibiting negative covariance despite nested counts, the theorem gives the sharp expected-one boundary, exact finite-region signs with a plateau, and a nontrivial sparse calibration. These specify when the multiscale dependence changes, not just that it can. No joint-law, independence, or testing-power improvement is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
