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

For the exact twelve-vertex labelled edge list, complete host-graph BFS and exhaustive distance-signature enumeration independently reproduce no resolving set of size at most three and 146 resolving four-sets. Adjacency of bases in the jump graph is symmetric difference of cardinality two; for sliding, its two vertices must be a host edge. All-source BFS on the resulting graphs confirms connectivity, 928 and 452 edges, radii 4 and 4, diameters 4 and 6, slide eccentricities 4:2, 5:104, 6:40 and exactly centers {2,8,9,11} and {3,6,7,10}. All 10585 unordered distinct pairs give jump excesses (10367,218) and slide excesses (4463,4944,1070,92,16) relative to 4−|S∩T|. The proof covers only minimum vertex-resolving sets and single simultaneous replacements. Replay: python3 /workspace/review_checks/1.py; saved output /workspace/review_checks/1.out. This was a fresh finite computation, distinct from inspection of the frozen verifier evidence.

## originality

PASS

The supported distinct claim is the exact Chvátal vertex-basis relocation geometry and detour census, not the host graph, the metric-basis definition or the jump/slide framework. Inspected sources do not establish this census. The closest exact same-host result uses a different feasibility predicate; the primary search was bounded and low-yield.

## value

PASS

The Chvátal graph is a classical small regular high-chromatic host with independent interest. Its complete minimum-state mobility geometry quantifies a real difference between global and adjacency-constrained replacements that neither connectivity nor metric dimension records: only two optimal slide starting states and positive jump detours even without locality. The exact pairwise excess census supplies a directly usable small benchmark and a contrast with other hosts where every jump attains the exchange lower bound. This is not a claimed general algorithm or a family-wide result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
