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

The exact polynomial cofactor calculation and physical-time coordinate reduction are given in `RESULT.md`. The nonstandard part is the square-root singular-integral limit: expanding the unique positive-root denominator at the torus section where \(r=\sqrt{a^2+1}\) and rescaling \(\varphi=\sqrt\varepsilon v\) yield a uniformly dominated integral and the two constants in (5). The exact stable multiplier product follows from the full-circle integral of \((u+v\cos\varphi)^{-1}\) for \(u>|v|\).

Run `python3 checker.py` with Python 3 standard library. The script tests two cofactor identities exactly over rational samples, compares the closed product and middle-period formulas to direct composite Simpson quadratures, tests the strict hierarchy and tracks the approach to the predicted sharp limiting coefficients. A passing run prints `ANISOTROPIC_TORUS_CHECK_OK`.

The finite test cases and quadratures corroborate algebra and normalization but do not certify the infinite or all-parameter theorem; the analytical proof is given in `RESULT.md`. No independent mathematical audit or separate external validation has been performed.
