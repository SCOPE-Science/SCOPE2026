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

# Reproducibility

Execute `python verify.py` from the extracted directory with Python 3, SymPy and mpmath installed. The supplied execution produced `PASS: 150 exact/symbolic/numerical assertions` and the strictly positive rational-sign margin `7.353156633380782e-05` (decimal rendering of an exact rational inequality). The script reconstructs the derivative identity and polynomial coefficient table, and proves a rational Taylor-error bound over the whole angle interval. It also evaluates independent high-precision slicing quadratures at 28 parameter values; those tests are supplementary, not an infinite proof. The proof in RESULT.md states the geometry, differentiability, signs, full interval bounds and endpoint limiting argument. This package does not constitute an independent mathematical audit or certification by an outside party.
