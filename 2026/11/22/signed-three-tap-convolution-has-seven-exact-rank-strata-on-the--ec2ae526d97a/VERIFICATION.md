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

The delivered proof package contains `RESULT.md`, `SLOGAN.txt`, `METADATA.json`, `REVIEW.md`, `AUDIT.json`, this verification file, `orbit_table.csv`, `verify_modular.py`, `verify_rational.py`, and `requirements.txt`. No external source code or previous computations are needed for the rank proof.

Run `python3 verify_modular.py`. It reconstructs all 60 even permutations of five points, their multiplication and inverse tables, conjugacy by 120 permutations, the two inversion-stable order-five classes, and the 23 orbit decomposition. It checks the intrinsic rank formula, exact row-echelon rank for every one of 3422 normalized signed masks at each of the two primes 1000000007 and 1000000009, and all seven counts across 102660 signed masks. The determinant bound \(3^{30}\), together with the stated prime product, lifts the characteristic-p ranks to exact ranks over \(\mathbb C\).

Run `python3 verify_rational.py`. Using independent permutation-composition code and exact rational sparse matrices, it checks the ranks of all 23 representatives, reproducing the histogram. Both programs were executed successfully on the supplied, finalized scientific source files prior to delivery. The proof is finite and exhaustive for its explicitly stated domain; it is not an assertion about other simple groups, arbitrary signs/weights, or singular values beyond zeros. No independent audit is claimed.
