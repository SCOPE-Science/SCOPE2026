---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and limits

The attached `verify.py` uses only the Python standard library. Run `python3 verify.py` and expect three PASS lines. For each of the two possible permutations it checks 100,000 deterministic forward images from random integer factors, 100,000 deterministic inverse membership samples, and all 19,683 target integer matrices with entries in \(\{-1,0,1\}\). Every included sample is reconstructed by explicit factors and multiplied back. It separately checks the strictly positive four-defect nonrepresentable example and the three exceptional boundary wings.

The proof in RESULT.md establishes the theorem for arbitrary real finite targets. The computational tests are finite checks and are not a proof of necessity over all real matrices, of uniqueness of factor parameters, or of any statement in dimensions greater than three. The excluded matrix illustrates failure of the restricted test involving only the four defects that use the bottom-left entry. It is not a counterexample to Grigoriev's Theorem 1.2(i), which at size three includes the fifth inequality as well.
