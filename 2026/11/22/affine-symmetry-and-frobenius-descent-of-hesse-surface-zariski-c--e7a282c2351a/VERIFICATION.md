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

Run `python3 verification/verify.py` from the extracted package, or run the script inside its own `verification` directory. It loads `verification/fixed_table.json` relative to its own path. Python 3 standard library only; no network or external CAS is required.

The program independently constructs the full exact negative-definite support set in two ways (integer Schur-complement determinants and incidence-forbidden patterns), checks all eleven affine conjugacy types against the table, checks that both Burnside sums divide by the relevant group sizes, directly enumerates 239 and 299 group orbits, and verifies the standard nonsplit finite-field Frobenius fixes 1,037 supports. The complete exact output is included in `verification/output.txt` and ends in `HESSE_AFFINE_CHAMBER_11_CLASSES_OK`.

The executable certificate verifies the finite incidence computation and all tabular arithmetic. It does not itself verify the geometric prerequisites that the Hesse surface has exactly the stated 21 negative curves; those are proved from adjunction and the cited elliptic-surface geometry. The group table is combinatorial; arithmetic interpretation requires the specified Frobenius action and does not assert existence of arbitrary twists. No independent expert mathematical audit has occurred.
