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

The proof is all-size and uses the spectral theorem for finite real symmetric matrices, the Rayleigh principle, and the elementary graph-Laplacian bound \(\|L_s\|\le4\). No computer computation is required for the mathematical inequalities.

Reproduce corroborating calculations by running `python3 checker.py` from this package directory. The standard-library checker constructs exact rational rejected-jump transition matrices and evaluates the proposed optimum for \(2\le n\le19\). Independently, a symmetric Jacobi eigenvalue routine tests 150 random proposal laws at each size \(2\le n\le13\) against the global inequality; proposals include nonzero wasted mass. The observed program output was `PASS: 15483 exact identities or independent numeric inequalities`.

Finite tests are not an infinite proof. The coefficient on the shape-deviation term is not claimed optimal. No independent review or publication-priority audit has been performed.
