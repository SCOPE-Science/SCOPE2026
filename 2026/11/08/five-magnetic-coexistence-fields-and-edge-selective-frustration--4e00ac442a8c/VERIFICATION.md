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

# Computational and mathematical verification

Run `python3 verify.py` using the delivered Python 3 standard-library checker. The program independently enumerates all 531441 labeled three-color assignments by (i) full ternary words, and (ii) a zero-spin subset followed by binary assignments to the complementary vertices. It compares both exhaustive results, the exact 13-sector minima and multiplicities, and the exact 24-edge one-frustrated-bond histogram. Eleven rational field tests verify all five coexistence degeneracies and six strict sectors. Equality of integer values and sorted successive slopes analytically proves the field envelope on **all real field values**; isolated sample values are not treated as proof. Graph identity was cross-checked with an independent standard graph generator. The accompanying CSV files contain all tables; the checker reproduces them without external dependencies.

The theorem is an exact finite graph result and requires no numerical limit, extrapolation or probabilistic certificate. It does not establish the novelty of published historical values: the 1970 primary graph article's complete text was inaccessible, and individual edge noncriticality has earlier literature. Independent scientific audit has not been performed.
