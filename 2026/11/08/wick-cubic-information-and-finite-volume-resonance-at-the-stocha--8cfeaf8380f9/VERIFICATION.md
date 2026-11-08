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

# Reproducibility and scope
Run `python3 verify_wick.py` in the extracted file directory. Verified output: `VERIFY_OK checks=182 finite_lengths=2 resonance_cases=2 continuum_eta=6`.

The program uses Python standard library exact fractions for 162 Gaussian moment identities and floating-point checks for large-volume convergence, 6 finite-resonance comparisons and 6 independent quadrature evaluations. Total 182 checks. Quartic-integral equality, continuum limit and every-parameter resonance behavior are established analytically in RESULT.md, not certified by the finite tests.

No independent audit or external validation was performed. The theorem is restricted to the conditional Gaussian linear-baseline score rather than global nonlinear dynamics.
