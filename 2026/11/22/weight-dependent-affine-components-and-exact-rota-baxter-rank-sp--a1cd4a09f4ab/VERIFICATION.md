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

# Verification and limits

The standalone `verify_weighted_rb.py` enumerates all matrices in the six stated pairs \((n,q)=(2,2),(2,3),(2,5),(3,2),(3,3),(4,2)\) using the standard basis \((u,v,w_1,\ldots)\), where the sole nonzero bracket is \([v,u]=u\). It tests all ordered basis pairs in the **original** weight-dependent Rota–Baxter identity, separately checks membership in the stated family union, then uses modular Gaussian elimination to obtain the matrix rank and compares the full distribution to the Gaussian-binomial formulas. The cases use weights \(0\) and every nonzero element for dimension two; weights \(0,1\) for the displayed higher dimensions and also \(2\) for \(q=3\), giving exactly 17 exhaustive checks.

Expected and obtained rank counts (rank zero first):

| Dimension | Field | Weight | Rank counts |
|---|---|---|---|
| 2 | \(\mathbb F_2\) | 0 | 1, 2, 0 |
| 2 | \(\mathbb F_2\) | 1 | 1, 3, 2 |
| 2 | \(\mathbb F_3\) | 0 | 1, 4, 0 |
| 2 | \(\mathbb F_3\) | 1 or 2 | 1, 5, 4 |
| 2 | \(\mathbb F_5\) | 0 | 1, 8, 0 |
| 2 | \(\mathbb F_5\) | 1, 2, 3 or 4 | 1, 9, 8 |
| 3 | \(\mathbb F_2\) | 0 | 1, 19, 12, 0 |
| 3 | \(\mathbb F_2\) | 1 | 1, 17, 34, 12 |
| 3 | \(\mathbb F_3\) | 0 | 1, 74, 96, 0 |
| 3 | \(\mathbb F_3\) | 1 or 2 | 1, 59, 186, 96 |
| 4 | \(\mathbb F_2\) | 0 | 1, 101, 714, 336, 0 |
| 4 | \(\mathbb F_2\) | 1 | 1, 81, 734, 1152, 336 |

Run using `python3 verify_weighted_rb.py`, with Python 3 and no external dependencies. Successful execution ends with `WEIGHTED_LEIBNIZ_RB_CENSUS_VERIFIED`. The tests are exhaustive only for the listed prime fields and dimensions; finite enumeration does not prove the infinite parameter family or extension-field cases. The general proof is the tensor classification, the component-intersection geometry, and the rectangular-rank enumeration in RESULT.md. No claim is made about the unreduced defining ideal of the algebraic scheme or about algebra-automorphism conjugacy classes.
