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

The proof derives the Gram entry formula by Möbius inversion on cyclic periods, diagonalizes it with the spatial discrete Fourier transform, and proves monotonicity through an exact nonnegative squared-sum representation. The only equality case is a length-two auxiliary word system, which forces the twice-odd-prime exception. Positivity of the smallest eigenvalue follows from a one-negative-coordinate primitive word.

Run `python3 check.py` with Python 3 and no third-party dependencies. The executed check passed the exact finite enumeration of all words at lengths 2 through 13, exact integer Gram identities, numerical Fourier eigen-equations and the finite subset-monotonicity check through length 200. These experiments are not an infinite proof; the preceding analytic identities cover all composite lengths at least four. Independent mathematical auditing has not been performed.
