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

# Reproducibility and verification

Run `python3 check_singer.py` in the directory containing this file and the checker. Python 3 and its standard library suffice. The checker prints the minimum divisible-trinomial spans of two explicit primitive polynomials, validates the worst-case span thresholds at all integer diameters 2 through 32, and compares three independently implemented exact binary-index computations over 207,628 positive-time/site/polynomial cases.

One computation tests root-of-unity/Singer incidence and dyadic valuations, a second tests direct divisibility of all seven nonzero pinned characters by the exact polynomial power, and the third constructs the recurrence kernel and computes its coordinate rank. The finite computations are diagnostics only. General correctness follows from the proof in `RESULT.md`; checking finite examples does not prove the all-degree statement.

The qualifying preprint first appeared on 12 November 2026. Independent mathematical validation has not been performed. Historical priority is provisional.
