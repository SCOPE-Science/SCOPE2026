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

# Reproducibility and checked limits

Run `python verification/check_certificates.py` with any recent Python 3 interpreter; the script needs only the standard library. It checks the generator's stochastic uniformization, four derivative signs at two rational quality endpoints, derivative-sign brackets for first and third stationary points, and disjoint rigorously enclosed peak-height gaps at those endpoints. Arithmetic for all acceptance signs and brackets uses exact `fractions.Fraction`. The exponential uniformization and rational tail bounds in RESULT.md imply that the uncomputed series cannot change any tested sign.

The analytic proof, not the finite checker, supplies the general \(n\le4\) impossibility, the no-extra-stationary-points theorem, the strictly increasing lane-four occupation probability, the unique equal-maxima quality, and globality at that quality. Decimal values are orientation only. No claim is made about all continuous river hydraulics, any ecological empirical calibration, or independent verification.
