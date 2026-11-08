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

# Verification and scope

Run `python verify.py` with Python 3 and the standard library. The verifier checks rational coefficient and covariance identities, direct spectral-radius classification on both sides of several thresholds, and representative asymptotic regimes. The proof in `RESULT.md`, rather than sampling or numerical tests, establishes all real-parameter conclusions. The numerical scheme is Euler–Maruyama for the **Itô version** of the stated reversible-noise SDE. The target covariance is the covariance of the continuous-time diffusion, not that of the numerical invariant law.

Directly examined literature: arXiv:2610.03191 §§3.1/6.1/7; arXiv:1903.03024 §§1–3; arXiv:0912.1968 §§2–4. Only the abstract and bibliographic record were accessible for DOI:10.1137/090771843. The exact-model historical priority may therefore require an additional literature assessment. No independent audit or universal computer certification is claimed.
