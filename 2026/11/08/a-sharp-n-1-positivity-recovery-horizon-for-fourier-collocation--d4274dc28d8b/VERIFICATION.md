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

# Verification scope

Run `python verify.py` from an extracted package with Python 3 and `mpmath` installed. The program uses high precision to compare periodized-Gaussian and Fourier expressions, bound omitted frequencies, verify mass preservation, and check sample signs. The package test passed **419 assertions**. The certificate of the asymptotic statement is the analytical proof in `RESULT.md`, not finite enumeration.

The independent-audit channel has not been exercised, and no separate expert or formal proof certification is asserted. The exact Fourier symbol and Nyquist convention, the requirement that \(N\) is even, the uniform \(t\ge c/N\) quantifier, and the negative near-antipodal construction are essential. The proof does not claim an exact finite-grid recovery time.
