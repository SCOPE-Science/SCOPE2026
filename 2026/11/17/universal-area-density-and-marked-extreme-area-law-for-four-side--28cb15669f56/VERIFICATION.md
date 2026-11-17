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

The area identity follows exactly from a four-vertex shoelace calculation. Independent triangular-product integration gives the density and survival formula, and a fourth-order Taylor expansion gives the two-term rare-event law. A uniform-on-a-converging-region argument gives the conditional five-component Dirichlet limit. The standalone numerical checker `verify.py` tests nine survival thresholds, the shoelace identity and variance, the product-density integral, endpoint ratios, and five conditional coordinate means with an independent four-deficit rejection sampler. Its fixed-seed execution completed with `FOUR_SIDE_QUADRILATERAL_AREA_LAW_OK`.

Numerical experiments are finite and do not establish the asymptotic results. No independent mathematical audit has been performed. Historical priority is provisional, especially for nonindexed expository formulas for products of triangular random variables.
