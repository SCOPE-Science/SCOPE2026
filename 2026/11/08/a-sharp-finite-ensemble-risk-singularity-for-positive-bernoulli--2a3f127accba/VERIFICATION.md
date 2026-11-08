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

The theorem is a finite-probability calculation with an analytic all-ensemble-size proof in `RESULT.md`. `checker.py` uses Python standard-library `fractions.Fraction` and exhaustively enumerates the eight Bernoulli row states via multinomial replicate histograms for ensemble sizes 2, 3 and 4. It verifies exact negative-Gram probabilities and exact-rational monotonic approach of \(\varepsilon\) times mean-square error to the proved leading constant at three rational parameter choices for each ensemble size.

Run with `python checker.py` in the directory containing this file. The expected terminal status is `CHECKS_OK`. This finite calculation is supplementary; it does not prove the result for arbitrary ensemble sizes. No external formal proof, independent mathematical validation, finite-precision FEM experiment or inverse-estimation certificate was performed.
