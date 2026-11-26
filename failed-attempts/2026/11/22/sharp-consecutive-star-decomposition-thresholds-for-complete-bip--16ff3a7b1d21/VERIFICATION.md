---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Orient each edge away from its star center; conversely, split each vertex's outgoing edges into stars of sizes k and k+1. This is equivalent to all outdegrees lying in the nonnegative semigroup they generate. The quotient–remainder representation proves the conductor k(k−1), with predecessor excluded by its residue. If a shore size is represented, a one-way orientation suffices; otherwise both sizes come from the finite positive gap lists below the conductor. Recomputed coverage consists of three exceptional pairs for k=4 and nine for k=5. An independent replay using dynamic-programming semigroup generation checked every row and column outdegree of the twelve frozen orientations and all twelve passed. Replay: /workspace/branches/6e55ef8d-6f98-43f7-9735-5e37d4fbd7c3/replay_record2.py and replay_record2.out in the same directory. The original verifier was inspected, not executed. This finite replay is sufficient only in combination with the analytic reduction. In K_{k−1,k(k−1)−1}, the larger shore's vertices have degree <k and must all be leaves, leaving forbidden outdegree k(k−1)−1 on the smaller shore; this proves the all-k lower bound analytically. The threshold concerns only positive shore sizes and does not require both star sizes to occur.

## originality

FAIL

A distinct indexed result, 0d9bcf03f46b, states and proves the same sharp biclique threshold for every k≥3 and uses the identical obstruction. It covers both exact threshold claims. The remaining k=2 instance of the lower bound is the immediate nondecomposability of the one-edge graph. This is established mathematical coverage, not a conclusion about which same-day record was earlier or whether one was derived from the other.

## value

FAIL

A sharp adjacent-degree-sum boundary is a meaningful target, and the matrices are valid reproducible witnesses. As a distinct contribution, this finite specialization supplies neither an uncovered cutoff nor a construction beyond the scope of the constructive all-k biclique result; the additional k=2 obstruction is immediate. The submission establishes no separate reason to need the particular twelve orientations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
