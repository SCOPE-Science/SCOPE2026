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

# Verification details

The analytic claim is proved by the quadratic Gauss-sum identity and two two-dimensional parity blocks in `RESULT.md`. Their characteristic polynomials, strict eigenvalue comparisons and eigenvector equations establish the infinite prime-family assertion. The classical positive Gauss-sum sign is supported by Satake, Lemma 11 (arXiv:2011.02907); no computational extrapolation is used for an infinite claim.

Run `python check_paley.py` with NumPy installed. The test enumerates the nonzero quadratic residues independently of the spectrum formulas, constructs the Fourier sampling matrix and its Gramian, checks all four singular-square values against the exact expressions for each of 37 primes below 400 in all four residue classes, tests the character-sum Gram formula independently, and asserts the exceptional two-dimensional kernel at \(p=5\). The observed maximum absolute error was \(6.11\times10^{-16}\) in IEEE floating arithmetic. Numerical tolerance is \(5\times10^{-12}\). These experiments are finite corroboration only, and floating-point outcomes are not exact arithmetic certificates.

The formula does not cover primes congruent to three modulo four, other sampling masks, or nonconsecutive frequency bands. A separate specialist bibliographic assessment and independent mathematical audit have not been performed.
