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

# Verification scope

From the extracted package root, run `python checks/verify_helix_acute.py`. The checker uses only Python's standard library and reports the critical scalar root, its pitch value and the sharp onset coefficient. It checks angle-dot identities against independent Cartesian calculations, a finite representative grid against the analytic bound, and deterministic integration near extinction. The exact all-parameter assertion follows from the concavity and one-variable strict-derivative argument in `RESULT.md`; no finite enumeration or quadrature is claimed to prove a continuum maximum.

The proof's critical steps are: (i) scalar-product identities for all vertices, (ii) strict log-sinc concavity for the equal-gap maximizer, (iii) strict monotonicity of the reduced critical equation, (iv) positivity of both Hessian eigenvalues, and (v) area-rescaled dominated convergence for the rare-event probability and conditional law. The mathematical result remains to be audited independently.
