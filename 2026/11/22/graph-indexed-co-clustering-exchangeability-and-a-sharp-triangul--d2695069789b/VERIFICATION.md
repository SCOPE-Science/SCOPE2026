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

# Reproducibility and verified limits
Run `python3 check.py` with Python 3 standard library in the same directory as this document. On this package's test cases the program reports `PASS: 2063 exact checks; all findings above require the separate symbolic proof`.

The program verifies finite EPPF normalizations, each of the eight three-edge triangle patterns, incident and disjoint edge probabilities, the forced exchangeable extension weights, and the all-simple-graphs-through-five-vertices shape criterion. Exact rational parameters include admissible negative \(\theta\) cases. Its exact arithmetic avoids floating-point rounding and does **not** establish any all-size or all-real-parameter assertion by itself. The proof in `RESULT.md` establishes the general theorem; exhaustive independent historical priority checks and independent mathematical audit are not claimed.
