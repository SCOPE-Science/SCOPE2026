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

# Reproducible finite checks

Use Python 3 with no nonstandard libraries. From the directory containing these files run `python verify_full_bfs.py` and `python verify_interval.py`.

The first checker performs breadth-first search on the exact original \(n\)-state power automaton augmented by a run counter for consecutive rotations. It reports `PASS: literal subset/constraint BFS, all n=3..14`.

The second checker independently enumerates full inverse images of every cyclic interval using the explicit block maps for `ab` and `aab` and uses Dijkstra to determine their weighted shortest paths. It reports three successful assertions: `full inverse-interval Dijkstra, all n=3..35`; `every Bellman inequality, all n=3..80`; and `explicit reset words, all n=3..150`. The constructed words have no `aaa`, their length equals the theorem formula, and their image is a singleton under the original two-letter action.

These were executed successfully on the actual included source files prior to packaging. Finite executions are not an all-parameter mathematical certification; the symbolic proof in `RESULT.md` supplies the general argument. No external or independent mathematical audit has been performed.
