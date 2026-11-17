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

The accompanying `check_depth.py` is standalone Python standard-library code. Invoke `python check_depth.py` in the extracted directory. Its deterministic numerical tests compare the exact two-branch CDF with independent one-dimensional radial/angular integration, check the mean against nested integration, and compare the first cap-overlap threshold for three distinct positive radial densities. The final checker completed **116 independent checks** successfully.

The proof in `RESULT.md` independently derives all claimed universal statements: the polyhedral reduction, the cap-union law and strict overlap, the exact uniform-disk CDF with its derivative jump, and the mean/bias formula. The checker has finite scope and floating-point tolerance and is not an exhaustive or formal proof. The general polyhedral reduction is a credited pre-existing result. Comprehensive historical priority and independent verification remain unperformed.
