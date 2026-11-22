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

# Reproducible finite checks

From the package directory, run `python3 verify_census.py` and `python3 verify_orbits.py` (Python 3.8 or later, standard library only). The success markers are `Q4_MIS_SHATTER_CENSUS_PASS` and `Q4_MIS_SHATTER_ORBITS_PASS`. The first script enumerates all \(2^{16}\) possible vertex sets to find the 42 independent dominating sets, then all \(2^{16}\) query supports, computes Boolean traces and maximal shattered supports. The second enumerates all maximal cliques of the graph complement, constructs all 384 cubical isometries, expands four facet orbits, and checks equality of the predicted and actual shattered-support families for every support. Both programs also verify the stated finite cardinalities and obstruction geometry.

Exact expected coefficients: `1,16,88,160,104`. Exact expected facet orbit cardinalities: `8,16,24,64`. Known MIS counts `42 = 24+16+2`. A complete finite enumeration proves only the stated finite-domain assertion. The checks are reproducible software certificates, not independent human audit or a claim about all dimensions.
