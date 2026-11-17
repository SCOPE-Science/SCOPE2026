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

# Internal reproducibility of the mathematical claim

Run `python3 check.py` with Python 3 standard library. It reconstructs the tupling graph by enumerating facets of the simplicial join and every complementary pair of \(r\)-element subsets. This approach does not assume the proposed component factorization. It also enumerates all \(r\)-faces independently, checks full vertex coverage, computes all graph components and checks every component's numbers of vertices, edges, and independent circles. Complete expected output is provided in `check_output.txt`.

Five tested parameter lists are: four unfilled complete three-vertex graphs; five such graphs; four unfilled pentagons; a four-factor mix of a pentagon, triangle, unfilled four-vertex complete graph and a five-vertex wheel; and a mixed-length cycle/triangle four-factor join. All factors are connected and nonbipartite. The output's final marker is `BALANCED_PATTERN_JOIN_TUPLING_PASS`.

The symbolic proof in `RESULT.md` establishes the theorem for all integer \(r\ge4\) and all allowed graphs. The finite program does not verify arbitrary parameters or prove nonexistence of unindexed prior work. No independent mathematical audit has been performed.
