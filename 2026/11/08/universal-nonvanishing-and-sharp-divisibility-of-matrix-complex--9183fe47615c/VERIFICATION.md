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
The proof uses two exact finite-field orthogonality identities and Möbius inversion with \(\mu(U,W)=(-1)^{\dim W-\dim U}q^{\binom{\dim W-\dim U}{2}}\), followed by an exact valuation comparison. The comparison is strict for every lower rank and every nonzero subspace term, including field size \(q=2\) and \(n=2\).

To reproduce, execute `python3 check_zero_product_fourier.py` using Python 3 (standard library only). The checker enumerates all Fourier frequencies for \((n,q)=(2,2),(2,3),(2,4),(3,2)\). It verifies integer coefficients using exact Walsh and Eisenstein-arithmetic transforms, the point count, modular congruence, nonzero spectrum, and attained least and greatest singular values. Expected final line: `ALL_ZERO_PRODUCT_FOURIER_CHECKS_OK`.

No numerical experiment is used as an infinite proof. No independent audit or external certification has been performed. Literature novelty remains subject to independent historical verification.
