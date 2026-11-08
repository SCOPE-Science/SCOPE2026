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

# Verification and limits

Run `python3 verify.py` using Python 3.9+ and only the standard library. The recorded output in `verification_output.txt` is `PASS: 396 exact-rational assertions; no infinite claim relies on grid sampling.` The verifier checks the matrix-free scalar amplification identity, imaginary-axis numerator, sharp threshold and high-frequency boundary equality at rational parameters, the exact symmetric-law stability polynomial, and strict positivity in representative nondegenerate centered laws.

The general half-plane theorem uses the subharmonic maximum principle, strict interior contraction, and a rigorous limit at infinity, not finite sampling. The universal centered-law statement uses the independent-copy covariance identity. The fourth-order weak-damping expansion uses uniform Taylor expansion for coefficients in the compact unit interval and the real-analytic implicit-function theorem. No full finite or computational enumeration can certify these infinite-parameter assertions by itself.

The supporting code is a reproducibility aid, not an independent audit or formal proof certificate.
