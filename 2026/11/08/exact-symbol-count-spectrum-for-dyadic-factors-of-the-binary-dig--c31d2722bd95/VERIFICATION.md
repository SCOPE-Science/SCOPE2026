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

Use `python3 verify.py`. The Python program has no third-party dependencies and checks the literal recurrence initialization, prefix extrema, six-step relations, and all predicted bounds through level 120. It also enumerates all phase-pair prefixes for 13 levels and literal sliding factor windows at 11 levels. Successful execution prints `VERIFIED` with the exact categories and base rows. The phase-enumeration check covers all nine boundary phases; direct sliding-window checks provide independent tests of real factor occurrences.

The mathematical proof is in RESULT.md. Finite execution is not used as proof for all levels. No formal kernel or independent scientific audit is asserted; scientific scope is confined to fixed-symbol counts at dyadic factor lengths.
