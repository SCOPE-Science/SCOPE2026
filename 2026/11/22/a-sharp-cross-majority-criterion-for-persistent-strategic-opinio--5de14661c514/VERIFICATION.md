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

# Verification

Run `python3 check.py` with Python 3 and its standard library. The script performs 1,579 exact-rational criterion and cycle tests, checks a four-vertex primitive network and the exact orbit at inertia \(\alpha=99/100\), and verifies full-dimensional strict-branch contraction for sampled states. It returns `VERIFY_OK` if all assertions pass.

The general theorem is certified by the algebraic two-step elimination in `RESULT.md`, not by finite testing. All purported cycles have strict margin from quantizer thresholds; the tie-breaking convention is never invoked. The published article's strategic interpretation is confined to fixed stationary two-bin Bayesian codes and synchronous updates. Literature searches cannot establish universal absence of earlier equivalent statements; no independent audit has been performed.
