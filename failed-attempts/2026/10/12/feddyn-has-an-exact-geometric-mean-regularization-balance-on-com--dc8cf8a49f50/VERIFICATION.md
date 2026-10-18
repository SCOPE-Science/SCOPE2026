---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

FAIL

The block-gradient recursion and mean/disagreement formulas are valid; independently replayed six rounds with rational 1D heterogeneous clients and verified these identities. But the claimed equalities ||alpha(H+alpha I)^(-1)||=alpha/(alpha+mu) and ||H(H+alpha I)^(-1)||=L/(L+alpha) are FALSE when mu,L are merely non-tight bounds, as the stated assumptions allow. Take H=[2], mu=1,L=3,alpha=2: both true norms equal 1/2, while the claimed values are 2/3 and 3/5. The claimed unique optimum alpha=sqrt(3) for this H is also false; the true joint norm maximum is minimized at alpha=2 with value 1/2. Requiring mu=lambda_min(H),L=lambda_max(H), or expressly redefining factors as uniform class upper envelopes, would correct this, but is not the current theorem. No complete changed scientific files were supplied, so the false final claim cannot be passed or called repaired.

## originality

PASS

The surviving exact common-Hessian recurrence, joint mean/disagreement spectral decomposition, and isotropic server cancellation are not stated in the inspected defining FedDyn paper or Resultary retrieval. However originality of a corrected theorem is not scientific acceptance of the broader false one.

## value

PASS

The true decomposition isolates a meaningful tension between consensus and optimization modes in a canonical federated quadratic benchmark. Such exact spectral tuning would be useful after a correctly stated endpoint convention; scientific value does not cure the false stated quantifier.

The dated certificate retains the supplied scientific assessment, sources and limitations.
