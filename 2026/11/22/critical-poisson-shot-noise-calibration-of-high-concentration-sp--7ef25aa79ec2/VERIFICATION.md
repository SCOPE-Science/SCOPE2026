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

The independent audit channel has not been run. The full analytic argument is in `RESULT.md`; the reproducibility script `check.py` uses only NumPy and SciPy and checks kernel normalization, the Poisson semigroup, the finite-sample and limiting covariances, the beta cumulants and rare-distance count calibration. Run `python check.py` from the extracted directory.

The checker passed 202 assertions with a fixed random seed. These finite calculations do not prove point-process convergence, the uniform tail bound or Gaussian endpoint by themselves; those are justified analytically in the proof. The published-source comparison checks originality to the extent of accessible materials, not historical uniqueness.
