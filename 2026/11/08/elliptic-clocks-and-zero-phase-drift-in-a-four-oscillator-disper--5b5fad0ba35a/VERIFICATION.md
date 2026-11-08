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

# Reproducibility and proof verification

## Reproduction

Run `python verify_phase4.py` using Python 3 with SymPy, NumPy, and SciPy installed. The program checks five exact trigonometric reductions, including the full-phase mean velocity. It uses adaptive DOP853 integration of the original four angular equations and the reduced phase-difference equations at 70 combinations of nonzero opposite-pair parameter and positive/negative noncritical energy. It evaluates the predicted complete-elliptic period, checks both equations return to their initial torus coordinates, and tests that the half-period is not a full return for these examples. The numerical tolerance is set to \(3\times10^{-9}\) radians for the period returns. It also tests period ordering and the small-energy and near-center limiting formulas on a finite grid.

## Mathematical checks and boundaries

The proof in `RESULT.md` explicitly gives the variable change, exact reduced equations, topology of every critical and regular energy level, the complete elliptic integral for the **minimal** period, and the reversing symmetry forcing zero full-phase holonomy. These analytic arguments apply to every initial state under the exact four-node assumptions. Finite computer checks cannot certify the global classifications, prove minimality for infinitely many orbits, or replace the symmetry argument. Very small \(|h|\) may require higher precision if the elliptic parameter is represented as a nearly-unit floating-point number. No independent scientific validation is claimed.
