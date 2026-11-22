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

# Verification procedure

The attached `check.py` requires Python 3 and SymPy and can be run by `python check.py`. It verifies the exact general discriminant and two-step characteristic polynomial, their specialization to the published two-parameter map, the rational orbit and return spectrum, plus 129 deterministic exact-algebraic samples of existing real two-cycles. The script was executed successfully with the output: `PASS: symbolic period-two census and Floquet identity; exact rational example; samples 129`.

The analytical argument in `RESULT.md` proves the universally quantified statements; finite tests are not completeness certificates. The existence classification is over all real states, with \(u\ne0\) for the general map and \(ab\ne0\) for the published specialization. No claims are made about higher periods or global basins. Originality remains subject to potentially unindexed equivalent literature.
