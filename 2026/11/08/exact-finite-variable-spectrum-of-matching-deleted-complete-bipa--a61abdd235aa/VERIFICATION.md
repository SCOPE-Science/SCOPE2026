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

# Verification record

The supplied Python 3 programs reproduce the independent finite checks. The logical-refinement program requires NumPy. Execute `python verify_pebbles.py` and `python verify_structure.py` from the directory containing the files. Their exact standard output is embedded as `verify_pebbles.out` and `verify_structure.out`.

The logical program computes stable colors of ordered \(k\)-tuples using equality, adjacency and the **sets**, not multiplicities, of successor colors in each coordinate; this is the counting-free fixed-variable refinement. Its test family includes all \(50\) matching-deleted complete bipartite graphs with \(3\le a\le b\le6\) and \(0\le t\le a\), at widths two and three. Its separate width-four sample has \(13\) graphs. The structural program evaluates the intrinsic same-side and deleted-pair formulas for \(168\) parameter triples with side sizes up to nine, and enumerates the clipped theory profiles for widths three through eight.

These executions are corroboration of finite instances, not a proof of the unrestricted result. The unlimited-round Duplicator strategy, variable-scoped counting formulas, and combinatorial count are proved in `RESULT.md`. Independent mathematical audit has not been performed.
