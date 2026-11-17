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

# Verification of the uncentered maximal averaging variation coefficient

Execute `python3 check_c5_two_input_variation.py` from the directory containing this file. The script needs only the Python standard library and derives every allowed graph ball from the five-cycle metric, without a precomputed lookup file.

Checks performed: the \(96\) rational endpoint cases for three cut orbits; all \(5^5\) independently chosen ball-averaging matrices tested against the \(30\) nontrivial cut indicators, giving \(93,750\) exact matrix/cut comparisons; strict uniqueness of the five active averaging sets for each of two explicit nonnegative inputs; exact input and output difference variations and the quotient \(7/5\).

Expected terminal marker: `ALL_C5_UNCENTERED_BV_STABILITY_CHECKS_PASSED`. The exact finite arithmetic covers the bounded table and the explicit sharpness pair. The analytic argument in RESULT.md separately supplies the coarea reduction and the piecewise-affine integration of branch bounds, so the certificate does not incorrectly extrapolate finite sampling to larger graphs. No independent external mathematical audit has been performed.
