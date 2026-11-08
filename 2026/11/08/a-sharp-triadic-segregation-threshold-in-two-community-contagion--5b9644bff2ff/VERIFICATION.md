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

# Verification instructions and limits

Run `python3 verify.py` with standard Python 3.9 or newer. No third-party library is required. The script checks the source-model equilibrium equations with exact rational arithmetic in quadratic extensions, independently differentiates the source vector field and verifies the symbolic Jacobian trace and determinant identities. It enumerates 544 physical parameter pairs and reports 120 stable and 424 saddle cases. It also checks the exact rational witness \(\varepsilon=9/10\), \(s=1/3\), \(d^2=2/27\), \(\lambda=9/2\), yielding trace \(-1\) and determinant \(6/25\).

The written proof supplies the all-parameter argument: physical interior conditions, determinant sign reduction, exact minimum of the stability boundary and a sum-of-squares proof that positive determinant forces negative trace. A separate symbolic identity check verified the displayed derivative, factorization and sum-of-squares identities. Finite computations alone do not establish the infinite theorem. No assessment is made of nonlinear stability at the critical nonhyperbolic equilibrium, basin volumes, stochastic dynamics, or independent external validation.
