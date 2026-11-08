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

The symbolic steps are written out in `RESULT.md`: the Hermite ambiguity formula, the elementary Laguerre three-term recurrence, the compact minimum's simple-root perturbation, and the competing monotone endpoint constraint. This proves the theorem for all fixed order pairs satisfying the stated hypothesis and sufficiently large radius.

Reproduce finite numerical checks by installing NumPy and SciPy and running `python3 check_hermite_weights.py` in the directory containing this file. The script constructs Laguerre polynomial coefficients exactly as rational formulas evaluated in floating point, finds all real stationary points of the weighted one-dimensional squared ambiguity function, and solves the compact/endpoint crossing for four test radii. It checks the predicted weight ratio, second-order deficit ratio, and the inner-root constant for Hermite orders one and two. It is not a computer-assisted proof of the infinite asymptotic.

The exact domain is the *closed* disk \(0\leq t\leq T\); weights range over the *closed* interval \([0,1]\). For sufficiently large radii the optimizer is uniquely interior. No quantitative numerical certification of the unbounded radius or the proof's onset radius is asserted.
