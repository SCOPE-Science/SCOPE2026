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

# Verification details

The attached `CHECK.py` uses the Python standard library and computes every ambiguity coefficient's *exact vanishing decision* through integer histograms of exponents modulo the prime cyclotomic polynomial. It checks the predicted zero set, the exact rank count, and—using exact integer cyclotomic autocorrelation reductions—every nontrivial quadratic Gauss magnitude required in the fourth-moment proof for all thirteen indicated primes. Run `python3 CHECK.py`; the expected final line is `ALL_EXACT_QUARTIC_CHECKS_PASSED`.

Independent direct complex-matrix rank computations of the full measurement projectors gave ranks \(17\), \(43\), and \(101\) for prime orders \(5\), \(7\), and \(11\), respectively; numerical tolerances in those supplementary SVD computations were not used to decide infinite-range statements. The analytic cyclotomic/permutation and Weyl proofs establish the all-prime result. The package does not assert independent review, a machine formalization, or a certificate of publication priority.
