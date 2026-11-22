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

The mathematical proof expands the exact three-stage scalar multiplier and averages over the four possible coupled signs. Sign classification of the resulting quadratic supplies an all-positive-step theorem and does not depend on sampling or finite precision.

To reproduce the standalone arithmetic checks, run `python3 verify.py` using Python 3 with only the standard library. The script computes exact rational real-vector stages independently of its complex multiplier calculation; it tests the symbolic coupling identity at many rational input values, the unique-coupling excess term, an exact rational stability contrast, and exact finite-history moment products. The output was `VERIFY_OK 1523 exact-rational assertions`; the companion `verify_output.txt` records this output.

Finite tests are diagnostic rather than exhaustive proof. The claim concerns an idealized symmetric multiplicative curvature oracle; no hardware floating-point experiment, nonlinear extension, independent expert audit or hardware performance measurement has been performed.
