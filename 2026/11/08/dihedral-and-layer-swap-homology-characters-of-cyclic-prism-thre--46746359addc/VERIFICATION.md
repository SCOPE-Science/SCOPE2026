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

The standalone `VERIFY.py` rederives the dual simplicial complex, tests all proposed elementary free-face deletions, and computes signed traces of all group elements over the actual chain bases. In particular, it checks the closed character and invariant-dimension formulas for each \(5\le n\le16\). It also independently enumerates the **ordinary** three-cut complex for \(5\le n\le8\) and compares direct Lefschetz traces with the duality-based answer. This avoids using the dual calculation as its own only cross-check.

The recorded stdout in `VERIFIER_OUTPUT.txt` documents the executed checks: \(756\) elementary collapse pairs, \(504\) group elements and \(104\) direct-Lefschetz comparisons; it finishes with `VERIFY_OK`. Run `python3 VERIFY.py` in a directory containing this file; no third-party package is required.

These tests establish the correctness of the finite certificates and formulas in the stated tested range, not a finite exhaustion of the unbounded theorem. The general claim rests on the uniform graph-face classification, exhaustive symmetry-case counting argument, Alexander duality and Hopf trace stated in `RESULT.md`. There has been no independent external scientific audit.
