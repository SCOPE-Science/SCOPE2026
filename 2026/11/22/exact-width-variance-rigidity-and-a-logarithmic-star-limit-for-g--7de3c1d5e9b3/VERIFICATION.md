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

# Mathematical verification and scope

Run `python3 verify.py` in the directory containing the files. The script uses Python standard-library quadrature, exact Prüfer-sequence degree enumeration, and independently seeded isotropic Gaussian directions normalized to a unit sphere. On the packaged source, it printed `DISCOTOPE_WIDTH_CHECK_PASS samples_per_graph=45000 graphs=20 trees=18247 c=0.2088435388 path_variance=0.2459703494`.

The exact first- and second-moment equations are proved by a Gaussian radius–direction decomposition and three edge-pair classes. The sharp tree extremizers follow from integer degree-excess inequalities, not finite enumeration. The path theorem follows from a one-dependent bivariate central limit theorem with explicit covariances and radial normalization. The star limit follows from conditional strong law of large numbers; its logarithmic edge comes from an explicit one-dimensional integral asymptotic. The checker is finite diagnostic evidence only. Numerical integration estimates the universal constant and cannot certify exact equality or any infinite asymptotic statement. Historical priority and independent mathematical validation are not certified here.
