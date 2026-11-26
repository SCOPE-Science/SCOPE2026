---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The three listed edge forms give the 24 edges of the 16-vertex graph. The closed-neighborhood union of the two endpoints is exactly the coverage witness for an edge. A pair of distinct edges has different distance signatures precisely when the selected vertices meet its distinguishing set, so the 24 coverage tests and 276 distinction tests are jointly necessary and sufficient. The independent exact replay enumerated all 65,536 subsets, reproduced the separate minima and four-set counts (368 resolving, 128 dominating, none joint), every coefficient of the joint polynomial including the total 50,363, and all 512 feasible five-sets. For distinct states, a symmetric difference of size two is exactly a jump, and adjacency of its two vertices is exactly the slide condition. All-root BFS confirms connectivity and 1,320 slide edges with all 512 eccentricities eight; for jumps, 3,616 edges and 368 eccentricities five and 144 six. The automorphism orbit computation reproduced all eight representatives and sizes. This is exhaustive for the specified finite graph; no inference from testing smaller subsets of states is needed.

## originality

PASS

The joint obstruction, joint labelled polynomial and configuration geometry are distinct on the evidence inspected. The separate edge metric dimension of this exact host was already known: Wang–Wang–Zhang explicitly give βe=4. Treat that scalar as a confirmed ingredient, not an original contribution; it does not imply the joint obstruction or census.

## value

PASS

On a canonical cubic symmetric graph, the two natural vertex-based requirements separately admit four-landmark solutions but no four-landmark solution meets both. The record identifies every achievable size and the orbit and shortest-reconfiguration structure of all optima. Uniform slide eccentricity despite unequal degrees, and the contrast to jumps, give information not available from the scalar minima or automorphism order alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
