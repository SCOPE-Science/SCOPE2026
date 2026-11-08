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

# Reproducibility and verification limits

Run `python verify.py` using the Python standard library to replay 1,782 five-by-five exact-rational resolvent inversions, one exact switching-point check, thirteen numerical bisection comparisons and one weak-coupling check. Expected output: `VERIFY_OK 1797`.

Run `python verify_symbolic.py` with SymPy installed for twelve symbolic matrix/cofactor and singular-expansion identities. Expected output: `SYMBOLIC_VERIFY_OK 12`.

Both programs were executed from these delivered source paths, not copied from an earlier result. The rational verifier uses exact `fractions.Fraction` Gaussian elimination for all full-matrix checks. Numerical bisection and the small-parameter example test floating-point approximations only. The analytical proof in `RESULT.md` is the basis of the all-real-parameter conclusion. No independent mathematical review or external certification is asserted.
