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

# Reproducible checks and limits

Run `python verify.py` with Python 3 standard library. The observed test return was `VERIFY_OK 67` with no failed assertions. The checker reconstructs comparable perfect pairings of all proper nonempty subsets for \(3\le s\le10\), verifies selected mixed binary/ternary shattering witnesses up to \(s=6\), computes exact online shattering dimensions using version-space recursion on selected finite grids, and independently brute-forces selected ordinary VC dimensions including the two-four-valued-coordinate boundary.

The all-parameter proof is in `RESULT.md`; the test checks do not extrapolate numerical experiments into infinite assertions. Direct mathematical rechecking covered the matching replacement, the count of thresholds, the exceptional one-coordinate case, and the independent-coordinate balanced-split construction. No third-party certification or independent mathematical review has been conducted.
