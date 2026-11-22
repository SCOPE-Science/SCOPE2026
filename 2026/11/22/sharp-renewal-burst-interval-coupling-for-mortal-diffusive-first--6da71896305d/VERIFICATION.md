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

Run `python3 verify_coupled_bursts.py` with Python 3 standard library. The executed checker prints three tail-rate values and confirms exact rational finite-time recursions against a separate direct first-arrival enumeration for every integer horizon from \(1\) to \(12\), equal two-point marginals and mean flux, exact algebraic roots, and overshoot envelopes through horizon \(500\).

The mathematical proof is independent of these calculations: conditional particle independence yields the all-time survival product, the mortality-clock tail and minimum interval yield uniform multiplicative bounds, bounded optional stopping proves the exact exponential rate, and a swap inequality plus bounded quantile approximation gives the sharp coupling order. The checker cannot certify originality or infinite-time limits by itself. Relevant general dependent renewal–reward literature leaves residual publication-priority uncertainty, and independent audit has not been performed.
