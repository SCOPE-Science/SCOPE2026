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

# Reproducibility and verification

All statements refer to an ordered sequence of complete overlapping read words, not window weights or read multisets. The theorem holds for every integer \(q\ge2\), integer \(\ell\ge2\), and integer \(n\ge\ell+1\).

Run `python3 checker.py`. The checker enumerates every source word for bounded parameter combinations, forms its **set** of distinct single-read-deletion observations, accumulates inverse parent sets, and compares the parent count to an independently implemented overlap/run formula. It separately compares the resulting complete inverse-list histogram to a run-composition formula, verifies the exact count of feasible outputs, and verifies the maximum possible parent count.

Execution completed successfully with 49 parameter combinations, 343,337 feasible outputs, and 631,205 distinct source/output incidences. These tests are finite corroboration, not a replacement for the symbolic all-parameter proof in `RESULT.md`.

For manual proof review, check that a deleted interior read leaves a single pair of flanking reads separated by two starting positions. Its length-\((\ell-2)\) overlap is both necessary and sufficient for a unique bridge. If the remaining read path is completely compatible, the bridge condition is equivalent to a constant run of \(\ell-1\) consecutive underlying symbols; duplications in the same run yield one parent. Boundary extensions are distinct except for the constant-word overlap. Counting run compositions gives the displayed rational generating function.

The complete primary manuscript of Ye and Ge was not available for exhaustive historical comparison; correctness of the present self-contained argument is logically independent of historical priority. No independent mathematical audit has been performed.
