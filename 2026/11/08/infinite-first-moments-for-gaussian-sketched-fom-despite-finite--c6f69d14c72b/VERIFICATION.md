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

# Reproducible analytic and computational checks

The main theorem is proven from Gaussian orthogonal and regression decompositions in `RESULT.md`. The finite computations below are consistency checks, not evidence of infinite-moment divergence by enumeration.

Run `python verify.py` with Python 3, NumPy and SciPy (`requirements.txt`). The program tests the exact SPD example, the derived Gaussian conditional-coefficient algebra, numerical density integrations for seven sketch heights, exact special-function probabilities, reciprocal tail constants, and finite Monte Carlo comparisons. The recorded output in `verify_output.txt` contains `PASS: 47 assertions`.

The exact analytic proof of the moment cutoffs is the density's strictly positive value at zero for FOM and the Student tail exponent for GMRES. Since finite random samples are almost surely non-singular, they can never establish the divergence of the first moment. The comparison is unconditional in exact arithmetic, includes every finite integer sketch height \(s\ge2\), and is restricted to \(\beta>0\), i.e. an initial vector that is not an eigenvector.

No independent scientific audit has been performed. The numerical sample is pseudorandom, finite and subject to statistical error; it does not evaluate the method under floating-point regularization or near-breakdown safeguards.
