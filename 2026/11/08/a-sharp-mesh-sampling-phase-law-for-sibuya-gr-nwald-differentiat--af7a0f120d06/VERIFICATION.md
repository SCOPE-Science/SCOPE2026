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

# Reproducibility checks

Run `python verify.py` after installing the declared `mpmath` dependency. The script checks positivity and exact partial survival identities for the Sibuya distribution using rational arithmetic, first-order Gamma-quotient constants, beta-integral and bias identities, and the finite-variance leading-risk mesh equation. It prints `PASS 2062 checks`; that output was obtained in the current scientific package and is saved in `verification_output.txt`.

The proof of infinite second moments is an analytic comparison with a power series and is **not** inferred from the finite numerical tests. The first-order mesh-bias assertion also relies on an absolutely-continuous Riemann-sum remainder argument, which the script does not certify. The numerical improper integrals use a finite precision tolerance and are cross-checks only. No external independent review or validation is represented.
