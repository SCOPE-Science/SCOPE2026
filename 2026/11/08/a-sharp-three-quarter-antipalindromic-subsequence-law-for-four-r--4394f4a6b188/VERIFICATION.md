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

# Verification and scope

The standalone `verify.py` uses a separate dynamic recurrence for the longest reverse-complement palindrome in each linear rotation: discard either endpoint, or match complementary endpoints and add two. This recurrence is exact by the standard extremal subsequence decomposition; it never uses the six-term formula.

Run `python3 verify.py`. Successful output reports 625 separate-method dynamic-programming comparisons for all run quadruples bounded by five, 328350 balanced algebraic comparisons, and the complete extremizer census at 79 multiples of four. These experiments test all boundary patterns in the specified finite ranges. The proof in `RESULT.md`, not the experiments, covers every positive integer run length and establishes sharpness for unbounded families.

The source comparison includes a material reading of the primary 2019 antipalindromic circular-word paper and focused searches of the three-quarter bound, four-block words, cyclic LCS and reverse-complement aliases. An unindexed equivalent mathematical result remains possible. This is a self-review, not independent verification or external certification.
