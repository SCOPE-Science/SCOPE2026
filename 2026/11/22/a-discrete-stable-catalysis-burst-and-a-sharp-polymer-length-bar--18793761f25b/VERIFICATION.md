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

# Verification and reproducibility

The accompanying standard-library `check.py` enumerates short ordered reaction counts, checks the exact Pareto-half no-link integral against quadrature, and recalculates finite cutoff probabilities and their asymptotic scaling. It verifies the explicit \(n=60\), \(\ell=28\) example and checks positivity and initial coefficients of the Sibuya mark distribution.

Run with `python check.py`; successful execution prints `checks passed` with the finite examples. All parameters are spelled out in `RESULT.md`. The program does not simulate existence of an RAF, prove a limiting distribution or replace the analytic argument. For the nonvacuous RAF probability-one assertion, the independent mathematical input is Kim and Sönmez (2026), Theorem 8, specialized as specified in `RESULT.md`.

Proof limits: model-specific asymptotics and a necessary molecular-length obstruction, not an exact minimal RAF length or finite-dimensional chemical-kinetics certification.
