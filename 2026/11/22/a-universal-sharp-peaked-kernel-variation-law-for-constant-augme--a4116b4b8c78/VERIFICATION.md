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

# Reproduction and verification

Run `python3 checker.py` from the directory containing that file. The program uses only the standard library, solves constant-augmented interpolation systems, verifies nodal interpolation and constant reproduction, and compares sampled total-variation gains with the analytically proved limit for Gaussian and exponential profiles on irregular meshes. It also checks the exact single-step operator-norm reduction numerically against sampled random input vectors.

A successful replay prints `ALL_LOCALIZED_KERNEL_VARIATION_CHECKS_PASS`. The finite sampled variations are lower approximations to continuous variations; they do not establish any infinite-parameter limit, exact finite-scale extremum, or general strict positive definiteness. Those are respectively proved analytically in RESULT.md and assumed as stated for the kernel class. The calculation is supplemental and is not an independent mathematical audit.
