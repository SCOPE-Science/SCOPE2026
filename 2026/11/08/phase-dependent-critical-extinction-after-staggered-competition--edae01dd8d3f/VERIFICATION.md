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
Run `python verify.py` in the directory containing this document, with a recent Python 3, NumPy, and SciPy available. The script evaluates the two-impulse Poincaré map and its numerical derivative and compares its center-direction quadratic decrement with the exact \(\kappa_\phi\) integral for three distinct pulse offsets. It checks the logistic resident cycle and its period integral, the neutrality eigenvalue, and strict phase ordering. Successful execution outputs the `VERIFY_OK` line and a table of analytic and finite-difference coefficients. In the displayed example the parameters are \(a=b=d=e=f=T=1\), \(c=1/2\), and \(m_x=m_y=1/2\).

These checks sample one admissible parameter set and cannot establish the exact theorem for all parameter values. The universal mathematical support is the analytic logistic identity, exact log-balance reduction, smooth center-manifold argument and reciprocal-iteration proof in `RESULT.md`. Numerical derivatives depend on ODE solver tolerances; the script reports a modest finite-difference tolerance. The local basin is not quantified and definitive historical priority is not certified.
