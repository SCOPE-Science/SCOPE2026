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

The modular model was independently checked for symmetry, no loops, degree seven, and 0 or 1 common neighbor for adjacent or distinct nonadjacent pairs, respectively, identifying the specified strongly regular graph. Initial observation is N[S] at t=1. During a wave an observed vertex contributes its sole unobserved neighbor if there is exactly one; the mask is updated only after scanning all contributing vertices. No-change states fail; every changing step strictly shrinks the missing set, so the process terminates. An independent batched recount exhausts all sets of sizes 1 through 6 (empty trivially fails), split by the smallest selected label into [0,2), [2,6), and [6,50). It visits 50, 1225, 19600, 230300, 2118760, and 15890700 sets respectively, with no successes below size six. For six, the only nonzero (round, induced edges):count cells are (2,0):12950, (3,0):448000, (3,1):63000, (4,0):378000, (4,1):630000, (4,2):294000, (5,1):378000, (5,2):126000. Their sum is 2329950, with the given probability 317/2162. Round one cannot observe all fifty because at most 48 neighborhood incidences are available. The two bundled C++ programs were inspected: they implement the stated graph constructions, compositional iteration, synchronous forcing and edge count under the same convention. The proof only concerns this graph.

## originality

PASS

The graph and algorithm are classical; the complete joint census on minimum sets, including sharp rounds and induced-edge restrictions, is distinct on the inspected evidence. No independent prior coverage of this count or table was demonstrated. The pass is for the exact finite census, not for a new general power-domination method or a priority guarantee for every subclaim.

## value

PASS

The Hoffman–Singleton graph is a canonical highly symmetric test case. The joint distribution answers a natural question left open by sensor minimization: how time-to-observe and the adjacency pattern of minimum sensor sets vary together. The exact cells give sharp time extremes, the exclusion of three induced edges, and an optimum-set density; none is mechanically fixed by the strongly regular parameters or by the optimum size alone. These data can serve as a benchmark for graph-specific structural or computational accounts of power domination.

The dated certificate retains the supplied scientific assessment, sources and limitations.
