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

# Reproducible verification and scope

Run `python3 check_weighted_cyclic_robustness.py` using a standard Python 3 installation. No third-party package, external data, network connection or hidden artifact is required. Its exact-integer tests include all binary cuts and all corners of the uncertainty cube for four through seven sites and three rational center weights, both at and above the proposed radius. It also exhaustively checks the elementary integer inequality in the proof for all parameter combinations up to 199 sites.

The recorded successful output is:

```
EXACT_CRITICAL_RADIUS_ALL_ENVIRONMENTS_AND_CUTS_PASSED 127680
EXACT_ALL_COMBINATORIAL_ROUNDNESS_CASES_PASSED 34324941
ROBUST_TWO_TAP_GINI_CHECKS_PASSED
```

These finite calculations check boundary cases and error signs. The general theorem for all finite cycle lengths, all allowed real probabilities, and arbitrary real signals follows from exact identities, the all-dimensional inequalities in the proof and the layer-cake argument. Independent mathematical audit has not been performed.
