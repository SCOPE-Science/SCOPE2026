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

# Verification and limits

The self-contained checker `check.py` was executed using Python 3. It directly enumerates all possible graphs on at most six vertices for the named connected motifs, computes their isolated-vertex and induced-motif counts, evaluates sample covariances with exact rational arithmetic, and compares with the all-parameter expression for each admissible edge count. It also checks exact strict product monotonicity on the recorded finite parameter grid. All 5,483 assertions passed.

The full finite enumeration is independent of the symbolic conditioning proof. The general assertions (including the uniform finite-order onset and dense-graph limit) depend on the written mathematical proof, not on tested values. No infinite computer certification, theorem-prover verification, inaccessible paper comparison, or independent assessment is asserted. Primary-paper comparisons are qualified in `REVIEW.md` and `AUDIT.json`.
