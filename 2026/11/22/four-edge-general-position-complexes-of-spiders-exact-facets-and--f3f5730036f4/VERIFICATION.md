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

The symbolic proof is in RESULT.md; `verify_spider4.py` is a reproducibility cross-check, not a substitute for the proof. Execute `python3 verify_spider4.py` with a Python 3 version supporting `int.bit_count()` and modular inverses via `pow(a,-1,p)`.

The checker constructs shortest-path edge masks independently of the counting argument and compares both cardinality polynomials against all edge subsets for 52 nonisomorphic length tuples. It checks reduced homology over characteristics 2, 3 and 101 and signed transposition actions at equal two-edge-arm orders 2 through 5.

The finite computation does not prove integral torsion-freeness, all-orders equivalence or publication priority. Integral torsion-freeness and the complete arm-permutation lattice follow from the explicit relative cellular-chain argument in RESULT.md. This verification is not independent mathematical audit.
