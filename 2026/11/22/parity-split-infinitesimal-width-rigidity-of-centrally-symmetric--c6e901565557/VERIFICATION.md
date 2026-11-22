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

The analytical argument proves the result for every integer \(m\ge2\) and every \(\ell>0\). The companion `verify_geometry.py` is a deterministic, standard-library-only finite diagnostic. Running `python verify_geometry.py` returned `PASS checks: 9317 m=2,...,23, 24 random configurations/order, 7 perturbations/order`.

It tests the exact facet-normal formula against independent absolute directional projections, the global upper bound, Fourier eigenvalue identities, finite differences of minimum width, and the alternating-path formula. Numerical tolerances are explicitly specified in the code. Sampling is not an exhaustive search over configurations or a proof beyond the analytically demonstrated range.
