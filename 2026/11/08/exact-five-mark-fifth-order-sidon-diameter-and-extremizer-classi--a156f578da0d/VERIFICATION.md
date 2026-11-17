---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Every increasing five-mark integer B5 set is uniquely represented by 0<a<b<c<d after translation. The collision-free criterion enumerates exactly 126 five-multisets, and its restriction to the first four marks is a necessary pruning condition. A freshly written C++17 nested-loop exhaustive search examined all 1,028,790 ordered quadruples with 4<=d<=72, 342,414 four-mark survivors, and found exactly (0,1,16,66,72) and its reflection (0,6,56,71,72). Therefore diameter 72 is minimal and the two listed optimizers are exhaustive; no extrapolation to other parameters.

## originality

PASS

Best-of-knowledge original at the exact final claim level after statement-level comparison with identified published results; credits previously known subclaims, keeps specific access and archival risks.

## value

PASS

This solves the first absent natural parameter of the relation-free five-letter B5 diameter sequence explicitly asked about by Zhang and gives a complete extremizer classification, a meaningful finite exact Sidon invariant rather than an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
