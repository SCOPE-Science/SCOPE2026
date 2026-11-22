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

# Verification record

The analytic proof in `RESULT.md` uses discrete convexity to establish a strict unique maximum of the relevant positive spectral ratio at frequency \(k\) when \(0<\alpha<1\), a flat tail when \(\alpha=1\), and divergence at infinity when \(\alpha>1\). The Fourier-product identity and the rank argument are exact.

The standalone `check.py` was run with Python 3 and the standard library. It passed 82,183 assertions, including exact Fraction identities for the Poisson endpoint and finite-grid sign checks for all three regimes. The sampling tests do not prove the universal theorem. The claimed equalities, domain, strictness, and limitations are derived in `RESULT.md`.

The research record has a self-review. Independent audit has not been performed.
