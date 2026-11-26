---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

In units of the least positive subnormal with U=2^133, an input scaled integer v gives the exact scaled arguments 4v(U-v)/U and 4v R_scaled(U-v)/U. My independent replay rounds by exact quotient/remainder on the exponent-local spacing, tests all adjacent bfloat16 midpoints through 256, evaluates both successors for every code 0x0000–0x3f80, asserts closure, and classifies every start by a separate Floyd orbit walk. It reproduces the representatives 0000, 3f40, 3dbc (periods 1,1,11) and 0000, 3f40, 3e8d (periods 1,1,4); all basin counts; depths 81 and 99 and depth sums 623656 and 773744; and both stated SHA-256 digests with unsigned little-endian two-byte successors. Exactly 275 successors differ; the four nonempty cross-basin cells have counts 4374 (zero to zero), 65 (3/4 to 3/4), 10423 (11-cycle to zero), and 1395 (11-cycle to 4-cycle). No negative zero or extra hidden rounding is used.

## originality

PASS

Prior bfloat16 logistic collapse and evaluation-order sensitivity are known. The distinct result supported here is the exact pair of specified finite graphs and their full cross-basin transfer, not discovery of these general phenomena or of the map itself.

## value

PASS

Parameter four is the canonical fully developed logistic example; bfloat16 and rounding a subtraction are independently motivated choices. The information added is not simply an alternative period list. On a shared state set, an exact comparison shows that changing only 275 one-step edges sends 10423 initial encodings from a long nonfixed basin to zero, while preserving the 65-code fixed-point basin. This quantifies the amplification of a specific local arithmetic choice and supplies a reproducible benchmark a numerical-dynamics researcher can use.

The dated certificate retains the supplied scientific assessment, sources and limitations.
