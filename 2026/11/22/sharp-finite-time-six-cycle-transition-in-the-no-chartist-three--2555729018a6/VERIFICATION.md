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

Run `python3 check_six_cycle.py`. The standard-library checker enumerates all nine possible normalized states for representative parameter values in each of the three graph regimes \(0<h/d<1\), \(1\le h/d<2\), and \(h/d\ge2\), verifies their directed edges, absorbing bounds, six-cycle closure and distinctness, and checks several arbitrary rational off-grid initial states and threshold-equality cases.

The complete real-plane classification follows analytically from two-step entry into the exact nine-point graph. Finite tests alone would not establish infinite-input coverage without this proof. The measure result uses invariance and finite-time capture, not statistical sampling. The independent audit has not been performed.
