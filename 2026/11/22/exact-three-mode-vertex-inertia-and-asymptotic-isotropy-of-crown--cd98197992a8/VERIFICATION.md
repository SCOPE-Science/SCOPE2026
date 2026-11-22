---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The proof derives the ordered-pair completion count and uses it to compute the covariance action exactly. The four orthogonal eigenspaces have dimensions summing to the entire coordinate space. The least eigenvalue factors into positive terms for each integer \(n\ge4\); strict separation and the simplified condition ratio follow algebraically.

Run `python3 verify_crown_3match.py` with Python 3 and no additional packages. It independently enumerates admissible triples for \(3\le n\le8\), checks exact rational first and second moments, tests the covariance eigen-equations and the trace normalization, and prints `CROWN_THREE_MATCH_PASS`. A finite checker does not prove a statement for unbounded \(n\); that relies on the proof in RESULT.md.

Historical priority is provisional. No independent audit has been performed.
