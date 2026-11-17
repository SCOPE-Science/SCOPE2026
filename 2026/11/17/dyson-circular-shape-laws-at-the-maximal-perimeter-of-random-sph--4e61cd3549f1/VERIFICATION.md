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

The proof is analytic, with numerical corroboration only. `check_perimeter.py` integrates the exact angle-conditioned spherical event using Gauss–Legendre quadrature and beta CDFs. It checks the exact constant at dimensions four and six, validates the circular normalizer at two exponents, and compares finite-threshold probabilities to the leading asymptotic in dimensions three, four, five, six, and eight. Required dependencies: Python 3, numpy, scipy. Execute `python check_perimeter.py` in the directory containing this file.

The total-variation claims are proved from pointwise joint density convergence plus domination, not from finite simulations. A relevant older full text was not accessible; historical priority remains provisional. Independent audit has not been performed.
