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

The standalone Python 3 checker `verify_zone.py` uses only standard-library modules. It compares the analytic identity with five Simpson-integrated two-point great-circle formulas and separately samples direct surface-area-uniform endpoint pairs at three widths. Each sampled geodesic is tested by exact optimization of its vertical sinusoid over the full shorter arc; no point grid is substituted for that optimization.

At widths \(0.08,0.27,0.60,1.00,1.38\) radians, quadrature and the closed expression agreed to absolute error below \(2\times 10^{-8}\). At widths \(0.13,0.64,1.23\), direct samples of 110,000 pairs each were consistent with the predicted values within specified sampling tolerances. The run terminated with `SPHERICAL_ZONE_GEODESIC_ESCAPE_ANALYTIC_AND_DIRECT_SAMPLE_OK`.

The mathematical proof uses an established spherical integral-geometric decomposition and explicit evaluation. Finite numerical checks do not prove the theorem; no independent review or automated mathematical certification is claimed. Source priority may be incomplete where historical articles are unindexed or use different terminology.
