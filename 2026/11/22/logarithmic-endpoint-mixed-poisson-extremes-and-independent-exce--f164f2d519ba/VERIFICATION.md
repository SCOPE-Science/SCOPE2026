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

The analytical proof consists of a uniform conditional Poisson-tail comparison, an endpoint Laplace estimate with negligible off-endpoint mass, Stirling's large-deviation expansion, the iid maximum identity, and dominated normalization of the marked exceedance density. All are stated in `RESULT.md`.

Install the declared `requirements.txt` dependency and run `python mixed_poisson_endpoint_checker.py` for numerical diagnostics. At precision 175 decimal digits, the checker passed 50 assertions for intensities \(c=1/2,1,2\), multiple logarithmic sizes, the exact uniform-mixture identity, and conditional-mark kernel ratios. The finite diagnostics do not prove limits or establish historical originality.

No independent mathematical audit has been performed.
