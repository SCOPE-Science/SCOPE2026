---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and limits

Run `python verify.py` with Python 3 in the directory containing the embedded script. It tests 120 finite numerical identities for illustrative i.i.d. return mixtures, the conditional hitting ratio, truncations of the hyperbolic product, cumulant positivity and zero-rate limits. These checks do not test history-dependent returns or prove an infinite identity.

The analytic proof uses a killed-diffusion Dirichlet calculation, conditioning on the complete failed prefix, and the Euler product and positive Lévy–Khintchine representation. Almost-sure convergence follows from finite expected summand size. The hypothesis is independence of each fresh exploration and clock from its complete past; the return durations themselves need not be independent. Nonexponential interruptions and absorption during return are not covered.
