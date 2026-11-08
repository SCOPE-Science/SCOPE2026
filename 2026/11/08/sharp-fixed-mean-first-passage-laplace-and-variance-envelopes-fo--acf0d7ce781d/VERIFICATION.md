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

# Verification notes

The stated theorem is supported by four analytic arguments: Brownian free first-passage Laplace transform and the full renewal identity; strict Jensen and secant-chord inequalities at each positive Laplace frequency; direct differentiation of the full transform at zero for mean and variance; uniqueness of Laplace transforms of tilted reset-distance measures. Its quantitative assumptions are in `RESULT.md`.

To reproduce the computational diagnostics, run `python3 verify.py` in the directory containing the extracted package. The script uses only Python's standard library, checks an explicit strict same-mean different-variance pair and transform inversion, and tests a broad fixed-mean family with separately calculated numerical differentiation. Finite diagnostics cannot establish the all-frequency inequalities or uniqueness; those are analytic statements proved separately.

The original renewal transform, variance formula and long-time approximation were already obtained in Méndez–Flaquer-Galmés–Campos (2024). The present theorem does not claim a new renewal formula, and makes no claims about independent expert or formal verification.
