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

# Verification and replay

Run `python check.py` with Python 3 and `mpmath`. The script independently compares the exact \(\gamma=1\) complex Beta-function coefficient against direct quadrature for 6 choices of degree, Fourier shift, and weight; it checks 6 dephased coefficients across the three regimes; and it checks 3 Gamma-modulus identities. Successful observed output:

`BERGMAN_SPIRAL_BETA_GAMMA_CHECKS_PASS 15`

The proof's universal quantifiers are not certified by those finite tests: the \(L^1\) Gamma boundary-layer limit, the three phase cases, the compactness of vanishing weighted shifts, and the Hardy Toeplitz spectral consequences are analytical. In particular, tests do not establish priority against unavailable literature, numerical uniformity as parameters change, or full operator spectrum.
