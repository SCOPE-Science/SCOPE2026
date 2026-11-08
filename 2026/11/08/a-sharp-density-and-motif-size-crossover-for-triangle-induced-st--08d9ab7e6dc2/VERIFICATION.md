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

# Verification of the covariance identity

Run `python check_star.py` with Python 3 and the standard library. The program reports `PASS 3213 exact assertions` after the following exact tests.

The first test computes the joint probability of every fixed triangle/centered induced-star pair directly from their required edge-presence and absence masks, without using the closed formula. It compares this with the formula for all `3 <= n <= 10`, `2 <= r < n`, and five rational `p` values. The second test enumerates **all** simple labeled graphs on `n <= 6` vertices, with explicit Bernoulli weights at three rational edge probabilities, and computes covariance from separate means and joint means. It includes the known `r=2` case solely as a regression cross-check. The third test substitutes exact proposed zeros and tests both signs for integers `3 <= n <= 79`.

The pair-mask calculation, exhaustive graph calculation, and the formula involve different computational paths. All use Python rational arithmetic; no floating-point tolerances or unrecorded input files are required. These tests validate finite cases only. The analytic proof in `RESULT.md` proves the infinite family; no external audit or formal proof certification is claimed.
