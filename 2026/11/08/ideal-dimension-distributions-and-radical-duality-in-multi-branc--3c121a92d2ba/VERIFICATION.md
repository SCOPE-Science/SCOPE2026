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

# Reproducible checks

Run `python3 branch_ideals_checker.py` with Python 3 and its standard library, from the directory containing the file. It exhaustively generates reduced-row-echelon subspaces of the maximal ideal over the indicated prime fields, tests closure against each algebra generator, and compares the resulting ideal-dimension histogram with an independent evaluation of the Gaussian inclusion-exclusion expression.

The archived `branch_ideals_verification.log` is the literal output of one successful run. The independent checks cover eight named finite configurations; the general theorem for arbitrary fields and branch lengths is proved algebraically in `RESULT.md` and is not certified solely by enumeration. No external validation of historical priority or proof was performed.
