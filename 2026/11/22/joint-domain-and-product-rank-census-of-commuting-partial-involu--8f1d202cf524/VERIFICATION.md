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

# Verification and reproducibility

The proof is the block-invariance/finite-group-action bijection and transitive orbit enumeration in RESULT.md. It is valid for all integers \(n\ge0\), \(t\ge1\); finite tests are corroboration only.

The accompanying standalone checker enumerates all partial involutions without using the theorem, compares their compositions explicitly, and separately computes the predicted weighted series with exact fractions. It checked the full joint domain-rank and product-rank distributions at \((t,n)=(1,5)\), \((2,0\ldots6)\), \((3,0\ldots4)\), and \((4,2),(4,3)\), all PASS. The pair totals are \(1,4,21,124,817,5844,45061\) at sizes zero through six. This is not a computer-assisted proof of the infinite formula; that proof is supplied symbolically.

Command: `python computations/checker.py` from the package root. Python 3 standard library only. No external certification, independent audit, or downloaded files were involved.
