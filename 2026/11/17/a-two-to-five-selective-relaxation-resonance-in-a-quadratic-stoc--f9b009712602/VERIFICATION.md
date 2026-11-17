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

# Reproduction and scope of verification

Execute `python verify.py` with Python 3 and SymPy. The expected marker is `QUASI_NONVOLTERRA_SELECTIVE_RESONANCE_OK`.

The checker verifies exact scalar and transverse polynomial identities and all numerical rational coefficients with SymPy, including \(\delta=\pm9/28\), the asymptotic transverse factor \(160\delta/81\), and the selective constant \(-20/63\). It also performs long finite trajectory comparisons at both resonance ratios and a special fixed-center trajectory. The trajectory computation uses the simplex-preserving triangular variables to avoid floating-point summation drift.

No finite run can prove the full \(n\to\infty\) statements. The actual proof is given in `RESULT.md`, including the global two-step reduction, inverse-square increment limit, contracting transverse recurrence, and exceptional initialization. No independent mathematical audit was performed. No claim of external certification is made.
