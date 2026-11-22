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

# Mathematical verification
Run `python3 check.py` in the directory containing this file and the checker. All checks use Python standard-library modules only.

The checker verifies the 16-state potential inequality for each of 32 binary transitions, exhaustively enumerates strict rank chambers for input sizes 4 through 8, tests exact rational attaining pairs through input length 30, and tests one-input sharpness with binary steps through length 30. It separately checks 3,500 random rational input pairs and one-input cases. Success ends with `FOUR_POINT_CENTRAL_SPACING_ALL_CHECKS_PASS`.

The finite checks are not exhaustive for arbitrarily large sequences. Arbitrary lengths are justified by the at-most-three-window derivative support, translation invariance, integration across rank chambers, and the telescoping sixteen-state coarea argument in `RESULT.md`. Attainment above eight input sites follows by an explicit extension of a strict rank-order witness. No external certification or independent mathematical audit is asserted.
