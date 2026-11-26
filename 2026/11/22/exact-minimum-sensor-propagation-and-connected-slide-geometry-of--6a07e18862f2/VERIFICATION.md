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

Reconstructed the 54-vertex point/axis-line incidence graph and verified the exhaustive claims with an independently written symmetry-reduced Python enumeration. Directly tested every anchored stabilizer orbit for sets of sizes 5 and 6: those containing point 0, and the all-line cases containing line 27. The coordinate group is transitive separately on points and lines, so these anchors cover all subsets under the group. Combinatorial ranks mark every member of each anchored orbit. The anchor universes had sizes (292825,14950) and (2869685,65780), with respectively (7265,531) and (64965,1940) tested orbits. For a white vertex the replay tests the three possible forcing witnesses by requiring the witness and its other two neighbors in the preceding observed set; round 1 is N[S]. The resulting fully expanded, deduplicated labeled census is zero successful five-sets and 880632 successful six-sets with all 18 time/point-count entries as claimed (including the zero), no other cells. Monotonicity of each observation step rules out smaller sets. An independent slide BFS generated all neighbors by toggling the two endpoints of each incident edge (an occupied destination gives a four-set and is rejected); membership in the census restricts to valid configurations. One component of size 880632, degree multiplicities 77760,58968,182736,316872,130896,92016,9072,12312 at degrees 4,6,7,8,9,10,11,12 and the half degree-sum 3412368 agree. The two supplied seed orbits under the coordinate group each have size 1296 and exhaust the time-10 sets. Points and lines have distinct distance-six sphere sizes (8 versus 4), verified at their respective orbit representatives. Any automorphism thus preserves points and acts faithfully on their collinearity graph H(3,3): the line vertices are determined by triples of points. The stabilizer of a point permutes the three pairs of neighbors and switches symbols within each pair; fixing the six neighbors fixes each distance-two vertex by its two predecessors and each distance-three vertex by its three predecessors. This bounds the automorphism group by 27·48=1296, attained by the checked coordinate actions. The frozen C++ and Python programs were inspected, not executed. Replay the independent code at /workspace/branches/independent-reproduction/gray_review.py with arguments 5, then 6, then slides, in that order (writes intermediate data under /tmp/opencode); retained logs gray-five.log, gray-six.log, gray-slides.log. This exhaustion is for this labeled graph only.

## originality

PASS

The supported distinct claim is the complete Gray-graph optimum-state census and synchronous timing/slide classification, not the Gray graph representation, its symmetry group, the underlying reconfiguration definitions or the value 6 as a freestanding novelty claim. The strongest distinct same-graph indexed result uses efficient open domination and a different trade rule. Indexed results with the same power-domination and slide vocabulary concern different graphs. No material earlier or same-day result was shown to cover this full invariant in the bounded comparison.

## value

PASS

For a standard semisymmetric graph the two inequivalent vertex types make the minimum-sensor time spectrum and the geometry of adjacency-preserving relocation natural exact questions. The slowest symmetry classes and connected minimum-state graph add precise information that a minimum number, radius, single feasible move or marginal count cannot supply. The complete finite census is usable as a benchmark for power-domination and reconfiguration results; no general graph-family theorem or slide diameter is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
