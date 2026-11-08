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

The analytical argument is fully contained in `RESULT.md`. For numerical spot checks, run `python mobius_cylinder_distance_check.py` with NumPy and SciPy installed. The script evaluates the explicit CDF integrals at four parameter pairs, compares them with direct geometric deck-transform distances for one million random pairs in total, and checks the exact threshold regimes and asymptotic coefficient at three small positive scales. The expected last line is `MOBIUS_CYLINDER_CHECK_OK profiles=4 thresholds=124 samples=1000000`. This is not independent or formal certification of the infinite proof; in particular the stochastic order and asymptotic coefficient are established by the algebraic-integral argument, not by numerical data.
