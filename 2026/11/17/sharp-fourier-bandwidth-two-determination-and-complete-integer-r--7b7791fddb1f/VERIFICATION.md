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

The proof uses the exact Fourier transform of one interval, Cartesian factorization, the double-angle identity, \(\sin^2 u+\cos^2 u=1\), and strict monotonicity of \(\sin u/u\) on \((0,\pi)\). These establish the all-dimensional reconstruction theorem, exact integer-side alias classification, first-bandwidth special case, and sharp bandwidth-two counterexample.

A separate Python standard-library script is available at `verification/check.py`. From the package root execute `python3 verification/check.py`. The script directly evaluates Fourier transforms of randomly generated boxes, reconstructs their integer-frequency coefficients using only the prescribed samples, and checks a planar first-frequency-cube ambiguity witness. On the saved candidate source it reported 43,460 passing numerical assertions, including the positive frequency-two separation of the witness. The script is supplementary, not an exhaustive mathematical certificate; the infinite claims rest on the written analytic proof.

There is no independent external audit. No numerical noise-stability guarantee is asserted, and no uniqueness is asserted for unknown centers on integer-width axes. The analysis concerns exact complex measurements and fixed axis coordinates only.
