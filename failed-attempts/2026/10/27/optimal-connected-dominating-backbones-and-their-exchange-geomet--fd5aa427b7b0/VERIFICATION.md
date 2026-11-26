---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For a connected dominating five-set the induced edge count must be four, since at least 11 outside vertices need a boundary edge and the cube has degree four. Each length-two tree path produces an outside common neighbor of the endpoints: their only other common neighbor is the middle vertex, and a second inside would give a four-cycle in the induced tree. At least three such paths cannot be accounted for by 12 boundary incidences on 11 vertices (only one outside vertex could have a pair of neighbors, and it could have just two). Smaller connected dominating sets can be enlarged, and the stated six-path dominates. Independent exact replay (python3 -B /workspace/branches/independent_replay.py 2) used Hamming adjacency and traversals on all subsets of sizes 1--6, verified all 11 stated orbit rows against independently chosen representatives, and generated exchanges via common five-subset buckets. It found all 192 optimizers equal to the flip-word family, 1,952 connected six-sets, and the frozen shell vector at every optimum. The common shells imply connectivity, degree four, diameter seven and the unordered-pair histogram. Attaching all vertices outside any minimum backbone as leaves gives a spanning tree, whose internal set must be the entire backbone by the established minimum; conversely a spanning tree's internal vertices dominate and are connected.

## originality

FAIL

The earlier Resultary finding on the Cayley exchange graph covers the actual minimum, entire path family and transitive action, exact exchange rule and full metric shell counts. The pair histogram and maximum-leaf restatement follow from those results. This is demonstrable prior coverage of the central finding, not a failure based on inaccessible texts. The 11-orbit table for all connected six-sets is a verified ancillary certificate whose row-by-row historical status is separate.

## value

FAIL

The minimum-layer exchange geometry is a naturally motivated finite invariant, but this submission primarily recomputes the already exact classification and metric. Its extra certificate for connected six-subsets tabulates the search space used to derive a conclusion already known; the frozen record does not motivate a separate scientific use of that census as a new claim, and its mere verification does not rescue the contribution. No substantive narrowed replacement is being delivered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
