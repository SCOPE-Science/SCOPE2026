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

The reproducibility artifact `verify.py` checks the exact affine epoch recursions for the two sample orders, the stochastic second-moment expressions, the rational formula for the risk ratio, the transformed quartic coefficients, the polynomial resultant and an exact rational example. Rational Sturm root counts certify the stated root isolation and multiplicity-bound transition; explicit sign arguments in the proof cover the whole real parameter region. The code does not constitute an independent mathematical audit or a formal proof assistant certificate.

Run `python verify.py` using Python 3 and SymPy. In the computed results, numeric decimals are for interpretation only; the decisive algebraic verifications use exact rational coefficients and root counts.
