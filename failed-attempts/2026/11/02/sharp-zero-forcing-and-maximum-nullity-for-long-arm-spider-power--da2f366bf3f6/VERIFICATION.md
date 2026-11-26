---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The forcing sequence uses (m−1)k seeds. The k distinct path eigenvalues each give an (m−1)-dimensional space of center-zero arm contrasts. In increasing eigenvalue order the kth root is at most 1 by 2(ℓ+1)≥3k, every positive root has its negative partner among the roots, and the smallest root is unpaired because k<ℓ. The resulting factors A, A+dI and A²−c²I are nonnegative entrywise. For distance r with 1≤r≤k, write r−z=2j+s for z∈{0,1} the number of zero roots, j the number of traveling quadratic factors and s the number of traveling shifted linear factors. The available intervals [2j,2j+a] cover the needed integers because a≥1 shifted linear factor exists. Place unused quadratic factors at a nonleaf endpoint for strictly positive diagonal entries even at c=1; two leaves are farther than k. This gives exact off-diagonal support, and M≤Z closes the bound. Both k=3 and k=4 meet the length restriction throughout ℓ≥k+1.

## originality

FAIL

The stated equality is already covered by two earlier constructive results. The proof is different, but cannot make the narrower exact equality a new resolution of the conjecture.

## value

FAIL

These are natural graph invariants and the positive-factor proof is mathematically useful as an alternative construction. But the submitted exact invariant resolves no remaining parameter case of the predicted equality and supplies no improved bound or classification beyond the earlier complete solutions. The more structured adjacency-algebra witness would need to be the subject of a distinct, independently assessed finding, not a justification for accepting the equality as a new result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
