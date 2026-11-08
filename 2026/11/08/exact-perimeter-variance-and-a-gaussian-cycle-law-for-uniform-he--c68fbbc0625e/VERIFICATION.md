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

# Reproducibility and scope

The proof is in `RESULT.md`; `checker.py` is an independent finite numerical corroboration using an explicit fixed pseudorandom seed. Run with `python checker.py` in Python 3.10+ with NumPy installed. The checker computes central-binomial coefficients exactly as integer ratios, applies the explicit tail inequality, then runs 420000 independent hemisphere-triple observations and 420000 independently sampled five-cycles. The final marker is `HEMISPHERE_GEODESIC_CYCLE_VARIANCE_OK`.

The series truncation error for the variance rate after 32 terms is at most `pi*pi/(224*32**7)`; no experiments certify the CLT or substitute for its analytic derivation. The theoretical conclusion is restricted to independent area-uniform points on the unit hemisphere; labelled cycles with more than three vertices may self-cross. External mathematical validation and exhaustive historical priority checking have not been performed.
