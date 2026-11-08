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

# Reproducibility and boundaries

Run `python3 verify.py` with a standard Python 3 installation. The checker independently enumerates all injective partial graph endomorphisms on star orders 2 through 6 and computes actual powers and the first regular power; it also brute-force checks existence of regularity witnesses on orders 2 through 4; it compares the rank-stratified hub-chain survival frequencies with the exact finite product and verifies the acyclic fraction, class counts and exact complete first-regular-power survival formula for every positive time through the maximal possible time. It also evaluates rank-mixed survival probabilities for 100, 400 and 1600 leaves numerically and compares them with the predicted exponential values. The successful run ends with `VERIFY_OK`.

Exhaustive cases are limited to the explicitly listed finite star sizes and do not establish the asymptotic statement. The proof in `RESULT.md` establishes rank concentration, the conditional product limit, and cycle exception negligibility for all increasing star orders. The theorem relies on the previously published semigroup-regularity criterion (arXiv:2401.11741v1, Theorem 2.3). Independent audit has not been performed.
