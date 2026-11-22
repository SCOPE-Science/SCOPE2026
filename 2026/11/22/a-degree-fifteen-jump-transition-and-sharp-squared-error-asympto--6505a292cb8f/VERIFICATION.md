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

# Reproduction and limits

Run `python3 check.py` using a standard Python 3 interpreter. It prints a PASS line after 618 exact rational comparisons and verifies the polynomial coefficients, all boundary-trace values up to degree 15, endpoint dominance through degree 14, the exact first interior maximum, and its two symmetric grid traces. No downloaded data or third-party packages are required.

The proof of the reduction from BV to steps, within-cell convexity and the global Gaussian limit is in `RESULT.md`. Neither finite checks nor numerical calculations are offered as certification of infinite-dimensional or asymptotic statements. Historical-priority risk remains for the inaccessible 2014 full text.
