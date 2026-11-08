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

# Reproducibility

Run `python verify_dual_homology.py` with both included Python scripts in one folder. The program directly enumerates \(D=A+\varepsilon B\) satisfying \(A^2=0\), \(AB+BA=0\), computes exact kernels and images of the full underlying-field differential, determines the rank of the induced scalar-\(\varepsilon\) action on homology, and checks all joint multiplicities against separate Gaussian flag counts. The extension-field configuration is handled by explicit \(\mathbb F_4\) arithmetic.

Six exhaustive configurations and 32 further symbolic parameter checks passed; see `homology_verification.log`. The full theorem for all dimensions and characteristics is proved in `RESULT.md`; finite verification alone does not establish it. No independent audit has been performed.
