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

# Verification and limits

The analytical proof in `RESULT.md` establishes all-parameter claims within the stated two-zone exponential-clock model. Run `python3 check.py` with Python 3 and no additional packages. A successful replay prints `PASS: 7146 diagnostic assertions`.

Checks consist of 1,200 exact rational first-step balance assertions; numerical spectral interlacing, positivity and unique-crossing signs on 240 deterministic randomized parameter tuples; independently computed four-state uniformization for five observation horizons per tuple; 100 further nonreactive and faster-storage boundary cases, monotonicity comparisons, and six small-rate endpoint diagnostics. These are finite consistency tests, not exhaustive verification of continuum parameter values or empirical field measurements.

The proof's strict convexity step assumes \(0\le\ell<k\), including the nonreactive case, and the coupling argument separately treats \(\ell\ge k\). The logarithmic asymptotic is only as \(\ell\downarrow0\) with other positive rates fixed. No alternative non-exponential transport law is validated. Independent external audit has not been performed.
