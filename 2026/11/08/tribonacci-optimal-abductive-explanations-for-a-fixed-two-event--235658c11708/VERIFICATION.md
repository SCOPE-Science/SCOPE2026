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

# Verification of the exact response-explanation spectrum

The reproducible standalone program `verify.py` uses only the Python standard library and is run using `python verify.py`. It enumerates all satisfying two-event traces through length eight and independently computes minimal transversals from their true clause literals. For lengths two through four it additionally checks all lock/unlock feature subsets directly against the semantic truth value of every compatible fixed-length trace, **without assuming the transversal characterization**. There are 242 such compliant short traces and 39,818 compliant traces examined for the sharp length-two-to-eight bound. Results are exactly \(3,5,9,17,31,57,105\), with precisely two maximizing traces at each length.

The program checks the precise polynomial distribution through length nineteen, the Tribonacci recurrence, the minimum and maximum AXp sizes, the coefficient four for maximal-size explanations at lengths three and above, and the sharp \(n-1\) contrastive count at maximizing traces. The proof in `RESULT.md` establishes the infinite family; no finite enumeration is treated as proof for all \(n\). No independent external assessment or certification has been conducted.
