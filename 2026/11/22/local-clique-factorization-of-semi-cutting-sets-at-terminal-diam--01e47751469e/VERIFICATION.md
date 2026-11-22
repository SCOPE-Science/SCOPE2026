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

# Reproducible checks

Run `python3 verify_semicut.py` and `python3 verify_multipartite.py` using Python 3; the scripts use only its standard library. These files are embedded alongside this document.

The first checker independently generates the full edge-subset distance comparison for every labelled graph with two through five vertices and all eligible terminal sets: `ALL_GRAPHS_TERMINAL_DIAMETER_TWO_DISTANCE_CENSUS_PASS graphs=1098 cases=17804`. It also checks the exact seven-vertex nonreal-root witness, cubic discriminant, and nine-vertex multipartite polynomial sample, then prints `VERIFY_OK`.

The second checker directly examines graph distances after deletion for 1,905 labelled complete-multipartite instances through order six, prints `SEMI_CUT_MULTIPARTITE_FULL_GRAPH_DISTANCE_EXHAUSTIVE_PASS cases=1905`, and exits normally.

The proof in `RESULT.md` supplies the unrestricted quantifiers and every critical step. Computations here cover finite test cases only; no independent audit or external mathematical certificate has been performed.
