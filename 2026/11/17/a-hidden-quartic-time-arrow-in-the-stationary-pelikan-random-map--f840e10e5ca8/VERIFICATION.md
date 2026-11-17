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

# Analytical and reproducibility checks

The proof identifies the invariant law with a geometric-depth/uniform-bit mixture, proves path-wise stationarity and detailed balance of the depth walk, computes all degree-at-most-four binary shift moments needed using exact finite sums, then transfers the reversal of two-time moments to those shift identities. Positivity follows from an explicit positive-probability event for every positive integer lag; it is not extrapolated from finite enumeration.

Running `python3 verify.py` from this package requires only the Python standard library and returns the marker `VERIFY_OK`. It performs 32 exact shift-moment comparisons for eight shift lengths, four independent one-step direct-branch integrations using the exact stationary fourth moment, and 28 exact finite-path evaluations across four probabilities and seven lags. Such checks do not independently prove the infinite-lag assertions, priority, or an external audit.

No mathematical result is claimed for \(p=1/2\), nonstationary initialization, full-path time reversibility, or arbitrary three-time cubic moments.
