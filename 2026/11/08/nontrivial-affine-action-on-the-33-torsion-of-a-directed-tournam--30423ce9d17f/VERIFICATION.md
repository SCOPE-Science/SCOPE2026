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
The included standard-library program `verify_paley_torsion_action.py` performs full cell and codimension-one incidence enumeration, verifies exact boundary-square-zero conditions, checks acyclicity over all cells, forms the integral 18-by-17 Morse differential and computes all maximal minors by exact Bareiss determinants plus a unit minor. Direct finite-field boundary ranks for primes 2, 3, 11 and 13 are recomputed independently from the original 165/495/330-cell complex. Integral spanning-tree cycles and modulo-eleven cocycles are evaluated under target multiplier/translation and source rotation. Every lifted cocycle is checked on each original two-cell; the resulting multiplication-by-three matrix is [[2,10],[10,2]], with determinant 3. The group-order argument and Chinese remainder formula supply the order-three factor, giving 25 modulo 33. The alternative acyclic matching is only a separate consistency check of combinatorial orientation and coverage, not a second Smith-form proof. No mathematical assertion beyond the stated exact finite CW model is checked. External independent validation is not performed.
