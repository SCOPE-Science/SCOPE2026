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

The analytical proof is contained in `RESULT.md`. The standalone `verify.py` checks the Euler coefficient identity against the rank-one scalar data, the infinite-product expression against a truncated series, the exact derivative at selected geometric zeros, the level-set equation with numerical complex root solving, and the first displacement term and predicted annuli. For each of three parameters \(q\), 189 total numerical tests passed.

Run `python verify.py` using Python 3 and `mpmath`. The code uses 115 decimal digits, up to 240 Euler factors, and finite truncations of degree 99 for the series comparison. The displayed pass count is from executing this exact packaged source. Such finite tests are not a proof of the infinite zero count; Rouche's theorem with the uniform circle estimate establishes that count for every sufficiently large index. The algebraic multiplicity assertion is justified by the simple zero of the analytic rank-one resolvent determinant.

The assertions do not concern a full classification at finite indices, nor uniform estimates as the parameters vary toward boundary values. No independent audit has been performed.
