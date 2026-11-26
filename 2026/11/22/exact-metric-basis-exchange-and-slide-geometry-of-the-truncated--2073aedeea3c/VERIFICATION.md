---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Independent enumeration of ordered-pair graph vertices and distance signatures rules out all smaller resolving sets, recovers 156 resolving triples in nine S4-orbits, and recomputes connectivity, all 12,090 pair distances for both move rules, all histograms and the nonmatroid witness. The 1,446 jump edges give a jump metric equal to 3−|A∩B| on every pair, not just matching marginal counts. There are 450 slide edges, radius 6, diameter 7, an eccentricity split of 108/48, and exactly 204 pairs with maximum penalty 4. A separate targeted replay uses the closed base-graph distance: within a corner the distance is 0 or 1; between corners a and c it is 3 minus the number of endpoints already on the unique cross edge between those corners. It verifies both landmark orbit tables, representative slide degrees and eccentricities, and distance seven for the two stated pair representatives. Their S4-orbits are disjoint and have sizes 24 and 12; together they account for all 36 diametral pairs from the census. This replay also checks the displayed seven-slide geodesic. The failed matroid swap of element 4 gives exactly eleven signatures for each candidate replacement, even though some minimum-length jump route exists between the two bases.

## originality

PASS

Best-of-knowledge pass for the exact jump and slide geometry, including the combination of Johnson isometry and failure of matroid exchange. The standard skeleton is known. The closest same-day metric-basis mobility result concerns a different graph, while same-graph studies located concerned different graph invariants.

## value

PASS

The fixed graph is a canonical cubic polyhedral skeleton rather than a cutoff chosen just to generate another table. The two move rules ask natural global metric questions for minimal resolving sets. The instance is a concrete witness separating a global geodesic property from matroid exchange, and it quantifies how requiring local moves on the very same feasible sets destroys the Johnson distance, with a sharp penalty and classified diameter pairs. Those exact conclusions are useful for testing sufficient conditions for short reconfiguration paths; the value does not rest on the mere ability to enumerate triples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
