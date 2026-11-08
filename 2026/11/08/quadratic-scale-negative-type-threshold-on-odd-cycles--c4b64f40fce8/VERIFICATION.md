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

The proof uses the exact circulant spectral formula for every odd cycle, a \(p=1\) trigonometric identity, a uniform Taylor remainder, a uniform Abel summation bound, and the strict separation of the limiting even-frequency derivatives. These exact arguments establish the infinite-family result without computation.

Run `python3 check_odd_cycle.py` in the same directory. It requires Python 3 standard-library modules only. It checks all nonconstant exponent-one Fourier eigenvalues for odd orders 5, 7, 9, 11, 21, 51, 101, 201, computes the first numerical zero among their modes, compares a numerical quadrature of the asymptotic constant, and checks the published four-point roundness formula. The expected terminal marker is `ODD_CYCLE_NEGATIVE_TYPE_FINITE_CHECKS_OK`.

The numerical roots, finite sample sizes, and quadrature do not certify the infinite sign comparison, the general theorem, novelty, or independent validation. A high-frequency uniform estimate and the exact integral comparison supply those steps analytically.
