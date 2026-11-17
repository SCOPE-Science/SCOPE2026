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

# Reproducibility and verification limits

Run `python CHECK.py` with Python 3, SymPy and mpmath. Successful execution prints three `*_OK` lines. The program reconstructs the exact cofactor identities for \(U=x^2+y^2-a^2\) and the torus equation, the exact angular formula and the orthogonal dot/determinant identities. It then compares both analytic return integrals with independent high-precision numerical quadratures in eight cases and checks explicit witnesses.

The essential mathematical verification is analytical: linearization in \(U\) **along the invariant torus** gives the normal variational equation, and the angular vector integral gives its full return exponent. The eight finite numerical cases check implementation only, not universal quantifiers. There is no formal proof assistant or independent third-party audit. No statement is made about the ambient three-dimensional normal multiplier, off-parallel periodic orbits, or nonlinear dynamics at unit Floquet multiplier.
