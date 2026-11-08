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

# Verification and reproducibility

The proof uses exact hyperbolic cosine and half-angle identities, geodesic polar volume, Gauss–Bonnet, independent Pareto tails, and the bound from the chord triangle inequality. No finite simulation is claimed to certify a continuum or infinite-radius statement.

The included `check_hyperbolic.py` directly samples three points from the hyperbolic ball radial distribution and Haar directional distribution in dimensions \(2\), \(3\), and \(5\), with radii \(5\), \(7\), and \(9\), totaling \(405000\) independent triples. Its exact finite-radius angle computation is compared to the proposed limiting expression under a common-quantile coupling; compact-coordinate sample errors decay with radius. It also tests the regular equilateral angular configuration, which yields limit \(4\sqrt3\).

**Replay:** execute `python check_hyperbolic.py` with `numpy` and `scipy` installed. Expected terminal marker: `HYPERBOLIC_TRIANGLE_AREA_LIMIT_NUMERIC_OK`.

**Scope:** weak convergence and positive-moment threshold for the limit; finite-radius moments, exceptional angular configurations, and independent external audit are not established here.
