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

From the directory containing `checker.py`, execute `python3 checker.py` using Python 3. No third-party packages or network access are needed. The expected output is `PASS 531 exact structural and independent-enumeration assertions`.

The checker computes the truncated bivariate exponential generating series for \(1\le h\le10\) and \(n\le21\), verifies the sign cutoff for the conditional leaf mean and the coefficientwise signed deficiency, then independently enumerates every recursive-tree parent sequence at orders two through nine. At depth three and order seven it checks the complete leaf-count profile \((1,31,21,1)\) and exact conditional mean \(65/27\).

This verifies finite cases only. The proof for all depths and orders is the coefficientwise induction displayed in `RESULT.md`. No separate external validation has been performed.
