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

Execute `python3 cactus_inertia_checker.py` in the directory containing this document. The checker is self-contained, uses only the standard library and `fractions.Fraction`, and verifies exact coefficients without floating-point thresholds. It computes each cycle's covariance by integrating separately over all \(k!\) order simplices, rather than copying the proposed closed form. It checks eight independently constructed cactus graphs and 238 entries of their covariance matrices, their exact traces, their weighted-Laplacian cofactors, and their spanning-tree counts. A separate full exact polyhedral triangulation of the non-cactus diamond checks its radial moment \(13/8\) (24 distinct signed coefficient images, 12 facets, 32 radial tetrahedra). Successful execution prints `CACTUS_UNIFORM_INERTIA_EXACT_CHECKS_PASSED 8 238` followed by the diamond certificate.

The checker tests finitely many instances, and cannot establish the all-parameter claim. The analytical argument proves the cycle decomposition, uniform product measure, Dirichlet gap covariance, weighted-Laplacian formula, volume identity, and extrema for all connected simple cactus graphs. No independent validation has been performed.
