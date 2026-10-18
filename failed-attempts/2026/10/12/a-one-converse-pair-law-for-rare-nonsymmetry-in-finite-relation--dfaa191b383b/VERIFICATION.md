---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The asserted asymptotic is mathematically valid under the explicitly uniform Maddux/Koussas formula: Q(n,n−2k)−Q(n,n)=−k(n−1), P(n,n−2k)=(n−2k−1)!k!2^k. Hence R_{n,k}=(n−1)!/[(n−2k−1)!k!2^k]·2^{−k(n−1)}, k<=floor((n−1)/2). The successive ratio is (n−2k−1)(n−2k−2)/[(k+1)2^n]; bounding it by n²/2^(n+1) controls tail/R_{n,1}=O(n²2^(−n)). R_{n,1}=(n−1)(n−2)/2^n, yielding both overall probability and conditional one-pair concentration. Uniform relative error is essential and present in the source. Fresh exact rational checks for n=7,10,15 corroborate the quotient and tail but do not validate the external asymptotic theorem.

## originality

FAIL

FAIL. The complete quantitative statement is a parameter specialization and elementary summation of the already published UNIFORM formula F(n,s) for EVERY admissible s. This theorem directly dominates all k-strata, and the tail ratio needed for conditional one-pair concentration is an immediate factorial quotient; absence of the exact phrase in titles does not restore originality. Under the rule that corollaries and special cases of stronger work are covered, this is covered rather than an independent new mathematical claim.

## value

PASS

The first-order rare-nonsymmetry mass and typical defect type are meaningful quantitative interpretation for readers of finite relation-algebra asymptotics, beyond the qualitative phrase almost all symmetric. The formula is useful as a derived corollary but has no independent new counting argument; this value observation does NOT rescue O failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
