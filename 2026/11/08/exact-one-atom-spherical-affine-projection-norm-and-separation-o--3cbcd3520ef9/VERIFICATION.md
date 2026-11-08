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

Run `python checker.py` with Python 3, SymPy and SciPy. The program checks exact symbolic identities for the fixed calibration, the sextic critical polynomial and its leading coefficient, the one-sided derivatives at the antipode, the strict off-antipodal comparison at mass weight \(1/3\), both limiting polynomial factorizations and the first-order expansion at vanishing mass. It also independently integrates the original affine kernel over the continuous spherical component for 35 parameter-latitude pairs, including the atomic contribution, and tests the sextic-root maximum against independent dense sampling for five rational weights.

The polynomial equalities and endpoint sign arguments in `RESULT.md` provide the infinite-range proof; numerical integration and finite root tests only corroborate. There are no external datasets or compiled artifacts. The global switching weight is proved to exist but is neither uniquely characterized nor numerically certified.
