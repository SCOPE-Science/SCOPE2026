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

Run the self-contained Python 3 program `check.py`. It uses only the standard library and prints `PASS: 3276 finite diagnostics` upon completion. The checks include rational binomial-log iteration identities for three transform parameters and three stretch exponents, the quadratic moment identity, and the finite-binomial absolute-deviation identity. Additional numerical diagnostics compare the Laplace norm exponent and Schatten leading factor at three increasing iteration counts.

The normal limit, global Gaussian domination, and infinite Schatten-sum asymptotic are mathematical arguments in `RESULT.md`, not assertions certified by finite sampling. In particular, the diagnostics do not establish originality, independent verification, or external certification.
