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

# Verification record

The two-state sign identity is proved analytically in RESULT.md, using strictly positive interpolation coefficients for the exponentials of real irreducible two-by-two Metzler matrices. The conclusion is quantified over every pair of strictly positive treatment times, all nonnegative phenotype-dependent drug-induced losses, all real common growth rates, all positive phenotype-switching rates, and all nonzero nonnegative initial vectors.

`checker.py` is standalone Python 3 standard library code. It creates three-state phenotype-transition and drug-killing matrices exactly as in RESULT.md; constructs rational Taylor sums to order 40 at times \(1/5\) and \(1\); computes the two ordered two-drug total counts; and checks that both rational values exceed their proved truncation errors in magnitude with opposite signs. The error bound derives from the row-sum operator norm and \(e^5<256\), not floating-point tolerances. The displayed decimals are descriptive only; sign acceptance uses exact `Fraction` comparisons. The two independent signs prove existence of a duration-dependent reversal by continuity; no numerical root-location or empirical claim is certified.

Limitations: Exact expected linear population dynamics are not a stochastic extinction model. The result does not identify an optimal dosing schedule for patients, does not include evolutionary adaptation, and does not exhaustively classify three-phenotype models. Independent audit and empirical validation have not been performed.
