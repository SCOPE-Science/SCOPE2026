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

The proof is analytic; the included `CHECK.py` provides independent finite checks of its formulas. Execute from the extracted package directory using `python CHECK.py` with SymPy and NumPy installed.

Observed result:

`CHECK_OK symbolic_Fourier_eigenbases=5 angular_exact_identities=6 singular_boundary_tests=3`

The checker exactly computes Fourier transforms of the five polynomial-times-Gaussian basis elements through differentiation and exactly verifies \(A=2B+B''/2\). Its six positive-angular-polynomial area calculations use a dense angular quadrature, including a case in which \(A\) is negative on a short angular arc and the positive-part correction is needed. Three asymptotic-scale tests check the singular boundary mechanism. Quadrature cannot establish the sharp inequality or equality conditions for all real parameters; those follow by integration by parts and the explicit zero-order argument in RESULT.md.

Scientific limitations: the claim applies only to planar degree-at-most-four real Gaussian-polynomial \(+1\) Fourier eigenfunctions vanishing at zero. It does not settle the general definite-set uncertainty principle. Independent audit has not been performed.
