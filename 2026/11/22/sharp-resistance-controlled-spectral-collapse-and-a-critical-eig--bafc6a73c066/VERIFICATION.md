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

The analytical argument uses the weighted endpoint Cauchy–Schwarz estimate, parity reduction, the normalized reciprocal-weight test, and the exact identity for the energy distance between the actual odd ground state and the resistance-coordinate test. Its only asymptotic inputs are explicit elementary integrals and \(\log((1+\epsilon)/\epsilon)/\log(1/\epsilon)\to1\). These cover the complete infinite-dimensional claim; finite tests are not substituted for proofs.

For reproducible finite diagnostics, run `python check.py` with Python, NumPy, and SciPy. The script integrates the weighted Sturm–Liouville first-order system in logarithmic coordinates, brackets the first odd eigenvalue by a sign-changing flux residual, and tests the two rigorous mass–resistance bounds, eigenfunction monotonicity, normalization, and finite-profile proximity. Eight prescribed parameter cases passed; solver tolerance does not certify roots or limiting statements.

Correctness, originality and mathematical value were assessed in the accompanying review. No independent validation or external audit has been performed.
