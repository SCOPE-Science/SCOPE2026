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

The included `checks/escape_checker.py` passed when run with Python, SymPy and SciPy. It checks the analytic reciprocal-height expansion and indicial roots, the explicit \((a,b,c,p,\kappa,X,Y,Z)=(1,0,2,3/4,3/2,1,1,10^4)\) inequality instance, and independently integrates the equations with increasing \(z\) as the independent variable to test the stated large-height asymptotic amplitude and finite-time horizon.

The proof of the all-parameter conclusions is in `RESULT.md`: exact reduction on the invariant axis; regular-singular second-order theory and reduction of order; uniform strict invariant-tube inequalities; and an integrable variation-of-constants estimate for the normalized nonlinear transverse amplitude. Numerical integration cannot prove those infinite claims. The regular-singular asymptotics are for a linearized system, not a statement about nonlinear stability for \(c\le1\). Neither source publication priority nor an external mathematical audit is certified.
