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

Exact rational replay: `python3 check_truncated_octahedral_adsorption.py` on a standard Python 3 installation. The checker constructs the vertices from signed permutations and tests adjacency by squared distance 2. It asserts all 24 degrees equal 3, the 36 edges are undirected, and tests every coefficient of the entire terminal distribution. The rational recursion visits 23,123 reachable residual induced masks. A separate include/exclude recursion enumerates the 363 maximal independent sets and returns the class counts 117, 208, 36, 2. Three exact positive tail differences prove stochastic domination; the expectation and probability-amplification fraction are asserted. All assertions executed without error in the packaged standalone script.

Proof limit: The finite exhaustive recurrences establish the facts for exactly this graph. They do not imply related facts on other graphs, or a continuum/infinite-substrate limit. Bibliographic search cannot establish publication priority conclusively; the full text of a relevant 1989 general model paper was not available through the accessed sources.
