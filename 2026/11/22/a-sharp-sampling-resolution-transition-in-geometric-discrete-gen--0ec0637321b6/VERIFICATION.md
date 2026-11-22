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

Analytical verification consists of (1) the exact geometric-maximum survival, (2) a sign-polynomial and generalized Descartes argument for continuous hazard shape, (3) monotonicity of integrated hazards across a unit sampling interval, (4) an exact algebraic first-step comparison, and (5) a derivative/limit proof of a unique resolution threshold.

Run `python check_hazard.py` using `mpmath` for independent arithmetic diagnostics: 378 parameter-grid sequences; 2,584 exact rational sign identities; two illustrative probability models with opposite discrete hazard shapes; a high-precision illustrative resolution root. These finite diagnostics do not certify all parameters or independently audit the proof.

Numerical precision limits deep-tail adjacent hazard differences; the checker ignores differences below its explicitly declared tolerance rather than interpreting floating-point equality as an exact statement. No external mathematical validation has been performed.
