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
# Verification of finite-chain centralizer rank distributions

The executable `verify_path_rank_centralizers.py` is standalone and uses only the Python 3 standard library. Running `python3 verify_path_rank_centralizers.py` directly enumerates every binary-increment chain map for lengths \(1\le n\le11\). It constructs each clamp directly, tests equality of compositions pointwise, records the image rank of every commuting map, and compares this complete vector against the formula. Every one of the 286 checked centralizers matched. The same program independently checks aggregate rational-series coefficients for these sizes, checks previously published unrefined total counts as a consistency condition, and tests reconstruction signatures for nonconstant intervals through chain length 35. The last output line is `RANK_REFINED_PATH_CENTRALIZERS_VERIFIED; cases=286`.

Exact checks at \(n=4\): 102 commuting ordered pairs with an idempotent first coordinate; the constant clamp's polynomial is \(1+3z+3z^2+z^3\), while the clamp to the middle pair has \(2+3z+2z^2+z^3\). Both sum to eight but differ in rank. At \(n=11\), the total is 65,658 pairs. The infinite formulas and central limit theorem are established by the mathematical derivation in `RESULT.md`, not finite exhaustive computations. Independent mathematical audit has not been performed.
