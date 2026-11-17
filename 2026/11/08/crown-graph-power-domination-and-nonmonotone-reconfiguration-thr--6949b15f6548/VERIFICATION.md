---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For n>=4, a mixed pair observes all but at most two vertices after the closed-neighborhood step and one-observed-neighbor forcing completes it; a pure r-set with r>=2 observes B and can force the n-r unseen same-shore vertices iff n-r<=2. A singleton stalls. The iff classification yields the two polynomials by direct shore selection and the minimal sizes 2,n-2. At TAR budget 2 all n^2 mixed pairs are isolated (n=4 additionally 12 pure pairs); at budget>=3 pairs exchange via an added token; at budget n-2 each minimal pure (n-2)-set is an isolated new vertex, and at n-1 adding one opposite-shore token joins every pure set. Verified n=4,5,6 independently by exhaustive domination and budget components; this is a finite cross-check, not the n-unbounded proof.

## originality

PASS

Prior original-source comparisons and Resultary queries show no earlier exact crown power-domination all-set and nonmonotone TAR component profile; ordinary domination on the same graph yields demonstrably different feasibility. The 2019 same-family generalized k-domination result was inspected as fully as available; text rendering remains a known risk.

## value

PASS

The power-domination all-set and minimal-set polynomials resolve a natural exact enumerative graph invariant. The nonmonotone component count and distinct first/stable connectivity thresholds give a complete, motivated example in reconfiguration theory, beyond knowing the power-domination number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
