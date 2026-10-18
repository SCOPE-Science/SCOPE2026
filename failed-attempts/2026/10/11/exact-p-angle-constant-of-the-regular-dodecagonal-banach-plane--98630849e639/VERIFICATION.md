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

For any unit pair, A=N(x+y),B=N(x−y), P-angle cosine=(A²+B²−4)/(2AB). The frozen source establishes A+√3B≤4 and √3A+B≤4 by dual signed-facet evaluations; Q=A²+B²−(2−√3)AB is positive definite and reaches its maximum ≤4 at the six explicitly checked feasible polygon vertices. Witness x=(1,2−√3), y=(−1,2−√3) yields A=2(2−√3),B=2, equality. The 12-vertex/144-ordered-pair exact Q(√3) verifier matched Git blob 97b57c... and printed VERIFY_OK. All B>0 cases and endpoints were handled analytically.

## originality

FAIL

The independently read, distinct published full dodecagonal angle-convexity profile is strictly stronger for the same norm: exact M(B)=max N(x+y) at EVERY separation B. Since P-angle increases with A for fixed B, the claimed constant and its extremizers follow immediately. Thus the mathematical claim is covered even though the prior result has a different invariant name and does not display S_P. This is a scientific originality failure, not an access failure.

## value

FAIL

The P-angle constant of a regular polygon is a natural useful invariant in isolation, but here its exact value and sharp geometry are mechanically entailed by a published full same-object chord profile. Repeating that stronger theorem’s dual bounds for one scalar consequence supplies no independently unknown natural invariant or new structural mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
