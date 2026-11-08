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

From the package directory, run `python3 affine_chain_line_checker.py`. It uses only the standard library and reconstructs all concepts from modular ring arithmetic. It separately enumerates point-trace patterns for all singleton/pair/triple supports, obtains complete depth-\(e+1\) mistake trees by recursive search within the two pencils, verifies every root-to-leaf path against the line sets, and computes exact minimax recurrence values for three small parameter pairs. The expected final line is `ALL_AFFINE_CHAIN_LINE_CHECKS_PASS`.

Cases tested: \((p,e)=(2,1),(3,1),(5,1),(2,2),(3,2),(2,3)\). There is no all-parameter exhaustive computation. The mathematical proof, not the finite tests, establishes the universal claim. The separate full scientific assessment is in `REVIEW.md` and `AUDIT.json`. Independent external audit: not performed.
