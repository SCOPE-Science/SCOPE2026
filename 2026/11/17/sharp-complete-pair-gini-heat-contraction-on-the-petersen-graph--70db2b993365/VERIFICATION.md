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

# Reproducible verification

`CHECKER.py` requires Python 3 and only its standard library. Execute `python3 CHECKER.py` in the extracted package directory. The script constructs Petersen vertices as unordered pairs of five points, checks all 100 entries of the strongly regular matrix identity, enumerates every nontrivial ten-bit cut, computes integer variation exactly, checks all nine cardinality maxima and their extremizer counts, and verifies the 32-orbit enumeration under all point permutations. Its rational interpolation checks are supplemental.

The proof of the all-time formula requires, in addition, the analytical coarea decomposition, spectral identity and convexity argument in `RESULT.md`. No numerical gridding of the real time parameter is used to establish the theorem. The proof covers \(t=0\), all \(t>0\), and the limiting \(t\to\infty\) behavior. Only binary extremizers are classified, not all multilevel equality signals.

The primary-source comparison was made with the accessible introductory theorem and main contraction formulas of Gaubert–Qu, arXiv:1307.4649. Targeted text searches found no Petersen or Gini result in that PDF. Published related-record summaries were checked, but their full texts were not retrieved; they remain a historical-priority limitation. No external independent audit was performed.
