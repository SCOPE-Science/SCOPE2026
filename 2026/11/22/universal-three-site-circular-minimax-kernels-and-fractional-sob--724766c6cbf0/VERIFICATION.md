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

# Verification and limits

The analytical argument is in `RESULT.md`: principal-matrix interlacing and circular-gap interval rigidity prove the general theorem; the Fourier sine Laplace representation proves strictly decreasing kernels for every \(s>1/2\); exact residue grouping and two local asymptotic expansions establish the limits. The hypotheses of these steps are explicitly checked in that proof.

`check.py` uses only the Python standard library. Executing `python check.py` in the directory containing that file passed **1,466** finite checks. These independently assemble finite Fourier Gram matrices, diagonalize them with symmetric Jacobi rotations, compare the sharp candidate against 720 random triples at four smoothness values, verify the previously known order-one formula, and stress-test the two large-smoothness limits.

Finite Fourier truncation, random numerical testing and convergence of computed roots cannot certify the universal assertions. The proof, not this script, is the evidence for all-exponent uniqueness and asymptotics. The root at the critical exponent is a **limit of optimizers** only, because point evaluation is unbounded at that exponent. No independent external audit has been performed.
