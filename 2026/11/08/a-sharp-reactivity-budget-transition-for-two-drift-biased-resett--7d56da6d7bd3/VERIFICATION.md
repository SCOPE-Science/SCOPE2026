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

# Reproducibility and verification

Run `python3 verify.py` with Python 3 (standard library only). The script performs 4,760 deterministic checks, including direct numerical inversion of the independently assembled Green-function matrix, phase-boundary uniqueness and downstream/interior optimizer checks, and a separate tridiagonal continuous-time random-walk approximation to the point killing problem. All checks passed on the supplied program before packaging.

The actual infinite-dimensional argument is the resolvent identity and strict local-time concavity in RESULT.md. Numerical grids neither establish global convexity nor exclude unexamined parameter regions; those facts rely on the written proof. The script samples a range of \(D,\mu,a,r,K\), tests the root equation, checks separate finite-grid optimizers around the transition, and compares with a discretized Markov generator. At the equal-drift boundary, symmetry and strictness are handled analytically.

A numerical nearest-neighbor approximation introduces a spatial discretization error; it is deliberately used only as an independent consistency check, with documented finite tolerance, not as a mathematical certificate. Independent audit and validation have not been performed.
