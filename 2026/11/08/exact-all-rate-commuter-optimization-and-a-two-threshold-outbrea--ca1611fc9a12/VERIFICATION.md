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

# Reproduction instructions

The source's demographic-balance formulas and next-generation reduction are reproduced exactly in the proof. With Python 3 and no third-party packages, run `python3 verify.py`. The script checks the independent six-group expressions against the compressed two-patch matrix for 200 exact rational choices, evaluates the three exact witness signs and the cleared quadratic identity, then runs supplemental floating-point sign tests. It prints `VERIFY_OK` only if all tests pass.

The universal strict monotonicity and one-minimum assertions depend on the displayed Perron-root derivative proof, **not** on the finite test set. The neutral threshold \(\mathcal R=1\) is intentionally not classified as attracting or repelling. The proof assumes demographic stationarity and strictly positive finite commuting and recovery rates. No external independent audit has been undertaken.
