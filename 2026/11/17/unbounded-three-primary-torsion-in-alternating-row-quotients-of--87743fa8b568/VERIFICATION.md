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

## Reproducibility checks

From this package, run `python verify_a4.py` with Python 3 and SymPy installed. The program reconstructs the displayed integral quotient cycle-basis boundary presentation, computes full Smith diagonal factors at four small widths, and checks the stable prediction in the seven- and eight-column cases. Compare against `verify_a4.out`.

These computations are finite sanity checks. The infinite statement depends on the explicit symbolic elimination in `RESULT.md` and Wilson's externally published inclusion-matrix diagonal theorem (Ghorbani et al., Corollary 3), read in its full open-access PDF. The exact quotient is a geometric orbit space, not a Borel construction. Homotopy cell attachments beyond the stated homology are not classified.
