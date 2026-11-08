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

# Verification of the mathematical result

The analytic argument in `RESULT.md` covers all positive real rate vectors and every integer cycle length at least five. The `verify.py` program independently constructs generator matrices and their fourth Taylor polynomials using rational arithmetic, then compares their entries against the five formulas given by the proof. Running `python3 verify.py` with Python 3 standard library reports:

- 14,200 exact-rational matrix entry agreements for lengths five through ten.
- 1,800 exact stochastic row-sum checks.
- 1,200 numerical tests just below and above the calculated endpoint for independently sampled positive rate vectors.
- Six exact-rational single-defect cubic phase identities, and two approximate isolated-root values.

These checks were executed from the staged `verify.py` and subsequently from the extracted file embedded in the delivery ledger. Randomly sampled matrices cannot establish any universal assertion. The proof establishes the global parameter range by walk enumeration, strict polynomial signs, and a stochastic-row bound. The numerical tests use floating point only in threshold bisection and two-sided stress tests; the matrix-entry comparisons and defect identities are exact.
