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

# Reproducibility
The proof in `RESULT.md` gives exact facet inequalities, extremal-ellipsoid semiaxis optimizations, vertex orbit classifications, and contact certificates for every integer dimension parameter. Run `python star_edge_diamond_verify.py` under standard Python 3 to replay the independent exact-rational finite consistency checks for parameters one through eight. The checks inspect the complete explicit vertex orbit list and all described contact equalities; they do not prove the unrestricted theorem by enumeration.

The outer geometry is certified analytically by the one-variable convexity identity on each vertex orbit. The inner geometry is certified analytically by the exact signed-facet support function and strict one-variable volume derivative. Classical existence and uniqueness of both extremal ellipsoids justify reduction to the invariant family without excluding tilted or shifted competing ellipsoids.

The historical comparison uses the publicly posted 2026 manuscript and indexed mathematical records. Full text of every related indexed record was not available, so absolute historical priority is not claimed. Independent mathematical audit has not been performed.
