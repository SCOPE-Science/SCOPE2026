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

# Reproducibility

Run `python CHECK.py` in any Python 3 environment with its standard library. The check script performed 930 exact-fraction and numerical assertions across weighted ball moments, the boundary sphere, and a two-shell singular mixture; homogeneous polynomials and mixed-degree test symbols; and exact coordinate finite-cutoff checks. No external data, compiler or third-party package is needed.

The checker verifies finitely many instances and does not formally certify the infinite-dimensional result. The proof uses the monomial reproducing-kernel identity, commutator telescoping, radial moment concentration, and dominated convergence/Fatou. Neither full publication priority nor independent mathematical auditing has been established.
