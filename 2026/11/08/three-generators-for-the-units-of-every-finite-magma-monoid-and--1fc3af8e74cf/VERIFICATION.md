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

# Verification record

Run `python3 check_unit_rank.py` with the accompanying Python 3 standard-library checker. The separately embedded `check_unit_rank_output.txt` is the observed stdout for the completed replay.

The checker independently enumerates equivariant permutation tables for orders \(n=1,2,3\), exhaustively generates the signed-permutation groups \(B_N\) from the specified pair for \(2\le N\le6\), and constructs and composes the actual binary-operation tables of all \(288\) units when \(n=3\). It tests the two-sided ideal of operations with nonbijective diagonal restriction over all \(16\) binary operations for \(n=2\). The predicted orders for dimensions \(3\) through \(6\) and conjugation identities are also evaluated.

These tests establish the stated finite instances only. The proof of the full quantification over all \(n\ge3\), the three-dimensional abelianization, and the five-generator obstruction is symbolic and is given in `RESULT.md`. The minimal number of generators of the entire monoid is **not** asserted to be five; five is a proved lower bound.
