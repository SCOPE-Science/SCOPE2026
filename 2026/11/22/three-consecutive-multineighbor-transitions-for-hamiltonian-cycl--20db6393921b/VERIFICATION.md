---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The frozen Finding and proof pass at all three stated thresholds. The separate frozen Limitations assertion that two shore components persist at every positive threshold is false: m=n-2 has 2n isolated vertices, and m>n-2 has no vertices. The complete replacement in /workspace/repairs/2/RESULT.md corrects this for the final claim. Sharing an open neighbor precludes mixed shores, and the union of excluded indices on one shore has size |S| plus the run count. At t=3 only cyclic edges survive. At t=4 each consecutive triple collapses with its distinct length-two diagonal; the remaining graph contains C_n, and a spanning tree containing all but one of its edges shows the cycle represents a primitive generator. At t=5 the excluded triples have positive cyclic gaps after removing one additional unselected vertex from each gap; the circular count is (n/3) binom(n-4,2). Each consecutive four-block collapses with the face {i,i+1,i+3}: the large gap n-3 is the unique possible exterior gap for a four-block. Before collapsing, triangles with a cyclic edge replace each chord by a cyclic path, and the fan at 0 fills the cycle. The resulting simply connected 2-complex has reduced Euler characteristic q_n and free H_2; Hurewicz and homological Whitehead give the stated integral wedge. The target H_1 is zero and each shore stays connected throughout these three stages, giving the stated maps.

## originality

PASS

The surviving distinct claim is the deterministic three-threshold integral homotopy and stated inclusion behavior for the open multineighbor filtration on this graph. It is unchanged by the limitation repair. The inspected same-graph results classify different complexes, and the foundational paper supplies the construction rather than these types or maps.

## value

PASS

This is a natural controlled perturbation of a complete bipartite graph and an exact deterministic test case for a multineighbor filtration. Three consecutive levels exhibit a primitive old class surviving alongside new loops, their joint disappearance at the next level, and a new second-homology contribution. Integral homotopy types and the specified maps supply more than three isolated numerical Betti counts. The correction restricts the component interpretation without reducing this contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
