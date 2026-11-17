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

# Reproducibility checks

The included `verify_rotor.py` is a standalone Python 3 standard-library script. Run `python3 verify_rotor.py 7` alongside `verify_output.txt`. For \(k=1,\ldots,7\) it enumerates all \(4^k\) labelled peripheral rotor assignments and calculates first entry in three independent ways: an explicit last-bad-petal formula, stepwise recognition of exactly one rotor cycle containing the chip, and full-state repetition with its earliest preperiod position. It checks all coefficients of the exact recurrence polynomial, means, maximum times and multiplicities. Totals: 21,844 configurations; no discrepancies.

The verification tests only seven finite sizes. The all-size assertion follows from the excursion proof in `RESULT.md`; Gaussian asymptotics follow from the binomial defect model. No external validator or formal proof certificate is claimed.
