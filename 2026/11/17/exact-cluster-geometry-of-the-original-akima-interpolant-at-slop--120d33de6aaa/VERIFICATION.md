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

# Reproduction and limits

Run `python3 verify_akima_clusters.py` in an ordinary Python 3 environment; the script uses only the Python standard library. The executed copy returned:

```text
EXACT_HERMITE_BUMP_MAXIMUM_AND_VARIATION_PASS 4/27 16/27
ALL_REGULAR_SLOPES_AND_CRITICAL_INTERVALS_PASS 3000
SIMULTANEOUS_TWO_CORNER_RATIO_ATTAINMENT_PASS 504
INDEPENDENT_CONTINUUM_BUMP_VARIATION_STRESS_PASS
ALL_AKIMA_CLUSTER_GEOMETRY_CHECKS_PASS
```

The analytic argument verifies the all-data theorem. Exact rational calculations prove the scalar Hermite bump extrema and two-corner ratios; randomized numerical tests stress the formulas but do not prove the universal quantifiers or historical novelty. The construction of every vector of critical-knot limits rests on the acyclicity of the graph with edges between gap indices two apart. The full 1970 original article and 1969 predecessor report were not available for complete primary-text comparison. No independent external audit has been performed.
