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

Run `python3 checker.py` with Python 3, SymPy and NumPy. The checker constructs the pure projector without reading a certificate, applies four local depolarizing channels, and exactly integrates its degree-four attenuation polynomial. It verifies trace, Hermiticity, the stationary generator, all eigenvalue characteristic polynomials block by block, and off-block decoupling. It compares all partial-transpose eigenvalues with independent numerical diagonalization at thirteen distinct rational rate ratios and verifies strict positivity of the resulting density matrix. Recorded successful run: 429 individual numerical components and ten exact symbolic block-polynomial checks.

Finite tests do not prove the continuum of rates. The infinite statement is established by the exact algebraic block factors and polynomial sign identities described in RESULT.md. This is a self-review, not an independent scientific audit or an external formal proof certificate.
