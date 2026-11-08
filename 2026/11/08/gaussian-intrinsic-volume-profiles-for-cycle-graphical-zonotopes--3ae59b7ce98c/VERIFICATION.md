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

# Reproducibility and mathematical limitations

Run `python verify_intrinsic.py` with Python 3. The script uses only the standard library, recomputes integer Gram determinants independently of the component-count proof, and compares cycle-forest wedge sums to cyclic-composition coefficients. It additionally computes full intrinsic-volume profiles through dimension \(149\) and compares their finite distributions with the explicit asymptotic constants. Successful output includes `CHECKS_PASS` with 4160 finite checks. The asymptotic theorem is proved analytically in `RESULT.md`; finite checks neither establish convergence nor prove historical originality. No independent mathematical audit has been performed.
