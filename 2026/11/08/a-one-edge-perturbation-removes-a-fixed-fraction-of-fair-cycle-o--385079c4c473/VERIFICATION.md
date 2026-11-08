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

# Verification of the exact orientation-count theorem

Run `python verify.py` from the package directory using Python 3 and only the standard library. It checks the exact **zero-inclusive EFX** definition by computing each recipient bundle, each potentially envious agent's valuation, and each possible one-good deletion. No fairness shortcut is used for this independent direct-definition test.

The executable exhaustively covers all \(2^n\) orientations for cycle lengths 3 through 13, at distinguished weights 1/2, 3/4, 1, 5/4 and 2, totaling **81,880 orientation-weight cases**. It compares the direct definition with the proved local inequality and with the sign-word forbidden-pattern characterization; exact counts are compared against the theorem. The script also calculates the transfer matrix powers and exact formula counts through length 100. The expected final line is `VERIFY_OK direct_efx_orientations=81880 counts_cases=55 matrix_cases=98`.

The mathematical proof itself, not the exhaustive finite testing, establishes the theorem for all cycle lengths at least four. Full formal independent audit and worldwide novelty certification have not been performed.
