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

# Computational verification and analytic boundaries

Run `python3 checker.py` using the Python 3 standard library. The script creates the full absorbing Markov equations for the first all-present hitting time, works entirely over exact rational numbers, and independently compares its solutions with the proposed integral formulas. It reports `PASS: 405 independent exact rational assertions`.

The checks cover twelve profiles for two, three, and four coupon types; at three distinct rational arguments the PGFs agree exactly. Additional checks cover five sizes and four budget levels for the sharp endpoint means and the concentrated geometric-factor law, independent exact polynomial sign certificates at the integer interlacing nodes, and strict pair-balancing inequalities. All verification code is embedded alongside the proof. No external data files or numerical tolerances are required.

The theorem for arbitrary finite \(m\) is supported by the analytic strong-Markov transform and strict-convexity argument in `RESULT.md`, not by an exhaustive computation over infinitely many parameters. The computational checks are regression and arithmetic checks only. A separate independent mathematical audit has not been conducted.
