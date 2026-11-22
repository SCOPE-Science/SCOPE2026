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

# Verification record

Execute `python checker.py` after placing the standalone checker alongside this file. Dependencies are Python 3, NumPy and SymPy; the program needs no network or datasets. It executes exact symbolic rational identities, compares explicitly integrated stationary density matrices against a separately assembled and solved 16-dimensional Lindblad-resolvent matrix, independently reconstructs the real Pauli correlation singular values and Wootters spin-flip eigenvalue concurrence, and checks the strict and equality sides of the CHSH threshold over positive and one-sided loss rates. The run passed 6,895 assertions.

This is a finite computational consistency check and is not a computer-assisted proof of the continuum assertion. The global correctness proof instead uses the explicit resolvent formula, an exact factorization of the witness difference, positivity of the balanced-source envelope and strict monotonicity of the loss-product formulas. The symmetric equal-loss limit agrees with the previously published result; the asymmetric ordering is the assessed additional statement. No external scientific audit has been performed.
