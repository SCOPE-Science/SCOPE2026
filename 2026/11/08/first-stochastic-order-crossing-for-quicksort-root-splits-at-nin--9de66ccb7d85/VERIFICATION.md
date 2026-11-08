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

# Exact finite verification

The certificate uses integer counts of full permutations, not floating-point probabilities or simulated evidence. Running `python checker.py` with Python 3.9 or later requires no dependencies beyond the standard library. The code recursively constructs each comparison-cost histogram, checks that the conditional mass is \((n-1)!\), verifies every entry of the table for \(2\le n\le8\), and confirms the sign change at the two exact thresholds for the nine-key first-pivot ranks four and five.

A separate algorithm builds binary search trees by insertion and counts actual comparisons across all \(2\cdot8!=80640\) distinct input permutations with these root ranks. The resulting distributions exactly match those derived by recursive conditioning. The execution passed: 109 exact assertion groups/vector checks, the 80,640 insertion outcomes, and the conditional-mean comparisons.

The recurrence and full coefficient table support a **finite universal cutoff**, not an infinite-size theorem. No independent external audit has been performed. The program's output establishes neither novelty nor protection against uninspected historical literature.
