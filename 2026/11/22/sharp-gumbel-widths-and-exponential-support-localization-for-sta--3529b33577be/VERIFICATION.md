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

# Verification and reproducibility

Run `python VERIFY.py` using the Python standard library. The script checks all deterministic stack-sorting orbits for sizes three to twenty-five, the exact orthogonal Gram matrix at each size, and the finite Gaussian joint-CDF expression at a sample point. It reports the finite exceedance sums for selected dimensions; the sums converge slowly and do not certify any infinite limiting distribution. The limiting theorem is established analytically by the normal-tail Riemann sum, two independent limiting marked Poisson processes, and spherical-Gaussian norm concentration documented in `RESULT.md`.

There has been no independent external audit or formal machine proof. The cited public works are background, not independent certification of the new theorem.
