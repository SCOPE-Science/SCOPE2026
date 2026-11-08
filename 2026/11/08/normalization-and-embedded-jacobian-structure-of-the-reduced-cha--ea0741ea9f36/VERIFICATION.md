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

# Computational verification and limitations

Run `python verify_quintic.py` with Python 3 and SymPy. This is a standalone deterministic calculation over the prime field and \(\mathbb F_4\). The accompanying `verification_output.txt` records one successful execution from the packaged source. The checked statements are the discriminant square identity, triangular-coordinate normal form, normalization's integral relation, the characteristic-two Jacobian partial derivatives, and all \(\mathbb F_4\) monic quintic squarefreeness equivalences. The program prints `ALL_CHECKS_PASSED` on success.

The exhaustive finite-field check is not an independent proof of normality, the conductor, or all-field quantifiers. Those follow from the explicit polynomial-ring and module proof in `RESULT.md`. No external independent scientific audit has been performed.
