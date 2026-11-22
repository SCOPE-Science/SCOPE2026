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

The separately embedded `CHECK.py` enumerates all ordered pairs of equal-size subsets independently of the generating-function derivation and counts those with no matching ordered coordinates. It checks every chain size from zero through ten against a convolution recurrence and reproduces the known scalar totals. The accompanying `CHECK_OUTPUT.txt` contains the actual successful run.

The limit-law proof is symbolic: a fixed-point criterion, inclusion-exclusion, explicit square-root singularity, uniform transfer, and differentiable moment-generating functions. No finite computation purports to establish an infinite limit. The large-deviation principle concerns closed and open subsets of the compact interval; the endpoint lower bounds follow from continuity of its rate. Independent mathematical audit and original full-text priority validation have not been performed.
