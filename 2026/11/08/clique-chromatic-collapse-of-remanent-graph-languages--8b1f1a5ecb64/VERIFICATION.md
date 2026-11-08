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

# Verification instructions and scope

Run `python checker.py` using Python 3.10 or later with only the standard library. The expected success line starts `CHECKS_OK tournaments=1099, oriented_small_graphs=760, random_multipartite_orientations=400`.

The checker constructs the signed-word reachability transition system directly from each orientation, and performs a complete product-state search against the canonical run-bounded DFA language. It exhausts all labeled tournaments of orders 1 through 5 and confirms that precisely \(k!\) orientations at each order lack directed triangles. It also exhausts all orientations of simple weakly perfect graphs through four vertices and checks 400 seeded orientations of larger complete multipartite graphs.

The proof for all finite graph sizes is in `RESULT.md`. In particular, the map from an arbitrary bounded-run signed path to a transitive tournament and the converse chromatic orientation are exact arguments; no finite experiment establishes their universal quantifiers. The DFA minimality is proved by explicit distinguishing suffixes. The checker does not establish publication priority or independent expert review. The most closely related original research article has not had its entire remanent-language portion inspected, leaving a specific priority risk.
