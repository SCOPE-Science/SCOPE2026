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

# Finite integer checks
Run `python check_fan_walsh.py` from the directory containing the standalone checker. It independently enumerates spanning trees as connected acyclic edge subsets, performs exact-integer Walsh transforms of the indicator, computes signed tridiagonal determinants, and compares every frequency for all \(1\le n\le9\). It checks exact tree totals, existence of zero frequencies, sharp nonzero absolute multiplier magnitude, greatest common divisor, and distinct zero witness masks. It also checks the explicit signed continuant witnesses for \(1\le n\le150\).

Observed success marker: `FAN_WALSH_EXACT_PASS n=1..9 full spectra; n=1..150 witnesses`.

For \(n=3,6,9\), direct exhaustive Fourier-zero counts are respectively \(10,304,10362\); these are checks only, not an extrapolated formula for all resonant sizes. The claims for arbitrarily large \(n\) rest on the analytic recurrences and explicit null vector in `RESULT.md` rather than on enumeration. Independent external review has not been performed.
