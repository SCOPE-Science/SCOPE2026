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

# Reproducible exact checks

Run `python3 verify.py` in the directory containing the seven delivered files (no third-party packages needed). This reconstructs finite transition graphs at the three stated capacities, checks every polynomial balance equation for the explicitly listed stationary weights, recomputes the partition functions, first and mixed moments, covariance numerators, and unit-rate rational fractions. It also tests the exact sign-change and endpoint hypotheses used with Descartes' rule. All computations are performed with exact integer coefficient arithmetic and exact rational arithmetic for endpoints.

The scientific proof additionally explains why the finite reachable classes are the unique recurrent classes and why the polynomial roots yield the asserted complete signs on the stated rate domain. No samples of \(t\) are used to prove an all-parameter claim. The verifier does not inspect capacities greater than three, prove publication priority or replace an independent scientific audit.
