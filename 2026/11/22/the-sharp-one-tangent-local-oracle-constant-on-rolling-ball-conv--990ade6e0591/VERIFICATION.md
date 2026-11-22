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

# Reproducibility and boundaries

Run `python3 verify.py` with Python 3 and no third-party packages. The script computes exact Euclidean geometric solutions in floating-point arithmetic, verifies feasibility and the improved error bound for 3,000 reproducible planar-disk cases, and evaluates seven explicit sharpness instances. It prints `PASS` if every assertion holds. The exact algebraic argument in `RESULT.md` is the proof: finite numerical tests cannot prove uniformity over every convex body or all dimensions.

For the sharpness family with \(\varepsilon\downarrow0\), the script computes the ratio of the observed error to \(s^2/(2\rho)\), tending to one. The result requires exact tangent and ball projection, and the verifier does not assess membership-oracle perturbations or rounding error in a deployed optimizer.
