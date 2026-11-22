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

The following verification is computational and mathematical reproduction for the explicitly specified three eighteen-vertex graphs; it is not independent external validation.

Run `python3 verify_closure.py` and `python3 verify_direct.py` from the directory containing `CONFIGURATIONS.json` and `EXPECTED_COUNTS.json`. Both programs use the Python standard library and compare every computed quantity with the complete exact tables. Recorded successful output is included in `closure_output.txt` and `direct_output.txt`.

The closure program checks the incidence conditions and all 512 subsets on each shore, the identities \(\alpha\beta\alpha=\alpha\) and \(\beta\alpha\beta=\beta\), exact fiber products, all basin-size histograms, and graph-distinguishing invariants. The separate exhaustive program computes the Boolean update directly at all 18 vertices of every one of the 262,144 states for each graph, checks \(F^3=F\), and obtains every recurrent orbit and basin directly from the functional graph. Thus the per-graph finite counts do not depend on numerical approximations or probabilistic sampling.

The uniform finite-time law is independently explained by the elementary incidence Galois identities in `RESULT.md`. The classification of three combinatorial \((9_3)\) types is taken from the cited earlier literature; exhaustive computer classification of **all** abstract cubic bipartite graphs is neither needed nor claimed. Historical uniqueness is not certified.
