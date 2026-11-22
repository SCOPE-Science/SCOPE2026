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

# Verification

Run `python3 checker.py` with Python 3 and no third-party modules. The checker exhaustively enumerates all 16384 configurations of the nonroot sites in a depth-three complete binary tree, verifies the graph's breadth-first root-cluster connectivity against the ancestral-word separator for each of 15 vertices, checks the closed word-count formula and rational expected-level recurrences, and numerically checks the supercritical survival expansion for two different offspring distributions of equal mean. The expected terminal report is `PASS 245892 exact enumeration and arithmetic assertions`.

These diagnostics test finite and special cases only; the complete threshold, susceptibility, and asymptotic amplitude are established by the proof in `RESULT.md`. No external or independent audit has yet been performed. The abstract-only comparison with Quine leaves a possible historical-priority uncertainty.
