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

Run `python3 check_friendship.py` using Python 3. No optional packages or data files are required. The program enumerates full permutations on \(2m+1\) labeled graph vertices for \(m=1,2,3,4\); it checks all \(6^m\) normal-cone orientation classes, exact factorial coefficients and collision probabilities. The expected terminal line is `FRIENDSHIP_ANGULAR_SPECTRUM_PASS`.

The analytic asymptotic relies on a proved strict global maximum of a two-variable polynomial kernel at two corners and a dominated-convergence Laplace calculation; finitely many exact cases alone cannot establish that limit. Normal-cone angles use isotropic Gaussian directions in the affine direction space. The verification status here is only self-review; there has been no independent validation.
