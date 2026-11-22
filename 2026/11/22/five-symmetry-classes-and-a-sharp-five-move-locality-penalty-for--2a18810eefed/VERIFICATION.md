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

The supplied independent standard-library programs `verify_affine.py` and `verify_lcf.py` both passed. They construct the same eighteen-vertex graph from distinct presentations and check a vertex-bijection certificate. Both independently implement power-domination closure, exhaustively test sets of sizes one, two, and three, independently construct the TJ and TS transition graphs, and compute shortest paths from every one of the 486 successful three-sets. Exact histograms, edge counts, eccentricities, and the all-pairs penalty distribution agree. `verify_affine.py` additionally checks a generated 216-element automorphism action and its five minimum-set orbits.

The computations are exhaustive for this fixed graph; no infinite graph family, other movement rule, or larger budget was analyzed. The programs constitute a reproducible computational proof, not an independent external mathematical audit.
