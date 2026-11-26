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
  "schema_version": 1,
  "record_status": "passed"
}
---
# Verification and scope

The formulas in `RESULT.md` are established analytically. Check the constants by combining the small-gap expansion \(4\cot(g/2)=8/g+O(g)\) with the exact Beta marginal for the upper tail and by using the determinant \(n\) in the free spacing coordinates for the lower tail. The boundary estimate at a gap tending to \(2\pi\) is needed to justify localization at the regular vertex set. Both tails are needed for the real-order moment criterion. No numerical simulation or formal proof checker is needed for these claims.
