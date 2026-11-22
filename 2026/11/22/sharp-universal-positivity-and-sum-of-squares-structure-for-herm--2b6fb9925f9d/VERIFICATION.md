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

# Verification of the Hermite-truncation positivity theorem

The proof uses two formal generating-function identities, a nonnegative binomial-series convolution, and a rigorous central-binomial asymptotic sign argument. In particular the infinite theorem is not based on tests.

The accompanying standalone Python 3/SymPy source `verify_hermite.py` makes 528 exact rational or symbolic assertions. Reproduce with `python verify_hermite.py` from the extracted files; the expected output is `PASS: 528 exact rational/symbolic assertions`.

The checks compare expanded Hermite polynomials and the claimed sum-of-squares expansion for degrees through 24 at five rational parameter values, including the two endpoints; six real rational evaluations are checked at each degree/parameter pair. They also exercise sample failure parameters outside the sharp interval. No finite verifier can replace the all-degree proof, and no assertion is made about exact Gaussian Gram-system quadrature weights or independent certification.
