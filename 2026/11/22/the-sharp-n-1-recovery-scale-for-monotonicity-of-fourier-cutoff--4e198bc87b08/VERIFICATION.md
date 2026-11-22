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

# Reproducible checks

Run `python3 verify.py` with Python 3 and the `mpmath` package. The recorded execution passed 585 finite high-precision assertions: theta-product/image identities, derivative identities, sign diagnostics on both parities at selected cutoff sizes, and convergence of the normalized leading omitted-frequency tail. The analytic argument in `RESULT.md` proves the infinite and uniform assertions; finite tests are not exhaustive and do not certify the limiting constant independently. No interval-arithmetic certificate or independent audit has been produced.
