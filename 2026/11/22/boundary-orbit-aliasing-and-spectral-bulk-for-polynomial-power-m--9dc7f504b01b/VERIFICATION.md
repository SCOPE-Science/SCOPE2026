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

# Verification and limitations

The exact monomial coefficient formula was independently derived by direct integration and checked in several polynomial cases. The identity \(\mathcal C_{g,k}\equiv k^{-(\alpha+3)/2}g(S)V_k\pmod{\mathcal K}\) follows from the fixed-degree Gamma-ratio limit and compactness of diagonal weights converging to zero. Orthogonality of the residue channels, Toeplitz symbol calculus, Weyl sequences at a boundary zero, the coefficient projection dimension argument, and finite-band Toeplitz normalized moment limits provide proofs of the infinite-dimensional claims.

Run the included `check.py` with Python 3 (standard library only). Its actual output was `POLYNOMIAL_ALIAS_COMPANION_FINITE_CHECK_OK 2368`, covering cyclic-average identities, several weighted Gram tails, monomial exact rational norms, contrast examples, and two finite-section trace moments. These are finite supplementary checks, **not** a proof that a compact difference holds or that a spectral limit is exhaustive.

The earlier two-channel slant Toeplitz norm is acknowledged as prior coverage. General analytic weighted-composition literature might implicitly contain stronger statements than the material accessible for comparison. Independent mathematical validation has not been performed.
