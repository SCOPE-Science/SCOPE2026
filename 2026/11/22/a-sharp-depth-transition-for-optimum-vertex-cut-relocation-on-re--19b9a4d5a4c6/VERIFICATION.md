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

# Reproduction and mathematical boundary

From a directory containing these embedded files, execute:

```sh
python3 verify_grid_bruteforce.py
python3 verify_grid_states.py
```

Expected success markers are `BRUTE_FORCE_PASS 56` and `PARAMETER_CHECK_PASS 1232`. The first program uses direct grid BFS for all subsets of cardinality at most three in 56 graphs with terminal placements, and constructs the full legal-move networks. The second independently implements a coordinate enumeration and verifies all graph-size, edge-count, component and degree formulas over 1,232 parameter choices. Neither script imports external packages. Both ran successfully before packaging. Exhaustive finite checks do not prove all orders and widths; the complete proof in `RESULT.md` covers those cases. The scientific evidence was self-reviewed; no independent audit has been performed.
