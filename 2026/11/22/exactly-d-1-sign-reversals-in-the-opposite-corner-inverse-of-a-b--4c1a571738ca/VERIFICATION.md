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

# Reproducibility and scope

Run `python3 check.py` using Python 3's standard library. The executed checker returned `VERIFY_OK 261`. It performs exact-rational Sturm root counts for dimensions 2 through 9, explicit matrix inverse comparisons for dimensions 2 through 4, and rational-parameter involution tests. The theorem for all integer dimensions 2 and above is proved analytically by an exact polynomial degree bound and vanishing logistic finite-difference moments. The finite checker is a supplementary consistency check, not an exhaustive or machine-checked proof.

The result is restricted to one unassembled orthotope scalar tensor-product mass matrix, with positive constant density. It does not certify assembled-mesh numerical stability, finite-precision behavior, or algorithmic performance. The dimension-three special case follows from a separate published formula and is not claimed as novel.
